from functions.write_file import write_file
from config import WORKING_DIRECTORY

print(write_file(WORKING_DIRECTORY, "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file(WORKING_DIRECTORY, "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file(WORKING_DIRECTORY, "/tmp/temp.txt", "this should not be allowed"))

