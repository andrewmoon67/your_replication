# code/analysis.py
# Reads clean_data.csv from temp/,
# computes Table 3 summary statistics for Seattle,
# writes LaTeX table fragment to output/tables/main_result.tex.

import pandas as pd
import os

# ── Paths ───────────────────────────────────────────────────────────────────
INPUT  = os.path.join("temp",            "clean_data.csv")
OUTPUT = os.path.join("output", "tables", "main_result.tex")

os.makedirs(os.path.join("output", "tables"), exist_ok=True)

# ── Load ────────────────────────────────────────────────────────────────────
df = pd.read_csv(INPUT)

# ── Filter to Seattle only
seattle = df[df["seattle"] == 1].copy()

# ── Pull the two key quarters
base = seattle[seattle["yearquarter"] == 20142.0].iloc[0]  # 2014 Q2
end  = seattle[seattle["yearquarter"] == 20162.0].iloc[0]  # 2016 Q2

# ── Compute the key statistics
jobs_base    = base["cum_nworkers_beg18"]
jobs_end     = end["cum_nworkers_beg18"]
jobs_change  = jobs_end - jobs_base
jobs_pct     = (jobs_change / jobs_base) * 100

hours_base   = base["cum_hours_flow18"]
hours_end    = end["cum_hours_flow18"]
hours_change = hours_end - hours_base
hours_pct    = (hours_change / hours_base) * 100

wage_base    = base["mean_wage18"]
wage_end     = end["mean_wage18"]
wage_pct     = ((wage_end - wage_base) / wage_base) * 100

# ── Console summary
print("=" * 55)
print("Replication Result")
print("=" * 55)
print(f"  {'':30s} {'2014 Q2':>10} {'2016 Q2':>10}")
print(f"  {'-'*50}")
print(f"  {'Jobs paying <$19/hr':30s} {jobs_base:>10,.0f} {jobs_end:>10,.0f}")
print(f"  {'Hours worked <$19/hr':30s} {hours_base:>10,.0f} {hours_end:>10,.0f}")
print(f"  {'Avg wage <$19/hr':30s} {wage_base:>10.2f} {wage_end:>10.2f}")
print(f"  {'-'*50}")
print(f"  Change in jobs:  {jobs_change:>8,.0f}  ({jobs_pct:.1f}%)")
print(f"  Change in hours: {hours_change:>8,.0f}  ({hours_pct:.1f}%)")
print(f"  Change in wage:  {wage_pct:>8.1f}%")
print()
print("  Paper reports (NBER 2017):")
print("  Jobs <$19:  92,959 → 88,431  (-4.8%)")
print("  Hours <$19: 37,408 → 35,681  (-4.5%)")
print("=" * 55)

# ── Write LaTeX table ────────────────────────────────────────────────────────
latex = r"""\begin{table}[h]
\centering
\caption{Replication of Summary Employment Statistics,
         from Jardim et al.\ (2022)}
\begin{tabular}{lccc}
\hline
 & 2014 Q2 & 2016 Q2 & Change \\
\hline
Jobs paying $<\$19$/hr    & %.0f & %.0f & %.1f\%% \\
Hours worked $<\$19$/hr   & %.0f & %.0f & %.1f\%% \\
Avg.\ wage $<\$19$/hr     & \$%.2f & \$%.2f & %.1f\%% \\
\hline
\end{tabular}
\label{tab:main}
\end{table}""" % (
    jobs_base,  jobs_end,  jobs_pct,
    hours_base, hours_end, hours_pct,
    wage_base,  wage_end,  wage_pct
)

with open(OUTPUT, "w") as f:
    f.write(latex)

print(f"\n  LaTeX table written to {OUTPUT}")
