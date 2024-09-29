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

def list_fits(path):
    """Return a list of .fit files"""
    return list(path.rglob('**/*.fit'))

def write_if_not_exist(dest: Path, src: Path):
    """Write file 'src' if it does not exist in 'dst'"""
    if not dest.exists():
        dest.write_bytes(src.read_bytes())
        print(f"(+) : {dest}")
