import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import shutil # For making a backup of the CSV

# Get the directory where the current Python script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the directory to save plots relative to the script's location
PLOTS_DIR = os.path.join(SCRIPT_DIR, 'plots')

# Define the path to the dataset
# IMPORTANT: Update this path to your actual dataset location
DATASET_PATH = r"C:\Users\admin\Downloads\dataset_project.csv"
BACKUP_DATASET_PATH = r"C:\Users\admin\Downloads\dataset_project_backup.csv" # Backup path

# Create the plots directory if it doesn't exist
if not os.path.exists(PLOTS_DIR):
    os.makedirs(PLOTS_DIR)
    print(f"Created directory: {PLOTS_DIR}")

# Set global style for plots
sns.set(style="whitegrid")

# Global DataFrame variable to be modified by CRUD operations
df = None

def load_and_preprocess_data(file_path):
    """
    Loads the dataset from the given file path and performs necessary preprocessing steps.
    Also creates a backup of the original CSV.

    Args:
        file_path (str): The path to the CSV dataset.

    Returns:
        pandas.DataFrame: The preprocessed DataFrame.
    """
    global df # Declare df as global to modify the global variable
    try:
        # Create a backup before loading/modifying
        if os.path.exists(file_path):
            shutil.copy(file_path, BACKUP_DATASET_PATH)
            print(f"Backup of original dataset created at: {BACKUP_DATASET_PATH}")
        
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the path.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

    # Converting the date column to datetime format.
    df['Date_of_Delivery'] = pd.to_datetime(df['Date_of_Delivery'])

    # Extracting Year and Month
    df['Year'] = df['Date_of_Delivery'].dt.year
    df['Month'] = df['Date_of_Delivery'].dt.month

    # Adding Season column based on Month
    df['Season'] = df['Month'].map({
        12: 'Winter', 1: 'Winter', 2: 'Winter',
        3: 'Spring', 4: 'Spring', 5: 'Spring',
        6: 'Monsoon', 7: 'Monsoon', 8: 'Monsoon',
        9: 'Autumn', 10: 'Autumn', 11: 'Autumn'
    })

    # Creating Age Groups for analysis
    df['Age_Group'] = pd.cut(df['Mother_Age'], bins=[0, 20, 30, 40, 100],
                             labels=['<20', '20-30', '30-40', '40+'])

    # Creating BMI categories
    df['BMI_Category'] = pd.cut(df['Mother_BMI'], bins=[0, 18.5, 25, 30, 100],
                                labels=['Underweight', 'Normal', 'Overweight', 'Obese'])

    print("Preprocessed DataFrame head:")
    print(df.head())
    return df

