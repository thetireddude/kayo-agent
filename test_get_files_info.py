from functions.get_files_info import get_files_info
from config import WORKING_DIRECTORY

print(get_files_info(WORKING_DIRECTORY, "."))
print(get_files_info(WORKING_DIRECTORY, "pkg"))
print(get_files_info(WORKING_DIRECTORY, "/bin"))
print(get_files_info(WORKING_DIRECTORY, "../"))