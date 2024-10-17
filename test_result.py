import pandas as pd
import json
import os

model_list =[
    'gpt4o', 'gpt4o_mini', 'gpt4_turbo', 'gemini_pro', 'gemini_flash'
]

result_list = []

# Loop over each file in the list
for model in model_list:
    file = f'result-{model}.json'.format(model)
    with open(file) as f:
        data = json.load(f)
        df = pd.json_normalize(data)
        df['source_file'] = model
        result_list.append(df)

merged_df = pd.concat(result_list, ignore_index=True)
csv_output_path = 'merged_results.csv'
merged_df.to_csv(csv_output_path, index=False)