""" Move all local 'OBJ-sub' folder to 'OBJ/lights' folder """

from pathlib import Path
import params
from common import list_fits, rm_tree

parent_path = Path(params.WORK_DIR)

for d in parent_path.iterdir():
    current_dir = Path(d)

    if d.name.endswith("-sub"):
        current_object = current_dir.name.replace("-sub","")
        dst_folder =  f"{parent_path}/{current_object}/{params.LIGHTS_FOLDER_NAME}"
        dst_path = Path(dst_folder)

        if not dst_path.is_dir():
            dst_path.mkdir()

        files = list_fits(d)

        for f in files:
            new_file = Path(dst_path / f.name)

            if not new_file.exists():
                new_file.write_bytes(f.read_bytes())
                print(f"+ : {new_file}")
        rm_tree(current_dir)
