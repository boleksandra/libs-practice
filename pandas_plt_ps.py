import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
# kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026", output_dir="datasets", force_download=True)
df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
# print(df.head())
# # depression = df[["depression_pct", "country"]]
# # print(depression)
# # mask = (df['region'] == 'Europe') & (df['depression_pct'] >= 5)
# # europe_depression = df[mask]
# # print(europe_depression [[ "country", "depression_pct"]])
#
# # df["millions_mul_rate"] = df["suicide_rate_per100k"] * df["population_millions"] * 10
# # print(df[["country", "millions_mul_rate"]])
# gdp_geq_40k = df[df["gdp_per_capita_usd"]>=4000]
# gdp_geq_40k_low_help = gdp_geq_40k[gdp_geq_40k["mh_system_score"]<5]
# gdp_geq_40k_low_help["lack_of_care_mln"] = (gdp_geq_40k_low_help["populattion_millions"]
# gdp_geq_40k_low_help["treatment_gap_pct"] / 100)
# print(gdp_geq_40k_low_help)

top5 = df.nlargest(5, 'depression_pct')
plt.figure(figsize=(6,7))
plt.plot(top5['country'], top5['depression_pct'], marker='o', label='depression', linewidth=2)
plt.plot(top5['country'], top5['anxiety_pct'], marker='s', label='anxiety')
plt.title('anxiety vs depression (%)')
plt.xlabel('countrys')
plt.ylabel('%')
plt.legend()
plt.show()
