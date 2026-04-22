import os
from pathlib import Path
import io
from config import READ_MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))    
    is_valid_path = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

    print(f"\ntarget file: {abs_file_path}")
    print(f"is_valid_path: {is_valid_path}\n")

    if not is_valid_path:
        return f'Error: Cannot read "{abs_file_path}" as it is outside the permitted working directory'
    if not Path(abs_file_path).is_file():
        return f'Error: File not found or is not a regular file: "{abs_file_path}"'
    
    content = ""

    try:
        with open(abs_file_path, "r") as f:
            content = f.read(READ_MAX_CHARS)

            limit_overflow = f.read(1)
            if not limit_overflow == "":
                    content += f'[...File "{file_path}" truncated at {READ_MAX_CHARS} characters]'
    except Exception as e:
        return f'Error: {e}'
    
    return content

