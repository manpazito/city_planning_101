"""
Example script demonstrating ArcGIS Python API integration.

This script shows how to:
1. Connect to ArcGIS Online
2. Search for spatial data
3. Work with feature layers
4. Create simple maps

Note: This example uses anonymous access. For full functionality,
you would need an ArcGIS Online account.
"""

from arcgis.gis import GIS
from arcgis.geocoding import geocode
from arcgis.geometry import Point
import pandas as pd


def connect_to_arcgis():
    """
    Connect to ArcGIS Online.
    
    Returns:
        GIS object for ArcGIS Online connection
    """
    print("Connecting to ArcGIS Online...")
    
    # Connect anonymously (no login required for public data)
    # For authenticated access, use: GIS("https://www.arcgis.com", username, password)
    gis = GIS()
    
    print(f"Connected successfully!")
    print(f"ArcGIS version: {gis.version}")
    
    return gis


def search_census_layers(gis):
    """
    Search for census-related feature layers in ArcGIS Online.
    
    Args:
        gis: GIS connection object
    """
    print("\n" + "=" * 60)
    print("Searching for Census Data Layers")
    print("=" * 60)
    
    # Search for census tract data
    search_results = gis.content.search(
        query="census tracts USA owner:esri",
        item_type="Feature Layer",
        max_items=5
    )
    
    print(f"\nFound {len(search_results)} items:")
    for idx, item in enumerate(search_results, 1):
        print(f"\n{idx}. {item.title}")
        print(f"   Type: {item.type}")
        print(f"   Owner: {item.owner}")
        print(f"   ID: {item.id}")
        if item.description:
            # Truncate description if too long
            desc = item.description[:100] + "..." if len(item.description) > 100 else item.description
            print(f"   Description: {desc}")
    
    return search_results


def geocode_addresses_example(gis):
    """
    Demonstrate geocoding with ArcGIS.
    
    Args:
        gis: GIS connection object
    """
    print("\n" + "=" * 60)
    print("Geocoding Examples")
    print("=" * 60)
    
    # Sample addresses for city planning locations
    addresses = [
        "1600 Pennsylvania Avenue NW, Washington, DC",
        "Empire State Building, New York, NY",
        "Golden Gate Bridge, San Francisco, CA",
        "Space Needle, Seattle, WA",
        "Willis Tower, Chicago, IL"
    ]
    
    results = []
    
    for address in addresses:
        print(f"\nGeocoding: {address}")
        try:
            geocoded = geocode(address, max_locations=1)
            if geocoded:
                location = geocoded[0]
                results.append({
                    'address': address,
                    'matched_address': location['address'],
                    'latitude': location['location']['y'],
                    'longitude': location['location']['x'],
                    'score': location['score']
                })
                print(f"  ✓ Lat: {location['location']['y']:.6f}, "
                      f"Lon: {location['location']['x']:.6f}")
            else:
                print(f"  ✗ No results found")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    # Convert to DataFrame
    df = pd.DataFrame(results)
    
    if not df.empty:
        print("\n" + "=" * 60)
        print("Geocoding Results Summary")
        print("=" * 60)
        print(df.to_string(index=False))
    
    return df


def explore_feature_layer_example(gis):
    """
    Explore a public feature layer.
    
    Args:
        gis: GIS connection object
    """
    print("\n" + "=" * 60)
    print("Feature Layer Exploration")
    print("=" * 60)
    
    try:
        # Search for USA demographic data
        search_results = gis.content.search(
            query="USA States Demographics owner:esri",
            item_type="Feature Layer",
            max_items=1
        )
        
        if search_results:
            item = search_results[0]
            print(f"\nExploring: {item.title}")
            
            # Get the first layer
            layer = item.layers[0]
            print(f"Layer name: {layer.properties.name}")
            print(f"Geometry type: {layer.properties.geometryType}")
            print(f"Feature count: {layer.query(return_count_only=True)}")
            
            # Query some features
            print("\nQuerying sample features...")
            feature_set = layer.query(where="1=1", out_fields="*", return_geometry=False)
            
            if feature_set.features:
                print(f"Retrieved {len(feature_set.features)} features")
                
                # Show first feature's attributes
                first_feature = feature_set.features[0]
                print("\nSample feature attributes:")
                for key, value in list(first_feature.attributes.items())[:10]:
                    print(f"  {key}: {value}")
            
            return layer
        else:
            print("No feature layers found")
            return None
            
    except Exception as e:
        print(f"Error exploring feature layer: {e}")
        return None


def create_spatial_dataframe_example():
    """
    Create a spatial DataFrame for city planning locations.
    """
    print("\n" + "=" * 60)
    print("Creating Spatial DataFrame")
    print("=" * 60)
    
    # Sample city planning facilities
    facilities = {
        'name': [
            'City Hall',
            'Central Park',
            'Community Center',
            'Public Library',
            'Fire Station'
        ],
        'type': [
            'Government',
            'Recreation',
            'Community',
            'Education',
            'Emergency'
        ],
        'latitude': [
            40.7128,
            40.7829,
            40.7589,
            40.7531,
            40.7308
        ],
        'longitude': [
            -74.0060,
            -73.9654,
            -73.9851,
            -73.9772,
            -73.9973
        ],
        'capacity': [
            500,
            50000,
            300,
            150,
            50
        ]
    }
    
    df = pd.DataFrame(facilities)
    
    print("\nCity Planning Facilities:")
    print(df.to_string(index=False))
    
    print("\n✓ Spatial DataFrame created with location data")
    print("  This data can be used to create feature layers or web maps")
    
    return df


def demonstrate_spatial_analysis():
    """
    Demonstrate basic spatial analysis concepts.
    """
    print("\n" + "=" * 60)
    print("Spatial Analysis Concepts")
    print("=" * 60)
    
    print("""
Key spatial analysis capabilities with ArcGIS Python API:

1. Geocoding & Reverse Geocoding
   - Convert addresses to coordinates
   - Find addresses from coordinates

2. Feature Layer Operations
   - Query spatial data
   - Filter by attributes and location
   - Update and add features

3. Spatial Relationships
   - Distance calculations
   - Proximity analysis
   - Buffer operations

4. Geoprocessing
   - Overlay analysis
   - Spatial joins
   - Interpolation

5. Web Maps
   - Create interactive maps
   - Add layers and widgets
   - Share maps online

For full functionality, sign up for ArcGIS Online:
https://www.arcgis.com/
    """)


if __name__ == '__main__':
    print("=" * 60)
    print("ArcGIS Python API Integration Example")
    print("=" * 60)
    
    try:
        # Connect to ArcGIS
        gis = connect_to_arcgis()
        
        # Search for census layers
        search_census_layers(gis)
        
        # Geocoding examples
        geocode_addresses_example(gis)
        
        # Explore feature layers
        explore_feature_layer_example(gis)
        
        # Create spatial DataFrame
        create_spatial_dataframe_example()
        
        # Show spatial analysis concepts
        demonstrate_spatial_analysis()
        
        print("\n" + "=" * 60)
        print("ArcGIS integration examples completed!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you have the arcgis package installed:")
        print("  pip install arcgis")
