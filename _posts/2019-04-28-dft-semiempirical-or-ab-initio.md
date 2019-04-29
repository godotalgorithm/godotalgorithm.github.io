---
layout: post
title: "DFT: semiempirical or ab initio?"
categories: nomenclature
---

I'm using this blog for informal, ad hoc discourse, which contrasts sharply
 with the formal, polished writing of my scientific publications.
I am more free to say things that don't naturally fit into a scientific paper, either because they stray too far from
 actual research results, they are too much of a personal opinion,
 or I am simply unable to articulate them in a precise or substantiated enough
 manner for my personal standards of scientific research.
I have plenty to say that should be of interest to people who are interested in electronic structure
 and that also advance the primary goals of this blog: 
 to promote more interest and activity in semiempirical electronic structure and
 to develop, implement, and advertise new semiempirical models.

In this post, I will compare and contrast semiempirical and ab initio electronic structure,
 which includes using density functional theory (DFT) as a convenient and relevant foil.
Much of DFT's great success stems from its ability to reuse or coopt popular and successful ideas
 from both semiempirical and ab initio traditions of electronic structure,
 and it is certainly worthwhile to analyze its success and learn from it.
In my previous post, I referred to DFT as an ab initio method because that is how it is popularly branded.
However, DFT along with many of the non-DFT-specific standard practices
 in ab initio electronic structure simulations are arguably forms of semiempiricism.
Much of this discussion is then necessarily that of nomenclature:
 what do people actually mean when they say "ab initio" or "semiempirical" when referring to electronic structure?

"Ab initio" is Latin for "from the beginning", and the beginning of electronic structure is the many-body Schr&ouml;dinger equation
 (or some variant of a many-body Dirac equation when relativistic effects are being treated).
Historically, ancient atomism was the philosophical pursuit of reducing a description of reality into its most elementary components,
 which were referred to as "atoms", long before modern scientists assigned that name to microscopic particles that they discovered.
Modern science has steadily pushed the boundary of our understanding of physical reality to smaller and smaller length scales.
The quantum behavior of electrons and atoms has been well understood for almost a century now,
 we understand the hadrons inside atomic nuclei quite well,
 and we understand the quarks that make up the hadrons,
 and all of our knowledge of subatomic particles is now well-described by the Standard Model of particle physics.
The lofty goals of ancient atomism continue now in the search for physics beyond the Standard Model.
However, there is a strong separation of scales between the quantum behavior of electrons and the inner quantum workings of atomic nuclei,
 and most of the behavior of the world as we perceive it can be very accurately described, at its core, by electrons
 and a simplified treatment of nuclei as structureless charged particles.
Thus the modeling of electrons and nuclei and equations that govern their behavior can be imagined as an effective
 point of origin for all other physical modeling and simulation of practical relevance.
Of course, most modeling and simulation activities do not need to resolve atomistic details
 and are perfectly well served by classical, continuum descriptions of physical objects
 with parameterized properties fit to experimental information.
This combination of reduced mathematical models and empirically informed parameters is "semiempiricism".
While the practical impact of atomistic simulations is still rather small,
 atomistic details and quantum physics will continue to become more technologically relevant
 as engineering and fabrication at sub-nanometer length scales becomes increasingly more common
 (e.g. in the semiconductor & pharmaceutical industries).

Ab initio electronic structure thus occupies itself with trying to solve the many-body Schr&ouml;dinger equation
 as generally, as accurately, and as efficiently as possible.
In terms of mathematical primitives, it is a partial differential equation where the number of spatial dimensions
 is three times the number of electrons being simulated,
 which has a na&iuml;ve simulation cost that scales exponentially in the number of electrons.
For systems with hundreds or thousands of electrons, this is not tractable without a lot of approximations.
Each approximation reduces costs but increases errors.
The efficacy of approximations can vary from system to system,
 driving a separation into easy-to-simulate systems and hard-to-simulate systems.
For a simulation methodology to be truly "ab initio", we must be able to revert every approximation
 and systematically approach exact solutions to the many-body Schr&ouml;dinger equation.
In this context, "semiempirical" modeling instead commits to a set of approximations,
 and attempts to mitigate their effect through inexpensive, parameterized models of residual errors
 and empirical parameter optimization to minimize errors with respect to some reference data.
