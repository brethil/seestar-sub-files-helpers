# seestar-sub-files-helpers

Some Python helper scripts to ease file manipulation for Seestar S50 processing

These scripts should work with python 3.8 or above.  
They have been tested on Windows 10 only for now but they should be system-agnostic.  
No dependencies: it's all basic plain Python.

## What for ?

Here is the standard Seestar file management:

```
MyWorks
 ├───IC 1318         # Object folder: contains .fit, jpg but also _thn.jpg that I don't want to keep
 ├───IC 1318-sub     # Sub folder: contains sub .fit, but also jpg that are not needed
 ├───IC 5070
 ├───IC 5070-sub
 ├───Lunar
...
```

I use Siril for stacking my Seestar .fits subs, and I found more convenient to store my datas this way :

```
MyComputer
 ├───IC 1318
 │    └───lights     # All the sub .fit go in there, and only .fit files
 │    └───processed  # All the temp files go in there, created while stacking, then deleted when stacking done
 ├───IC 5070
 │    └───lights
 ├───Lunar           # Keep some files in this level: .fits, .jpg... Not everything is stack

...
```

I wanted to clean up my work worker to same some space and automate the file copying to add only new .fits files from Seestar into my work folder.  
I also wanted to get the total time of exposure on a specific object.  
And of course to generate a backup file for my subs, with a zip file by object, better safe than sorry !

**These scripts does not delete anything from the Seestar, just from your local work folder**

A first I had a copy of the Sveestar\MyWorks to my computer as a work dir.

I ran once :

- cleanup.py
- move_to_light.py

To get the file structure I wanted.

Now I just run :

- import.py after a Seestar session,
- exposure_time.py to see what deserves a new stacking
- cleanup.py when my processing is done.
- backup.py every week

## Set you up

With a code or a text editor (notepad is ok, Word not so much :-)), open the file `prepare.py`  
In this file you'll find 3 mandatory variables you must set up before launching the script.  
(Lines starting with a "#" are comments)

```
# SEESTAR_DIR = r'D:\MyWorks'
SEESTAR_DIR = r'<REPLACE WITH YOUR OWN>'

# WORK_DIR = r'F:\Seestar_Data\MyWorks'
WORK_DIR = r'<REPLACE WITH YOUR OWN>'

# BACKUP_DIR = r'G:\Autres ordinateurs\USB et périphériques externes\Seestar\MyWorks'
BACKUP_DIR = r'<REPLACE WITH YOUR OWN>'
```

### The scripts

### cleanup.py

**Remove unwanted files from your work folder**  
If you local work folder is a copy of your Seestar MyWorks folder, you can run this one first.
You might want to edit these variables from params.py to match you own needs :

- DELETE_FROM_EVERYWHERE, -> you don't want these, nowhere
- DELETE_FROM_SUB_FOLDERS, -> you don't want them in -sub folders
- DELETE_FROM_OBJECT_FOLDERS -> you don't want them in a OBJ folder at root level

```
python cleanup.py
```

### move_to_light.py

**Move data from -sub folder to OBJ/lights folder and remove -sub (from local work folder only)**

```
python move_to_light.py
```

### exposure_time.py

**Prints minimum exposure time for all light folder and number of subs**
Still in work in progress as the exposure is just number of subs \* 10, it was enough for me as I only take 10s shoot.  
I might add a version that actually reads this from .fit files.

```
python exposure_time.py
```

### import.py

**Imports only new fit files from Seestar to OBJ/lights folder**
When your initial clean up is done, this is the way to add your new subs only.

```
python import.py
```

### backup.py

**Backs up your work folder in the backup folder (see params.py), with a .zip by object in a global archive**

```
python backup.py
```
