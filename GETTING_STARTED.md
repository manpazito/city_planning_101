# Getting Started with City Planning 101

This guide will help you quickly get started with importing census data, performing data analysis, and creating visualizations for city planning applications.

## Quick Setup (5 minutes)

### 1. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn census requests python-dotenv
```

### 2. Run Your First Example

```bash
# Try the data analysis example (no API keys required)
python examples/02_pandas_numpy_analysis.py
```

This will analyze sample city district data and show:
- Population statistics
- Urban planning metrics
- Correlation analysis
- Data aggregations

### 3. Try Visualization

```bash
# Create charts and dashboards
python examples/03_data_visualization.py
```

This generates:
- Population distribution charts
- Income vs crime scatter plots
- District metrics heatmaps
- Comprehensive dashboards

## Working with Census Data

### Get Your Census API Key

1. Visit: https://api.census.gov/data/key_signup.html
2. Fill out the form to receive your free API key via email
3. Set the environment variable:

```bash
export CENSUS_API_KEY='your_key_here'
```

### Run the Census Import Example

```bash
python examples/01_import_census_data.py
```

This example shows how to:
- Query state-level population data
- Query county-level demographic data
- Work with Census variables
- Convert data to pandas DataFrames

## Using the Jupyter Notebook

For an interactive learning experience:

```bash
# Install Jupyter
pip install jupyter

# Launch the tutorial notebook
jupyter notebook notebooks/city_planning_tutorial.ipynb
```

The notebook walks through:
- Census data concepts
- Data manipulation with pandas/numpy
- Creating visualizations
- Spatial data concepts

## Optional: ArcGIS Setup

The ArcGIS Python API is a large package with many dependencies. Install it only if you need GIS capabilities:

```bash
pip install arcgis
```

The ArcGIS example (`examples/04_arcgis_integration.py`) works with or without the package installed, providing educational information either way.

## Example Workflow

Here's a typical workflow for city planning analysis:

### 1. Import Data

```python
from census import Census
import pandas as pd

# Connect to Census API
c = Census('your_api_key')

# Query population data
data = c.acs5.state(
    ('NAME', 'B01001_001E'),  # State name and total population
    Census.ALL,
    year=2021
)

# Convert to DataFrame
df = pd.DataFrame(data)
```

### 2. Analyze with Pandas/NumPy

```python
import numpy as np

# Calculate statistics
mean_pop = np.mean(df['B01001_001E'])
std_pop = np.std(df['B01001_001E'])

# Calculate per-capita metrics
df['density'] = df['population'] / df['area']
df['parks_per_10k'] = (df['parks'] / df['population']) * 10000
```

### 3. Visualize Results

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Create visualizations
plt.figure(figsize=(12, 6))
plt.bar(df['state_name'], df['population'])
plt.title('Population by State')
plt.xticks(rotation=45)
plt.show()
```

## Common Census Variables

Here are some commonly used Census variables for city planning:

| Variable | Description |
|----------|-------------|
| B01001_001E | Total Population |
| B19013_001E | Median Household Income |
| B25077_001E | Median Home Value |
| B15003_022E | Bachelor's Degree or Higher |
| B25003_001E | Total Housing Units |
| B08301_001E | Means of Transportation to Work |
| B01002_001E | Median Age |
| B17001_002E | Population Below Poverty Level |

## Tips for Success

1. **Start Simple**: Begin with the pandas/numpy example that doesn't require API keys
2. **Explore Incrementally**: Try one example at a time
3. **Use the Notebook**: The Jupyter notebook provides interactive explanations
4. **Read the Code**: Each example is well-commented with explanations
5. **Modify Examples**: Change parameters to explore different data

## Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### Census API key issues
- Make sure you've signed up for a key
- Verify the environment variable is set: `echo $CENSUS_API_KEY`
- Try setting it in your script: `os.environ['CENSUS_API_KEY'] = 'your_key'`

### Visualization not showing
- On servers: Use `MPLBACKEND=Agg` environment variable
- Save plots instead: `plt.savefig('plot.png')`

### ArcGIS installation problems
- The package is large and optional
- Examples work without it installed
- Consider using it only when needed for GIS operations

## Next Steps

1. Review the comprehensive README.md
2. Work through the Jupyter notebook tutorial
3. Explore each example script
4. Modify examples for your specific use case
5. Check out the official documentation:
   - Census API: https://www.census.gov/data/developers/
   - Pandas: https://pandas.pydata.org/
   - Matplotlib: https://matplotlib.org/

## Need Help?

- Check example comments for detailed explanations
- Review error messages carefully
- Consult official documentation
- Experiment with sample data first

Happy city planning! 🏙️
