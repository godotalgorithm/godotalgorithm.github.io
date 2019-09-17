---
layout: post
title: "Triage of my Cauchy kernel project"
categories: research
---

This is a post about my latest paper, ["Minimax separation of the Cauchy kernel"](https://arxiv.org/abs/1909.06911),
 which I have just posted to the arXiv and submitted to the
 [SIAM Journal on Numerical Analysis](https://www.siam.org/Publications/Journals/SIAM-Journal-on-Numerical-Analysis-SINUM).
I have wanted to write and publish a math paper for a long time, to signify an increased emphasis in my research
 on the mathematical underpinnings of atomistic simulation.
It has taken me longer than expected to reach this goal because it has been difficult to focus on mathematical work
 that is entirely unrelated to work obligations,
 and my attempts to align employment with this sort of research activity have repeatedly failed.
However, I am an extremely stubborn person,
 and I will persist in my more mathematical work even if my pace is slower than I'd like.
For example, I had to heavily triage my original plan to complete this already massively delayed paper in a timely manner
  by dropping a set of planned applications and saving them for follow-up papers.

I have always enjoyed math a lot, since early in grade school.
It was my favorite subject all throughout high school (I was underwhelmed by my science classes until college),
 and was even on several competitive high school math teams.
I would have been a math major in college (rather than the hedge of a dual math/physics major),
 but I wanted to pursue academic research and was repeatedly told that a math degree could only lead to an actuarial career.
While I strayed from a more mathematical career by going to graduate school for physics,
 my research interests in physics have always been of a highly mathematical nature.
I like to view computational physics as a kind of experimental math,
 where approximations and algorithms are tested for their relevance to physical simulation.
My overly simple grad-school perspective on quantum mechanics was as a physical manifestation of linear algebra,
 which meant that computational condensed matter physics was just a very complicated numerical linear algebra problem.
However, working in quantum information theory for five years have given me a broader perspective
 on the statistical and complexity-theoretic aspects of quantum mechanics.

I discussed the background on this project a bit in a [previous post]({% post_url 2019-05-12-linear-scaling-too-little %}).
Around 2007, I was working on a banded Hermitian eigensolver that was inspired by the physics concept of Wannier functions
 (a.k.a. Boys orbitals in quantum chemistry).
These functions demonstrated that simultaneous spatial and spectral locality was possible,
 which allowed for more flexibility in divide-and-conquer strategies for eigensolving beyond the
 [one that had already been established at the time](https://doi.org/10.1137/S0895479892241287).
In the course of these numerical experiments,
it became necessary to fit low-rank approximations of the Cauchy kernel with a general form

$$ \frac{1}{x - y} \approx \sum_{i=1}^{r} \frac{f_i(y)}{x - y_i} $$

where I was free to choose both $$y_i$$ and $$f_i(y)$$.
For a fixed value of $$y$$, this was a standard linear minimax optimization problem.
I had previously messed around with linear and nonlinear minimax optimization problems
 that I thought would be useful in electronic structure
 (for example, [my paper on rational approximations of Fermi-Dirac functions](https://doi.org/10.1063/1.4965886) originated from earlier attempts during grad school),
 so I already had some experience with problems of this form.
I proceeded as I had in the past, with an ad-hoc implementation of the Remez algorithm.
This time, I could make use of the analytical expressions for Cauchy matrix inverses and determinants
 in fitting the approximant at a set of max-residual points.
It turned out that the relative error was what would lead to the tightest error bounds in
 my intended application, so I adapted my solution to minimize relative error.
I then noticed something very surprising: the location of the maximum residual points did not change when I changed $$y$$.
Because of the Cauchy matrix inverse formula,
 this meant that the optimal $$f_i(y)$$ were rational functions rather than something more general and arbitrary.
Also, I was observing much more regular trends in the solutions than in other problems that I had solved,
 such as the maximum residual points and optimal $$y_i$$ values for different $$r$$ values collapsing
 onto a common function just like with Chebyshev nodes.

I don't keep detailed research records (I've mostly operated under the assumption that published papers are record enough),
 but at some point either in late grad school or early in my academic post-doc at UT Austin,
 I decided that this result was probably optimal with respect to maximum relative error from a basic dimension-counting argument
 (I couldn't see how a more general functional form could reduce the maximum error) and I wanted to prove it.
I'm not really big into proving things because it's hard and you aren't really rewarded for doing so as a physicist.
However, I do think electronic structure simulations need a more rigorous underpinning,
 and there is probably a small set of core results waiting to be discovered that are important enough for a formal proof.
I decided that this was one such result.
My basic proof strategy was to prove separate upper and lower bounds, whereby optimality was proven if the bounds were equal.
I proved the upper bound very quickly because it was a very straightforward task of restricting a minimization to a simple subset of the original domain.
However, the lower bound just kicked my ass and I got nowhere in explaining all the special structure that I observed, so I eventually gave up and put it aside.

I finally put together the lower-bound proof while at Sandia,
 but only after returning to it multiple times for brief but intense bursts of activity.
Around summer 2012, I finally learned about Zolotarev's work in applying elliptic integrals/functions to rational approximation.
This was very exciting at the time, because it explained all of the special structure that I had observed numerically.
I can't imagine how anyone could make the connection from those numerical observations to the theory of elliptical integrals,
 and indeed Zolotarev had worked in the other direction - his adviser, Chebyshev, had instructed him to look for useful applications of elliptic integrals.
Unfortunately, my excitement died down when I realized that none of this made a lower-bound proof any easier,
 although I could now rule out the previously-unexplained structure as being relevant to a proof.
I did eventually cobble together a lower-bound proof as I was exposed to the necessary mathematical ideas while at Sandia.
I worked on an idea for [relaxing classical stat mech problems into linear programs](https://arxiv.org/abs/1603.05180),
 which was itself a catastrophic failure, but it increased my familiarity with convex optimization and linear programming (two linear programs being essential steps in my proof).
Also, I was exposed to many lower-bound proofs of classical computational complexity in quantum information theory
 that were a part of complexity-theoretic separation proofs between classical and quantum computing power.
While none of those proofs were directly relevant, I learned about the wide variety of clever tricks and strategies
 that are often employed in producing lower bounds for optimization problems.
I finally had a serviceable draft of a proof in summer 2017, which I polished up a few months ago for this paper.
I probably could have wrapped this up a lot sooner if Sandia was supportive of my research interests, but it was not,
 and research tends to go a lot slower when you are being paid to do something else as your full-time job.

This is my oldest research project that has been brought to fruition,
 and hopefully it is a sign of maturity and a precursor to other results following suit (albeit very slowly).
My initial proof in summer 2017 was tied to a paper on banded Hermitian eigensolvers,
 and it collapsed under the weight of trying to accomplish too much at once.
Up until three weeks ago, this paper was tied to three applications that would have further delayed it by many months if I hadn't cut them.
I have a natural tendency to make big plans for papers,
 and I need to actively fight that by breaking up projects into smaller publishable pieces.
Having shorter, more numerous papers is advantageous for many reasons,
 and it is almost essential for surviving the rat race of modern academia.

My immediate next research priority is finishing up the first delayed application of this paper to electronic structure calculations.
However, I need to do a better job of mixing blog posts about active research papers
 with other research discussions about other interests that are in a more passive mode.
I'd like to start discuss quantum computing on this blog soon, and I have two quantum computing papers lined up as #2 and #4 in my publication queue.
I also continue to refine and develop my semiempirical electronic structure plans,
 and I will discuss that at some point as well.
I am happy to have finally finished this long-delayed paper,
 but my research agenda and career are very deep in a hole
 and it will take a lot of work before I can escape that hole.
There will be a lot more research triage in my future.
