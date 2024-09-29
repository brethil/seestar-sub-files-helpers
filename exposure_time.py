""" Prints total exposure time """

from pathlib import Path
from collections import OrderedDict
import datetime
import params

my_sky_objects = {}

def get_datas_from_sub(my_dir: Path):
    """Return a list of .fit files"""
    my_object = my_dir.parent.name
    fit_files = list(my_dir.rglob('*.fit'))
    my_sky_objects[my_object] = len(fit_files)

def print_my_sky_objects():
    """ Print exposure time from all objects with light folder """
    mso_desc = OrderedDict(sorted(my_sky_objects.items(), key=lambda kv: kv[1], reverse=True))
    print(f"\n           Directories */{params.LIGHTS_FOLDER_NAME}")
    print("-----------------------------------------------")
    print("Object name |  Min exp time  | Number of subs")
    for k, v in mso_desc.items():
        expo = datetime.timedelta(seconds=v*10)
        print(f" {k:<10} |   {expo}      |  {v}")
    print("-----------------------------------------------")

parent_path = Path(params.WORK_DIR)

for d in parent_path.iterdir():
    lights_folder = Path(f"{d}/{params.LIGHTS_FOLDER_NAME}")
    if lights_folder.is_dir():
        get_datas_from_sub(lights_folder)

print_my_sky_objects()
