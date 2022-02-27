import datetime
import pathlib
from typing import Union

from pathlib import Path
from django.conf import settings
from fsspec import get_fs_token_paths


social_netoworks = [
    ('Facebook', 'www.facebook.com', '<i class="fab fa-facebook-f"></i>'),
    ('LinkedIn', 'www.linkedin.com', '<i class="fab fa-linkedin-in"></i>'),
    ('Instagram', 'www.instagram.com', '<i class="fab fa-instagram"></i>'),
    ('YouTube', 'www.youtube.com', '<i class="fab fa-youtube"></i>'),
]

tags = [
    ('Addresses', 'addresses', 'default/icons/001-address.png', 'Location of properties based on address identifiers, usually by road name, house number, postal code.'),
    ('Administrative units', 'administrative-units', 'default/icons/002-united-arab-emirates.png', 'Units of administration, dividing areas where Member States have and/or exercise jurisdictional rights, for local, regional and national governance, separated by administrative boundaries.'),
    ('Cadastral parcels', 'cadastral-parcels', 'default/icons/002-united-arab-emirates.png', 'Areas defined by cadastral registers or equivalent.'),
    ('Geographical grid system', 'geographical-grid-system', 'default/icons/003-world.png', 'Harmonised multi-resolution grid with a common point of origin and standardised location and size of grid cells.'),
    ('Geographical names', 'geographical-names', 'default/icons/004-signpost.png', 'Names of areas, regions, localities, cities, suburbs, towns or settlements, or any geographical or topographical feature of public or historical interest.'),
    ('Hydrography', 'hydrography', 'default/icons/005-river.png', 'Hydrographic elements, including marine areas and all other water bodies and items related to them, including river basins and sub-basins.'),
    ('Protected sites', 'protected-sites', 'default/icons/006-wild-harvested-ingredients.png', 'Area designated or managed within a framework of international, Community and Member States\' legislation to achieve specific conservation objectives.'),
    ('Coordinate reference systems', 'coordinate-reference-systems', 'default/icons/007-coordinates.png', 'Systems for uniquely referencing spatial information in space as a set of coordinates (x, y, z) and/or latitude and longitude and height, based on a geodetic horizontal and vertical datum.'),
    ('Transport networks', 'transport-networks', 'default/icons/008-infrastructure.png', 'Road, rail, air and water transport networks and related infrastructure. Includes links between different networks.'),
]


# def create_site_logo() -> pathlib.PosixPath:
#     """Create temporary logo path
#
#     :return: pathlib.PosixPath
#     """
#     # Get temporary logo from
#     # static folder
#     # TODO path doesn't existis
#     logo = pathlib.Path('./static/images/logo.png')
#     logo_name = logo.stem
#     logo_extension = logo.suffix
#     logo_name_extension = logo_name + logo_extension
#     print(logo)
#     print(logo.exists())
#     print(logo_name_extension)
#     # Create destination folder
#     site_logo_folder = settings.MEDIA_FOLDER / pathlib.Path('default')
#     fs, fs_token, paths = get_fs_token_paths(site_logo_folder)
#     fs.mkdirs(path=site_logo_folder, exist_ok=True)
#
#     # Copy temporary logo
#     # to destination folder
#     destination = site_logo_folder / logo_name_extension
#     print(destination)
#     print(f"Copying file: {logo} ---> {destination}")
#     fs.put_file(logo, destination)
#
#     return destination

def to_folder_today(
        file:  Union[str, pathlib.PosixPath],
        output_folder:  Union[str, pathlib.PosixPath]
) -> pathlib.PosixPath:
    # Chech if file is it a pathlib.PosixPath
    file = _str_to_path(file)
    file_name = file.stem
    file_extension = file.suffix
    file_name_extension = file_name + file_extension

    # Create the today folder
    today = datetime.datetime.now()
    destination_folder = Path(f"{output_folder}/{today.year}/{today.month}/{today.day}")
    fs, fs_token, paths = get_fs_token_paths(destination_folder)
    fs.mkdirs(path=destination_folder, exist_ok=True)

    # Copy file to today folder
    destination = destination_folder / file_name_extension
    print(f"Copying file: {file} ---> {destination}")
    fs.put_file(file, destination)

    return destination


def _str_to_path(path_string:  Union[str, pathlib.PosixPath]) -> pathlib.PosixPath:
    """Check if the input is a string or a pathlib.PosixPath.
    If it is a string will be translated in a pathlib.PosixPath.
    Args:
        path_string:  Union[str, pathlib.PosixPath].
    Returns:
        pathlib.PosixPath
    Raises:
        Must be str or pathlib.PosixPath!
    """
    if isinstance(path_string, pathlib.PosixPath):
        print(f"{path_string} is already a pathlib.PosixPath")
        return path_string
    elif isinstance(path_string, str):
        return pathlib.Path(path_string)
    else:
        raise Exception("Must be str or pathlib.PosixPath!")