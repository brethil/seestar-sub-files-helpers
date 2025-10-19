""" Library of functions used in other scripts """

from pathlib import Path

def rm_tree(pth: Path):
    """Deletes the directory 'pth' and all its sub directories"""
    for child in pth.iterdir():
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()

def dir_is_empty(path) -> bool:
    return not any(path.iterdir())    

def list_fits(path):
    """Return a list of .fit files"""
    return list(path.rglob('**/*.fit'))

def write_if_not_exist(dest: Path, src: Path):
    """Write file 'src' if it does not exist in 'dst'"""
    if not dest.exists():
        dest.write_bytes(src.read_bytes())
        print(f"(+) : {dest}")
        
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