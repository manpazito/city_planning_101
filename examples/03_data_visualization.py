"""
Example script demonstrating data visualization with matplotlib and seaborn.

This script shows how to:
1. Create various types of plots for urban planning data
2. Customize visualizations
3. Save plots to files
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def create_sample_data():
    """Create sample city planning data for visualization."""
    data = {
        'district_name': [
            'Downtown', 'North Side', 'South Side', 'East Side', 'West Side',
            'Riverside', 'Hillside', 'Industrial', 'Suburban', 'Commercial'
        ],
        'population': [25000, 18500, 22000, 15000, 19000, 12000, 8500, 3000, 28000, 5000],
        'area_sq_miles': [2.5, 4.2, 3.8, 5.1, 3.5, 2.8, 6.2, 8.5, 12.0, 1.5],
        'median_income': [65000, 52000, 48000, 45000, 58000, 70000, 55000, 42000, 72000, 85000],
        'parks_count': [5, 8, 6, 4, 7, 10, 15, 2, 20, 1],
        'crime_rate': [3.2, 2.8, 4.1, 3.5, 2.5, 1.8, 1.2, 2.0, 1.5, 2.3]
    }
    
    df = pd.DataFrame(data)
    df['population_density'] = df['population'] / df['area_sq_miles']
    return df


def plot_population_distribution(df):
    """Create a bar chart of population by district."""
    plt.figure(figsize=(12, 6))
    
    # Sort by population for better visualization
    df_sorted = df.sort_values('population', ascending=False)
    
    # Create bar plot
    bars = plt.bar(df_sorted['district_name'], df_sorted['population'], 
                   color='steelblue', edgecolor='navy', alpha=0.7)
    
    # Customize plot
    plt.title('Population by District', fontsize=16, fontweight='bold')
    plt.xlabel('District', fontsize=12)
    plt.ylabel('Population', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    return plt.gcf()


def plot_income_vs_crime(df):
    """Create a scatter plot showing relationship between income and crime."""
    plt.figure(figsize=(10, 6))
    
    # Create scatter plot
    scatter = plt.scatter(df['median_income'], df['crime_rate'], 
                         s=df['population']/100, alpha=0.6,
                         c=df['population_density'], cmap='viridis',
                         edgecolors='black', linewidth=1)
    
    # Add labels for each point
    for idx, row in df.iterrows():
        plt.annotate(row['district_name'], 
                    (row['median_income'], row['crime_rate']),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8, alpha=0.7)
    
    # Add colorbar
    cbar = plt.colorbar(scatter)
    cbar.set_label('Population Density (per sq mi)', rotation=270, labelpad=20)
    
    # Customize plot
    plt.title('Median Income vs Crime Rate by District', 
             fontsize=14, fontweight='bold')
    plt.xlabel('Median Household Income ($)', fontsize=12)
    plt.ylabel('Crime Rate (incidents per 1000)', fontsize=12)
    plt.grid(alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return plt.gcf()


def plot_density_heatmap(df):
    """Create a heatmap of district metrics."""
    plt.figure(figsize=(10, 8))
    
    # Select numeric columns for heatmap
    metrics = ['population', 'median_income', 'parks_count', 
               'crime_rate', 'population_density']
    
    # Normalize data for better visualization
    df_normalized = df[metrics].copy()
    for col in metrics:
        df_normalized[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    
    # Set district names as index
    df_normalized.index = df['district_name']
    
    # Create heatmap
    sns.heatmap(df_normalized.T, annot=True, fmt='.2f', cmap='YlOrRd',
                cbar_kws={'label': 'Normalized Value'},
                linewidths=0.5, linecolor='gray')
    
    plt.title('District Metrics Heatmap (Normalized)', 
             fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('District', fontsize=12)
    plt.ylabel('Metric', fontsize=12)
    
    plt.tight_layout()
    return plt.gcf()


def plot_parks_distribution(df):
    """Create a horizontal bar chart for parks count."""
    plt.figure(figsize=(10, 6))
    
    # Sort by parks count
    df_sorted = df.sort_values('parks_count', ascending=True)
    
    # Create horizontal bar plot
    colors = plt.cm.Greens(np.linspace(0.4, 0.8, len(df_sorted)))
    bars = plt.barh(df_sorted['district_name'], df_sorted['parks_count'],
                    color=colors, edgecolor='darkgreen', alpha=0.8)
    
    # Customize plot
    plt.title('Parks Count by District', fontsize=14, fontweight='bold')
    plt.xlabel('Number of Parks', fontsize=12)
    plt.ylabel('District', fontsize=12)
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, df_sorted['parks_count'])):
        plt.text(val + 0.3, bar.get_y() + bar.get_height()/2,
                str(int(val)), va='center', fontsize=9)
    
    plt.tight_layout()
    return plt.gcf()


def create_dashboard(df):
    """Create a multi-plot dashboard."""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('City Planning Dashboard', fontsize=16, fontweight='bold')
    
    # Plot 1: Population by district
    ax1 = axes[0, 0]
    df_sorted = df.sort_values('population', ascending=False)
    ax1.bar(range(len(df_sorted)), df_sorted['population'], 
           color='steelblue', alpha=0.7)
    ax1.set_xticks(range(len(df_sorted)))
    ax1.set_xticklabels(df_sorted['district_name'], rotation=45, ha='right')
    ax1.set_title('Population by District')
    ax1.set_ylabel('Population')
    ax1.grid(axis='y', alpha=0.3)
    
    # Plot 2: Income distribution
    ax2 = axes[0, 1]
    ax2.hist(df['median_income'], bins=8, color='green', alpha=0.7, edgecolor='black')
    ax2.set_title('Median Income Distribution')
    ax2.set_xlabel('Median Income ($)')
    ax2.set_ylabel('Frequency')
    ax2.grid(axis='y', alpha=0.3)
    
    # Plot 3: Crime rate by district
    ax3 = axes[1, 0]
    ax3.scatter(df['population_density'], df['crime_rate'], 
               s=100, alpha=0.6, c='red', edgecolors='black')
    ax3.set_title('Crime Rate vs Population Density')
    ax3.set_xlabel('Population Density (per sq mi)')
    ax3.set_ylabel('Crime Rate')
    ax3.grid(alpha=0.3)
    
    # Plot 4: Parks vs Population
    ax4 = axes[1, 1]
    ax4.scatter(df['population'], df['parks_count'], 
               s=100, alpha=0.6, c='forestgreen', edgecolors='black')
    ax4.set_title('Parks Count vs Population')
    ax4.set_xlabel('Population')
    ax4.set_ylabel('Number of Parks')
    ax4.grid(alpha=0.3)
    
    plt.tight_layout()
    return fig


if __name__ == '__main__':
    print("=" * 60)
    print("Data Visualization Example")
    print("=" * 60)
    
    # Set style for better-looking plots
    sns.set_style("whitegrid")
    plt.rcParams['figure.dpi'] = 100
    
    # Create sample data
    print("\nCreating sample data...")
    df = create_sample_data()
    
    # Create visualizations
    print("Creating visualizations...")
    
    print("  1. Population distribution chart...")
    fig1 = plot_population_distribution(df)
    
    print("  2. Income vs Crime scatter plot...")
    fig2 = plot_income_vs_crime(df)
    
    print("  3. District metrics heatmap...")
    fig3 = plot_density_heatmap(df)
    
    print("  4. Parks distribution chart...")
    fig4 = plot_parks_distribution(df)
    
    print("  5. Comprehensive dashboard...")
    fig5 = create_dashboard(df)
    
    print("\n" + "=" * 60)
    print("Visualizations created successfully!")
    print("Close the plot windows to continue...")
    print("=" * 60)
    
    # Display all plots
    plt.show()
