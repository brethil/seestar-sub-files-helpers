""" Imports new fit files from Seestar to OBJ/lights folders"""

from pathlib import Path
import params
from common import list_fits, write_if_not_exist

src_path = Path(params.SEESTAR_DIR)
dst_path = Path(params.WORK_DIR)

src_folders = [x.name for x in src_path.glob('*') if x.is_dir()]
dst_folders = [x.name for x in dst_path.glob('*') if x.is_dir()]

delta_folders = [x for x in src_folders if (x not in dst_folders and not x.endswith("_sub"))]

# Creating new folders
for d in delta_folders:
    new_folder = dst_path / d
    new_folder.mkdir()
    new_light_folder = new_folder / params.LIGHTS_FOLDER_NAME
    new_light_folder.mkdir()
    if params.CREATE_PROCESS_FOLDER :
        new_processed_folder = new_folder / params.PROCESSED_FOLDER_NAME
        new_processed_folder.mkdir()

# File copy
for d in src_path.iterdir():
    files = list_fits(d)
    # Not in _sub : copy fit
    if not d.name.endswith("_sub"):
        for f in files:
            new_file = Path(dst_path / d.name / f.name)
            write_if_not_exist(new_file, f)

    # In a _sub: copy fit in "lights" folder
    else:
        for f in files:
            current_object = d.name.replace("_sub","")
            new_file_str = f"{dst_path}/{current_object}/{params.LIGHTS_FOLDER_NAME}/{f.name}"
            new_file = Path(new_file_str)
            write_if_not_exist(new_file, f)
