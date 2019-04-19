---
layout: post
title:  "Hello, World!"
categories: career
---

Besides posting preprints to the [arXiv](https://arxiv.org) and publishing papers,
I have not maintained an internet presence for my research work.
My research interests do not follow popular trends, and my research style often involves
attempting to make progress on difficult problems by rapidly cycling through ideas that almost always fail.
Other scientists tend to find both of these traits off-putting, and so I mainly work on my personal research interests alone.
Also, while I've expended a lot of effort into developing new algorithms and models to improve electronic structure simulations,
 none of them have been successful enough to warrant any sort of publicity.
Thus my attitude has been that an internet presence would be a waste of time.

This blog and the research work that I intend for it to document are the result of a recent recalibration of my research attitudes and habits.
My opportunities to pursue independent, self-directed research have been in steady decline over the last decade, and it has become clear to me that
 my research career is unlikely to survive indefinitely unless I establish a core research program that is steady, useful, and predictable.
I simply have not proven my worth as a scientist, and it is time for me to make a serious effort at doing so
 in order to compete more effectively for the scarce resources allocated to basic scientific research.
I certainly enjoy risky, long-term research and chipping away at difficult problems,
 but I need to be more useful to earn the opportunity to continue such time-consuming activities.

The basic premise of this research blog is straightforward.
Atomistic simulation is strongly polarized towards two extremes, and I plan to develop a more viable middle ground.
These extremes are:

* _classical molecular dynamics (MD)_ where interatomic forces are described by simple, inexpensive interatomic potentials
  to enable atomistic simulations to be as large as possible in both number of atoms and amount of time simulated.
  These potentials are highly empirical and heavily parameterized, which allows them to be quite accurate but only
  in a narrow regime of validity. Electrons do not appear explicitly in these simulations, or they are described in a very simple manner (e.g. bond charges).

* _ab initio electronic structure_ where electrons are simulated explicitly by solving the many-body Schr&ouml;dinger equation
  to some level of approximation that is somehow systematically improvable. The least expensive and most popular method in this category
  is density functional theory (DFT), which maps the problem to a nonlinear partial differential equation (PDE) where each electron
  corresponds to an eigenfunction of the PDE.
  By limiting the role of empirically tuned parameters,
  these methods have a broad regime of validity and relatively uniform accuracy.
  However, it can be very expensive to make reliable, quantitative predictions.

Classical MD emphasizes efficiency over accuracy, and ab initio electronic structure emphasizes accuracy over efficiency.
Because of these differing priorities, ab initio electronic structure is many, many orders of magnitude more expensive than classical MD.
I believe that there should be a vibrant and active middle ground between these extremes to offer computational scientists
 more options in the unavoidable cost-versus-accuracy tradeoff in atomistic simulation.
_Semiempirical electronic structure_ was developed as one such middle ground long before we had the computing power for
 routine ab initio electronic structure calculations.
However, it was overtaken in academic popularity by DFT in the 2000's and there is now very little method or software development in the area.
I believe that reimagined and modernized semiempirical electronic structure methods and software
 can provide useful new capabilities in atomistic simulation.
I am confident that I have the necessary skills and experience to develop such a capability,
 and I am now trying to do so.

What should a reader expect from this blog? I'm not going to deliver a new simulation capability tomorrow.
However, I will discuss my planned technical path towards a new simulation capability and provide regular updates on progress.
Initially, most of this progress will be organized around writing scientific publications to document the refinement of new technical ideas
 that I believe are essential for semiempirical electronic structure to regain its competitiveness.
Each paper will have accompanying software implementations,
 and I intend to coalesce this software into a coherent simulation code as soon as it makes sense to do so.
I will also editorialize on research in atomistic simulation and related topics,
 and I'm happy to take feedback from readers who might also want to contribute to this editorialization.
I certainly don't and can't speak for everyone with an interest in atomistic simulation.
Because the area is not very active or competitive right now, I am going to be very open about my research in semiempirical electronic structure,
 which will include discussions of research in progress and unrefined ideas (some of which will inevitably fail).
I hope to eventually inspire readers to collaborate and/or compete with me in this area, both of which I see as positive outcomes.
I mainly want to catalyze research interest and activity in semiempirical electronic structure,
 which I believe can have a mutually beneficial effect for all participants.

There is of course a backstory to my new attitude and new research direction.
I was academically raised in the physics tradition of ab initio electronic structure (planewave-based DFT w/ post-DFT many-body Green's function corrections),
 but I've always been wary of having too narrow a perspective.
In grad school, I interacted with and learned from chemists working in the chemistry tradition
 of ab initio electronic structure (Gaussian-based Hartree-Fock (HF) w/ post-HF many-body/coupled-cluster corrections)
 and also from mathematicians working in numerical linear algebra.
The grandiose research vision that I nurtured in grad school was to unify the physics and chemistry traditions of electronic structure
 and make substantial improvements to its efficiency and scaling through fundamental algorithmic advances in numerical linear algebra.
I did not expect to accomplish this alone.
I hoped that somehow things would "work out" by developing small bits and pieces,
 finding like-minded people through the natural course of scientific interactions,
 and attaining a critical mass to pursue this goal more substantively.
Unfortunately, the bits and pieces were more modest and less successful than I expected, and none of the other things happened at all.

I was given a very serious reality check after leaving academia to work in a more applied setting at Sandia National Labs.
In academia, electronic structure simulation is generally perceived as a useful tool,
 and it is indeed very useful in the sense of being capable of generating a large number of scientific publications.
At Sandia, I used and observed others using electronic structure for various applications
 to Sandia's engineering missions, usually related in some way to nuclear weapons & national security.
The ability for electronic structure to make productive contributions in such a setting is extremely limited.
Sandia does plenty of multiscale modeling, which in practice is a social activity in which expert practitioners of various simulation methodologies
 interact to parameterize coarse-scale models using more expensive fine-scale simulations and eventually make connections with experiment.
My understanding is that the present state of computational science at Sandia was largely shaped by various nuclear weapon test bans,
 which led to a large investment in simulation software at Sandia during the 1990's.
This produced [continuum simulation software](https://sierradist.sandia.gov/) for solids, fluids, and plasmas
 and [classical MD simulation software](https://lammps.sandia.gov/),
 and three separate pieces of electronic structure simulation software based on the traditional
 [physics/planewave](https://dft.sandia.gov/socorro/mainpage.html) and [chemistry/Gaussian](https://mpqc.org/) approaches
 and a [mix of the two](https://dft.sandia.gov/quest/).
Continuum and classical MD simulations have flourished at Sandia, but electronic structure simulations have faltered.
My experience has been that electronic structure is too expensive and not reliably accurate enough
 to play a productive role in most multiscale modeling efforts.
Thus electronic structure simulations have struggled to contribute to Sandia's engineering missions,
 and as a result they have not been able to justify regular funding for development and have only fallen further behind.
In the few places where electronic structure is useful,
 Sandia now largely relies on popular commercial simulation software (i.e. Gaussian and VASP).

It is worth noting here that Gaussian is the most popular chemistry/Gaussian electronic structure software
 and VASP is the most popular physics/planewave electronic structure software.
Sandia was simply making the same decision that many other scientists and engineers have made.
I have used them both for multiple projects, and I have no major complaints about them as a user.
To visualize their dominance and in turn the dominance of DFT over semiempirical electronic structure,
 I will display some trends in scientific publications related to electronic structure:

![publications: DFT versus SQM](/assets/DFT-vs-SQM.pdf){:height="100%" width="100%"}

This is based on Google Scholar searches of ["density functional theory"] for DFT,
 [("semiempirical" OR "semi empirical") AND ("electronic structure" OR "chemistry" OR "quantum")] for semiempirical electronic structure,
 and either [VASP], [MOPAC], or ["Gaussian, Inc"] to narrow down the search to specific software.
We can make several interesting observations:

* VASP and Gaussian combined now account for almost half of all scientific papers using DFT.

* DFT is now roughly 3x more popular than semiempirical electronic structure.

* Gaussian is more popular for semiempirical calculations than the most popular special-purpose semiempirical electronic structure software, MOPAC.
  Gaussian implements more semiempirical models than MOPAC,
  but has fewer features that are compatible with semiempirical calculations.

How does this correlate to the actual, practical impact of electronic structure simulations?
I have no idea, and that's probably a difficult question to answer.

My research activity in ab initio electronic structure came to an end in 2014.
I received an offer to convert from postdoc to staff scientist at Sandia on the condition
 that I switched research topics to quantum computing, which had surplus funding at that time.
The position of staff scientist made me eligible for one last funding opportunity in ab initio electronic structure:
 the Department of Energy (DOE) early career award.
I did not apply for this grant with great confidence since funding decisions were partly based on how relevant the research was to Sandia,
 and with electronic structure's unfavorable status at Sandia, I had a hard time even securing a small amount of funds to write the proposal.
Even so, this was my first-ever opportunity to write a long research proposal,
 and it was a useful exercise in collecting a bunch of methodology ideas into a coherent narrative and plan.
As per my grad school ambitions, I proposed to unify the physics and chemistry traditions of electronic structure
 by combining smooth, uniform basis sets with disjoint atomic orbitals,
 improve linear-scaling solver algorithms by combining localized and randomized algorithms,
 and develop a new electron correlation model based on the random-phase approximation (RPA).
The proposal was not funded, and I mostly worked on quantum computing instead of electronic structure
 until I left Sandia in 2018 to pursue better opportunities in electronic structure research.
I will discuss some of my experiences with quantum computing in future blog posts.
While I enjoy quantum computing research and continue to work on it,
 I didn't want it to be my full-time job, and Sandia had no middle ground to offer me.

In returning to electronic structure research, I am abandoning ab initio for a semiempirical approach for several reasons.
Ab initio is too crowded a research area, too entrenched in its methodological practices, and too dominated by commercial software.
In contrast, semiempirical method and software development is almost completely abandoned at this point,
 so there isn't anyone left to be entrenched in a methodology.
While Gaussian has a dominant presence in semiempirical electronic structure, it is because of a shared computational core
 with ab initio electronic structure (i.e. a Hartree-Fock self-consistent field (SCF) cycle based on matrix diagonalization).
If the core of semiempirical electronic structure changes, then Gaussian would lose its first-mover advantage.
It is quite surprising how little development there is in semiempirical electronic structure,
 given how many papers it continues to produce.
For example, there are 300 interatomic potentials in the [OpenKIM database](https://openkim.org/browse/models/alphabetical)
 and over 200 density functionals in the [libxc library](https://tddft.org/programs/libxc/),
 but only around a dozen semiempirical quantum chemistry models (AM1, PM3, PM6, PM7, RM1, MNDO/d, AM1/d, AM1*, OM1, OM2, OM3) developed in the last 40 years.
There have been other semiempirical electronic structure efforts, most notably density-functional tight-binding (DFTB)
 and the Naval Research Lab's tight-binding models, but they don't really add much to a count of models.
My final reason for switching to semiempirical electronic structure is that
 there are fundamental methodological imbalances in ab initio electronic structure
 that are easiest to fix using a semiempirical strategy.

I will end this first blog post with a preview of my semiempirical research plan.
Electronic structure methodology can be organized into three main technical components:
 electron correlation __models__, __basis__ sets and their matrix elements,
 and __solver__ algorithms.
Each component requires approximations that produce errors.
Ab initio electronic structure, especially DFT, operates in a regime where these errors are well-separated:

$$ \epsilon_{\mathrm{solver}} \ll \epsilon_{\mathrm{basis}} \ll \epsilon_{\mathrm{model}} $$

However, if we used more approximate solvers and smaller basis sets, then we might be able to afford more expensive and accurate correlation models.
This could increase the sub-leading sources of error while reducing the largest source of error,
 leading to smaller and more balanced overall errors.
My basic plan for these technical components is as follows (in expected chronological order):

* __Model__ - an RPA correlation model using [cubic-scaling algorithms](https://doi.org/10.1063/1.4855255), which are not that much more expensive than SCF
          calculations when using small basis sets. I will improve the accuracy of RPA correlation and uniquely define a reference mean field
          by using Lagrange-multiplier-based representability constraints in a free-energy minimization
          to repair the largest errors in the approximate 2-electron reduced density matrix.

* __Basis__ - a smooth, uniform basis set with disjoint atomic orbitals results in a pseudopotential-like semiempirical framework
          that enables downfolding of atomic orbitals so that large matrix problems are only defined on a coarse grid.
          The parameterization of matrix elements will be simplified using a semiempirical version of resolution-of-identity tricks
          from ab initio electronic structure to avoid problematic linear dependencies among 2-electron matrix elements,
          which has historically complicated the parameterization of semiempirical models beyond an s+p atomic basis.
          A pseudopotential will be used for the electron-electron interaction to remove many-body wavefunction cusps and the associated
          slow convergence with basis set size.

* __Solver__ - a [localization self-energy](https://arxiv.org/abs/1812.05264) that minimizes the backwards error of localize Green's functions.
           This will be the computational core of a linear-scaling solver that systematically reduces localization errors using a perturbation series
           in the localization self-energy. The computational bottleneck can be moved to a high-order perturbative correction so that the uncertain
           iterative cost of calculating the Green's function and self-energy becomes sub-leading order.

These components are largely semiempirical variants of my old DOE early career proposal with several years of additional refinements.
As this blog progresses, these components will be fleshed out into notes, papers, and software.
