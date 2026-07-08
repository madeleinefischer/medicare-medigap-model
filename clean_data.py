# Test

import pandas as pd
import numpy as np

dir = "C:/Users/MadeleineFischer/OneDrive - Committee for a Responsible Federal Budget/Documents/Medicare"

# Import survey data and clean
# survey_data = pd.read_csv(f"{dir}/Medicare Current Beneficiary Survey - Survey File/SFPUF2023_Data/sfpuf2023_1_fall.csv")
cost_data = pd.read_csv(f"{dir}/Medicare Current Beneficiary Survey - Cost Supplement/CSPUF2023_Data/cspuf2023.csv")

# Format into DataFrame
cost_supplement = pd.DataFrame(cost_data)

# Part A = inpatient + share(home health) + 
cost_supplement['medicare_partA'] = cost_supplement['PAMTIP'] + cost_supplement['PAMTHH']

# Part B = outpatient + share(home health) + medical provider + dental + vision + hearing
cost_supplement['medicare_partB'] = cost_supplement['PAMTMP'] + cost_supplement['PAMTDU'] + cost_supplement['PAMTVU'] + cost_supplement['PAMTHU'] + cost_supplement['PAMTDU']

# Calculate effective coinsurance rates for Part A and Part B





# INS_D_PRIVNUM: has private insurance
# INS_D_PVESI : employer-sponsored private insurance
# INS_D_PVSELF: self-purchased private insurance
# ACC_MCDRSOON: Usually go to Dr as soon as feel bad 

# Use the cost data to apply CBO formula to figure out spending changes
