import json
import pandas as pd
import matplotlib.pyplot as plt

# Load the JSON files
file_turbo = 'result-gpt4_turbo.json'
file_gpt4o = 'result-gpt4o.json'
file_gpt4o_mini = 'result-gpt4o_mini.json'

# Helper function to load JSON files
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to normalize and prepare the data for new models easily
def prepare_model_data(file_paths):
    models_data = {}
    for model_name, file_path in file_paths.items():
        data = load_json(file_path)
        models_data[model_name] = data
    return models_data

# Prepare data for the models
model_files = {
    'gpt-4-turbo': file_turbo,
    'gpt-4o-2024-08-06': file_gpt4o,
    'gpt-4o-mini-2024-07-18': file_gpt4o_mini
}

models_data = prepare_model_data(model_files)

# Function to create dataframes for category-wise comparison
def create_category_dataframe(models_data, score_type):
    categories = ['self-harm', 'dangerous behavior', 'morality', 'illegal activities & crime', 
                  'controversial topics, politics', 'discrimination & stereotyping', 
                  'religion beliefs', 'information misinterpretation', 'privacy violation']
    
    return pd.DataFrame({
        model: [models_data[model]['category_averages'][cat][f'avg_{score_type}'] for cat in categories] 
        for model in models_data
    }, index=categories)

# Create dataframes for safetyness, helpfulness, and combined
df_safetyness = create_category_dataframe(models_data, 'safetyness')
df_helpfulness = create_category_dataframe(models_data, 'helpfulness')
df_combined = create_category_dataframe(models_data, 'combined')

# Function to plot and save figures
def plot_and_save(df, title, ylabel, filename):
    df.plot(kind='bar')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(f'{filename}')
    plt.close()

# Plot and save the figures
plot_and_save(df_safetyness, 'Average Safetyness Comparison', 'Safetyness', 'safetyness_comparison.png')
plot_and_save(df_helpfulness, 'Average Helpfulness Comparison', 'Helpfulness', 'helpfulness_comparison.png')
plot_and_save(df_combined, 'Average Combined Score Comparison', 'Combined', 'combined_comparison.png')

# Output file paths for the saved plots
plot_files = {
    'safetyness_plot': 'safetyness_comparison.png',
    'helpfulness_plot': 'helpfulness_comparison.png',
    'combined_plot': 'combined_comparison.png'
}

plot_files
