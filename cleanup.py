"""Remove unwanted files from your work folder, 
   Edit variables
    DELETE_FROM_EVERYWHERE,
    DELETE_FROM_SUB_FOLDERS,
    DELETE_FROM_OBJECT_FOLDERS
   To match you own needs 
"""

from pathlib import Path
import params



def get_folder_size(path: Path):
    """ Return the size of a folder in human-readable format """
    total = sum(f.stat().st_size for f in path.glob('**/*') if f.is_file())
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if total < 1024.0:
            return f"{total:3.1f} {x}"
        total /= 1024.0
    return "Error"

def delete_all(path: Path, to_delete):
    """ Deletes list of files listed in 'to_delete' from path """
    for extension in to_delete:
        files = list(path.rglob(extension))
        for file in files:
            file.unlink()

work_path = Path(params.WORK_DIR)
folder_size_before = get_folder_size(work_path)

delete_all(work_path, params.DELETE_FROM_EVERYWHERE)

for d in work_path.iterdir():
    current_dir = Path(d)
    if d.name.endswith("-sub"):
        delete_all(current_dir, params.DELETE_FROM_SUB_FOLDERS)
    else:
        delete_all(current_dir, params.DELETE_FROM_OBJECT_FOLDERS)

folder_size_after = get_folder_size(work_path)

print(f"\nSize of {work_path} before clean-up: {folder_size_before}")
print(f"Size of {work_path} after clean-up: {folder_size_after}")
