from functions.get_files_info import get_files_info
from config import working_directory

print(get_files_info(working_directory, "."))
print(get_files_info(working_directory, "pkg"))
print(get_files_info(working_directory, "/bin"))
print(get_files_info(working_directory, "../"))