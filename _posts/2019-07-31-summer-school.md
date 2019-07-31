---
layout: post
title: "Teaching at a summer school"
categories: education
---

The Molecular Sciences Software Institute (MolSSI) where I work runs a summer school every other year
 to help computational chemists who are just starting research with the basics of modern open-source software development
 (e.g. Git, Github, Python, documentation standards, continuous integration).
Much of this teaching is organized around domain projects, one based in quantum mechanics (QM) and the other based in classical molecular mechanics (MM),
 so that students learn in the context of scientific concepts that they are somewhat familiar with and that is related to their research.
This year, I was tasked with creating the QM project.
I don't consider myself to be a very good teacher and I'm still not an expert at many of the modern tools and practices that were being taught at the summer school,
 so I was somewhat hesitant to do this.
I did ultimately agree to do it, and I used this task as an opportunity to fill in some of my knowledge gaps and also to push my research agenda a bit.

The 2017 MolSSI summer school used a QM project that was derived from preliminary versions of the [Psi4NumPy tutorials](https://github.com/psi4/psi4numpy).
There were pros and cons to this approach.
It encapsulated most of the mountain of complexity that is modern Gaussian-based quantum chemistry inside of Psi4 and its convenient Python wrapper
 so that students could focus their attention on a few of the key computational tasks such as the self-consistent field cycle of a Hartree-Fock calculation.
This is in many ways consistent with the practical realities of most computational chemistry research - not too many people poke at the low-level guts
 of either quantum chemistry software or theory, it is taken as a given by most people for most projects.
However, I wanted to give students some exposure to QM as something that can be made simple and self-contained and fully rationalizable,
 just so that they can have a simple proxy in their minds when working with more complicated QM software and theories in the future.
It would also be more consistent with our MM project, which is a self-contained Metroplis-based Markov-chain Monte Carlo simulation of a Lennard-Jones potential.
Unfortunately, it is difficult to make a QM calculation as simple as an MM calculation.

Of course, building a simple QM model and simulation software was a good chance to mess around with semiempirical electronic structure.
It was also very appropriate for the setting.
The MolSSI summer school was hosted this year at the Texas Advanced Computing Center (TACC), which is located right next to the Mopac Expressway.
MOPAC is also the name of the most popular special-purpose semiempirical quantum chemistry code, which is a pun rather than a coincidence.
MOPAC was developed in the early 1980's by Jimmy Stewart while working in Michael Dewar's group at UT Austin.
My QM project is far, far more modest than MOPAC, the goal being to simulate clusters of Argon atoms so that we could couple the QM project
 with the Lennard-Jones-based MM project as an exercise in QM-MM coupling using the [MolSSI Driver Interface](https://github.com/MolSSI/MDI_Library).
I wanted to get the "right answer for the right reason", so the project performed both a Hartree-Fock calculation to capture the short-ranged repulsion between
 Argon atoms and a second-order Moller-Plesset (MP2) calculation to capture the weak long-range attraction.
I also wanted to keep everything as simple as possible to be able to present the project in my short block of teaching time (3 hours).
The development process and final product are contained in a [GitHub repository](https://github.com/godotalgorithm/qm_project_sss2019).
It took me a while to put this together because it was a lot of firsts for me: my first attempt at building a custom semiempirical model,
 my first use of Jupyter notebooks, my first serious scientific calculation in Python,
 and my first attempt at assembling teaching materials for software development.
Overall, I'm happy with the outcome, particularly in how it is emphasizing the utility of a tight coupling between theory and implementation.
The entire model is derived within the notebook, and each mathematical expression is implemented in software as soon as it is defined in theory.
I also enjoyed working with Jupyter notebooks, and I plan to use them in the near future in conjunction with this blog.

Finally, I ran into an interesting problem while developing the QM project that will be the subject of my next blog post in a few days.
My simple semiempirical model, which relied on common approximations and forms (e.g. Slater-Koster tight binding and the neglect of differential diatomic overlap),
 failed miserably at producing a strong repulsion between closed-shell atoms at the Hartree-Fock level.
I ended up having to introduce a repulsive pseudopotential to fix the model,
 and other models commonly use a repulsive interatomic potential to compensate for this well-known problem.
Having this somewhat artificial additional correction term complicated the fitting process of model parameters to reference data,
 which is another common issue with semiempirical modeling.
In retrospect, this felt like a very unacceptable and avoidable problem (i.e. the right answer for the WRONG reasons),
 and I will examine it in more detail in my next blog post.
