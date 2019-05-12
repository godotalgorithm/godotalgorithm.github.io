---
layout: post
title: "Linear-scaling electronic structure: too little, too late"
categories: [history,editorial]
---

This is the first instance of a tradition that I expect to maintain as long as I am actively writing for this blog:
 editorializing my research papers as they are published to provide more context for why I wrote them and what they mean to me.
My latest paper, ["Assessment of localized and randomized algorithms for electronic structure"](https://doi.org/10.1088/2516-1075/ab2022),
 just became available online with a citable DOI.
Sometimes I will write about papers when they are published in a journal, such as in this instance,
 and other times I will write about papers shortly after I post them to [the arXiv](https://arxiv.org).

This particular paper is special to me for several reasons.
First, I have been extremely interested in linear-scaling electronic structure algorithms since just after starting grad school in 2002.
I've initiated multiple projects on the subject over the years,
 but they were always too risky and too ambitious to matriculate successfully into published papers.
These projects have at least done a lot to shape my opinions and views on the subject,
 and I've left a few unpublished papers languishing on the arXiv that serve as breadcrumbs along a trail.
Second, this is the first proper electronic structure paper that I've published since being forced out of the field in 2014
 because my funding in the area was cut.
I do have [a paper from 2016](https://doi.org/10.1063/1.4965886) on rational approximations of the Fermi-Dirac function
 that was effectively a short prelude to the present paper, which I had originally intended to write several years ago.
Before I got the boot, which I knew was coming, I wrote [a paper in 2013](https://doi.org/10.1063/1.4855255) on fast algorithms
 for random-phase approximation (RPA) calculations, so that I could end my active research period in electronic structure
 with a paper that I was very proud of.
My research career hasn't exactly gone smoothly, but I feel like my electronic structure research agenda is back on track
 with a newfound sense of purpose.

My interest in linear-scaling electronic structure began with my gung-ho, bigger-and-better attitude upon starting grad school.
I was very fortunate to have a solid undergraduate research experience that prepared me well for computational science
 research, and I was eager to do research related to atomistic simulation.
[Stephan Goedecker's review](https://doi.org/10.1103/RevModPhys.71.1085) of linear-scaling electronic structure research in the 1990's was still relatively new,
 and I tried to learn everything about the subject by carefully going through it and following references through the literature.
Ultimately, I decided on an ambitious technical approach to treat this as much as possible like a numerical linear algebra problem,
 since the core technical problem was to perform traces of functions of sparse-matrices while avoiding eigenvalue decompositions.
Trying to follow a reductionist strategy, I focused my effort on developing a new elementary transformation for manipulating sparse matrices.
The canonical problem with transforming sparse matrices is that you inevitably incur fill-in of the matrix that quickly spirals out
 of control and produces dense matrices long before the problem is solved.
I interpreted this as the outcome of a "greedy" solver strategy, since any single elementary transformation (e.g. Given's rotation or Gaussian elimination step)
 was usually very simple, very inexpensive, and only appeared to make the sparsity pattern slightly worse.
Instead, I performed some numerical experiments on very general but localized transformations (i.e. mostly identity)
 of the form

$$ A' \approx X^T A X $$

where $$A$$ is sparse and symmetric (but not positive definite), $$X$$ is the numerically optimized local transformation,
 and $$A'$$ is the new sparse matrix with a specified target sparsity pattern but variable matrix elements.
While any one optimized sparsity-preserving transformation would be more expensive than other elementary matrix transformations,
 they would prevent costs from spiraling out of control as matrices would otherwise become more and more dense.
These numerical experiments showed that you could diagonalize rows and columns in $$A'$$ without creating new fill-in,
 with errors that appeared to decay exponentially in the number of matrix elements that I allowed to vary in $$X$$.
However, the numerical optimization of these transformations turned out to be very ill-conditioned as the transformations
 became more accurate, and there were basic arguments suggesting that this relationship was inevitable.
Also, I couldn't come up with a theoretical framework to explain the numerical behavior I was seeing.
I did write this up as my very first attempt to publish a research paper in grad school,
 but it was rejected by referees and I let it [languish on the arXiv](https://arxiv.org/abs/math/0505157)
 because I didn't know what else to do and received no advice on an alternate course of action.

My interest in linear-scaling electronic structure and numerical linear algebra did not end with that failure.
I was quite committed in grad school to the linear-algebraic approach to the problem, so I decided to work on easier
 open problems in numerical linear algebra to prepare myself for future efforts in sparsity-preserving matrix transformations.
The new problem that I focused on was a banded Hermitian eigensolver, since the tridiagonal case had been solved in the mid-1990's.
I also saw this as an opportunity to mathematically formalize the concept of Wannier functions in electronic structure theory,
 again pursuing an agenda of treating physical concepts in a more mathematically careful manner.
By the time I graduated, I had a basic plan for a banded Hermitian eigensolver and some numerical experiments demonstrating that the plan was reasonable.
However, I was still in a bit over my head as there were key technical results that I had numerical evidence for but lacked an ability to prove.
I finally managed to prove the most basic and tricky result in summer 2017,
 but it was part of a paper that stalled out as I became more and more distracted by planning my exit from Sandia.
Recently, I have revisited this proof, and it will now be the main result of my very next paper (in preparation)
 that I will probably discuss on this blog in the not-too-distant future.
I hope to finally finish developing my banded Hermitian eigensolver at some point in the next few years.

So, my interest in linear-scaling electronic structure ended up getting diverted into other technical pursuits.
Meanwhile, there haven't been any major advances in linear-scaling electronic structure research for the entire time that I've been interested in it.
I've tried to rationalize and quantify this opinion by measuring publication rates in Google Scholar:

![linear-scaling literature data](/assets/linear-scaling.pdf){:height="100%" width="100%"}

Here, I'm plotting papers mentioning ["electronic structure"] versus ["electronic structure" AND ("linear scaling" OR "scale linearly" OR "scaling linearly")],
 which shows that interest in linear scaling is growing with the activity in the field of electronic structure as a whole
 and has even become a larger fraction of papers with time.
However, when this is compared against the rate of citations to three major linear-scaling electronic structure papers --
 [Weitao Yang's divide-and-conquer paper](https://doi.org/10.1103/PhysRevLett.66.1438) that popularized the topic,
 [Walter Kohn's paper](https://doi.org/10.1103/PhysRevLett.76.3168) on the nearsightedness of electrons,
 and [Stefan Goedecker's review paper](https://doi.org/10.1103/RevModPhys.71.1085) --
 it shows that the literature associated with linear-scaling solver algorithms isn't growing at all.
This is mostly explained by a combination of papers superficially mentioning the concept of linear-scaling electronic structure,
 often noting its conceptual importance,
 and papers discussing other linear-scaling electronic structure algorithms not associated with solvers,
 such as Fock matrix construction and localized electron correlation methods in quantum chemistry.
On the software side, there are no popular or widely used linear-scaling electronic structure simulation codes.
Perhaps the two oldest and most established efforts are ONETEP, a commercial code related to CASTEP,
 and CONQUEST, which has been promising an as-yet-unfulfilled a public release for over a decade now.
They each get fewer than 100 mentions in the scientific literature per year,
 which is far behind the most popular electronic structure codes.

My first linear-scaling electronic structure paper does not contain any new, notable results in numerical linear algebra.
It is a much more mundane work, partly a review, partly some modest brainstorming about future solver concepts,
 and an attempt to compare some competing technical ideas (randomized and localized algorithms)
 that quite surprisingly had never been directly compared before.
My younger, more idealistic self would probably have seen this as a waste of time,
 but I wanted to demonstrate that I am knowledgeable in this research area
 and try to nudge it in a slightly better direction even if I had no amazing technical breakthroughs to report.
It also just grew organically from a phase that I went through while I was at Sandia of attemping to write Comments
 for Physical Review Letters, which was mostly just me venting frustration for my lack of research funding in electronic structure.
Unsurprisingly, my targets were related to trendy research areas that had diverted money away from electronic structure at Sandia
 ([machine learning](https://arxiv.org/abs/1208.1085) and [quantum computing](https://arxiv.org/abs/1310.6676))
 and [linear-scaling electronic structure itself](https://arxiv.org/abs/1311.6576).
I wrote 3 Comments and got 1 published, before I decided (and was convinced by others) that this was not a productive activity.
The body of scientific publications is just too large to bother pointing out errors except in the most egregious of cases.
I think it was somewhat worthwhile in my case because it has helped me to shape my self-criticism
 (sharpening it in some areas but relaxing it overall after realizing that other, successful scientists have much laxer standards that I do)
 and was temporarily effective at venting frustration.
It was the final Comment on stochastic linear-scaling DFT that formed the seed for my paper.
While it was eventually rejected (relevance standards for Comments are very high), the editors strongly encouraged that I develop
 my benchmarking and analysis of different electronic structure solver algorithms into a full paper.
It took 5 years to finish, since my research efforts during that time were mostly shifted to quantum computing,
 but I got it done in the end.
I think the paper's essential message also nicely distills down to a very basic research lesson
 that if a field of research is unable to measure progress (in this case meaningful computational benchmarks),
 then it will not be able to make progress.

Because I mostly work alone on research (although I would love to collaborate with like-minded people),
 I have found that I am most productive when I successfully "flatten" my research plans
 into an ordered sequence of projects and papers with a clear and self-convincing rationale for the ordering
 (i.e. inter-dependence and relative importance).
I'd then like to end this post with a preview for my next paper,
 which I've been actively writing for about a month now, and some related concluding thoughts.
In [Goedecker's review](https://doi.org/10.1103/RevModPhys.71.1085) of the active period (1991-1999) of linear-scaling electronic structure research,
 he concluded that

> O(N) methods have become an essential part of most large-scale atomistic simulations based on either tight-binding or semiempirical methods.

However, that opinion was not reflected in any capability or feature of any simulation code that was available at that time,
 and linear-scaling solvers still have very limited applicability and availability 20 years later.
Goedecker was certainly correct that the available algorithmic concepts were more readily applicable to tight-binding/semiempirical models,
 but he assumed it to be an inevitable foregone conclusion that simply didn't ever happen
 (which is perhaps a result of *everyone else* thinking that way, too).
I now very much want to make this happen,
 and most of my planned papers are now organized around key technical components of the semiempirical simulation software that I have envisioned.
While most of these papers will be narrowly focused on this goal,
 my very next paper is a little different.
As I mentioned in this post, I have a long-overdue theorem/proof that I am finally preparing for publication.
While the theorem/proof is about a rather esoteric problem, low-rank approximations of the Cauchy kernel,
 it is directly related to thoroughly optimizing and finalizing
 the function approximations that will be at the heart of future linear-scaling electronic structure solvers.
It also encompasses and concludes my [earlier effort](https://doi.org/10.1063/1.4965886) to numerically optimize rational approximations of
 the Fermi-Dirac function into a slightly larger and mostly analytical approximation framework.
As I work through this next project, I am going to experiment with a radically open research style
 and present unpublished work in progress on this blog.
