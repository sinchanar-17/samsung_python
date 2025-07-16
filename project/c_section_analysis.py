import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set global style for plots
sns.set(style="whitegrid")

def load_and_preprocess_data(file_path):
# Loads the dataset from the given file path and performs necessary preprocessing steps.
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

def plot_delivery_type_distribution(df):
# Generating a countplot and pie chart for Delivery Type Distribution.
    print("\n--- 1. Delivery Type Distribution ---")
    # Countplot
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Delivery_Type', data=df, palette='Set2')
    plt.title("Count of Delivery Types")
    plt.xlabel("Delivery Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    # Pie-chart
    delivery_counts = df['Delivery_Type'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(delivery_counts, labels=delivery_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
    plt.title("Delivery Type Distribution")
    plt.show()

def plot_institutional_comparison(df):
# Generating a countplot for Delivery Type by Hospital Type.
    print("\n--- 2. Institutional Comparison ---")
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Hospital_Type', hue='Delivery_Type', data=df, palette='Set3')
    plt.title("Delivery Type by Hospital Type")
    plt.xticks(rotation=45)
    plt.xlabel("Hospital Type")
    plt.ylabel("Count")
    plt.legend(title="Delivery Type")
    plt.tight_layout()
    plt.show()

def plot_regional_disparity(df):
# Generating a countplot for Delivery Type by Region.
    print("\n--- 3. Regional Disparity in Delivery Type ---")
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Region', hue='Delivery_Type', data=df, palette='pastel')
    plt.title("Delivery Type by Region")
    plt.xlabel("Region")
    plt.ylabel("Count")
    plt.legend(title='Delivery Type')
    plt.tight_layout()
    plt.show()

def plot_seasonal_effect(df):
# Generating a countplot for Delivery Type by Season.
    print("\n--- 4. Seasonal Effect on Delivery Type ---")
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Season', hue='Delivery_Type', data=df, palette=['#90ee90', '#ff9999'])
    plt.title("Delivery Type by Season")
    plt.xlabel("Season")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_maternal_age_vs_delivery_type(df):
# Generating a countplot for Delivery Type by Mother's Age Group.
    print("\n--- 5. Maternal Age Group vs Delivery Type ---")
    plt.figure(figsize=(7, 4))
    sns.countplot(x='Age_Group', hue='Delivery_Type', data=df, palette='Accent')
    plt.title("Delivery Type by Mother's Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_nicu_admission_rate(df):
# Generating a stacked bar chart for NICU Admission by Delivery Type.
    print("\n--- 6. NICU Admission Rate (Stacked Bar Chart) ---")
    # Create a cross-tabulation table
    nicu_table = pd.crosstab(df['Delivery_Type'], df['NICU_Admission'])

    # Plot as stacked bar
    nicu_table.plot(kind='bar', stacked=True, figsize=(8,4), colormap='Set2')
    plt.title("NICU Admission by Delivery Type")
    plt.xlabel("Delivery Type")
    plt.ylabel("Count")
    plt.legend(title="NICU Admission")
    plt.tight_layout()
    plt.show()

def plot_medical_complication_impact(df):
# Generating a countplot for Delivery Type by Medical Complication.
    print("\n--- 7. Medical Complication Impact ---")
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Medical_Complication', hue='Delivery_Type', data=df, palette='Set1')
    plt.title("Delivery Type by Medical Complication")
    plt.xlabel("Medical Complication")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_bmi_vs_delivery_type(df):
# Generating a countplot for Delivery Type by Mother's BMI Category.
    print("\n--- 8. BMI vs Delivery Type ---")
    plt.figure(figsize=(8, 5))
    sns.countplot(x='BMI_Category', hue='Delivery_Type', data=df, palette='Set3')
    plt.title("Delivery Type by Mother's BMI Category")
    plt.xlabel("BMI Category")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_child_weight_vs_delivery_type(df):
# Generating a box plot for Child Weight by Delivery Type.
    print("\n--- 9. Child Weight vs Delivery Type (Box Plot) ---")
    plt.figure(figsize=(7, 4))
    sns.boxplot(x='Delivery_Type', y='Child_Weight_kg', data=df, palette='Set2')
    plt.title("Child Weight by Delivery Type")
    plt.xlabel("Delivery Type")
    plt.ylabel("Child Weight (kg)")
    plt.tight_layout()
    plt.show()

def analyze_csection_by_region(df):
# Analyzes and visualizes C-section deliveries by Region.
    print("\n--- Q1) Which part of the country has more C-section deliveries? ---")
    # Count C-section deliveries by Region
    region_c_sections = df[df['Delivery_Type'] == 'C-section']['Region'].value_counts()

    # Display as DataFrame
    print("C-section Deliveries by Region:")
    print(region_c_sections)

    # plot
    plt.figure(figsize=(8, 5))
    region_c_sections.plot(kind='bar', title='C-section Deliveries by Region', xlabel='Region', ylabel='Count', color='salmon')
    plt.tight_layout()
    plt.show()

def analyze_csection_by_hospital(df):
# Analyzes and visualizes C-section deliveries by Hospital Name.
    print("\n--- Q2) Which hospitals have more C-section deliveries? ---")
    # Count C-section deliveries by Hospital Name
    hospital_c_sections = df[df['Delivery_Type'] == 'C-section']['Hospital_Name'].value_counts()

    # Display top 10 (since the dataset is quite big)
    print("Top 10 Hospitals by C-section Deliveries:")
    print(hospital_c_sections.head(10))

    # plot
    plt.figure(figsize=(8, 5))
    hospital_c_sections.head(10).plot(kind='barh', title='Top Hospitals by C-section Deliveries', color='skyblue')
    plt.xlabel('Number of C-sections')
    plt.ylabel('Hospital Name')
    plt.tight_layout()
    plt.show()

def analyze_csection_relation_with_season(df):
# Analyzes and visualizes the relation between C-section delivery and Season.
    print("\n--- Q3) Does C-section delivery have any relation with Season? ---")
    # Cross-tab of Season vs Delivery Type
    season_table = pd.crosstab(df['Season'], df['Delivery_Type'], normalize='index') * 100
    print("Percentage of Delivery Types by Season:")
    print(season_table.round(1))

    # Plot it
    season_table.plot(kind='bar', stacked=True, colormap='coolwarm', title='Delivery Type by Season (%)')
    plt.ylabel("Percentage")
    plt.tight_layout()
    plt.show()

def calculate_second_child_normal_after_csection(df):
    # Calculates the percentage of 2nd child births that were normal when the 1st was a C-section.
    print("\n--- Q4) What percentage of 2nd child births were normal when 1st was C-section? ---")
    
    # Only second-child births where the first was a C-section
    mask = (df['Child_Birth_Order'] == 2) & (df['Previous_Delivery_Type'] == 'C-section')
    
    # Total cases
    total_second_after_csection = df[mask].shape[0]
    
    # How many were normal this time
    normal_now = df[mask & (df['Delivery_Type'] == 'Normal')].shape[0]
    
    # Calculate percentage
    percentage = (normal_now / total_second_after_csection) * 100 if total_second_after_csection > 0 else 0
    
    print(f"Percentage of 2nd child births that were normal after 1st C-section: {percentage:.2f}%")
    
    # Pie chart for visual
    import matplotlib.pyplot as plt
    
    subset = df[mask]
    delivery_counts = subset['Delivery_Type'].value_counts()
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(delivery_counts,
           labels=delivery_counts.index,
           autopct='%1.1f%%',
           startangle=90,
           colors=['lightgreen', 'lightcoral'])
    ax.set_title("2nd Child Delivery Type (After 1st C-section)")
    plt.show()


def main():
    """
    Main function to run the entire analysis workflow.
    """
    file_path = r"C:\Users\admin\Downloads\dataset_project.csv"
    df = load_and_preprocess_data(file_path)

    if df is not None:
        print("\n--- Generating Visualizations ---")
        plot_delivery_type_distribution(df)
        plot_institutional_comparison(df)
        plot_regional_disparity(df)
        plot_seasonal_effect(df)
        plot_maternal_age_vs_delivery_type(df)
        plot_nicu_admission_rate(df)
        plot_medical_complication_impact(df)
        plot_bmi_vs_delivery_type(df)
        plot_child_weight_vs_delivery_type(df)
        print("\n--- Answering Specific Questions ---")
        analyze_csection_by_region(df)
        analyze_csection_by_hospital(df)
        analyze_csection_relation_with_season(df)
        calculate_second_child_normal_after_csection(df)


if __name__ == "__main__":
    main()
