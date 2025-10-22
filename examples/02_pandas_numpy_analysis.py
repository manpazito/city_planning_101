"""
Example script demonstrating pandas and numpy data manipulation for city planning.

This script shows how to:
1. Create and manipulate DataFrames with pandas
2. Perform numerical computations with numpy
3. Aggregate and transform data
4. Calculate urban planning metrics
"""

import pandas as pd
import numpy as np


def create_sample_data():
    """
    Create sample city planning data for demonstration.
    
    Returns:
        DataFrame with sample urban planning metrics
    """
    # Sample data for city districts
    data = {
        'district_id': range(1, 11),
        'district_name': [
            'Downtown', 'North Side', 'South Side', 'East Side', 'West Side',
            'Riverside', 'Hillside', 'Industrial', 'Suburban', 'Commercial'
        ],
        'population': [25000, 18500, 22000, 15000, 19000, 12000, 8500, 3000, 28000, 5000],
        'area_sq_miles': [2.5, 4.2, 3.8, 5.1, 3.5, 2.8, 6.2, 8.5, 12.0, 1.5],
        'median_income': [65000, 52000, 48000, 45000, 58000, 70000, 55000, 42000, 72000, 85000],
        'parks_count': [5, 8, 6, 4, 7, 10, 15, 2, 20, 1],
        'schools_count': [3, 5, 4, 3, 4, 2, 3, 1, 8, 0],
        'crime_rate': [3.2, 2.8, 4.1, 3.5, 2.5, 1.8, 1.2, 2.0, 1.5, 2.3]
    }
    
    return pd.DataFrame(data)


def calculate_urban_metrics(df):
    """
    Calculate various urban planning metrics using pandas and numpy.
    
    Args:
        df: DataFrame with city district data
        
    Returns:
        DataFrame with additional calculated metrics
    """
    # Create a copy to avoid modifying original
    df = df.copy()
    
    # Calculate population density (people per square mile)
    df['population_density'] = df['population'] / df['area_sq_miles']
    
    # Calculate parks per capita (parks per 10,000 people)
    df['parks_per_10k'] = (df['parks_count'] / df['population']) * 10000
    
    # Calculate schools per capita (schools per 10,000 people)
    df['schools_per_10k'] = (df['schools_count'] / df['population']) * 10000
    
    # Normalize crime rate to a 0-100 scale using min-max normalization
    crime_min = df['crime_rate'].min()
    crime_max = df['crime_rate'].max()
    df['crime_index'] = 100 * (df['crime_rate'] - crime_min) / (crime_max - crime_min)
    
    # Calculate livability score (simple weighted average)
    # Higher income, lower crime, more parks/schools = better livability
    df['livability_score'] = (
        (df['median_income'] / df['median_income'].max()) * 30 +
        ((df['crime_rate'].max() - df['crime_rate']) / df['crime_rate'].max()) * 30 +
        (df['parks_per_10k'] / df['parks_per_10k'].max()) * 20 +
        (df['schools_per_10k'] / df['schools_per_10k'].max()) * 20
    )
    
    return df


def numpy_statistical_analysis(df):
    """
    Perform statistical analysis using numpy.
    
    Args:
        df: DataFrame with city district data
    """
    print("\n" + "=" * 60)
    print("NumPy Statistical Analysis")
    print("=" * 60)
    
    # Population statistics
    pop_array = df['population'].values
    print(f"\nPopulation Statistics:")
    print(f"  Mean: {np.mean(pop_array):,.0f}")
    print(f"  Median: {np.median(pop_array):,.0f}")
    print(f"  Std Dev: {np.std(pop_array):,.0f}")
    print(f"  Min: {np.min(pop_array):,.0f}")
    print(f"  Max: {np.max(pop_array):,.0f}")
    
    # Population density statistics
    density_array = df['population_density'].values
    print(f"\nPopulation Density Statistics (people/sq mi):")
    print(f"  Mean: {np.mean(density_array):,.0f}")
    print(f"  Median: {np.median(density_array):,.0f}")
    print(f"  Percentiles (25th, 50th, 75th): {np.percentile(density_array, [25, 50, 75])}")
    
    # Income statistics
    income_array = df['median_income'].values
    print(f"\nMedian Income Statistics:")
    print(f"  Mean: ${np.mean(income_array):,.0f}")
    print(f"  Std Dev: ${np.std(income_array):,.0f}")
    
    # Correlation between income and crime
    correlation = np.corrcoef(df['median_income'], df['crime_rate'])[0, 1]
    print(f"\nCorrelation (Income vs Crime Rate): {correlation:.3f}")


def pandas_aggregation_examples(df):
    """
    Demonstrate pandas aggregation and grouping operations.
    
    Args:
        df: DataFrame with city district data
    """
    print("\n" + "=" * 60)
    print("Pandas Aggregation Examples")
    print("=" * 60)
    
    # Categorize districts by population size
    df['size_category'] = pd.cut(
        df['population'],
        bins=[0, 10000, 20000, 30000],
        labels=['Small', 'Medium', 'Large']
    )
    
    # Group by size category and aggregate
    print("\nDistrict Statistics by Size Category:")
    summary = df.groupby('size_category').agg({
        'population': ['count', 'mean', 'sum'],
        'median_income': 'mean',
        'crime_rate': 'mean',
        'livability_score': 'mean'
    }).round(2)
    print(summary)
    
    # Find top districts by livability score
    print("\n\nTop 5 Districts by Livability Score:")
    top_districts = df.nlargest(5, 'livability_score')[
        ['district_name', 'livability_score', 'median_income', 'crime_rate']
    ]
    print(top_districts.to_string(index=False))


if __name__ == '__main__':
    print("=" * 60)
    print("Pandas & NumPy Data Analysis Example")
    print("=" * 60)
    
    # Create sample data
    print("\nCreating sample city planning data...")
    df = create_sample_data()
    
    # Calculate metrics
    print("Calculating urban planning metrics...")
    df = calculate_urban_metrics(df)
    
    # Display processed data
    print("\n" + "=" * 60)
    print("Processed District Data")
    print("=" * 60)
    print(df[['district_name', 'population', 'population_density', 
              'livability_score']].to_string(index=False))
    
    # NumPy analysis
    numpy_statistical_analysis(df)
    
    # Pandas aggregation
    pandas_aggregation_examples(df)
    
    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("=" * 60)
