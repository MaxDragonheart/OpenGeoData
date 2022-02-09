import datetime
import pathlib
import geopandas as gpd

from pathlib import Path
from typing import Union

from fsspec import get_fs_token_paths
from owslib.wms import WebMapService
from shapely.geometry import Polygon


WMS_THUMBNAILS = Path('gis-data/wms-thumbnails')


def get_centroid_coords(bbox: tuple) -> tuple:
    """Generate centroid from bounding box coordinates.
    Args:
        bbox: Tuple
    Returns:
        Centroid coordinates
    """
    # Create Polygon from bounds.
    bbox_polygon = Polygon(
        [
            (bbox[0], bbox[3]),
            (bbox[2], bbox[3]),
            (bbox[2], bbox[1]),
            (bbox[0], bbox[1]),
            (bbox[0], bbox[3]),
        ]
    )
    # Read centroid coords
    polygon = gpd.GeoSeries([bbox_polygon])
    centroid = polygon.centroid[0].x, polygon.centroid[0].y

    return centroid


def get_wms_bbox(
        wms_url: str,
        service_version: str,
        layer_name: str,
) -> tuple:
    """Get BBOX from WMS layer.
    Args:
        wms_url: String.
        service_version: String.
        layer_name: String.
    Returns:
        Tuple of coordinates.
    """
    wms = WebMapService(url=wms_url, version=service_version)
    bbox = wms[layer_name].boundingBoxWGS84

    return bbox


def get_wms_thumbnail(
        wms_url: str,
        service_version: str,
        layer_name: str,
        output_data_folder: Union[str, pathlib.PosixPath],
        srs: str = 'EPSG:4326',
        width: int = 300,
        high: int = 300,
) -> pathlib.PosixPath:
    """Get thumbnail from WMS layer, it's saved into selected folder and also return
    the saved path.
    Args:
        wms_url: String.
        service_version: String.
        layer_name: String.
        output_data_folder: Union[str, pathlib.PosixPath]
        srs: String.
        width: Integer.
        high: Integer.
    Returns:
        pathlib.PosixPath
    """
    # Read WMS
    wms = WebMapService(url=wms_url, version=service_version)

    # Get bounding box from selected layer
    layer = wms[layer_name]
    bbox = layer.boundingBoxWGS84

    # Create thumbnail
    img = wms.getmap(
        layers=[layer_name],
        srs=srs,
        bbox=bbox,
        size=(width, high),
        format='image/jpeg',
        transparent=True
    )

    # # Create the today folder
    # today = datetime.datetime.now()
    # today_folder = f"{today.year}/{today.month}/{today.day}"
    # destination_folder = Path(f"{output_data_folder}/{today_folder}")
    # print(destination_folder)
    # fs, fs_token, paths = get_fs_token_paths(destination_folder)
    # fs.mkdirs(path=destination_folder, exist_ok=True)

    # Put thumbnail into destinantion folder
    img_path = Path(f'{output_data_folder}/{layer.title}.jpg')
    out = open(img_path, 'wb')
    out.write(img.read())
    out.close()

    return img_path
