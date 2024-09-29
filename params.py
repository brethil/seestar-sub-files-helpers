""" Parameters for the scripts """

# Your Seestar MyWorks folder
# (The r before the path is important)
# Examples :
# SEESTAR_DIR = r'D:\MyWorks'
SEESTAR_DIR = r'<REPLACE WITH YOUR OWN>'

# Your local (on your computer) work folder
# (The r before the path is important)
# Example :
# WORK_DIR = r'F:\Seestar_Data\MyWorks'
WORK_DIR = r'<REPLACE WITH YOUR OWN>'

# For the backup script, your back-up destination (here a Google drive folder)
# (The r before the path is important)
# Example :
# BACKUP_DIR = r'G:\Autres ordinateurs\USB et périphériques externes\Seestar\MyWorks'
BACKUP_DIR = r'<REPLACE WITH YOUR OWN>'

# Name you use to store all your sub fits files before processing
# Example :
# LIGHTS_FOLDER_NAME = "lights"
LIGHTS_FOLDER_NAME = "lights"

# The files you do not want to keep when your processing is done
# They will be deleted from WORK_DIR only (not from Seetar)
DELETE_FROM_EVERYWHERE = ["*.lst","*.seq", "*.txt","process*/*.fit", "*_thn.jpg"]

# The files you want to remove from OBJECT-sub directories only
# They will be deleted from WORK_DIR only (not from Seetar)
DELETE_FROM_SUB_FOLDERS = ["*.jpg"]

# The files you want to remove from OBJECT directories only
# They will be deleted from WORK_DIR only (not from Seetar)
DELETE_FROM_OBJECT_FOLDERS = []
