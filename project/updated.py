import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import io
import base64
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS # Needed for cross-origin requests from your HTML

# --- Flask App Setup ---
app = Flask(__name__)
CORS(app) # Enable CORS for all routes, so your HTML can fetch data

# Get the directory where the current Python script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the path to the dataset
# IMPORTANT: Ensure 'dataset_project.csv' is in the same directory as this 'app.py' file
DATASET_PATH = os.path.join(SCRIPT_DIR, 'dataset_project.csv')

# Set global style for plots
sns.set(style="whitegrid")

# Global DataFrame variable to store data after initial load
# This prevents reprocessing the data on every API request
df_global = None

# --- Data Loading and Preprocessing ---
def load_and_preprocess_data():
    """
    Loads the dataset and performs necessary preprocessing steps.
    This function is designed to be called once to load data into df_global.
    """
    global df_global
    if df_global is not None: # If data is already loaded, return it
        return df_global

    try:
        df_loaded = pd.read_csv(DATASET_PATH)
    except FileNotFoundError:
        print(f"Error: The dataset file '{DATASET_PATH}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

    # Convert Date_of_Delivery to datetime
    df_loaded['Date_of_Delivery'] = pd.to_datetime(df_loaded['Date_of_Delivery'])

    # Extract Year and Month
    df_loaded['Year'] = df_loaded['Date_of_Delivery'].dt.year
    df_loaded['Month'] = df_loaded['Date_of_Delivery'].dt.month

    # Add Season column based on Month (using pd.cut for ranges or explicit mapping)
    # Using a list of conditions and choices for clarity, similar to Power BI logic
    conditions = [
        (df_loaded['Month'] == 12) | (df_loaded['Month'] == 1) | (df_loaded['Month'] == 2), # Winter
        (df_loaded['Month'] >= 3) & (df_loaded['Month'] <= 5), # Spring
        (df_loaded['Month'] >= 6) & (df_loaded['Month'] <= 8), # Monsoon
        (df_loaded['Month'] >= 9) & (df_loaded['Month'] <= 11) # Autumn
    ]
    choices = ['Winter', 'Spring', 'Monsoon', 'Autumn']
    # Initialize 'Season' column with NaN or a default, then apply conditions
    df_loaded['Season'] = pd.Series(pd.NA, index=df_loaded.index, dtype=str)
    for cond, choice in zip(conditions, choices):
        df_loaded.loc[cond, 'Season'] = choice

    # Create Age Groups for analysis
    df_loaded['Age_Group'] = pd.cut(df_loaded['Mother_Age'], bins=[0, 20, 30, 40, 100],
                                     labels=['<20', '20-30', '30-40', '40+'])

    # Create BMI categories
    df_loaded['BMI_Category'] = pd.cut(df_loaded['Mother_BMI'], bins=[0, 18.5, 25, 30, 100],
                                        labels=['Underweight', 'Normal', 'Overweight', 'Obese'])

    print("Data loaded and preprocessed.")
    df_global = df_loaded # Store in global variable
    return df_global

# --- Helper to convert Matplotlib figure to base64 image ---
def fig_to_base64(fig):
    """Converts a matplotlib figure to a base64 encoded PNG image."""
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig) # Close the figure to free up memory
    return base64.b64encode(buf.getvalue()).decode('utf-8')

# --- Visualization Functions (Modified to return base64 images) ---

