from send2trash import send2trash
from pathlib import Path
import shutil
import os

root = Path.home()
empty = []
exclusions = {
    "Windows",
    "Program Files",
    "Program Files (x86)",
    "AppData",
    "$Recycle.Bin",
    "Release",
    "GitHub",
    "3ds stuff",
    "Desktop",
    "My Games"
}
for currentPath, dirs, files in os.walk(root, topdown=True):
    dirs[:] = [d for d in dirs if d not in exclusions]
    if not dirs and not files:
        print(f"Empty: {currentPath}")
        empty.append(currentPath)
print(f"found {len(empty)} empty registries.")
confirm = input("Enter to confirm delete: ")
if confirm == "":
    toDelete = Path("EmptyFolders")
    try:
        toDelete.mkdir()
        print(f"Directory '{toDelete}' created successfully.")
    except FileExistsError:
        print(f"Directory '{toDelete}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{toDelete}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    for folder in empty:
        folderPath = Path(folder)
        newPath = toDelete / f"{folderPath.parent.name}_{folderPath.name}"
        shutil.move(folder, newPath)

    send2trash(toDelete)
    print("deleted")