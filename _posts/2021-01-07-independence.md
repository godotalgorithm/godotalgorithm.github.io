---
layout: post
title: "Intellectual independence requires financial independence"
categories: career
---

This is a very belated follow-up to [my post last year about career problems]({% post_url 2020-03-27-career-hopelessness %}).
It was a very long and cathartic post right as the coronavirus pandemic began to engulf the United States,
 and it largely pinned my future research career hopes on being able to monetize research software of some kind.
Such a venture is very unlikely to succeed, thus the general feelings of hopelessness.
However, I regained hope again a few months later after giving myself a crash course in investment and financial planning.
The bittersweet reality that I have come to accept is that through a few more years of careful saving, planning, and investing,
 I should be able to finance a future independent research career for the remainder of my life through the average long-term
 expected returns from investments into financial markets (e.g. stocks, bonds, and commodities, but mostly stocks).
The modern US scientific enterprise has not been willing to support my research despite me devoting my entire adult life so far to it
 (rather than seeking out more lucrative jobs), and I no longer have any real expectations of it ever doing so.
It was simultaneously very uplifting and frustrating to realize that independent research opportunities are realistically something
 that I will be able to afford to give myself in the not too distant future rather than something I have to be given by someone else
 (but likely never will be).
To be fair, while the scientific enterprise has failed to give me any explicit independent research opportunities since graduate school,
 it also operates in a relatively lax and inefficient manner so that I have certainly managed to carry out
 many independent research projects on the margins, albeit much more slowly than I'd like,
 with my research priorities still heavily distorted, and carrying the guilt of mis-using work time.

A major point of frustration for me was that I've been struggling with and focusing on career problems for most of the last decade,
 while I've had no financial problems at all and thus have paid little attention to financial matters.
If I had been more mindful of my finances in the past, then I would have been investing my growing non-retirement savings
 in a prudent manner, and I would now be a lot closer to a financial solution to my career problems.
Also, it was a bit unfortunate to learn about investing in a time of high economic uncertainty,
 negative real interest rates, and overinflated asset prices (the crown jewel of overvaluation right now being Tesla, Inc.).
These frustrations aside, it was very comforting to read about the Financial Independence, Retire Early (FIRE) movement,
 which shows that financial independence is within reach for frugal people who can maintain highish-paying jobs for long enough.
It was also very encouraging to see the inflation-adjusted total return of the S&P 500 index (and its precursors) over the last century
 on a semilog plot against an exponential fit - it is an impressive historical record of American prosperity
 that persists and is more accessible than ever through exchange-traded index funds.
Stock markets have some disconcerting behavior - the extreme correlations between all liquid assets
 make it effectively impossible to fully mitigate the volatility of stocks with other stocks (i.e. the volatility of an index fund
 relative to its components is not reduced in accordance to the averaging of independent random variables),
 and the time correlations of volatility mean that deviations from the robust long-time exponential growth trend can persist for a decade or more.
Still, the good very clearly outweighs the bad, and my past inattention to investment was a regrettable mistake.

I obsessively read about investing in mid-2020 and messed around a bit with fitting historical financial data to simple models
 to get more comfortable with investment, and I could definitely imagine an alternate reality in which I pursued a career in economics or finance.
Nothing profound came out of that exercise, but I can share a representative exercise that might be of broader interest.
For the most part, I plan to invest only in large exchange-traded funds with low expense ratios,
 and so the main impactful decision that I have to make is the allocation of my money between assets with low and high risk/volatility.
For this exercise, I'll model the low-risk asset as having fixed value with no volatility (e.g. some mix of cash and high-grade bonds)
 and the high-risk asset as a historical time series of the inflation-adjusted total return of the US stock market between 1870 and now.
The simple-minded investment strategy is to adjust the cash/stock ratio based on the immediate value of stock market relative
 to its uniform exponential growth baseline of around 6.5%.
This ignores economic indicators that are surely much better than deviations from a uniform baseline,
 but it illustrates the basic exercise of balancing the risks and rewards of volatile assets.
The optimization of this investment strategy is a straightforward numerical exercise conducted and plotted with Python,
 which shows a very limited benefit from reallocating assets (blue curve) relative to the underlying risk asset (red curve).

![investment optimization](/assets/invest.pdf){:height="80%" width="80%"}

Inevitably, the optimal investment strategy obtained from this numerical exercise is an artifact of the specific details of the historical data,
 and its details do not reflect a useful forward-looking investment strategy.
However, a useful observation is that deviations from full stock market exposure only occur above a 50% overvaluation.
With a more uniform strategy of completely removing stock market exposure above 50% overvaluation,
 the growth of investments is unchanged from full exposure to the stock market under all conditions.
This suggests that overvalued stock markets have already realized all meaningful profits for investors,
 and whether you pull money out early or ride the overvaluation back down, your outcome will be roughly the same on average.
This is consistent with general advice against timing the stock market,
 although this exercise suggests that it is more futile than actually harmful.
I will eventually settle on an allocation strategy much like this for my own money,
 but I still need to learn more about various economic indicators to decide on which ones to use in practice.
While market crashes and bear markets cannot be predicted,
 economic indicators can identify periods of increased risk (such as right now)
 when stock market exposure should probably be reduced.

Because I still need more money before I am financially independent with a comfortable buffer,
 I am trying to shift my discretionary research interests and activities in a more profit-seeking direction for the foreseeable future.
Of my established skills and interests, I have decided that the most likely to be lucrative is quantum computing.
I have two recent quantum computing preprints that I need to revise and publish -
 a [quantum Metropolis algorithm](https://arxiv.org/abs/1903.01451) and a
 [finite-temperature variational Monte Carlo method](https://arxiv.org/abs/2003.04171) -
 that might help me find a higher-paying job in quantum computing.
I took my present job for the potential opportunity to continue my electronic structure research rather than compelling financial compensation,
 but that opportunity has unfortunately not panned out.
Quantum computing is a very hot topic right now with numerous scientists working at high-compensation tech companies like Microsoft, Google, and Amazon.
Also, I have some very promising unpublished ideas in quantum error correction (QEC)
 that I will attempt to patent when they are sufficiently developed.
There are some very inefficient aspects of existing QEC protocols (e.g. logical non-Clifford gates),
 and patents on more efficient methods could end up being very lucrative.
I've read up enough about patents to appreciate the difficulty of their monetization (their main use is as a legal defense, not a monetizable asset),
 but I have the opportunity to file patents with my employer covering the costs in exchange for half of any future profits.
While I could probably make more money if I tried to pivot away from research altogether for a while,
 I see quantum computing research as a reasonable compromise for now.

While I still have a long road ahead of me on my path to intellectual independence through financial independence,
 it is overwhelmingly more plausible than the prospect of finding a job that will allow me to pursue my research interests.
The modern US scientific enterprise is simply not supportive of intellectual independence -
 it tightly controls the active topics of research through the narrow flow of funding and the very low success rates of grants.
This works for scientists with very malleable interests or whose narrow interests align with funding priorities,
 but career starvation starts to set in when a scientist's interests fall out of favor
 and they aren't willing to choose from a narrow pool of acceptable new interests.
I've seen this happen multiple times so far in my career,
 and I consider it to be extremely shameful that the scientific enterprise does this to people.
In some cases, the unfortunate scientist has had enough savings that they could afford to continue their research on their own dime.
In other cases, they burned through their life savings and then gave up on science altogether.