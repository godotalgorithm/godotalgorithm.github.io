---
layout: post
title: "The original sin of semiempirical electronic structure"
categories: research
---

Error analysis is an important aspect of my research.
First and foremost, I strongly believe in introspection and self-criticism as important traits of a scientist.
I don't think scientists should rely on others to provide the most useful criticisms of their work -
 they should be able to identify flaws in their own work and make appropriate adjustments.
Whatever mistakes you fail to identify are likely to persist in some form, possibly limiting the efficacy of your work
 in some subtle way or perhaps being identified by competitors long after the fact to be used against you.
I also have no shortage of research ideas, so I end up in cyclic process of coming up with ideas,
 critically assessing them until they (usually) fall apart, learn some valuable lesson,
 and then proceed to churn out more ideas informed by such lessons.
This does tend to waste a lot of time, and it has probably been detrimental to my research career so far
 (if anything, this kind of behavior is more an investment in the future than a prudent short-term strategy).
Also, when I begin to work in the vicinity of well-established ideas and results,
 I will often target my engine of criticism onto the work of others,
 so that I can put their work through sufficient criticism for me to accept or trust it in some form.
Too often, scientists take criticism of their work as a personal insult, but I try my best to be polite about it.

As per my last blog post, I've begun to build some very simple semiempirical electronic structure models
 to gain some hands-on experience (and to co-opt other work responsibilities).
I've already done a lot of background research in this area, so I was prepared to put the problems that I encountered
 into an informed historic perspective.
I put together a model inspired by the popular modified neglect of diatomic overlap (MNDO) approximations,
 and I encountered one of the basic, well-known problems that result from them: a lack of repulsion between closed-shell atoms/molecules.
I avoided using the historic correction of a short-ranged repulsive interatomic potential because
 I was trying to show how a simple quantum-mechanical model of noble gases produces a Lennard-Jones-like potential
 for the "correct" physical reasons.
I was admitting failure if ended up with a model that already contained the repulsive half of a Lennard-Jones potential.
Instead, I put in an extra short-ranged repulsive electron-ion potential inspired by pseudopotentials,
 which achieved the same outcome but at least appeared to be "more quantum".
However, I didn't have time for enough analysis to really understand the root causes of this problem,
 as there are multiple possible culprits.
