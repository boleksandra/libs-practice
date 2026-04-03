import kagglehub
import pandas as pd

kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026", output_dir="datasets", force_download=True)
df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
print(df.head())



