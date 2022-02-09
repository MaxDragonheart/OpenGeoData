import datetime
import pathlib
from typing import Union

from pathlib import Path

from fsspec import get_fs_token_paths


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