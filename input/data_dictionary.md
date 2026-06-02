# Data Dictionary

## Source
Jardim et al. (2022), AEJ: Economic Policy replication package.
Downloaded from: https://www.openicpsr.org/openicpsr/project/133921/version/V1/view
File: region_level_cumulative.dta

## Unit of Observation
One row = one PUMA (Public Use Microdata Area) × one quarter.

## Variables Used

| Variable | Description | Units | Source |
|---|---|---|---|
| yearquarter | Year and quarter identifier (e.g. 20142 = 2014 Q2) | YYYYQ | ESD |
| region0 | Indicator: 1 = Seattle PUMA, 0 = rest of Washington | Binary | ESD |
| cum_nworkers_beg12 | Cumulative jobs paying under $13/hour (beginning-of-quarter) | Count | ESD |
| cum_nworkers_beg18 | Cumulative jobs paying under $19/hour (beginning-of-quarter) | Count | ESD |
| cum_nworkers_beg40 | Cumulative jobs at all wage levels (beginning-of-quarter) | Count | ESD |
| cum_hours_flow12 | Total hours worked in jobs paying under $13/hour | Thousands | ESD |
| cum_hours_flow18 | Total hours worked in jobs paying under $19/hour | Thousands | ESD |
| cum_hours_flow40 | Total hours worked across all wage levels | Thousands | ESD |
| cum_payroll_flow12 | Total payroll in jobs paying under $13/hour | 2015 Q2 dollars | ESD |
| cum_payroll_flow18 | Total payroll in jobs paying under $19/hour | 2015 Q2 dollars | ESD |
| cum_payroll_flow40 | Total payroll across all wage levels | 2015 Q2 dollars | ESD |

## Notes
- Wages are inflation-adjusted to 2015 Q2 dollars using CPI-W.
- Analysis is restricted to "locatable" employers (single-site firms and
  multi-site firms with separate UI accounts by location).
- King County PUMAs are excluded from the control region in the
  synthetic control analysis.