def get_delivery_type_distribution_plots(df_local):
    plots_data = {}

    # Countplot
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.countplot(x='Delivery_Type', data=df_local, palette='Set2', ax=ax1)
    ax1.set_title("Count of Delivery Types")
    ax1.set_xlabel("Delivery Type")
    ax1.set_ylabel("Count")
    plots_data["delivery_type_countplot"] = fig_to_base64(fig1)

    # Pie-chart
    delivery_counts = df_local['Delivery_Type'].value_counts()
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    ax2.pie(delivery_counts, labels=delivery_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
    ax2.set_title("Delivery Type Distribution")
    plots_data["delivery_type_piechart"] = fig_to_base64(fig2)
    
    return plots_data

def get_institutional_comparison_plot(df_local):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Hospital_Type', hue='Delivery_Type', data=df_local, palette='Set3', ax=ax)
    ax.set_title("Delivery Type by Hospital Type")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_xlabel("Hospital Type")
    ax.set_ylabel("Count")
    ax.legend(title="Delivery Type")
    fig.tight_layout()
    return fig_to_base64(fig)

def get_regional_disparity_plot(df_local):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Region', hue='Delivery_Type', data=df_local, palette='pastel', ax=ax)
    ax.set_title("Delivery Type by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Count")
    ax.legend(title='Delivery Type')
    fig.tight_layout()
    return fig_to_base64(fig)

def get_seasonal_effect_plot(df_local):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Season', hue='Delivery_Type', data=df_local, palette='Paired', ax=ax)
    ax.set_title("Delivery Type by Season")
    ax.set_xlabel("Season")
    ax.set_ylabel("Count")
    fig.tight_layout()
    return fig_to_base64(fig)

def get_maternal_age_vs_delivery_type_plot(df_local):
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(x='Age_Group', hue='Delivery_Type', data=df_local, palette='Accent', ax=ax)
    ax.set_title("Delivery Type by Mother's Age Group")
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Count")
    fig.tight_layout()
    return fig_to_base64(fig)

def get_nicu_admission_rate_plot(df_local):
    nicu_table = pd.crosstab(df_local['Delivery_Type'], df_local['NICU_Admission'])
    fig, ax = plt.subplots(figsize=(8,4))
    nicu_table.plot(kind='bar', stacked=True, colormap='Set2', ax=ax)
    ax.set_title("NICU Admission by Delivery Type")
    ax.set_xlabel("Delivery Type")
    ax.set_ylabel("Count")
    ax.legend(title="NICU Admission")
    fig.tight_layout()
    return fig_to_base64(fig)

def get_medical_complication_impact_plot(df_local):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Medical_Complication', hue='Delivery_Type', data=df_local, palette='Set1', ax=ax)
    ax.set_title("Delivery Type by Medical Complication")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_xlabel("Medical Complication")
    ax.set_ylabel("Count")
    fig.tight_layout()
    return fig_to_base64(fig)

def get_bmi_vs_delivery_type_plot(df_local):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='BMI_Category', hue='Delivery_Type', data=df_local, palette='Set3', ax=ax)
    ax.set_title("Delivery Type by Mother's BMI Category")
    ax.set_xlabel("BMI Category")
    ax.set_ylabel("Count")
    fig.tight_layout()
    return fig_to_base64(fig)

def get_child_weight_vs_delivery_type_plot(df_local):
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(x='Delivery_Type', y='Child_Weight_kg', data=df_local, palette='Set2', ax=ax)
    ax.set_title("Child Weight by Delivery Type")
    ax.set_xlabel("Delivery Type")
    ax.set_ylabel("Child Weight (kg)")
    fig.tight_layout()
    return fig_to_base64(fig)

# --- Analysis Questions Functions (Modified to return textual results and their plots) ---

def get_csection_by_region_analysis(df_local):
    region_c_sections = df_local[df_local['Delivery_Type'] == 'C-section']['Region'].value_counts()
    
    # Plot for this question
    fig, ax = plt.subplots(figsize=(8, 5))
    region_c_sections.plot(kind='bar', title='C-section Deliveries by Region', xlabel='Region', ylabel='Count', color='salmon', ax=ax)
    fig.tight_layout()
    plot_base64 = fig_to_base64(fig)

    return {
        "text": "C-section Deliveries by Region:\n" + region_c_sections.to_string(),
        "plot": plot_base64
    }

def get_csection_by_hospital_analysis(df_local):
    hospital_c_sections = df_local[df_local['Delivery_Type'] == 'C-section']['Hospital_Name'].value_counts()
    
    # Plot for this question
    fig, ax = plt.subplots(figsize=(8, 6))
    hospital_c_sections.head(10).plot(kind='barh', title='Top Hospitals by C-section Deliveries', color='skyblue', ax=ax)
    ax.set_xlabel('Number of C-sections')
    ax.set_ylabel('Hospital Name')
    fig.tight_layout()
    plot_base64 = fig_to_base64(fig)

    return {
        "text": "Top 10 Hospitals by C-section Deliveries:\n" + hospital_c_sections.head(10).to_string(),
        "plot": plot_base64
    }

