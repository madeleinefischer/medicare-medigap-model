# Test

import pandas as pd
import numpy as np

dir = "C:/Users/MadeleineFischer/OneDrive - Committee for a Responsible Federal Budget/Documents/Medicare"
survey_data = pd.read_csv(f"{dir}/Medicare Current Beneficiary Survey - Survey File/SFPUF2023_Data/sfpuf2023_1_fall.csv")
cost_data= pd.read_csv(f"{dir}/Medicare Current Beneficiary Survey - Cost Supplement/CSPUF2023_Data/cspuf2023.csv")

# Check for matches of participant IDs between the two datasets
participant_ids_survey = set(survey_data['PUF_ID'])
participant_ids_cost = set(cost_data['PUF_ID'])
matching_ids = participant_ids_survey.intersection(participant_ids_cost)

if len(matching_ids) > 0:
    pass