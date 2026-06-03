# Replication: Jardim et al. (2022)

This repository replicates the summary employment statistics from:

Jardim, Ekaterina, Mark C. Long, Robert Plotnick, Emma van Inwegen, Jacob
Vigdor, and Hilary Wething. 2022. "Minimum Wage Increases and Low-Wage
Employment: Evidence from Seattle." AEJ: Economic Policy 14(2): 263-314.

Specifically, I replicate Table 5, which reports that jobs paying under $19/hr
in Seattle declined from 92,959 to 88,431 (a 4.8% drop) and hours fell 4.5%
between 2014 Q2 and 2016 Q2.

## Data

Data are from the publicly available replication package:
https://www.openicpsr.org/openicpsr/project/133921/version/V1/view

Download region_level_cumulative.dta and place it in input/.

## Prerequisites

- Python 3.x with packages: pandas, pyreadstat
- LaTeX (TeX Live or equivalent)
- GNU Make

Install Python packages with: pip3 install pandas pyreadstat

## Reproducing the Paper

Clone the repo, place region_level_cumulative.dta in input/, then run:

    make

Or using the convenience wrapper:

    ./run_all.sh

The compiled paper will be at paper/paper.pdf.

## Results

| | 2014 Q2 | 2016 Q2 | Change |
|---|---|---|---|
| Jobs paying under $19/hr | 90,757 | 89,188 | -1.7% |
| Hours worked under $19/hr | 36,450,720 | 35,466,512 | -2.7% |
| Avg wage under $19/hr | $14.19 | $15.00 | +5.7% |

Paper reports (NBER 2017 version): jobs -4.8%, hours -4.5%.
Differences reflect data revisions between the 2017 draft and 2022 publication.

## Repository Structure

    your_replication/
    ├── input/                         # Raw data (read-only)
    │   ├── region_level_cumulative.dta
    │   └── data_dictionary.md
    ├── code/
    │   ├── preprocess.py              # Cleans data → temp/
    │   └── analysis.py                # Produces results → output/
    ├── output/
    │   └── tables/
    │       └── main_result.tex        # LaTeX table fragment
    ├── temp/                          # Intermediate files (gitignored)
    ├── paper/
    │   ├── paper.tex
    │   └── paper.pdf
    ├── Makefile
    ├── run_all.sh
    └── README.md
