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
    ('Elevation', 'elevation', 'default/icons/009-topographic.png', 'Digital elevation models for land, ice and ocean surface. Includes terrestrial elevation, bathymetry and shoreline.'),
    ('Geology', 'geology', 'default/icons/010-geological.png', 'Geology characterised according to composition and structure. Includes bedrock, aquifers and geomorphology.'),
    ('Land Cover', 'land-cover', 'default/icons/011-allocate.png', 'Physical and biological cover of the earth\'s surface including artificial surfaces, agricultural areas, forests, (semi-)natural areas, wetlands, water bodies.'),
    ('Orthoimagery', 'orthoimagery', 'default/icons/012-map.png', 'Geo-referenced image data of the Earth\'s surface, from either satellite or airborne sensors.'),
    ('Atmospheric conditions', 'atmospheric-conditions', 'default/icons/013-meteorology.png', 'Physical conditions in the atmosphere. Includes spatial data based on measurements, on models or on a combination thereof and includes measurement locations.'),
    ('Agricultural and acquaculture facilities', 'agricultural-and-acquaculture-facilities', 'default/icons/014-fish.png', 'Farming equipment and production facilities (including irrigation systems, greenhouses and stables).'),
    ('Area management, restriction and regulation', 'area-management-restriction-and-regulation', 'default/icons/015-land.png', 'Areas managed, regulated or used for reporting at international, European, national, regional and local levels.'),
    ('Bio-geographical regions', 'bio-geographical-regions', 'default/icons/016-land-1.png', 'Areas of relatively homogeneous ecological conditions with common characteristics.'),
    ('Buildings', 'buildings', 'default/icons/017-buildings.png', 'Geographical location of buildings.'),
    ('Environmental monitoring facilities', 'environmental-monitoring-facilities', 'default/icons/018-system.png', 'Location and operation of environmental monitoring facilities includes observation and measurement of emissions, of the state of environmental media and of other ecosystem parameters.'),
    ('Energy resources', 'energy-resources', 'default/icons/019-renewable-energy.png', 'Energy resources including hydrocarbons, hydropower, bio-energy, solar, wind, etc., where relevant including depth/height information on the extent of the resource.'),
    ('Habitats and biotopes', 'habitats-and-biotopes', 'default/icons/020-owl.png', 'Geographical areas characterised by specific ecological conditions, processes, structure, and (life support) functions that physically support the organisms that live there.'),
    ('Human health and safety', 'human-health-and-safety', 'default/icons/021-hospital-sign.png', 'Geographical distribution of dominance of pathologies (allergies, cancers, respiratory diseases, etc.), information indicating the effect on health (biomarkers, decline of fertility, epidemics) or well-being of humans.'),
    ('Land use', 'land-use', 'default/icons/022-cityscape.png', 'Territory characterised according to its current and future planned functional dimension or socio-economic purpose (e.g. residential, industrial, commercial, agricultural, forestry, recreational).'),
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