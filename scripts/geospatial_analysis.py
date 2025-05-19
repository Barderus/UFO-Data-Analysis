import geopandas as gpd
from shapely.geometry import Point
import geodatasets
import matplotlib.pyplot as plt


def prepare_geodata(df, lon_col='longitude', lat_col='latitude'):
    geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
    gdf = gpd.GeoDataFrame(df.copy(), geometry=geometry, crs="EPSG:4326")
    return gdf

def plot_world_map(gdf, output_file=None):
    # Load world basemap from geodatasets
    world = gpd.read_file(geodatasets.get_path('naturalearth.land'))

    # Plot base map and UFO points
    ax = world.plot(figsize=(15, 10), color='lightgray', edgecolor='black')
    gdf.plot(ax=ax, markersize=2, color='red', alpha=0.5)

    ax.set_title("Global UFO Sightings", fontsize=16)
    ax.axis('off')

    # Save image if output path is provided
    if output_file:
        plt.savefig(output_file, dpi=300)

    plt.show()