I consider all of these research activities to constitute "modern atomism" (i.e. the name of this blog),
 which is the development of methods and models for atomistic simulation that
 provide a range of simulation options with different balances between cost and accuracy/transferability.
As noted in the previous post, most research in this area has polarized into two extremes of
 low cost/low transferability (interatomic potentials without any quantum mechanics at all)
 and high cost/high transferability (ab initio electronic structure), with very few options in between.
Historically, simulation methods and software were developed by experts for their own applications or for use by other experts.
As atomistic simulation software has become more popular, it has attracted many non-expert users, and its use now consumes
 a sizeable fraction of all scientific computing resources
 (e.g. [in 2016, VASP accounted for more than 10% of NERSC supercomputer usage](https://www.nersc.gov/assets/Uploads/2017NERSC-AnnualReport.pdf)).
I (somewhat selfishly) believe that the development and study of atomistic simulation methodology
 needs to be taken more seriously as a science in its own right, now more than ever as its usage grows,
 with one of its goals being the maintenance and validation of a wide range of simulation capabilities designed to maximize the efficacy of non-expert users.

Summaries of the history of electronic structure usually begin with [a quote from Dirac in 1929](https://doi.org/10.1098/rspa.1929.0094):

> The underlying physical laws necessary for the mathematical theory of a large part of physics and the whole of chemistry
> are thus completely known, and the difficulty is only that the exact application of these laws leads to equations
> much too complicated to be soluble. It there­fore becomes desirable that approximate practical methods of applying quantum
> mechanics should be developed, which can lead to an explanation of the main features of complex atomic systems without too much computation.

He went on in that paper to advocate for a specific approximation, Hartree's mean-field theory of non-interacting electrons
coupled to a background of their average electrostatic potential, and discussed the effects of exchange between electrons.
There was a lot of activity at that time in developing approximations to facilitate calculations of quantum systems.
A common feature of early calculations was the use of mean-field theories, but different approaches were used to simplify
 the spatial degrees of freedom of the problem.
[H&uuml;ckel in 1931](https://doi.org/10.1007/BF01339530) used a simple linear combination of atomic orbitals (LCAO) to study pi electrons in small, conjugated, organic molecules.
[Hellmann in 1934](https://doi.org/10.1063/1.1749559) developed the concept of the pseudopotential to remove core electrons from
 calculations of valence electrons for alkali atoms.
While sophisticated electronic structure calculations had to wait until the availability of digital computers in the 1960's,
 the widespread use of Hartree-Fock or Hartree-like mean-field theories, atomic orbitals, and pseudopotentials are rooted in these old results
 and other work from the early days of quantum mechanics.

I have often studied the history of electronic structure to understand the development of computational methodology, both to follow the path
 of successful developments, and to examine historic dead ends and promising ideas that failed to fulfill their full potential.
However, I am not a historian, and I don't claim to offer a complete and fully representative perspective on all of this history.
I recently sought out the first reported "modern" electronic structure computation, which I delineate by the use of matrix factorizations
 rather than (inefficiently) searching for roots of secular equations to solve matrix eigenvalue problems.
This occurred in a paper by [Hoffmann and Lipscomb in 1962](https://doi.org/10.1063/1.1732849) where they simulated boron hydrides
 using a H&uuml;ckel-like model (Lipscomb won the chemistry Nobel prize in 1976 for his experimental and theoretical studies of boron chemistry,
 and Hoffmann won it in 1981 for other theoretical chemistry work).
Semiempirical models thrived in the early days of computational electronic structure
 because limited computing resources forced scientists to work with simple, efficient models
 and semiempiricism enabled these models to maximize their predictive and/or descriptive power.
In chemistry, there has been a persistent effort to develop minimal-basis total-energy LCAO models
 with a small number of parameterized matrix elements.
While there were many variations, the three major model types were the Complete Neglect of Differential Overlap ([CNDO](https://doi.org/10.1063/1.1701475))
 and Intermediate Neglect of Differential Overlap ([INDO](https://doi.org/10.1063/1.1712233)) developed by Pople's group in the mid-1960's
 and the Modified Neglect of Differential Overlap ([MNDO](https://doi.org/10.1021%2Fja00457a004)) developed by Dewar's group in 1977.
While they are now less popular than DFT, MNDO-style models have seen steady development for the last 40 years,
 primarily through the efforts of two alumni of Dewar's group - Walter Thiel and James Stewart.
In physics, semiempirical efforts have been less systematic or persistent, and they were almost completely superceded by DFT.
Marvin Cohen led perhaps the most systematic effort to fit semiempirical pseudopotentials for planewave calculations of
 diamond/zinc-blende semiconductor band structures,
 using [local potentials in 1966](https://doi.org/10.1103/PhysRev.141.789) and improving their accuracy with
 [nonlocal potentials in 1976](https://doi.org/10.1103/PhysRevB.14.556).
In both physics and chemistry, the total amount of development activity in semiempirical electronic structure --
 most of which occurred in the 1960's and 1970's --
 was much smaller than the amount of development activity in ab initio electronic structure that would follow it
 and continue to grow up the present day.

The development of ab initio electronic structure methodology occurred rather independently in physics and chemistry,
 although both had strong ties to their respective semiempirical modeling efforts.
The historic division between physics and chemistry approaches to electronic structure occurred because
 they were each focused on a different minimal use-case: stable few-atom molecules in chemistry and crystals with few-atom unit cells in physics.
Chemistry has pursued the straightforward long-term strategy of using Hartree-Fock mean-field theory
 as the starting point for systematic many-body perturbation theory expansions.
Chemists have developed and maintained atomic basis sets based on contracted atom-centered Gaussian functions
 to enable efficient analytical calculations of all the matrix elements involved in these calculations.
Hartree-Fock theory is a good starting point for simulating stable small molecules because they have a large energy gap for electronic excitations.
However, these calculations are still very expensive, and semiempirical models were developed mainly as simple proxies
 before they could be converged enough (in basis-set size and perturbation-theory order)
 to exceed the accuracy of semiempirical calculations.
Pople, whose central role in this development led to his chemistry Nobel prize in 1998,
 organized this systematic convergence as a hierarchy of nested ["model chemistries"](https://doi.org/10.1103/RevModPhys.71.1267).
Physics has pursued a less systematic and more pragmatic strategy because periodic electronic structure calculations are inherently more expensive.
The use of planewave basis sets and semiempirical pseudopotentials was repurposed for ab initio calculations
 by fitting pseudopotentials to computational data from atomic scattering calculations instead of experimental data.
While it was straightforward to include a Hartree potential into these simulations,
 periodic Fock exchange was both exceedingly expensive and phenomenologically less relevant for periodic systems
 where electronic correlation effects (screening) cause electronic exchange to have a weaker, more localized effect.
To make periodic simulations computationally tractable, physicists were forced to seek out simpler models to approximate missing physics,
 such as using [Slater's model of exchange](https://doi.org/10.1103/PhysRev.81.385) as a density-dependent local potential.

Formally, DFT was developed as a way of encapsulating the complexity of interacting electrons in a local external potential,
 by expressing their total ground-state energy as an unknown but well-defined functional of electron density.
Practically, DFT was a way to connect what physicists were able to simulate --
 non-interacting electrons in the presence of local potentials --
 to what they wanted to simulate -- interacting electrons in the presence of local potentials --
 through the [Kohn-Sham variant of DFT](https://doi.org/10.1103/PhysRev.140.A1133).
Kohn-Sham theory provided a formal rationale and technical refinement of Slater's local model of exchange,
 and it guided the future development of more accurate local exchange-correlation models.
DFT was also an effective vehicle for cross-pollination between the chemistry and physics electronic structure communities,
 which is why Kohn shared the 1998 chemsitry Nobel prize with Pople.
Generalized Kohn-Sham theory and "hybrid" functionals allowed chemists to use DFT to improve the accuracy of
 their Hartree-Fock-like calculations without having to use many-body perturbation theory.
The benefits of DFT didn't come for free: chemists were forced to evaluate and integrate DFT-related quantities on numerical grids
 even with Gaussian atomic orbitals, and physicists in turn were pushed to implement the more accurate hybrid functionals
 and confront both the large cost of periodic Fock exchange and the limitations that they revealed in simpler density functionals.

In administering any sort of "ab initio purity test" to DFT, it is important to first address the broader adherence to the ab initio ideal.
None of the available computational methodologies or software are able to systematically remove all sources of error without bound.
The practical, working notion of "ab initio" is that many methodologies and software allow for enough systematic refinement
 to exhaust most computational budgets for problems that are large enough to be interesting.
There are limits, but they can often be ignored.
However, they shouldn't be forgotten.
A few of the more basic and pervasive issues:

* Gaussian basis sets are pre-tabulated, so you cannot approach the complete basis set limit indefinitely without building your own basis sets.
  Furthermore, their convergence is not guaranteed in scenarios where electrons have nontrivial density far from any atom, which can occur in
  uncommon physical situations (e.g. electrides). Finally, large Gaussian basis sets have substantial ill-conditioning problems for crystals
  and other condensed systems that complicates their convergence.

* Planewave basis sets are orthogonal and systematically improvable, but their practical convergence relies on the use of pseudopotentials,
  which are not so easy to improve or converge systematically. There has been progress towards pseudopotential formalisms which have more
  direct, constructive connections to an all-electron solution (e.g. the [projector-augmented wave method](https://doi.org/10.1103/PhysRevB.50.17953)),
  but like Gaussian basis sets there is a general reliance on a limited set of pretabulated pseudopotentials.

* Many-body perturbation theory is often used outside its formal radius of convergence (which is very expensive to determine),
  so it may not actually converge. Non-perturbative
  many-body methods such as coupled-cluster theory do not have a clear radius of convergence, but their behavior and numerical convergence
  can become erratic when Hartree-Fock theory is a poor starting point. Variational methods such as truncated configuration interaction
  are numerically well-behaved but not size-consistent, which causes problems with systematically converging in the amount of truncation.

* Many-body Green's function methods are formally exact, but their theory does not prescribe a clear hierarchy of systematically improved calculations.
  There are many ad-hoc approaches used in practice, and this produces a practical error bar to the methodology
  between conceptually equivalent results that can be surprisingly large.

Compared to all of this, the most glaring mark against DFT's ab-initio-ness is probably that almost every single density functional in practical
 use has a component that is semiempirically fit to reference data on the uniform electron gas (i.e. the local density approximation).
This is computational data on a simple model system ([Ceperley and Alder's diffusion Monte Carlo results](https://doi.org/10.1103/PhysRevLett.45.566))
 rather than experimental data on a physical material, but it still a form of semiempiricism.
DFT has a [prescribed hierarchy](https://doi.org/10.1063/1.1390175) of nested models with increasingly expensive ingredients,
 which allows it to adhere to the practical "ab initio" notion of exhausting computational resources,
 even if the hierarchy is finite (the random-phase approximation (RPA) is at the top of this hierarchy, and it is too expensive for regular use)
 and not as well-defined as perturbation theory (only model ingredients are prescribed, not how they are used).
I personally consider the "ab initio" label as being more aspirational than a strict reality
 for the present state of computational electronic structure, and DFT certainly aspires to it as much as anything else.

I have been long-winded in answering the question posed at the beginning of this post,
 but that is because it could only be answered with sufficient context about the history of electronic structure simulations.
I would characterize DFT, along with the rest of electronic structure, as aspiring to the ideal of being ab initio
 while being semiempirical in nitty-gritty details (i.e. many design choices that only make sense in the context of observed phenomenology).
In chasing the ab initio ideal, scientists have been pushing the envelope of what can be simulated for over fifty years
 and expanding their ambitions to fill available computational resources.
This has included algorithmic improvements and software optimization,
 but largely confined to the context of established methodology and software.
Some improvements such as linear-scaling solver algorithms have been conceptually appealing,
 but have failed to achieve practical success and adoption because they don't function well in the regime that ab initio electronic structure
 typically operates (e.g. large basis sets and high solver accuracy being the sources of difficulty for linear scaling).
As expanding computational resources have enabled larger simulations, the distinction between the interests of physics and chemistry
 continue to blur since the difference between a large molecule and a crystal with a large unit cell becomes an increasingly irrelevant boundary effect.
At some point, it may make sense to re-evaluate the basic, foundational design choices of electronic structure simulations
 such as their basis sets, solver strategies, and "native" mean-field theory,
 but that will require overcoming a large amount of intellectual inertia and limited availability of funding.
I have recently begun carrying out such a re-evaluation for semiempirical models,
 where the technical overhead is much lower and development timescales are much shorter.
If I am successful, perhaps a new generation of semiempirical models will become
 the precursor to a new generation of ab initio electronic structure,
 echoing the history that I have summarized in this post.
