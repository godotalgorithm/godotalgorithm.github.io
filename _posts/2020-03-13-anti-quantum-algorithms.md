---
layout: post
title: "Anti-quantum algorithms"
categories: research
---

It has been about 6 months since my last blog post.
I have been busy since then with various projects, both associated with my job and my personal research program,
 but I haven't had any bloggable results until now.
I had intended to start blogging more on thoughts and opinions that aren't connected to research results,
 but my thoughts got caught up in a slow-burning existential career crisis that I didn't really want to blog about until they had converged.
I will be discussing these thoughts in my next blog post in the near future.

I'd also like to briefly take stock of how what I've actually been up to matches the plans that I articulated in my last blog post.
I noted a queue of 4 planned papers.
The first paper was an electronic structure application of the Cauchy kernel paper that was the subject of my last post.
I ended up putting that on hold,
 but I will now be finishing that up for the SIAM Annual Meeting in July (I was invited to present a talk and hopefully the conference won't be cancelled).
The second paper was a final revision of the [quantum Metropolis algorithm paper](https://arxiv.org/abs/1903.01451) that I presented at the 2019 APS March Meeting.
I heavily revised the paper and improve it substantially,
 but I uncovered an important technical problem at the end of the revision process
 (the repeat-until-success loop of the algorithm has a fat tail of success probabilities that can cause a divergence in average run times)
 that will necessitate yet another major revision later this year.
The third paper was a very old project on designing molecules with extremely low ionization potentials,
 which I resumed technical work on but had to pause as the 2020 APS March Meeting grew closer.
The fourth paper is the subject of this blog post.
As suggested by this mismatch between intent and outcomes,
 scientific research is often fraught by large uncertainties and frequent delays.

This post is mainly about my latest preprint, ["Robust decompositions of quantum states"](https://arxiv.org/abs/2003.04171),
 which I was planning to speak about at the 2020 APS March Meeting before it was cancelled because of the global coronavirus outbreak.
I'm trying to make the best of this situation, and I've instead [recorded my talk on YouTube](https://youtu.be/sUka7hj5e_E).
Perhaps it will eventually reach a wider audience than it would have at the conference.
Indirectly, this project has an exceptionally long history.
I started trying to develop new computational methods for simulating quantum many-body systems before I even started graduate school in 2002.
Like many of my research passions, I had a lot of enthusiasm, lofty goals, and high standards, which resulted in a steady stream of failed ideas for years on end.
I was particularly obsessed with trying to solve the 2D Hubbard model,
 which was and still is an important, unsolved model of strong electron correlations and possibly electron-mediated superconductivity.
My modus operandi at the time was to focus on whatever methodological idea seemed promising at the moment,
  mess around with it and stress test it in some way until it inevitably broke,
  and then brainstorm up a new idea to focus on that was informed by the past failures.
At times, the churn on this approach became super high, and ideas sometimes wouldn't last more than a day.
Those were fun times, but I wasn't able to produce papers from this process, which I eventually acknowledged to be a serious career problem.
As a post-doc, I decided to commit to one last, best idea for treating strong quantum correlations that only produced [an incomplete preprint](https://arxiv.org/abs/1003.2596)
 after the preliminary numerical results that I generated turned out to be absolutely terrible.
After that, I stopped working on strong-correlation methods and started working on more modest weak-correlation methods based on the random-phase approximation (RPA).
My RPA work was a lot more successful, and I ended up with [a published paper](https://doi.org/10.1063/1.4855255) that I am still quite proud of.
Unfortunately, I had to stop working on RPA methods when my funding for electronic structure research at Sandia National Labs suddenly dried up,
 and I was pushed into working on quantum computing research instead.

Working on quantum computing research at Sandia National Labs was a frustrating experience.
I was very interested in developing simulation methods for quantum systems,
 but funding for electronic structure research in very pragmatic and heavily applied environments like Sandia and the other DOE weapons labs (Livermore and Los Alamos)
 has been on a long slow-and-steady decline because such methods just don't have enough practical value.
One of the big rationales for quantum computing, both at Sandia and more broadly,
 is to improve our ability to simulate quantum systems,
 but it is absolutely bizarre, counterintuitive, and counterproductive that we would be increasing our investment in developing
 quantum algorithms for quantum computers that we don't have yet while steadily decreasing our investment in developing classical algorithms
 for classical computers that we have plenty of and are arguably using very inefficiently.
As a trendy research topic, quantum computing gets the benefit of the doubt, while the older and no-longer-trendy topic of electronic structure doesn't anymore.
It is especially bizarre given that researchers generally agree that
 (1) a lot of methodology is shared, so that improvements to classical algorithms will have residual benefits for quantum algorithms,
 (2) quantum computers will likely supplement or accelerate simulations that mostly occur on classical computers, and
 (3) the benefits of quantum computers for quantum simulation are asymptotic in accuracy and system size,
 so they might not have any benefits at all for the accuracies and system sizes that people normally deal with.
While I learned about quantum algorithm development and made numerous attempts at developing new quantum algorithms at Sandia,
 I also tried my best to inject classical algorithm development wherever I could get away with it.
This was also an excuse to return to research in strong-correlation methods, now considering a broader set of tools and ingredients
 including classical algorithms, both deterministic and stochastic, and quantum algorithms.

I did not have a clear agenda or program of research when I started working in quantum computing.
At first, I spent a lot of time just learning the subject and catching up with several decades of research.
Eventually, after a period of more exploratory efforts, I settled into a program of quantum computing research
 that I have now carried with me beyond my time at Sandia.
The premise is that someday, once we finally have large digital quantum computers in a few decades or so,
 we will carry out atomistic simulations containing both classical and quantum degrees of freedom
 that are distributed over classical and quantum computers.
I am interested in delineating these classical/quantum boundaries in both simulation and computation:
 (1) what degrees of freedom should be treated classically, semi-classically, or fully quantum mechanically and
 (2) how should we partition the simulation between classical and quantum computers and how should they be coupled together?
My approach to resolving these boundaries right now is a two-pronged attack
 aimed at developing better classical algorithms to push on the classical side of the boundary
 and better quantum algorithms to push on the quantum side of the boundary,
 so that the boundary is resolved evenly from both sides.

The quantum side of this research program is much farther along, as it was developed first.
For now, it mainly consists of two parts: quantum error correction (QEC) algorithms and quantum Metropolis algorithms.
The overall cost of quantum computing depends on multiple layers: the underlying physical qubit technology,
 the QEC layer, and the algorithms layer.
For reasons of long-term career stability, I am very loath to commit to a specific physical qubit technology,
 so I've instead focused on the other two layers.
I wrote several papers on QEC at Sandia, and I find the topic to be very interesting, but it just isn't a very popular research topic right now.
While I have a lot of ideas for future projects, my QEC research has been on hold for several years now,
 and I don't plan to return to it until a logical qubit has been experimentally realized.
My interest in QEC is now more about patenting essential components of future quantum computers rather than purely academic curiosity,
 and there is no point in starting a patent clock in a world without logical qubits.
Instead, I've been working on quantum algorithms for preparing thermal states.
This started at Sandia, where I tried to develop a quantum analog of the Langevin thermostat.
The development of a quantum Langevin thermostat turned into a horrible technical slog (that I might eventually recount in this blog),
 but it eventually evolved into the development of a quantum Metropolis algorithm that I released a [preprint](https://arxiv.org/abs/1903.01451)
 on shortly before starting this blog.
The quantum Metropolis algorithm is very promising but still has a few outstanding technical problems,
 and I expect to finish it and release a final version of the paper later this summer.

The classical side of this research program also started at Sandia, but it was much slower to develop.
The basic premise of the project was that noise and uncertainty in quantum systems must inevitably drive them to some kind of classical limit
 that is described by classical physics and is efficient to simulate on classical computers.
As quantum systems are driven towards that limit, they should become easier to simulate on classical computers even while retaining much of their quantum identity.
There are some very nice results in quantum information theory that embody this concept very clearly.
Perhaps the best example are quantum stabilizer circuits (Clifford gates with qubit preparation and measurement operations)
 that include T gates (a non-Clifford gate that enables universal quantum computation) with polarizing noise.
When the noise in the T gates is smaller than a known threshold,
 the noise can be "distilled" away to a negligible amount using a process known as magic state distillation,
 which is an important ingredient in many plans for digital quantum computers.
As the threshold is approached, the efficiency of magic state distillation drops to zero (a diverging number of noisy T gates is needed to distill out a low-noise T gate).
When the noise is at or above the threshold, these circuits can be efficiently simulated on a classical computer
 and are no longer capable of universal quantum computation.
While this is a very compelling result, it has very little to do with physical quantum devices or any applications other than QEC.
With a lot of popular interest in using noisy quantum devices for quantum simulation tasks without any QEC,
 I wanted to develop a comparable result that was relevant to simulation (i.e. showing that noise made quantum simulation tasks easier for classical computers).
For a long time, this project was too hung up on trying to model specific instances of analog quantum simulators,
 but realistic noise is messy and does not directly make systems easier to simulate.
In fact, a lot of experimental noise is actually very difficult to model and simulate,
 and makes some noisy quantum systems even harder to simulate than their idealized versions.
I finally started to make progress when I gave up on realistic physical noise
 and decided to design noise that was tailored to making quantum systems easier to simulate.
This noise was based on qubit measurements, which introduced a stochastic component that effectively made it a type of quantum Monte Carlo method.
I had always discounted stochastic algorithms in my previous attempts at developing strong-correlation solvers
 because of the inherently high cost of reducing sampling errors,
 but here it was natural and inevitable in mimicking the capabilities of quantum computing hardware.

In a way, the development of classical algorithms to simulate quantum systems by introducing noise that saps them of their inherent quantum computing power
 is kind of like developing "anti-quantum" algorithms, at least for the purposes of a catchy title for a blog post.
As I will discuss more in my next blog post, I now feel a strong need to consolidate my research into a more narrowly focused technical path.
My end goal on the timescale of several years is still to develop a new generation of semiempirical models,
 but that research area is extremely unpopular now (making it impossible to get any sort of support for it or career benefit from it)
 and in need of a major technical overhaul.
Right now, I believe that further developing the results of this project, both the theory and software implementation,
 will both help with the technical overhaul of semiempirical models (by distinguishing between Hamiltonian model errors and correlation model errors)
 and be a direct benefactor of it (by gaining access to simple model Hamiltonians that are quantitative representations of real molecules and materials).
I'm trying to balance my research program so that it aligns as much as possible with what I want to work on and what I believe to be the best science that I am capable of doing
 while also maintaining connections to popular research topics that give me a better chance of eventually finding financial support to sustain a research career
 that is presently in a slow but inevitable decline.
