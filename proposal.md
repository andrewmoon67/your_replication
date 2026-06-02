# Replication Proposal

## 1. Full Citation
Jardim, Ekaterina, Mark C. Long, Robert Plotnick, Emma van Inwegen, Jacob Vigdor,
and Hilary Wething. 2022. "Minimum Wage Increases and Low-Wage Employment:
Evidence from Seattle." *AEJ: Economic Policy* 14(2): 263–314.

## 2. Data Source
https://www.openicpsr.org/openicpsr/project/133921/version/V1/view

## 3. Result to Replicate
I will replicate the summary statistics in Table 5 of Jardim et al. (2022),
which reports cumulative employment and wage statistics for Seattle's locatable
establishments. Specifically, I target the finding that jobs paying under $19/hour
in Seattle declined from 92,959 (2014 Q2) to 88,431 (2016 Q2), a reduction of
4,528 jobs or 4.8%, and that total hours worked in such jobs fell 4.5% over the
same period (from 37,408 thousand to 35,681 thousand hours).

## 4. Planned Toolchain
- Python 3.x
- pandas, pyreadstat (data loading and manipulation)
- LaTeX (paper compilation)
- GNU Make (pipeline automation)

## 5. Why This Paper
Seattle's minimum wage experiment is one of the most closely studied local labor
market policies in recent economics literature. The debate over whether large
minimum wage increases reduce hours for low-wage workers — and the methodological
innovation of using actual wage data rather than industry proxies — makes this
paper an ideal subject for a replication exercise.
