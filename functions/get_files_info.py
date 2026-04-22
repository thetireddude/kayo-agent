import os
from pathlib import Path

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)

    # a path beginning with "/" becomes root-relative on the current drive
    # os.path.join will discard abs_working_dir and return the absolute path.
    target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))

    is_valid_path = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir

    print(f"\ntarget directory: {target_dir}")
    print(f"is_valid_path: {is_valid_path}\n")

    if not is_valid_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not Path(target_dir).is_dir():
        return f'Error: "{target_dir}" is not a directory'

    
    dir_contents = []
    with os.scandir(target_dir) as entries:
        for entry in entries:
            try:
                file_size = entry.stat().st_size
                name = entry.name
                is_dir = entry.is_dir()
                dir_contents.append(f"{name}: file_size={file_size} bytes, is_dir={is_dir}")
            except Exception as e:
                return f"Error: {e}"
        
    return dir_contents

