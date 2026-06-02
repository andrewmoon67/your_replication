# code/preprocess.py
# Reads region_level_cumulative.dta from input/,
# filters and aggregates to Seattle x quarter level,
# writes clean_data.csv to temp/.

import pandas as pd
import pyreadstat
import os

# ── Paths (relative to repo root) ──────────────────────────────────────────
INPUT  = os.path.join("input", "region_level_cumulative.dta")
OUTPUT = os.path.join("temp",  "clean_data.csv")

os.makedirs("temp", exist_ok=True)

# ── Load ────────────────────────────────────────────────────────────────────
df, meta = pyreadstat.read_dta(INPUT)

# ── Filter to quarters used in the paper (2014 Q2 through 2016 Q3)
df = df[(df["yearquarter"] > 20141) & (df["yearquarter"] < 20164)]

# ── Flag Seattle vs. rest-of-WA
df["seattle"] = (df["region0"] == 1).astype(int)

# ── Keep only columns we need
keep = [
    "yearquarter", "seattle",
    "cum_nworkers_beg12", "cum_nworkers_beg18", "cum_nworkers_beg40",
    "cum_hours_flow12",   "cum_hours_flow18",   "cum_hours_flow40",
    "cum_payroll_flow12", "cum_payroll_flow18", "cum_payroll_flow40",
]
df = df[keep]

# ── Aggregate: sum across PUMAs within (seattle x yearquarter)
df = df.groupby(["seattle", "yearquarter"], as_index=False).sum()

# ── Derive average wage rate = total payroll / total hours
for thresh in ["12", "18", "40"]:
    df[f"mean_wage{thresh}"] = (
        df[f"cum_payroll_flow{thresh}"] / df[f"cum_hours_flow{thresh}"]
    )

# ── Save to temp/
df.to_csv(OUTPUT, index=False)

# ── Console summary
seattle = df[df["seattle"] == 1]
q_min = df["yearquarter"].min()
q_max = df["yearquarter"].max()
baseline = seattle[seattle["yearquarter"] == 20142]

print("=" * 50)
print("Preprocessing complete")
print(f"  Rows written to temp/: {len(df)}")
print(f"  Quarter range: {q_min} to {q_max}")
print(f"  Seattle regions in data: {df[df['seattle']==1]['yearquarter'].nunique()} quarters")
if not baseline.empty:
    print(f"  Seattle 2014 Q2 jobs <$19:  "
          f"{baseline['cum_nworkers_beg18'].values[0]:>10,.0f}")
    print(f"  Seattle 2014 Q2 hours <$19: "
          f"{baseline['cum_hours_flow18'].values[0]:>10,.0f}")
    print(f"  Seattle 2014 Q2 avg wage:   "
          f"${baseline['mean_wage18'].values[0]:>9.2f}/hr")
print("=" * 50)