def save_plot(fig, plot_name):
    """Helper function to save a plot and close the figure."""
    file_path = os.path.join(PLOTS_DIR, f"{plot_name}.png")
    fig.savefig(file_path, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved plot: {file_path}")

# --- Visualization Functions (unchanged, just added to menu) ---

def plot_delivery_type_distribution(df_local):
    """
    Generates countplot and pie chart for Delivery Type Distribution and saves them.
    """
    print("\n--- 1. Delivery Type Distribution ---")
    # Countplot
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.countplot(x='Delivery_Type', data=df_local, palette='Set2', ax=ax1)
    ax1.set_title("Count of Delivery Types")
    ax1.set_xlabel("Delivery Type")
    ax1.set_ylabel("Count")
    save_plot(fig1, "delivery_type_countplot")

    # Pie-chart
    delivery_counts = df_local['Delivery_Type'].value_counts()
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    ax2.pie(delivery_counts, labels=delivery_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
    ax2.set_title("Delivery Type Distribution")
    save_plot(fig2, "delivery_type_piechart")

def plot_institutional_comparison(df_local):
    """
    Generates a countplot for Delivery Type by Hospital Type and saves it.
    """
    print("\n--- 2. Institutional Comparison ---")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Hospital_Type', hue='Delivery_Type', data=df_local, palette='Set3', ax=ax)
    ax.set_title("Delivery Type by Hospital Type")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right') # Rotate labels for readability
    ax.set_xlabel("Hospital Type")
    ax.set_ylabel("Count")
    ax.legend(title="Delivery Type")
    fig.tight_layout()
    save_plot(fig, "institutional_comparison")

def plot_regional_disparity(df_local):
    """
    Generates a countplot for Delivery Type by Region and saves it.
    """
    print("\n--- 3. Regional Disparity in Delivery Type ---")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Region', hue='Delivery_Type', data=df_local, palette='pastel', ax=ax)
    ax.set_title("Delivery Type by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Count")
    ax.legend(title='Delivery Type')
    fig.tight_layout()
    save_plot(fig, "regional_disparity")

def plot_seasonal_effect(df_local):
    """
    Generates a countplot for Delivery Type by Season and saves it.
    (Colors changed to 'Paired')
    """
    print("\n--- 4. Seasonal Effect on Delivery Type ---")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Season', hue='Delivery_Type', data=df_local, palette='Paired', ax=ax) # Changed palette
    ax.set_title("Delivery Type by Season")
    ax.set_xlabel("Season")
    ax.set_ylabel("Count")
    fig.tight_layout()
    save_plot(fig, "seasonal_effect")

def plot_maternal_age_vs_delivery_type(df_local):
    """
    Generates a countplot for Delivery Type by Mother's Age Group and saves it.
    """
    print("\n--- 5. Maternal Age Group vs Delivery Type ---")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(x='Age_Group', hue='Delivery_Type', data=df_local, palette='Accent', ax=ax)
    ax.set_title("Delivery Type by Mother's Age Group")
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Count")
    fig.tight_layout()
    save_plot(fig, "maternal_age_vs_delivery_type")

def plot_nicu_admission_rate(df_local):
    """
    Generates a stacked bar chart for NICU Admission by Delivery Type and saves it.
    """
    print("\n--- 6. NICU Admission Rate (Stacked Bar Chart) ---")
    # Create a cross-tabulation table
    nicu_table = pd.crosstab(df_local['Delivery_Type'], df_local['NICU_Admission'])

    # Plot as stacked bar
    fig, ax = plt.subplots(figsize=(8,4))
    nicu_table.plot(kind='bar', stacked=True, colormap='Set2', ax=ax)
    ax.set_title("NICU Admission by Delivery Type")
    ax.set_xlabel("Delivery Type")
    ax.set_ylabel("Count")
    ax.legend(title="NICU Admission")
    fig.tight_layout()
    save_plot(fig, "nicu_admission_rate")

def plot_medical_complication_impact(df_local):
    """
    Generates a countplot for Delivery Type by Medical Complication and saves it.
    """
    print("\n--- 7. Medical Complication Impact ---")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Medical_Complication', hue='Delivery_Type', data=df_local, palette='Set1', ax=ax)
    ax.set_title("Delivery Type by Medical Complication")
    ax.set_xlabel("Medical Complication")
    ax.set_ylabel("Count")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right') # Rotate labels for readability
    fig.tight_layout()
    save_plot(fig, "medical_complication_impact")

def plot_bmi_vs_delivery_type(df_local):
    """
    Generates a countplot for Delivery Type by Mother's BMI Category and saves it.
    """
    print("\n--- 8. BMI vs Delivery Type ---")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='BMI_Category', hue='Delivery_Type', data=df_local, palette='Set3', ax=ax)
    ax.set_title("Delivery Type by Mother's BMI Category")
    ax.set_xlabel("BMI Category")
    ax.set_ylabel("Count")
    fig.tight_layout()
    save_plot(fig, "bmi_vs_delivery_type")

def plot_child_weight_vs_delivery_type(df_local):
    """
    Generates a box plot for Child Weight by Delivery Type and saves it.
    """
    print("\n--- 9. Child Weight vs Delivery Type (Box Plot) ---")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(x='Delivery_Type', y='Child_Weight_kg', data=df_local, palette='Set2', ax=ax)
    ax.set_title("Child Weight by Delivery Type")
    ax.set_xlabel("Delivery Type")
    ax.set_ylabel("Child Weight (kg)")
    fig.tight_layout()
    save_plot(fig, "child_weight_vs_delivery_type")

# --- Analysis Questions Functions (unchanged, just added to menu) ---

def analyze_csection_by_region(df_local):
    """
    Analyzes and visualizes C-section deliveries by Region and saves the plot.
    Returns the textual analysis.
    """
    print("\n--- Q1) Which part of the country has more C-section deliveries? ---")
    # Count C-section deliveries by Region
    region_c_sections = df_local[df_local['Delivery_Type'] == 'C-section']['Region'].value_counts()

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    region_c_sections.plot(kind='bar', title='C-section Deliveries by Region', xlabel='Region', ylabel='Count', color='salmon', ax=ax)
    fig.tight_layout()
    save_plot(fig, "csection_by_region")

    return "C-section Deliveries by Region:\n" + region_c_sections.to_string()

def analyze_csection_by_hospital(df_local):
    """
    Analyzes and visualizes C-section deliveries by Hospital Name and saves the plot.
    Returns the textual analysis.
    """
    print("\n--- Q2) Which hospitals have more C-section deliveries? ---")
    # Count C-section deliveries by Hospital Name
    hospital_c_sections = df_local[df_local['Delivery_Type'] == 'C-section']['Hospital_Name'].value_counts()

    # Display top 10 (since the dataset is quite big)
    # Plot top 10
    fig, ax = plt.subplots(figsize=(8, 6)) # Increased height for better readability of hospital names
    hospital_c_sections.head(10).plot(kind='barh', title='Top Hospitals by C-section Deliveries', color='skyblue', ax=ax)
    ax.set_xlabel('Number of C-sections')
    ax.set_ylabel('Hospital Name')
    fig.tight_layout()
    save_plot(fig, "csection_by_hospital")

    return "Top 10 Hospitals by C-section Deliveries:\n" + hospital_c_sections.head(10).to_string()

def analyze_csection_relation_with_season(df_local):
    """
    Analyzes and visualizes the relation between C-section delivery and Season and saves the plot.
    Returns the textual analysis.
    (Colors changed to 'Paired')
    """
    print("\n--- Q3) Does C-section delivery have any relation with Season? ---")
    # Cross-tab of Season vs Delivery Type
    season_table = pd.crosstab(df_local['Season'], df_local['Delivery_Type'], normalize='index') * 100

    # Plot it
    fig, ax = plt.subplots(figsize=(8, 5))
    season_table.plot(kind='bar', stacked=True, colormap='Paired', title='Delivery Type by Season (%)', ax=ax) # Changed colormap
    ax.set_ylabel("Percentage")
    fig.tight_layout()
    save_plot(fig, "csection_by_season")

    return "Percentage of Delivery Types by Season:\n" + season_table.round(1).to_string()

def analyze_second_child_normal_after_csection(df_local):
    """
    Calculates the percentage of 2nd child births that were normal when the 1st was a C-section.
    Also generates a pie chart for the counts of delivery types in this specific subset.
    Returns the textual analysis.
    """
    print("\n--- Q4) What percentage of 2nd child births were normal when 1st was C-section? ---")

    # Only second-child births where the first was a C-section
    mask = (df_local['Child_Birth_Order'] == 2) & (df_local['Previous_Delivery_Type'] == 'C-section')
    subset = df_local[mask]

    # Total cases
    total_second_after_csection = subset.shape[0]

    # How many were normal this time
    normal_now = subset[subset['Delivery_Type'] == 'Normal'].shape[0]

    # Calculate percentage
    percentage = (normal_now / total_second_after_csection) * 100 if total_second_after_csection > 0 else 0

    # Pie chart for visual
    delivery_counts = subset['Delivery_Type'].value_counts()

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(delivery_counts,
           labels=delivery_counts.index,
           autopct='%1.1f%%',
           startangle=90,
           colors=['lightgreen', 'lightcoral']) # Using the colors you provided
    ax.set_title("2nd Child Delivery Type (After 1st C-section)")
    save_plot(fig, "q4_delivery_type_counts") # Save the pie chart with the same name

    return f"Percentage of 2nd child births that were normal after 1st C-section: {percentage:.2f}%"

# --- Main Functions for Running Analysis and Visualizations ---

def run_all_visualizations():
    """Runs all visualization functions."""
    global df
    if df is None:
        print("DataFrame not loaded. Loading data...")
        load_and_preprocess_data(DATASET_PATH)
        if df is None: # Check if loading was successful
            return

    print("\n--- Generating All Visualizations and Saving Plots ---")
    plot_delivery_type_distribution(df)
    plot_institutional_comparison(df)
    plot_regional_disparity(df)
    plot_seasonal_effect(df)
    plot_maternal_age_vs_delivery_type(df)
    plot_nicu_admission_rate(df)
    plot_medical_complication_impact(df)
    plot_bmi_vs_delivery_type(df)
    plot_child_weight_vs_delivery_type(df)
    print("\nAll visualizations generated and saved to the 'plots' folder.")

def run_specific_visualization():
    """Allows user to run a specific visualization."""
    global df
    if df is None:
        print("DataFrame not loaded. Loading data...")
        load_and_preprocess_data(DATASET_PATH)
        if df is None:
            return

    print("\n--- Select a Visualization ---")
    print("1. Delivery Type Distribution")
    print("2. Institutional Comparison")
    print("3. Regional Disparity in Delivery Type")
    print("4. Seasonal Effect on Delivery Type")
    print("5. Maternal Age Group vs Delivery Type")
    print("6. NICU Admission Rate")
    print("7. Medical Complication Impact")
    print("8. BMI vs Delivery Type")
    print("9. Child Weight vs Delivery Type")
    choice = input("Enter visualization number (1-9): ")

    viz_functions = {
        '1': plot_delivery_type_distribution,
        '2': plot_institutional_comparison,
        '3': plot_regional_disparity,
        '4': plot_seasonal_effect,
        '5': plot_maternal_age_vs_delivery_type,
        '6': plot_nicu_admission_rate,
        '7': plot_medical_complication_impact,
        '8': plot_bmi_vs_delivery_type,
        '9': plot_child_weight_vs_delivery_type,
    }

    if choice in viz_functions:
        viz_functions[choice](df)
    else:
        print("Invalid choice.")

def run_all_analyses():
    """Runs all analysis question functions and prints results."""
    global df
    if df is None:
        print("DataFrame not loaded. Loading data...")
        load_and_preprocess_data(DATASET_PATH)
        if df is None:
            return

    print("\n--- Running All Analysis Questions ---")
    q1_output = analyze_csection_by_region(df)
    q2_output = analyze_csection_by_hospital(df)
    q3_output = analyze_csection_relation_with_season(df)
    q4_output = analyze_second_child_normal_after_csection(df)

    print("\n--- TEXTUAL ANALYSIS RESULTS (Copy these for HTML dashboard) ---")
    print("Q1 Output:\n", q1_output)
    print("\nQ2 Output:\n", q2_output)
    print("\nQ3 Output:\n", q3_output)
    print("\nQ4 Output:\n", q4_output)

def run_specific_analysis():
    """Allows user to run a specific analysis question."""
    global df
    if df is None:
        print("DataFrame not loaded. Loading data...")
        load_and_preprocess_data(DATASET_PATH)
        if df is None:
            return

    print("\n--- Select an Analysis Question ---")
    print("1. C-section deliveries by Region")
    print("2. C-section deliveries by Hospital")
    print("3. C-section relation with Season")
    print("4. 2nd child normal birth after 1st C-section percentage")
    choice = input("Enter analysis number (1-4): ")

    analysis_functions = {
        '1': analyze_csection_by_region,
        '2': analyze_csection_by_hospital,
        '3': analyze_csection_relation_with_season,
        '4': analyze_second_child_normal_after_csection,
    }

    if choice in analysis_functions:
        output = analysis_functions[choice](df)
        print("\n--- ANALYSIS RESULT ---")
        print(output)
    else:
        print("Invalid choice.")

def main():
    """
    Main function to run the interactive menu for analysis and visualization operations.
    """
    global df # Ensure we are working with the global DataFrame

    # Load data once at the start
    print("Loading and preprocessing data...")
    load_and_preprocess_data(DATASET_PATH)
    if df is None:
        print("Failed to load data. Exiting.")
        return

    while True:
        print("\n--- Normal Vs C-section Delivery Analysis Menu ---")
        print("1. Run All Visualizations")
        print("2. Run Specific Visualization")
        print("3. Run All Analysis Questions")
        print("4. Run Specific Analysis Question")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            run_all_visualizations()
        elif choice == '2':
            run_specific_visualization()
        elif choice == '3':
            run_all_analyses()
        elif choice == '4':
            run_specific_analysis()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 4, or 0 to exit.")

if __name__ == "__main__":
    main()
