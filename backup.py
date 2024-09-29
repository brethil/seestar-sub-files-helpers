"""Backs up your work_dir in the back_dir (see params.py), 
   with a .zip by object in a global archive"""

from pathlib import Path
import shutil
from datetime import datetime
import os
import params
from common import rm_tree, write_if_not_exist


data_path = Path(params.WORK_DIR)
backup_path = Path(params.BACKUP_DIR)
run_path = Path(__file__).resolve().parent
mytimestamp = datetime.today().strftime('%Y-%m-%d')
backup_folder = Path(f"{run_path}/{mytimestamp}-backup")

if not backup_folder.exists():
    backup_folder.mkdir()

os.chdir(backup_folder)

for d in data_path.iterdir():
    current_dir = Path(d)
    file_name = f"{d.name}_{mytimestamp}"
    shutil.make_archive(file_name, 'zip', current_dir)

os.chdir(run_path)

backup_file_name = f"backup_{mytimestamp}"
shutil.make_archive(backup_file_name, 'zip', backup_folder)

rm_tree(backup_folder)

full_backup_src = Path(f"{run_path}/{backup_file_name}.zip")
full_backup_dst = Path(f"{backup_path}/{backup_file_name}.zip")

write_if_not_exist(full_backup_dst,full_backup_src)

full_backup_src.unlink()
