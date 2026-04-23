import os
import subprocess
from config import EXECUTION_TIMEOUT
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=f"Runs python file at the specified file path relative to the working directory. Accepts addtional CLI arguments as an optional array. Execution times out at {EXECUTION_TIMEOUT} seconds.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to run python code from, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="content to write to file, of type STRING"
            ),
        },
        required=["file_path"]
    ),
)

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)

    # a path beginning with "/" becomes root-relative on the current drive
    # os.path.join will discard abs_working_dir and return the absolute path.
    abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path)) 

    is_valid_path = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

    print(f"\ntarget directory: {abs_file_path}")
    print(f"is_valid_path: {is_valid_path}\n")

    if not is_valid_path:
        return f'Error: Cannot execute "{abs_file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: "{abs_file_path}" does not exist or is not a regular file'
    if not (abs_file_path.split(".")[-1] == "py"):
        return f'Error: "{abs_file_path}" is not a Python file'
    
    command = ["python", abs_file_path]

    if args is not None:
        command.extend(args)

    try:
        result = subprocess.run(
                command,
                cwd=abs_working_dir,
                capture_output=True,
                text=True,
                timeout=EXECUTION_TIMEOUT,
        )
    except Exception as e:
        return f'Error: executing python file: {e}'

    output = []
    if result.returncode != 0:
        output.append(f"Process exited with code {result.returncode}")
    if not result.stdout and not result.stderr:
        output.append("No output produced")
    if result.stdout:
        output.append(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        output.append(f"STDERR:\n{result.stderr}")
    return "\n".join(output)

