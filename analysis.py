import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """Load and verify the dataset"""
    try:
        df = pd.read_csv("data\owid-covid-codebook.csv")
        print("✅ Data loaded successfully!")
        print(f"📊 Shape: {df.shape}")
        print(f"📅 Date range: {df['date'].min()} to {df['date'].max()}")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None
# Plot total cases over time for a specific country
def plot_country_cases (df, country="UnitedStates"):
    country_df = df[df["location"] == country]
    plt.figure(figsize=(10 , 5))
    plt.plot(pd.to_datetime(country_df["date"]), (country_df["total_cases"]))
    plt.title(f"Covid total cases overtime - {country}")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.grid(True)
    plt.tight_layout
    plt.savefig(f"output/{country.lower().replace("", "_")}_case.png")
    print(f"📊 {country} plot saved.")


def analyze_data(df):
    """Perform key analyses"""
    if df is not None:
        # Example analysis - customize as needed

        latest = df[df['date'] == df['date'].max()]
        print("\n🌍 Latest data summary:")
        print(latest[['location', 'total_cases', 'total_deaths']].head())

        # Basic visualization
        df.groupby('location')['total_cases'].last().nlargest(10).plot(kind='barh')
        plt.title("Top 10 Countries by Total Cases")
        plt.tight_layout()
        plt.savefig('output/top_cases.png')  # Saves visualization
        print("\n📈 Visualization saved to output/top_cases.png")

if __name__ == "__main__":
    print("\n=== COVID-19 Data Analysis ===")
    covid_df = load_data()
    analyze_data(covid_df)
    print("\nAnalysis complete! Open output/ folder for results.")