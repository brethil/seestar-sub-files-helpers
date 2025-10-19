""" Prints total exposure time in the console and in a json file"""

from pathlib import Path
from astropy.io import fits
from collections import OrderedDict
import datetime
import params
from prettytable import PrettyTable
import common


my_sky_objects = {}

def get_datas_from_sub(my_dir: Path):
    """Return infos from .fit files"""
    folder_size = common.get_folder_size(my_dir)
    my_object = my_dir.parent.name
    fit_files = list(my_dir.rglob('*.fit'))
    total_exposure_alt_az = 0
    total_exposure_eq = 0
    filters = []
    sessions = []

    for fit_file in fit_files :
        read_file = fits.open(fit_file)
        exposure = read_file[0].header["TOTALEXP"]
        headers = read_file[0].header.keys()
        eqmode = 0
        
        if "EQMODE" in headers :
            eqmode = read_file[0].header["EQMODE"]
            
        date_obs = datetime.datetime.strptime(read_file[0].header["DATE-OBS"], "%Y-%m-%dT%H:%M:%S.%f")
        day_obs = datetime.datetime.strftime(date_obs, "%Y-%m-%d")
        if day_obs not in sessions :
            sessions.append(day_obs)
        filter = read_file[0].header["FILTER"]
        if filter not in filters:
            filters.append(filter)
        if eqmode == 1 :
            total_exposure_eq += exposure
        else :
            total_exposure_alt_az += exposure
        
        
    my_sky_objects[my_object] = {
        "total_exp_altaz" : total_exposure_alt_az,
        "total_exp_eq" : total_exposure_eq,
        "nb_subs" : len(fit_files),
        "filters" : filters,
        "folder_size" : folder_size,
        "sessions" : sessions
        }

def print_my_sky_objects():
    """ Print exposure time from all objects and save to json """
    mso_desc = OrderedDict(my_sky_objects.items())
    
    x = PrettyTable()
    x.field_names = ["Object name", "Exposure Time (alt-az)", "Exposure Time (EQ)", "Number of subs", "Filters", "Folder size", "Sessions"]
    x.align["Object name"] = "l"
    x.align["Exposure Time (alt-az)"] = "c" 
    x.align["Exposure Time (EQ)"] = "c" 
    x.align["Number of subs"] = "r" 
    x.align["Filters"] = "l" 
    x.align["Folder size"] = "r" 
    x.align["Sessions"] = "l"
    x.sortby = "Number of subs"
    x.reversesort = True
    for k, v in mso_desc.items():
        expo_altaz = datetime.timedelta(seconds=v["total_exp_altaz"])
        expo_altaz_str = str(expo_altaz)      
        expo_eq = datetime.timedelta(seconds=v["total_exp_eq"])
        expo_eq_str = str(expo_eq)
        x.add_row([k, expo_altaz_str[:-3], expo_eq_str[:-3], v["nb_subs"],v["filters"],v["folder_size"],v["sessions"]])
    print(x.get_string(fields=["Object name", "Exposure Time (alt-az)", "Exposure Time (EQ)", "Number of subs", "Filters", "Folder size"]))
    
    f = open('exposure_time.json', 'wb')
    f.write(x.get_json_string().encode())
    

parent_path = Path(params.WORK_DIR)

for d in parent_path.iterdir():
    lights_folder = Path(f"{d}/{params.LIGHTS_FOLDER_NAME}")
    if lights_folder.is_dir():
        get_datas_from_sub(lights_folder)

print_my_sky_objects()
