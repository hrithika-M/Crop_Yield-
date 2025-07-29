import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("crop_yield.csv")
print("Dataset preview:")
print(df.head())

group_A_high_water = df[(df['Fert'] == 'A') & (df['Water'] == 'High')]['Yield']
group_A_low_water = df[(df['Fert'] == 'A') & (df['Water'] == 'Low')]['Yield']
group_B_high_water = df[(df['Fert'] == 'B') & (df['Water'] == 'High')]['Yield']
group_B_low_water = df[(df['Fert'] == 'B') & (df['Water'] == 'Low')]['Yield']

print("\nGroup A - High Water:", group_A_high_water.tolist())
print("Group A - Low Water:", group_A_low_water.tolist())
print("Group B - High Water:", group_B_high_water.tolist())
print("Group B - Low Water:", group_B_low_water.tolist())

t_stat_A, p_val_A = ttest_ind(group_A_high_water, group_A_low_water)
print("\nGroup A T-test:")
print("t-statistic:", t_stat_A)
print("p-value:", p_val_A)

print("Conclusion for Group A:")
if p_val_A < 0.05:
    print("Reject the null hypothesis → Significant difference exists.")
else:
    print("Accept the null hypothesis → No significant difference.")

t_stat_B, p_val_B = ttest_ind(group_B_high_water, group_B_low_water)
print("\nGroup B T-test:")
print("t-statistic:", t_stat_B)
print("p-value:", p_val_B)

print("Conclusion for Group B:")
if p_val_B < 0.05:
    print("Reject the null hypothesis → Significant difference exists.")
else:
    print("Accept the null hypothesis → No significant difference.")
