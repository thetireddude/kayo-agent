import os
from pathlib import Path
import io
from config import READ_MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Returns file contents of a specified file path relative to the working directory. Truncates at a maximum character limit of {READ_MAX_CHARS}",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to get file contents from, relative to the working directory (default is the working directory itself)",
            ),
        },
        required=["file_path"]
    ),
)

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

