---
layout: post
title: "Writing rigorous math papers is very time consuming"
categories: research
---

Once again, it has been about 6 months since my last blog post.
I really need to work on posting incrementally about research in progress,
 otherwise this blog will frequently have large gaps when I'm working on longer projects.
Also, the isolation from the coronavirus pandemic has caused me to reflect a lot more on career problems and plans,
 and the views expressed in [my previous post]({% post_url 2020-03-27-career-hopelessness %})
 have undergone some important revisions.
I will blog about that some more in the near future.

This post isn't about a new project or paper,
 but rather the revisions to the low-rank approximation paper that I submitted for publication towards the end of 2019
 and [blogged about]({% post_url 2019-09-16-cauchy-kernel-triage %}).
Much to my surprise, I got the reviews back for the paper in late January.
The timescale of mathematical publication is notoriously slow,
 so I didn't expect to hear from the journal for at least 6 months.
I was initially given until the end of March to revise the paper,
 but I didn't even start the revision process until after I finished my last paper for the 2020 APS March Meeting.
I was able to get multiple extensions from the journal, but eventually they gave me a hard deadline on October 1st.
It has been a long and tiring journey from the first to the [second version of this paper](https://arxiv.org/abs/1909.06911),
 and I feel like I've grown as a mathematician in the process.

As I previously discussed, the first version of this paper was heavily restricted in scope compared with my original plans for it.
There were three intended applications that were dropped, and the central proof of the paper was a touched-up version of a proof
that I wrote several years ago.
My focus in preparing that proof for publication was correctness rather than clarity,
 and it resulted in a terse and hard to understand final product.
Also, part of that terseness was minimizing the amount of time devoting to discussing external results that the proof relied upon,
 partly because I did not fully understand those external results.
While it was a much better proof than every previous attempt I had made,
 it still wasn't very good in any objective sense, but it was the best outcome I could produce with the effort I could afford to expend on it.

If I thought it was appropriate, I would post the two referee reports that I received.
However, referees retain copyright, and it would be inappropriate for me to post them without permission,
 which I simply cannot obtain from anonymous referees.
What's important is that I consider them to be fair mathematical assessments of the paper.
They were intrigued by the central theorem of the paper, found the central proof very difficult to understand,
 and were not that interested in the remaining content of the paper outside of the central theorem and proof.
I felt like I had a strong opportunity to obtain the approval of these referees
 if I reworked the central proof into a more readable form,
 and I enthusiastically embarked on paper revisions after the 2020 APS March Meeting.

Revising this paper also meant revising my expectations on what constitutes good mathematical writing.
According to my previous expectations, the original version of the paper was "good enough",
 and whatever my new expectations were to be, that paper could no longer be "good enough".
There were completeness, notation, and organizational problems.
The original, terse version of the proof made some terse arguments that would actually take a lot more space to justify thoroughly.
For example, I defined optimization problems over closed domains that I could explicitly solve for most but not all elements in the domain.
I decided to simply remove the problematic elements, since their contributions to the set of possible optimizers could be recovered
 from limiting arguments - "nearby" elements would contribute very similar values to the set of possible optimal values.
However, a truly rigorous proof would either have to show that the contribution of these discarded elements were recovered
 or at least cite something that showed this to be true for a general enough class of problems that this specific case was covered.
When considering the amount of space such an argument would take, that no longer seemed like a good proof strategy at all.
Also, I got way too eager to define a zoo of auxiliary variables and didn't clearly explain what they were useful for.
However, the trickiest aspect of the revision was deciding how to break up the proofs using intermediate lemmas.
This is a canonical aspect of mathematical writing - breaking up a complicated argument into smaller, technically distinct pieces
 to make the argument more understandable.
Sometimes those intermediate steps are interesting and useful in their own right, and sometimes they are just a means to an end.
I struggled with this the most, as I had to work through trial proofs for each of the possible intermediate lemmas that I considered,
 and it took many attempts to find one that made the cleanest separation between the lemma's proof and the central theorem's proof
 that would depend on the lemma.
Right now (pending further revisions to my math writing expectations), I'm quite happy with the end result,
 but I'm not happy with just how long it took to get there.

I'm not completely happy with everything in the revised paper.
The paper is about an optimization problem,
 and I strengthened up the formal results of the paper to rigorously characterize optimal solutions.
This made it feasible to solve the optimization problem numerically,
 and I dived into writing a numerical solver to add to the paper.
Unfortunately, that was its own time sink.
With priority given to cleaning up the theorems and proofs, I didn't give the numerical solver the time it needed to develop fully.
What ended up in the paper is the third completed version of a numerical solver,
 which was a massive improvement to the previous two versions,
 but just managed to stumble into an uncanny valley where it was just good enough to clarify what the remaining technical problems were
 without actually being able to solve them.
Unfortunately, I just ran out of time for a fourth version, so I cleaned up what I had before the resubmission deadline.

With this experience behind me, I feel like the revised paper is now legitimately my "first" math paper,
 but that feeling might not survive the next round of the review process.
Outside of further revisions, I'm done with math research for the foreseeable future.
While I have unfinished math projects and plans for future math research,
 I just don't have the time to pursue this kind of work right now.
A lack of research resources has consequences, even for theorists.
If you don't financially support an experimentalist, then they just can't afford to run a lab, and all research quickly grinds to a halt.
With theory work, the most valuable resource is a theorist's time.
I want to spend as much of my time as possible on research, but my full-time job is not a research job,
 and it has obligations that frequently divert my time and attention from research.
I can pretend that I can effectively carry out two full-time jobs, but in reality everything suffers as a result.
I wish that I could afford to focus exclusively on research right now, but I simply can't,
 or at least not without throwing away my financial future.

So, what comes next?
I'm trying to escape the death spiral of my research career.
So far in my career, none of my research has generated enough interest to expand my future resources and opportunities,
 which has lead to a negative feedback loop of dwindling resources and opportunities.
For example, this math project and paper originated from my personal interest in a problem
 and my beliefs about its future utility to my research.
It wasn't some big open math problem that lots of people cared about,
 and very few people are going to care about it or understand it.
Unfortunately, I now see that such research predilections are quite fatal in the long run to a research career,
 and my run has been long enough that I can really feel it dragging me down to the bottom now.
Next, I'm going to try something different for a while.
I'm going to prioritize research based on how I think others might value it.
Specifically, I'm going back to quantum computing research, which I consider to be overhyped and overvalued.
My plan is to patent new quantum error correction (QEC) protocols that will be essential to future digital quantum computers.
Of all my research interests, this is the one with the most immediate and explicit possible value.
For once, I'll attempt to play into excessive hype and overvaluation by trying to sell something for more than it is truly worth.
In upcoming blog posts, I will rant some more about career issues,
 offer my somewhat negative perspective on quantum computing in general,
 and discuss these QEC plans further.
