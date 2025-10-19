"""Remove unwanted files from your work folder, 
   Edit variables
    DELETE_FROM_EVERYWHERE,
    DELETE_FROM_SUB_FOLDERS,
    DELETE_FROM_OBJECT_FOLDERS
   To match you own needs 
"""

from pathlib import Path
import params
import common





work_path = Path(params.WORK_DIR)
folder_size_before = common.get_folder_size(work_path)

common.delete_all(work_path, params.DELETE_FROM_EVERYWHERE)

for d in work_path.iterdir():
    current_dir = Path(d)

    if d.name.endswith("_sub"):
        common.delete_all(current_dir, params.DELETE_FROM_SUB_FOLDERS)
    else:
        common.delete_all(current_dir, params.DELETE_FROM_OBJECT_FOLDERS)
    for p in current_dir.iterdir():
        if p.name.endswith(params.PROCESSED_FOLDER_NAME) :
            processed_folder = Path(p)
            if params.CREATE_PROCESS_FOLDER == False:
                if common.dir_is_empty(processed_folder):
                    common.rm_tree(processed_folder)

folder_size_after = common.get_folder_size(work_path)

print(f"\nSize of {work_path} before clean-up: {folder_size_before}")
print(f"Size of {work_path} after clean-up: {folder_size_after}")
