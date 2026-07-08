# Test

import pandas as pd
import numpy as np

dir = "C:/Users/MadeleineFischer/OneDrive - Committee for a Responsible Federal Budget/Documents/Medicare"

# Import survey data and clean
# survey_data = pd.read_csv(f"{dir}/Medicare Current Beneficiary Survey - Survey File/SFPUF2023_Data/sfpuf2023_1_fall.csv")
cost_data = pd.read_csv(f"{dir}/Medicare Current Beneficiary Survey - Cost Supplement/CSPUF2023_Data/cspuf2023.csv")

# Format into DataFrame
cost_supplement = pd.DataFrame(cost_data)

# Calculate share of participants with a private plan
participation_rate = cost_supplement[cost_supplement['PAMTALPR'] > 0].shape[0] / cost_supplement.shape[0]

# Share of home health costs in Medicare Part A
share_home_health = 0.5

# Part A = inpatient + share(home health) 
cost_supplement['medicare_A_total_cost_baseline'] = cost_supplement['PAMTIP'] + (cost_supplement['PAMTHH'] * share_home_health)

# Part B = outpatient + share(home health) + medical provider
cost_supplement['medicare_B_total_cost_baseline'] = cost_supplement['PAMTOP'] + (cost_supplement['PAMTHH'] * (1 - share_home_health)) + cost_supplement['PAMTMP']

# Calculate effective coinsurance rates for Part A and Part B





# INS_D_PRIVNUM: has private insurance
# INS_D_PVESI : employer-sponsored private insurance
# INS_D_PVSELF: self-purchased private insurance
# ACC_MCDRSOON: Usually go to Dr as soon as feel bad 

# Use the cost data to apply CBO formula to figure out spending changes
