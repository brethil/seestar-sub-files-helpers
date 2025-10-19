# seestar-sub-files-helpers

Some Python helper scripts to ease file manipulation for Seestar S50 processing

All these scripts (except exposure_time.py that requires astropy) should work with python 3.8 or above.  
They have been tested on Windows 10/11 only for now but they should be system-agnostic.  
No dependencies: it's all basic plain Python.

## What for ?

Here is the standard Seestar file management:

```
MyWorks
 ├───IC 1318         # Object folder: contains .fit, jpg but also _thn.jpg that I don't want to keep
 ├───IC 1318_sub     # Sub folder: contains sub .fit, but also jpg that are not needed
 ├───IC 5070
 ├───IC 5070_sub
 ├───Lunar
...
```

I use Siril for stacking my Seestar .fits subs, and I found more convenient to store my datas this way on my computer :

```
MyWorkDir
 ├───IC 1318
 │    └───lights            # All the sub .fit go in there, and only .fit files
 │    └───process           # All the temp files go in there, created while stacking, then deleted when stacking done
 │    └───stacked.fit       # the stacked .fits, by Seestar or by Siril that I keep
 ├───IC 5070
 │    └───lights
 ├───Lunar                  

...
```

I wanted to clean up my work worker to save up some disk space and automate file copying to add only new .fits files from Seestar into my work folder.  
I also wanted to get the total time of exposure on a specific object.  
And of course to generate a backup file for my subs, with a zip file by object, better safe than sorry !

**These scripts does not delete anything from the Seestar, just from your local work folder**

A first I had a copy of the Sveestar\MyWorks to my computer as a work dir.

I ran once :

- cleanup.py
- move_to_light.py

To get the folder structure I wanted.

Now I just run :

- import.py after a Seestar session,
- cleanup.py when my processing is done and my stacked images saved back in the object folder.
- backup.py when needed
- exposure_time.py to see what object deserves a new stacking

## Set you up

With a code or a text editor (notepad is ok, Word not really), open the file `params.py`  
In this file you'll find 3 mandatory variables you must set up before launching the scripts.  
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
- DELETE_FROM_OBJECT_FOLDERS -> you don't want them in a Object folder at root level

```
python cleanup.py
```

### move_to_light.py

**Move data from _sub folder to OBJ/lights folder and remove _sub (from local work folder only)**

```
python move_to_light.py
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

### exposure_time.py

**Prints exposure time for all light folder and number of subs**

Create a console print and a json containing these datas :

+-------------------+------------------------+--------------------+----------------+-----------------+-------------+
| Object name       | Exposure Time (alt-az) | Exposure Time (EQ) | Number of subs | Filters         | Folder size |
+-------------------+------------------------+--------------------+----------------+-----------------+-------------+
| M 31              |          0:59          |        2:36        |            856 | ['IRCUT', 'LP'] |      3.3 GB |
| IC 5070           |          0:20          |        2:59        |            600 | ['LP']          |      2.3 GB |
| M 51              |          0:47          |        1:42        |            529 | ['IRCUT', 'LP'] |      2.0 GB |
| C2025 A6 (Lemmon) |          0:00          |        1:22        |            364 | ['IRCUT']       |      1.4 GB |
| NGC 7000          |          0:11          |        1:12        |            360 | ['LP']          |      1.4 GB |
| M 27              |          0:28          |        0:28        |            243 | ['LP']          |    962.4 MB |
| M 13              |          0:28          |        0:31        |            243 | ['IRCUT', 'LP'] |    962.4 MB |
+-------------------+------------------------+--------------------+----------------+-----------------+-------------+

exposure_time.json
```
[
    [
        "Object name",
        "Exposure Time (alt-az)",
        "Exposure Time (EQ)",
        "Number of subs",
        "Filters",
        "Folder size",
        "Sessions"
    ],
    {
        "Exposure Time (EQ)": "2:36",
        "Exposure Time (alt-az)": "0:59",
        "Filters": [
            "IRCUT",
            "LP"
        ],
        "Folder size": "3.3 GB",
        "Number of subs": 856,
        "Object name": "M 31",
        "Sessions": [
            "2024-08-21",
            "2025-10-12",
            "2024-08-10",
            "2024-10-03",
            "2025-07-15",
            "2025-10-10",
            "2025-08-16"
        ]
    },
```

Requires [astropy](https://docs.astropy.org/en/stable/install.html) and [prettytable](https://pypi.org/project/prettytable/).


```
python exposure_time.py
```