There is a [thorough recent assessment](https://doi.org/10.1021/acs.jctc.8b00601)
 on the neglect of differential diatomic overlap (NDDO) approximation
 of the 2-body Coulomb integrals in MNDO-based models,
 while the [main effort](https://doi.org/10.1021/acs.jctc.5b01046) to repair the underlying MNDO flaws
 has focused on the effects of atomic-orbital orthogonalization.
If I want to build new semiempirical models and avoid past mistakes,
 then I need to understand and the leading sources of error and their relative importance.

Since I just learned how to use Jupyter notebooks and had a positive experience with them,
 I decided to [carry out my MNDO analysis in a Jupyter notebook](/assets/2019-08-06-MNDO-He-dimer.ipynb).
In retrospect, there was enough of an emphasis on analytical manipulations (that I did by hand)
 over numerical computations that it would have probably been easier to use a Mathematica notebook here.
However, most of my work is heavily numerical, so I'll probably stick with Jupyter notebooks and the conveniences of NumPy.
The simple example that I used for this analysis was a Hartree-Fock calculation of a helium dimer
 with a single-Gaussian atomic orbital basis for each atom.
This is of course a very crude description of atomic effects,
 but it was able to preserve interatomic effects reasonably well
 while enabling the entire calculation to be done by hand without too much effort.
I was a little bit surprised by the outcome at first, but it wasn't so surprising in hindsight.
In the absence of covalent bonding, NDDO errors were small and irrelevant.
The problem was specifically that the on-site 1-body matrix element (excluding the electron-ion Coulomb interaction)
 was a constant and did not depend on interatomic separation.
This is appropriate for a non-orthogonal basis,
 but the orthogonalization process induces an effective short-ranged repulsive electron-ion interaction
 that overwhelms the long-ranged attractive Coulomb interaction when the orbitals of two atoms begin to overlap appreciably.
By introducing this repulsion as an interatomic potential rather than an electron-ion potential,
 MNDO-based models suppressed both the occupation-dependence of this energy contribution
 and its effect on the electronic structure.
This is a sub-optimal design choice that in effect makes an additional approximation of a fixed average electronic occupation of atoms
 in some parts of the model, thus causing problems for atoms that can occur in multiple charge states.
However, it doesn't cause any catastrophic problems, and the semiempirical modeling process is flexible enough
 to smooth over the effects of various approximations.
Unfortunately, this limits the transferability of models between different atomic charge states
 and exhausts more of the model parameters in correcting avoidable errors.

This ambiguity between ion-ion and electron-ion potentials has persisted to the present day
 in popular semiempirical electronic structure models.
The direct decendents of MNDO (AM1, PMx, etc.) continue to use repulsive interatomic potentials
 and continue to increase their complexity with an increasing number of diatomic model parameters.
The completely independent DFTB family of semiempirical models, the most recent variant of which is [GFN2-xTB](https://doi.org/10.1021/acs.jctc.8b01176)
 perform their electronic structure calculations in a non-orthogonal basis,
 which avoids the approximations that caused the lack of repulsion in MNDO-based models.
However, DFTB models still include a short-ranged interatomic repulsion between neutral reference atoms
 even though they have a flexible enough form to capture this correctly as a purely electronic contribution to the total energy.
Because these models are primarily fit to total energy data (or similiarly heats of formation or total energy differences or structural properties)
 rather than electronic properties like excitation spectra,
 the more complicated model forms begin to develop multiple ways of approximately fitting the same data.
This creates a poorly conditioned parameter fitting process,
 where there are nearly redundant parameters with respect to the reference data that is being fit.
It isn't simply a matter of not having enough data, it is that the combination of limited scope
 and flexible model forms has produced fundamentally underconstrained models
 that do not attempt to predict diverse enough physical observables to define themselves unambiguously.

To conclude this discussion, the "original sin" that I teased in the title of this blog post
 is the limited scope of semiempirical electronic structure models that limits their ability to define model parameters robustly.
They are models of electrons and ions that have not constrained their electronic subsystems with a broad enough set of electronic properties.
The ion-ion/electron-ion potential ambiguity was simply the first and most consequential symptom of this underlying problem.
If these models were also constrained to predict atomic charges (which unfortunately need to be artificially defined in some way),
 then they would have more rigorously constrained the electron-ion potential.
This is analogous to Kohn-Sham density functional theory (DFT), where the modeling of the electronic density
 formally constrains the electronic potential in a [1-to-1 mapping](https://doi.org/10.1103/PhysRev.140.A1133).
Similarly, pure interatomic potential/energy models are simply functions of atomic coordinates
 and well-behaved functional forms can be systematically increased in complexity as more reference data becomes available to constrain them.
As a result, both DFT and interatomic potentials have been better defined and overall more successful modeling activities
 than semiempirical quantum chemistry in recent decades.
Even some [notable missteps](https://doi.org/10.1126/science.aah5975) reinforce my point:
 DFT reference data has been emphasizing total energies much more than electronic densities,
 and the accuracy of electronic density predictions has begun to degrade in some models as a result.
Semiempirical electronic structure models need more constraints to remain well-defined as they introduce more parameters,
 either from direct connections to ab-initio quantum chemistry or from predicting a broader set of physical observables
 (even if they are less capable of predicting those observables accurately).
Two examples of the former approach are the [OMx models](https://doi.org/10.1021/acs.jctc.5b01046)
 and Michael Dewar's last model, [SAM1](https://doi.org/10.1016/S0040-4020(01)81868-8),
 that both obtain more of their matrix elements directly from ab-initio quantum chemistry.

My research plans in semiempirical electronic structure are evolving, as I explore and learn more and as circumstances change.
I will discuss these plans and the thought process behind them in an upcoming blog post.
In particular, I'm trying to stake out some practical short-term research projects to add value to semiempirical electronic structure
 as soon as possible to gain more clout in this research area while isolating, deferring,
 and organizing my more ambitious, risky, and technically sophisticated ideas into a longer-term research plan.
Without some tangible short-term successes, this research effort probably won't survive long enough to have a "long term".
