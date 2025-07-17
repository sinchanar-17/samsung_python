import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get the directory where the current Python script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the directory to save plots relative to the script's location
PLOTS_DIR = os.path.join(SCRIPT_DIR, 'plots')

# Create the plots directory if it doesn't exist
if not os.path.exists(PLOTS_DIR):
    os.makedirs(PLOTS_DIR)
    print(f"Created directory: {PLOTS_DIR}")

# Set global style for plots
sns.set(style="whitegrid")


def load_and_preprocess_data(file_path):
    """
    Loads the dataset from the given file path and performs necessary preprocessing steps.

    Args:
        file_path (str): The path to the CSV dataset.

    Returns:
        pandas.DataFrame: The preprocessed DataFrame.
    """
    try:
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


def plot_delivery_type_distribution(df):
    """
    Generates countplot and pie chart for Delivery Type Distribution and saves them.
    """
    print("\n--- 1. Delivery Type Distribution ---")
    # Countplot
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.countplot(x='Delivery_Type', data=df, palette='Set2', ax=ax1)
    ax1.set_title("Count of Delivery Types")
    ax1.set_xlabel("Delivery Type")
    ax1.set_ylabel("Count")
    save_plot(fig1, "delivery_type_countplot")

    # Pie-chart
    delivery_counts = df['Delivery_Type'].value_counts()
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    ax2.pie(delivery_counts, labels=delivery_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
    ax2.set_title("Delivery Type Distribution")
    save_plot(fig2, "delivery_type_piechart")

def plot_institutional_comparison(df):
    """
    Generates a countplot for Delivery Type by Hospital Type and saves it.
    """
    print("\n--- 2. Institutional Comparison ---")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Hospital_Type', hue='Delivery_Type', data=df, palette='Set3', ax=ax)
    ax.set_title("Delivery Type by Hospital Type")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right') # Rotate labels for readability
    ax.set_xlabel("Hospital Type")
    ax.set_ylabel("Count")
    ax.legend(title="Delivery Type")
    fig.tight_layout()
    save_plot(fig, "institutional_comparison")

def plot_regional_disparity(df):
    """
    Generates a countplot for Delivery Type by Region and saves it.
    """
    print("\n--- 3. Regional Disparity in Delivery Type ---")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Region', hue='Delivery_Type', data=df, palette='pastel', ax=ax)
    ax.set_title("Delivery Type by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Count")
    ax.legend(title='Delivery Type')
    fig.tight_layout()
    save_plot(fig, "regional_disparity")

def plot_seasonal_effect(df):
    """
    Generates a countplot for Delivery Type by Season and saves it.
    (Colors changed to 'Paired')
    """
    print("\n--- 4. Seasonal Effect on Delivery Type ---")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Season', hue='Delivery_Type', data=df, palette='Paired', ax=ax) # Changed palette
    ax.set_title("Delivery Type by Season")
    ax.set_xlabel("Season")
    ax.set_ylabel("Count")
    fig.tight_layout()
    save_plot(fig, "seasonal_effect")

def plot_maternal_age_vs_delivery_type(df):
    """
    Generates a countplot for Delivery Type by Mother's Age Group and saves it.
    """
    print("\n--- 5. Maternal Age Group vs Delivery Type ---")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(x='Age_Group', hue='Delivery_Type', data=df, palette='Accent', ax=ax)
    ax.set_title("Delivery Type by Mother's Age Group")
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Count")
    fig.tight_layout()
    save_plot(fig, "maternal_age_vs_delivery_type")

def plot_nicu_admission_rate(df):
    """
    Generates a stacked bar chart for NICU Admission by Delivery Type and saves it.
    """
    print("\n--- 6. NICU Admission Rate (Stacked Bar Chart) ---")
    # Create a cross-tabulation table
    nicu_table = pd.crosstab(df['Delivery_Type'], df['NICU_Admission'])

    # Plot as stacked bar
    fig, ax = plt.subplots(figsize=(8,4))
    nicu_table.plot(kind='bar', stacked=True, colormap='Set2', ax=ax)
    ax.set_title("NICU Admission by Delivery Type")
    ax.set_xlabel("Delivery Type")
    ax.set_ylabel("Count")
    ax.legend(title="NICU Admission")
    fig.tight_layout()
    save_plot(fig, "nicu_admission_rate")

def plot_medical_complication_impact(df):
    """
    Generates a countplot for Delivery Type by Medical Complication and saves it.
    """
    print("\n--- 7. Medical Complication Impact ---")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Medical_Complication', hue='Delivery_Type', data=df, palette='Set1', ax=ax)
    ax.set_title("Delivery Type by Medical Complication")
    ax.set_xlabel("Medical Complication")
    ax.set_ylabel("Count")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right') # Rotate labels for readability
    fig.tight_layout()
    save_plot(fig, "medical_complication_impact")

def plot_bmi_vs_delivery_type(df):
    """
    Generates a countplot for Delivery Type by Mother's BMI Category and saves it.
    """
    print("\n--- 8. BMI vs Delivery Type ---")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='BMI_Category', hue='Delivery_Type', data=df, palette='Set3', ax=ax)
    ax.set_title("Delivery Type by Mother's BMI Category")
    ax.set_xlabel("BMI Category")
    ax.set_ylabel("Count")
    fig.tight_layout()
    save_plot(fig, "bmi_vs_delivery_type")

