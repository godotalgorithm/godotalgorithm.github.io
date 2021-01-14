---
layout: post
title: "A career bookmark for semiempirical modeling"
categories: research
---

When I walk away from a research program for an indefinite period of time, I like to leave some kind of "bookmark" for myself,
 usually in the form of a scientific publication. The first time I did this was with
 [my cubic-scaling RPA algorithm paper](https://arxiv.org/abs/1303.3847), which I finished as my electronic structure funding was being
 cut at Sandia National Labs. I knew that I probably wouldn't have any opportunities to work on that kind of research again for a long time,
 and I wanted to have something to show for myself and to act as a starting point if I ever return (which I still cannot justify).
This time around, I have a [somewhat recent paper](https://arxiv.org/abs/1812.05264) that is adjacent to semiempirical modeling,
 and my general views have not changed from what was articulated in that paper.
I did sink a lot of time into a refining a technical plan for new semiempirical models,
 but the amount of effort required to write a thorough paper about it is much more than I can afford right now.
Instead, I will summarize this plan in a blog post, which should give me enough catharsis to step away from this plan and clear my mind of it.
Unlike my previous career bookmark, this isn't predicated on a specific external event,
 just my decision to halt all research that has no chance of being supported or opening up new career opportunities.
This is particularly frustrating in the case of semiempirical modeling, because I was initially drawn to it as a possible compromise
 between my more high-risk research interests and more pragmatic research that I thought would better attract funding and broader interest.
Unfortunately, that was a mis-assessment, and semiempirical modeling simply cannot compete with popular topics like machine learning
 for funding right now. Why bother to build and fit semiempirical models with careful physical reasoning and cost/accuracy balancing
 when you can just turn the crank on popular machine learning models fed with ever-larger mountains of reference data?

Semiempirical modeling is about carefully chosen compromises between cost and accuracy, and the results can get a little ugly.
While the elements of my design all seem reasonable enough on paper, there is still the very real possibility that
 a fully fleshed out implementation wouldn't be accurate enough or efficient enough to have practical value.
For a research project with little career value (because no one will pay me to work on it)
 and little academic value (because very few scientists are interested in the topic anymore),
 this makes it even easier to walk away from.
Sometimes it is best to let a research area lie fallow until the technical and financial conditions are better.
On the technical side, future advances in sparse numerical linear algebra could have a major impact on cost/accuracy balances
 and really shift around the design landscape and enable fewer compromises.
On the financial side, semiempirical models might get another chance from funding agencies when machine learning models
 fail to be transferrable enough to take their place, which I consider to be inevitable.

Before I move on to the details of my technical plan, I should note that I consider the biggest problem of semiempirical modeling
 to be a branding problem rather than any technical problem.
The effort to build general-purpose, transferrable semiempirical models, from its origins in the 1960's,
 was always seen as a stop-gap measure before computers were powerful enough for Gaussian-based quantum chemistry to become routine.
While semiempirical models were eventually valued in their own right, density functional theory (DFT) became the preferred approach
 to semiempirical modeling in the 1990's because it was perceived as more systematically improvable and co-opted most of the machinery of Gaussian-based
 quantum chemistry, despite being several orders of magnitude more expensive than the more traditional models.
The cheaper, traditional semiempirical models could have tried to more strongly embrace (and further reduce) their low cost
 and distinguish themselves in that way, but it just never happened.
There was definitely an attempt at this in the linear-scaling electronic structure literature of the 1990's,
 but those methods were not as reliable as hoped, and their limited range of applicability eroded the transferability of the underlying models.
This disconnect is most clear in the recent developments of the most popular semiempirical software, [MOPAC](http://openmopac.net).
Its newest model, PM7, further improved on transferability relative to older models,
 but this came at the expense of some accuracy for organic molecules,
 which is problematic for organic chemists.
In contrast, the linear-scaling solver of MOPAC, MOZYME, only functions for organic molecules with identifiable Lewis dot structures.
Thus, the efforts of MOPAC to become more transferrable and more efficient took it in different, somewhat conflicting directions.
A future branding strategy that I envision for semiempirical modeling is to categorize atomistic simulation methodologies by
 three attributes - efficiency, accuracy, and transferability.
The two most popular methodologies - classical interatomic potentials and first-principles electronic structure -
 are both very focused on accuracy, but interatomic potentials must sacrifice transferability to build their extremely efficient models,
 and first-principles calculations must sacrifice efficiency to attain accuracy from adherence to the underlying many-body Schrodinger equation
 (or some Kohn-Sham DFT proxy).
In this worldview, you have to pick two out of these three attributes, and the traditional approaches to semiempirical modeling
 are unique in their emphasis of efficiency and transferability at the expense of accuracy.
However, no one has ever made a successful popular case for this sort of worldview, much to the detriment of semiempirical modeling.

In the rest of this post, I will discuss the main components of my (now defunct) technical plan for a new semiempirical model.
The goal of this plan was to design a model entirely around low-cost linear-scaling solvers and to emphasize efficiency as much as possible
 in all design choices. Accuracy improvements are only sought when they don't conflict with (or even enable) cost reductions.

# Atom-centric state variables

The first design choice, which has implications for all the other design choices, is the choice of state variables.
Given just a set of atomic coordinates, the nonlinear SCF equations have to be solved to determine a ground state,
 and the successful identification of the global energy minimum cannot be guaranteed.
This global convergence issue can be sidestepped if the nonlinear state variables are provided,
 which reduces the standard SCF equations to a linear eigenvalue problem.
The number of state variables can vary quite a bit - MOPAC's models contain Fock exchange, thus its state variables
 are the full single-electron density matrix, while density-functional tight-binding (DFTB)
  models only contain a monopole approximation to a Hartree potential,
 thus their state variables are the total charge on each atom.
Consistent with the widespread empirical success of screened-exchange models in DFT,
 I would retain the on-site density matrices to construct on-site Fock exchange terms
 (assuming that screening effects suppress inter-site Fock exchange).
I would allow for diatomic contributions to the charge density in defining the Hartree potential,
 but this can be reduced to an atom-centric state variable by using the Hartree potential rather than the charge density
 as the state variable and expanding the smooth part of the Hartree potential as a Taylor series about each atom
 (to be interpolated in some manner).
This set of state variables is small enough that users could tinker with SCF convergence by hand-tuning
 the initial guess for the state variables, and there is also a natural neutral-atom guess that is straightforward to construct.

Tracking a limited set of state variables is particularly important for accommodating Born-Oppenheimer molecular dynamics,
 to limit the amount of information that needs to be propagated in time.
Designing a semiempirical model for use with molecular dynamics also means that the total electronic energy must be targeted
 rather than an enthalpy that contains vibrational contributions for proper atomic forces to be defined as energy gradients.
This is one of the unfortunate disconnects of the PMx models in MOPAC, which target enthalpies directly,
 while comparisons with first-principles electronic structure requires careful separation of electronic and vibrational contributions to enthalpy.
With molecular dynamics cheap and accessible, a semiempirical model could efficiently estimate the vibrational contributions
 to enthalpy, avoiding a baked-in vibrational enthalpy that needs to be explicitly removed to define molecular dynamics
 without vibrational double-counting.

# Compact SCF cycle

With a modest number of state variables and an emphasis on dynamics, it may be possible to accelerate the SCF cycle,
 particularly SCF solution updates following small changes to atomic coordinates, by linearizing the SCF stationary conditions
 in terms of the state variables. With enforced localization of the density matrix, the linearized SCF equations would be sparse
 for large systems. This reduced form of the SCF equations would be particularly important for large metallic systems that typically
 cause "charge-sloshing" problems in the SCF cycle. These problems would correspond to large condition numbers for the linearized SCF equations,
 which is an opportunity to test various matrix preconditioning strategies to reduce the number of iterations
 when iteratively solving these equations.

If atomic forces and atomic coordinate perturbations are included alongside the state variables in the linearized SCF equations,
 then a harmonic model of atomic displacements becomes accessible. This could enable 2-stage molecular dynamics where a system
 is linearized, the harmonic model is propagated in time until atomic coordinate perturbation exceed a threshold,
 and then the system is linearized again about the new set of atomic coordinates.
This could reduce the average simulation cost per time step, since many steps would only use the cheaper harmonic proxy model.

# New matrix-element models

The one detail that surprises me the most about chemistry-centric semiempirical models is that they continue to use variants
 of the extended Huckel model, which prescribe very crude relationships between the Hamiltonian and overlap matrices.
In contrast, physics-centric models typically use the more general Slater-Koster tight-binding formalism.
I believe that it is worthwhile to model interatomic matrix elements using simple models of the atomic orbitals themselves.
A particularly simple and cheap approximation would be to modify the popular contracted-Gaussian form
 by retaining the widest Gaussian and replacing the remaining Gaussians by a delta function for the purpose of computing
 just the interatomic matrix elements (p orbitals would have 1st derivatives of delta functions and d orbitals would have 2nd derivatives).
In this manner, the electronic density associated with a product of two atomic orbitals is a single Gaussian plus
 some atom-centered point charges associated with the delta functions.
This keeps the form of the electronic density manageable without introducing an auxiliary basis set.

A separate problem for older matrix-element models is the definition of on-site Coulomb integrals for d orbitals.
The simple approach of independently parameterizing each distinct integral becomes a problem with d orbitals
 because they have several dozen parameters and there isn't enough atomic spectroscopy data to constrain them.
The standard solution is to define the on-site Coulomb integrals by a proxy Slater-type orbital with an adjustable decay exponent,
 but this ends up having a complicated functional form and far less flexibility than the treatment of s and p orbitals.
A more uniform approach would be to embrace the use of an auxiliary basis set, which would split the
 on-site Coulomb integrals with four orbital indices into products of integrals with three indices - two of the atomic orbital basis
 and one of a semiempirical auxiliary basis set.
This would amount to a more consistent reduction in variational freedom of the model
 while reducing the number of independent parameters for d orbitals enough to be manageable.

# More atomic orbitals

It is empirically well-established that double-zeta basis sets are substantial improvements over minimal basis sets in DFT calculations,
 while triple-zeta and larger offer much more diminishing returns.
Semiempirical models have never incorporated double-zeta basis sets for reasons of both cost and the difficulty of parameterization.
With a Gaussian plus delta function model of atomic orbitals,
 there is a natural opportunity to define a double-zeta semiempirical basis by separating the Gaussian from the delta function.
Furthermore, with no interatomic Fock exchange, the Fock matrix will have block structure whereby
 the delta-function orbitals on one atom have no matrix elements with the delta-function orbitals on other atoms.
If matrix inversion (i.e. Green's function) methods are used instead of matrix diagonalization,
 these localized basis functions can be efficiently downfolded
 using Schur complements, meaning that the double-zeta basis retains a minimal-basis cost after the downfolding step.

# Localization expansions

In my recent [review and benchmark of linear-scaling electronic structure algorithms](https://arxiv.org/abs/1812.05264),
 I explored some new algorithm ideas based on perturbative corrections to localized Green's functions.
The rationale for those ideas was that the simplest localization methods independently computed each column of a Green's function
 and that introducing coupling between these independent calculations might improve their accuracy.
However, I now realize that retaining the independence between calculations of matrix columns is important for both parallelization
 and retaining sparsity in response matrices (and thus the linearized SCF equations).
The use of localization expansions is still possible while maintaining column independence
 by defining a different partition between "local" and "nonlocal" parts of the Hamiltonian for each column
 and directly inverting the "local" part for use in a Dyson series expansion of the "nonlocal" part.
I believe that such expansions will be worthwhile because they allow for more aggressive truncation
 of the local regions since localization errors will receive a perturbative correction.

Another important change I plan to make relative to the review paper is to avoid direct calculations of the density matrix
 in terms of Green's functions and instead compute all observables as responses from the free-energy matrix
 as described by [Barros and coworkers](https://arxiv.org/abs/1711.10570).
There were two novelties of their work - the use of a new random vector ensemble in stochastic trace estimation
 and the use of response-based observable calculations.
In my review paper, I studied their random vector ensemble, but I did not implement the response formalism.
While I didn't find substantial benefits to their random vector ensemble over localized calculations,
 I do believe that their response formalism is highly beneficial and would combine well with localized calculations.
The key idea is that the spatial decay of the free-energy matrix is more rapid than for the density matrix,
 so it can be computed more accurately for the same amount of localization.

In prescribing only an approximate, localized treatment of electronic structure, I would be allowing appreciable errors
 relative to the conventional matrix diagonalization approach to electronic structure.
As long as these errors don't contain severe numerical artifacts and are proportional to the underlying semiempirical model
 errors, then they don't substantially degrade the accuracy of the overall formalism while enabling substantial cost reductions.
Forcing linear-scaling algorithms to be numerically indistinguishable from conventional algorithms puts them at a severe handicap,
 and this led to their abandonment after being a popular research topic in the 1990's.
I believe that they have unrealized value for use in low-accuracy applications like semimempirical modeling
 if their accuracy standards are carefully relaxed.
For example, to avoid truncation-related artifacts in localized calculations, spatial truncations need to be smeared
 out in some way to avoid discontinuities in potential energy surfaces when an interatomic distance crosses a sharp
 truncation threshold.

# Density-dependent dispersion model

Prescribing a density dependence in dispersion models certainly isn't new,
 it is a feature of [D4](https://doi.org/10.1063/1.5090222), the latest version of Grimme's popular dispersion models.
However, I plan to introduce it in a much simpler manner as an approximation of a direct MP2 calculation
 between the explicit orbital degrees of freedom in the semiempirical model and implicit high-energy virtual orbitals.
By allowing for only on-site orbital transitions and expanding energy denominators of perturbation theory
 in inverse virtual orbital energy, a simple density-dependent form can be derived.
This derivation would forgo any diatomic parameters, so that the entire semiempirical model can be defined
 without the introduction of diatomic parameters, which is important for being able to optimize all model parameters
 simultaneously with modest amounts of reference data.

# The sum of its parts

In aggregate, I am proposing a large number of changes relative to traditional semiempirical models such as PMx and DFTB.
However, that shouldn't be surprising since most of the model forms that they adhere to were formulated in the 1960's and 1970's.
Electronic structure methodology as a whole has change enormously since then,
 and semiempirical modeling has changed very little to account for the substantial amount of new empirical knowledge
 that has been accrued in the much more active area of first-principles electronic structure over the last 40 years.
This stagnation of semiempirical modeling is mainly the result of very limited academic interest,
 which limits both accessible funding and available manpower.
There is unfortunately a lot of feedback, both positive and negative, in the modern scientific enterprise,
 and once a subdiscipline drops below a threshold of self-sustainability, it is very hard for it to recover.
By my account, semiempirical modeling dropped below the self-sustainability threshold in the early 1990's,
 and I just don't think it can recover at this point without a dedicated patron.
Is this technical plan even worth pursuing?
I'm not sure - it would definitely be a lot of work, and I think it could eventually produce a more useful simulation tool,
 but I'm not clear on how much better it would be than existing tools,
 and there won't be much value in it if there aren't a lot of people interested in using a new tool.
A older, worse tool is still making more of an overall contribution to science if more people are using it.
Ultimately, this is a moot point for me, since it is extremely unlikely for anyone to ever support my pursuit of this technical plan.
It's just another project to add to my growing pile of broken research dreams.

There is a decent chance that I will eventually salvage some of this plan for building semiempirical models
 specifically for use with quantum computers.
People are eager to run realistic-looking atomistic simulations on quantum computers, but there are and will continue to be
 extreme limitations in the size of such simulations.
By their basic nature, semiempirical models try to extract as much value as possible from each electronic degree of freedom.
However, this specific application would have slightly different design constraints.
For maximum model efficiency, we would probably want an absolutely minimal basis, which might include removing d orbitals from
 atoms outside of the transition metal block and other orbitals that might be treated perturbatively (e.g. orbitals on noble gases).
It is also important to limit the number of terms in the many-body Hamiltonian,
 which might justify a return to the neglect-of-diatomic-differential-overlap (NDDO) form of Hartree-Fock-based semiempirical models
 that retains only 2-center Coulomb matrix elements.
The accuracy of the NDDO form can be improved somewhat by working in an explicitly orthogonalized basis,
 as shown in [recent work by the Reiher group](https://arxiv.org/abs/1806.05615).
