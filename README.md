# City Planning 101

A comprehensive tutorial repository for learning to work with census data, ArcGIS, and data visualization tools for city planning applications.

## Overview

This repository provides examples and tutorials for:
- **Census Data Import**: Access and work with U.S. Census Bureau data
- **Pandas & NumPy**: Data manipulation and statistical analysis
- **Data Visualization**: Create informative charts and dashboards
- **ArcGIS Integration**: Spatial data analysis and GIS operations

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository:
```bash
git clone https://github.com/manpazito/city_planning_101.git
cd city_planning_101
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. (Optional) Get a Census API key:
   - Sign up at: https://api.census.gov/data/key_signup.html
   - Set environment variable:
     ```bash
     export CENSUS_API_KEY='your_key_here'
     ```

## Project Structure

```
city_planning_101/
├── examples/               # Standalone Python scripts
│   ├── 01_import_census_data.py      # Census data import examples
│   ├── 02_pandas_numpy_analysis.py   # Data manipulation examples
│   ├── 03_data_visualization.py      # Visualization examples
│   └── 04_arcgis_integration.py      # ArcGIS API examples
├── notebooks/             # Jupyter notebooks
│   └── city_planning_tutorial.ipynb  # Comprehensive tutorial
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Usage

### Running Example Scripts

Each example script can be run independently:

```bash
# Example 1: Census data import (requires API key)
python examples/01_import_census_data.py

# Example 2: Data analysis with pandas/numpy
python examples/02_pandas_numpy_analysis.py

# Example 3: Data visualization
python examples/03_data_visualization.py

# Example 4: ArcGIS integration
python examples/04_arcgis_integration.py
```

### Using the Jupyter Notebook

For an interactive tutorial:

```bash
# Install Jupyter if not already installed
pip install jupyter

# Launch Jupyter
jupyter notebook notebooks/city_planning_tutorial.ipynb
```

## Examples Included

### 1. Census Data Import (`01_import_census_data.py`)
- Connect to Census API
- Query state and county-level data
- Import demographic and economic data
- Create pandas DataFrames from census data

### 2. Pandas & NumPy Analysis (`02_pandas_numpy_analysis.py`)
- Calculate urban planning metrics (population density, amenities per capita)
- Perform statistical analysis
- Create aggregations and summaries
- Calculate livability scores

### 3. Data Visualization (`03_data_visualization.py`)
- Population distribution charts
- Income vs crime scatter plots
- District metrics heatmaps
- Comprehensive dashboards
- Multiple visualization types with matplotlib and seaborn

### 4. ArcGIS Integration (`04_arcgis_integration.py`)
- Connect to ArcGIS Online
- Search for spatial data layers
- Geocode addresses
- Work with feature layers
- Create spatial DataFrames

## Key Concepts

### Census Data Variables

Common census variables used in city planning:
- `B01001_001E`: Total Population
- `B19013_001E`: Median Household Income
- `B25077_001E`: Median Home Value
- `B15003_022E`: Population with Bachelor's Degree or Higher

### Urban Planning Metrics

- **Population Density**: People per square mile
- **Amenity Access**: Parks, schools, facilities per capita
- **Crime Rate**: Incidents per 1,000 residents
- **Livability Score**: Composite metric of various factors

### Visualization Best Practices

- Use appropriate chart types for data
- Include clear labels and titles
- Normalize data for comparison
- Use color effectively
- Create multi-panel dashboards for comprehensive views

## Resources

### Census Data
- [Census API Documentation](https://www.census.gov/data/developers/data-sets.html)
- [Census Variables Explorer](https://api.census.gov/data.html)
- [Python census package](https://github.com/datamade/census)

### ArcGIS
- [ArcGIS Python API](https://developers.arcgis.com/python/)
- [ArcGIS Online](https://www.arcgis.com/)
- [API Documentation](https://developers.arcgis.com/python/api-reference/)

### Data Visualization
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Pandas Visualization](https://pandas.pydata.org/docs/user_guide/visualization.html)

## Dependencies

Main packages used:
- `pandas`: Data manipulation and analysis
- `numpy`: Numerical computing
- `matplotlib`: Data visualization
- `seaborn`: Statistical data visualization
- `census`: U.S. Census data access
- `arcgis`: ArcGIS Python API

See `requirements.txt` for complete list with versions.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for improvements.

## License

This project is open source and available for educational purposes.

## Acknowledgments

- U.S. Census Bureau for providing open data
- Esri for the ArcGIS Python API
- The Python data science community for excellent tools