def get_csection_relation_with_season_analysis(df_local):
    season_table = pd.crosstab(df_local['Season'], df_local['Delivery_Type'], normalize='index') * 100
    
    # Plot for this question
    fig, ax = plt.subplots(figsize=(8, 5))
    season_table.plot(kind='bar', stacked=True, colormap='Paired', title='Delivery Type by Season (%)', ax=ax)
    ax.set_ylabel("Percentage")
    fig.tight_layout()
    plot_base64 = fig_to_base64(fig)

    return {
        "text": "Percentage of Delivery Types by Season:\n" + season_table.round(1).to_string(),
        "plot": plot_base64
    }

def get_second_child_normal_after_csection_analysis(df_local):
    mask = (df_local['Child_Birth_Order'] == 2) & (df_local['Previous_Delivery_Type'] == 'C-section')
    subset = df_local[mask]

    total_second_after_csection = subset.shape[0]
    normal_now = subset[subset['Delivery_Type'] == 'Normal'].shape[0]
    percentage = (normal_now / total_second_after_csection) * 100 if total_second_after_csection > 0 else 0

    # Pie chart for visual
    delivery_counts = subset['Delivery_Type'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(delivery_counts,
           labels=delivery_counts.index,
           autopct='%1.1f%%',
           startangle=90,
           colors=['lightgreen', 'lightcoral'])
    ax.set_title("2nd Child Delivery Type (After 1st C-section)")
    plot_base64 = fig_to_base64(fig)

    return {
        "text": f"Percentage of 2nd child births that were normal after 1st C-section: {percentage:.2f}%",
        "plot": plot_base64
    }

# --- Flask Routes ---

@app.route('/')
def home():
    # Redirect to the dashboard HTML for convenience
    return send_from_directory(SCRIPT_DIR, 'dashboard.html')

@app.route('/get_dashboard_data')
def get_dashboard_data():
    """
    API endpoint to generate and return all dashboard data (plots and analysis text).
    """
    df_data = load_and_preprocess_data() # Ensure data is loaded/preprocessed
    if df_data is None:
        return jsonify({"error": "Failed to load or preprocess data. Check dataset path."}), 500

    response_data = {
        "visualizations": {},
        "analysis_questions": {}
    }

    # Get all visualization plots
    response_data["visualizations"].update(get_delivery_type_distribution_plots(df_data))
    response_data["visualizations"]["institutional_comparison"] = get_institutional_comparison_plot(df_data)
    response_data["visualizations"]["regional_disparity"] = get_regional_disparity_plot(df_data)
    response_data["visualizations"]["seasonal_effect"] = get_seasonal_effect_plot(df_data)
    response_data["visualizations"]["maternal_age_vs_delivery_type"] = get_maternal_age_vs_delivery_type_plot(df_data)
    response_data["visualizations"]["nicu_admission_rate"] = get_nicu_admission_rate_plot(df_data)
    response_data["visualizations"]["medical_complication_impact"] = get_medical_complication_impact_plot(df_data)
    response_data["visualizations"]["bmi_vs_delivery_type"] = get_bmi_vs_delivery_type_plot(df_data)
    response_data["visualizations"]["child_weight_vs_delivery_type"] = get_child_weight_vs_delivery_type_plot(df_data)

    # Get all analysis questions with their plots and text
    response_data["analysis_questions"]["q1"] = get_csection_by_region_analysis(df_data)
    response_data["analysis_questions"]["q2"] = get_csection_by_hospital_analysis(df_data)
    response_data["analysis_questions"]["q3"] = get_csection_relation_with_season_analysis(df_data)
    response_data["analysis_questions"]["q4"] = get_second_child_normal_after_csection_analysis(df_data)

    return jsonify(response_data)

# --- Main entry point for Flask app ---
if __name__ == '__main__':
    # Initial load and preprocess of data when the Flask app starts
    load_and_preprocess_data()
    # Run the Flask app
    print(f"Flask app running. Open http://127.0.0.1:5000/ in your web browser.")
    app.run(debug=True) # debug=True allows auto-reloading on code changes and provides more info
