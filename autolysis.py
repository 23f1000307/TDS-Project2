import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import traceback
import requests
import chardet
import sys

# Set the AIPROXY_TOKEN environment variable (set your API token here)
os.environ["AIPROXY_TOKEN"] = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjEwMDAzMDdAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.NWYw284TTLJOpKuDvkoXtsnviW8y5rZeDGo4-Mv6wpU"

# Prompt the user for their API token (if you want user input instead)
api_proxy_token = os.environ.get("AIPROXY_TOKEN", "Token not found")

if api_proxy_token == "Token not found":
    raise ValueError("API proxy token is required.")

# Ensure a CSV file is provided as a system argument
if len(sys.argv) < 2:
    raise ValueError("Please provide the path to the CSV file as a command-line argument.")

csv_file_path = sys.argv[1]
if not os.path.isfile(csv_file_path) or not csv_file_path.lower().endswith(".csv"):
    raise ValueError("A valid CSV file path is required.")

# Function to detect the encoding of a file
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read(1024))  # Read the first 1 KB for detection
        return result['encoding']

# Function to read a CSV file
def read_csv(filename):
    encodings_to_try = ['latin1', detect_encoding(filename), 'utf-8', 'utf-8-sig',  'ISO-8859-1']
    for encoding in encodings_to_try:
        try:
            df = pd.read_csv(filename, encoding=encoding)
            print(f"Dataset loaded: {filename} (Encoding: {encoding})")
            return df
        except Exception as e:
            print(f"Failed with encoding {encoding}: {e}")
    print(f"All encoding attempts failed for {filename}.")
    return None

# Function to analyze the dataset
def analyze_data(df):
    try:
        analysis = {
            "shape": df.shape,
            "columns": df.dtypes.to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "summary_statistics": df.describe(include="all").to_dict(),
        }
        numeric_data = df.select_dtypes(include=["number"])
        if not numeric_data.empty:
            analysis["correlation_matrix"] = numeric_data.corr().to_dict()
        else:
            analysis["correlation_matrix"] = None
        return analysis
    except Exception as e:
        print(f"Error analyzing data: {e}")
        traceback.print_exc()
        return {}

# Function to visualize the dataset
def visualize_data(df, output_prefix):
    charts = []
    try:
        # Correlation Heatmap
        numeric_columns = df.select_dtypes(include=["number"]).columns
        if len(numeric_columns) > 0:
            plt.figure(figsize=(14, 12))
            heatmap = sns.heatmap(
                df[numeric_columns].corr(),
                annot=True,
                cmap="coolwarm",
                fmt=".2f",
                cbar_kws={'shrink': 0.8}
            )
            heatmap.set_title("Correlation Heatmap")
            heatmap_file = f"{output_prefix}_heatmap.png"
            plt.savefig(heatmap_file, dpi=300)
            charts.append(heatmap_file)
            plt.close()

        # Distribution of numerical columns
        for column in numeric_columns:
            plt.figure(figsize=(8, 5))
            df[column].hist(bins=30, color="skyblue", edgecolor="black")
            plt.title(f"Distribution of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            dist_file = f"{output_prefix}_{column}_distribution.png"
            plt.savefig(dist_file, dpi=300)
            charts.append(dist_file)
            plt.close()
    except Exception as e:
        print(f"Error visualizing data: {e}")
        traceback.print_exc()
    return charts

# Function to interact with the LLM (Updated for gpt-4o-mini model)
def query_llm(prompt):
    try:
        response = requests.post(
            'https://aiproxy.sanand.workers.dev/openai/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {os.environ["AIPROXY_TOKEN"]}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'gpt-4o-mini',  # Use the gpt-4o-mini model
                'messages': [{"role": "user", "content": prompt}],
                'temperature': 0.7,
            }
        )
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        print(f"Response Text: {response.text}")
        return None
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()
        return None

# Function to save the analysis and insights to a Markdown file
def save_markdown(analysis, charts, insights, output_file):
    try:
        with open(output_file, "w") as f:
            f.write("# Analysis Report\n\n")
            f.write("## Dataset Analysis\n")
            f.write(f"Shape: {analysis.get('shape')}\n")
            f.write(f"Columns:\n{analysis.get('columns')}\n")
            f.write(f"Missing Values:\n{analysis.get('missing_values')}\n")
            f.write(f"Summary Statistics:\n{analysis.get('summary_statistics')}\n")
            f.write("\n## LLM Insights\n")
            f.write(insights + "\n")
            f.write("\n## Charts\n")
            for chart in charts:
                f.write(f"![{chart}]({chart})\n")
    except Exception as e:
        print(f"Error saving Markdown file: {e}")
        traceback.print_exc()

# Ensure a directory exists for saving results
def ensure_output_directory(dataset_name):
    output_dir = dataset_name
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

# Main function to process the CSV file
def main():
    print(f"Processing {csv_file_path}...")
    df = read_csv(csv_file_path)
    if df is None:
        return

    # Determine dataset name from CSV filename
    dataset_name = os.path.splitext(os.path.basename(csv_file_path))[0]

    # Create output directory for this dataset
    output_dir = ensure_output_directory(dataset_name)

    # Analyze and visualize data
    analysis = analyze_data(df)
    charts = visualize_data(df, os.path.join(output_dir, dataset_name))

    # Generate insights using LLM
    insights = query_llm(f"Create a detailed analysis report based on this dataset:\n\n{analysis}")
    if insights is None:
        insights = "No insights generated from the LLM."

    # Save Markdown and charts to the dataset folder
    readme_file = os.path.join(output_dir, "README.md")
    save_markdown(analysis, charts, insights, readme_file)

    print(f"Completed analysis for {csv_file_path}. Results saved to {readme_file}.")

if __name__ == "__main__":
    main()
