"""
Utility functions for GIS operations.
"""
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon
from typing import Union, List, Tuple

def read_spatial_data(file_path: str) -> gpd.GeoDataFrame:
    """
    Read spatial data from various file formats.
    
    Args:
        file_path (str): Path to the spatial data file
        
    Returns:
        gpd.GeoDataFrame: Loaded spatial data
    """
    return gpd.read_file(file_path)

def reproject_data(gdf: gpd.GeoDataFrame, target_crs: str) -> gpd.GeoDataFrame:
    """
    Reproject spatial data to a different coordinate reference system.
    
    Args:
        gdf (gpd.GeoDataFrame): Input GeoDataFrame
        target_crs (str): Target CRS in EPSG format (e.g., 'EPSG:4326')
        
    Returns:
        gpd.GeoDataFrame: Reprojected GeoDataFrame
    """
    return gdf.to_crs(target_crs)

def create_point_from_coordinates(
    latitude: float,
    longitude: float,
    crs: str = "EPSG:4326"
) -> gpd.GeoDataFrame:
    """
    Create a GeoDataFrame from latitude and longitude coordinates.
    
    Args:
        latitude (float): Latitude coordinate
        longitude (float): Longitude coordinate
        crs (str): Coordinate reference system (default: WGS84)
        
    Returns:
        gpd.GeoDataFrame: Point geometry in a GeoDataFrame
    """
    point = Point(longitude, latitude)
    return gpd.GeoDataFrame(
        geometry=[point],
        crs=crs
    )

def calculate_area(
    geometry: Union[Polygon, gpd.GeoDataFrame],
    units: str = "m2"
) -> float:
    """
    Calculate area of a polygon geometry.
    
    Args:
        geometry: Input polygon geometry or GeoDataFrame
        units (str): Area units ('m2' or 'km2')
        
    Returns:
        float: Area in specified units
    """
    if isinstance(geometry, gpd.GeoDataFrame):
        # Ensure the geometry is in a projected CRS
        if geometry.crs and geometry.crs.is_geographic:
            geometry = geometry.to_crs(geometry.estimate_utm_crs())
        area = geometry.area.sum()
    else:
        area = geometry.area
        
    return area / 1_000_000 if units == "km2" else area