def plot_child_weight_vs_delivery_type(df):
    """
    Generates a box plot for Child Weight by Delivery Type and saves it.
    """
    print("\n--- 9. Child Weight vs Delivery Type (Box Plot) ---")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(x='Delivery_Type', y='Child_Weight_kg', data=df, palette='Set2', ax=ax)
    ax.set_title("Child Weight by Delivery Type")
    ax.set_xlabel("Delivery Type")
    ax.set_ylabel("Child Weight (kg)")
    fig.tight_layout()
    save_plot(fig, "child_weight_vs_delivery_type")

def analyze_csection_by_region(df):
    """
    Analyzes and visualizes C-section deliveries by Region and saves the plot.
    Returns the textual analysis.
    """
    print("\n--- Q1) Which part of the country has more C-section deliveries? ---")
    # Count C-section deliveries by Region
    region_c_sections = df[df['Delivery_Type'] == 'C-section']['Region'].value_counts()

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    region_c_sections.plot(kind='bar', title='C-section Deliveries by Region', xlabel='Region', ylabel='Count', color='salmon', ax=ax)
    fig.tight_layout()
    save_plot(fig, "csection_by_region")

    return "C-section Deliveries by Region:\n" + region_c_sections.to_string()

def analyze_csection_by_hospital(df):
    """
    Analyzes and visualizes C-section deliveries by Hospital Name and saves the plot.
    Returns the textual analysis.
    """
    print("\n--- Q2) Which hospitals have more C-section deliveries? ---")
    # Count C-section deliveries by Hospital Name
    hospital_c_sections = df[df['Delivery_Type'] == 'C-section']['Hospital_Name'].value_counts()

    # Display top 10 (since the dataset is quite big)
    # Plot top 10
    fig, ax = plt.subplots(figsize=(8, 6)) # Increased height for better readability of hospital names
    hospital_c_sections.head(10).plot(kind='barh', title='Top Hospitals by C-section Deliveries', color='skyblue', ax=ax)
    ax.set_xlabel('Number of C-sections')
    ax.set_ylabel('Hospital Name')
    fig.tight_layout()
    save_plot(fig, "csection_by_hospital")

    return "Top 10 Hospitals by C-section Deliveries:\n" + hospital_c_sections.head(10).to_string()

def analyze_csection_relation_with_season(df):
    """
    Analyzes and visualizes the relation between C-section delivery and Season and saves the plot.
    Returns the textual analysis.
    (Colors changed to 'Paired')
    """
    print("\n--- Q3) Does C-section delivery have any relation with Season? ---")
    # Cross-tab of Season vs Delivery Type
    season_table = pd.crosstab(df['Season'], df['Delivery_Type'], normalize='index') * 100

    # Plot it
    fig, ax = plt.subplots(figsize=(8, 5))
    season_table.plot(kind='bar', stacked=True, colormap='Paired', title='Delivery Type by Season (%)', ax=ax) # Changed colormap
    ax.set_ylabel("Percentage")
    fig.tight_layout()
    save_plot(fig, "csection_by_season")

    return "Percentage of Delivery Types by Season:\n" + season_table.round(1).to_string()

def analyze_second_child_normal_after_csection(df):
    """
    Calculates the percentage of 2nd child births that were normal when the 1st was a C-section.
    Also generates a pie chart for the counts of delivery types in this specific subset.
    Returns the textual analysis.
    """
    print("\n--- Q4) What percentage of 2nd child births were normal when 1st was C-section? ---")

    # Only second-child births where the first was a C-section
    mask = (df['Child_Birth_Order'] == 2) & (df['Previous_Delivery_Type'] == 'C-section')
    subset = df[mask]

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

def main():
    """
    Main function to run the entire analysis workflow, save plots, and print textual results.
    """
    # IMPORTANT: Update this path to your actual dataset location
    file_path = r"E:\Learning\samsung_python\project\dataset_project.csv"
    df = load_and_preprocess_data(file_path)

    if df is not None:
        print("\n--- Generating Visualizations and Saving Plots ---")
        plot_delivery_type_distribution(df)
        plot_institutional_comparison(df)
        plot_regional_disparity(df)
        plot_seasonal_effect(df)
        plot_maternal_age_vs_delivery_type(df)
        plot_nicu_admission_rate(df)
        plot_medical_complication_impact(df)
        plot_bmi_vs_delivery_type(df)
        plot_child_weight_vs_delivery_type(df)

        print("\n--- Answering Specific Questions (Copy these outputs for the HTML dashboard) ---")
        q1_output = analyze_csection_by_region(df)
        q2_output = analyze_csection_by_hospital(df)
        q3_output = analyze_csection_relation_with_season(df)
        q4_output = analyze_second_child_normal_after_csection(df) # Call the updated function

        print("\n--- TEXTUAL ANALYSIS RESULTS ---")
        print("Q1 Output:\n", q1_output)
        print("\nQ2 Output:\n", q2_output)
        print("\nQ3 Output:\n", q3_output)
        print("\nQ4 Output:\n", q4_output)

if __name__ == "__main__":
    main()
