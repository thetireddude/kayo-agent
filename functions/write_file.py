import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)

    # a path beginning with "/" becomes root-relative on the current drive
    # os.path.join will discard abs_working_dir and return the absolute path.
    abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path)) 

    is_valid_path = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

    print(f"\ntarget directory: {abs_file_path}")
    print(f"is_valid_path: {is_valid_path}\n")

    if not is_valid_path:
        return f'Error: Cannot write to "{abs_file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abs_file_path):
        return f'Error: Cannot write to "{abs_file_path}" as it is a directory'
    
    # makes all intermediate dire needed to contain the leaf dir
    # If exist_ok False, FileExistsError raised if a dir exists
    # makedirs() raises error even if exist_ok=True when trying to create a file
    os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

    try:
        with open(abs_file_path, 'w') as f:
            len_written = f.write(content)
            return f'Successfully wrote to "{abs_file_path}" ({len_written} characters written)'
    except Exception as e:
        return f'Error: {e}'