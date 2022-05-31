from django.conf import settings

import pathlib
import geopandas as gpd

from pathlib import Path
from typing import Union

from owslib.wms import WebMapService
from shapely.geometry import Polygon


WMS_THUMBNAILS = Path('gis-data/wms-thumbnails')
LOCAL_DOMAINS = [
    f"127.0.0.1:{settings.GS_HTTP_PORT}",
    f"127.0.0.1:{settings.GS_HTTP_PORT}",
    f"localhost:{settings.GS_HTTP_PORT}",
    f"localhost:{settings.GS_HTTP_PORT}",
]


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


def set_geoserver_origin(input_url: str) -> str:
    """
    Check url of Geoserver services. If Geoserver
    is activated from docker-compose, he must share the same
    network of OpenGeoData. [ref](https://stackoverflow.com/questions/72434631/connection-refused-between-two-containers#comment127961219_72434631)
    """
    domain = input_url.split("/")[2]

    if domain in LOCAL_DOMAINS:
        domain_list = input_url.split("/")
        url = f"{domain_list[0]}//geoserver:8080/{domain_list[3]}/{domain_list[4]}/{domain_list[5]}"
    else:
        url = input_url

    return url


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
