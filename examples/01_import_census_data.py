"""
Example script demonstrating how to import Census data using the census package.

This script shows how to:
1. Set up connection to Census API
2. Query demographic data
3. Store data in pandas DataFrame

Before running:
- Get a Census API key from: https://api.census.gov/data/key_signup.html
- Set the API key as environment variable: export CENSUS_API_KEY='your_key_here'
"""

import os
from census import Census
import pandas as pd


def get_census_api_key():
    """Get Census API key from environment variable."""
    api_key = os.environ.get('CENSUS_API_KEY')
    if not api_key:
        raise ValueError(
            "Census API key not found. Please set CENSUS_API_KEY environment variable.\n"
            "Get your key at: https://api.census.gov/data/key_signup.html"
        )
    return api_key


def import_census_data_example():
    """
    Import census data for demonstration purposes.
    
    This example retrieves population data from the ACS5 (American Community Survey 5-Year)
    for all states.
    """
    # Initialize Census client
    api_key = get_census_api_key()
    c = Census(api_key)
    
    # Query ACS5 data for all states
    # B01001_001E: Total Population
    # NAME: Geographic Area Name
    print("Fetching census data...")
    census_data = c.acs5.state(
        ('NAME', 'B01001_001E'),  # Geographic name and total population
        Census.ALL,  # All states
        year=2021
    )
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(census_data)
    
    # Rename columns for clarity
    df = df.rename(columns={
        'B01001_001E': 'total_population',
        'NAME': 'state_name'
    })
    
    # Sort by population
    df = df.sort_values('total_population', ascending=False)
    
    print("\nTop 10 states by population:")
    print(df[['state_name', 'total_population']].head(10))
    
    return df


def import_county_data_example():
    """
    Import census data at county level for a specific state.
    """
    api_key = get_census_api_key()
    c = Census(api_key)
    
    # Query data for California counties (state FIPS code: 06)
    # B01001_001E: Total Population
    # B19013_001E: Median Household Income
    print("\nFetching county-level data for California...")
    census_data = c.acs5.state_county(
        ('NAME', 'B01001_001E', 'B19013_001E'),
        '06',  # California FIPS code
        Census.ALL,  # All counties
        year=2021
    )
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(census_data)
    
    # Rename columns
    df = df.rename(columns={
        'B01001_001E': 'total_population',
        'B19013_001E': 'median_household_income',
        'NAME': 'county_name'
    })
    
    # Clean up and sort
    df = df.sort_values('total_population', ascending=False)
    
    print("\nTop 10 California counties by population:")
    print(df[['county_name', 'total_population', 'median_household_income']].head(10))
    
    return df


if __name__ == '__main__':
    print("=" * 60)
    print("Census Data Import Example")
    print("=" * 60)
    
    try:
        # Example 1: State-level data
        state_df = import_census_data_example()
        
        # Example 2: County-level data
        county_df = import_county_data_example()
        
        print("\n" + "=" * 60)
        print("Data import successful!")
        print(f"State data shape: {state_df.shape}")
        print(f"County data shape: {county_df.shape}")
        print("=" * 60)
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Make sure you have a valid Census API key set.")
