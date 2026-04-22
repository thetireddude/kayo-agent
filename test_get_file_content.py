from functions.get_file_content import get_file_content
from config import WORKING_DIRECTORY

print(get_file_content(WORKING_DIRECTORY, "lorem.txt"))
print(get_file_content(WORKING_DIRECTORY, "main.py"))
print(get_file_content(WORKING_DIRECTORY, "pkg/calculator.py"))
print(get_file_content(WORKING_DIRECTORY, "/bin/cat"))
print(get_file_content(WORKING_DIRECTORY, "pkg/does_not_exist.py"))