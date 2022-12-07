
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirectories = {}
        self.files = []

    def get_subdirectory(self, subdirectory_name):
        return self.subdirectories[subdirectory_name]

    def add_subdirectory(self, subdirectory):
        self.subdirectories[subdirectory.name] = subdirectory

    def add_file(self, file):
        self.files.append(file)

    def get_size(self):
        file_sizes = [file.size for file in self.files]
        directory_sizes = [directory.get_size() for directory in self.subdirectories.values()]
        return sum(file_sizes) + sum(directory_sizes)

with open("day7_input.txt") as f:
    terminal_output = [x.strip().split(" ") for x in f.readlines()]

root_directory = Directory("/", None)
current_directory = root_directory
all_directories = []
for line in terminal_output:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                current_directory = current_directory.parent
            elif line[2] == "/":
                current_directory = root_directory
            else:
                current_directory = current_directory.get_subdirectory(line[2])
        else:
            pass  # No need to process ls commands
    elif line[0].isdigit():
        current_directory.add_file(File(size=int(line[0]), name=line[1]))
    elif line[0] == "ls":
        pass
    else:
        new_directory = Directory(line[1], current_directory)
        current_directory.add_subdirectory(new_directory)
        all_directories.append(new_directory)

directory_sizes = [dir.get_size() for dir in all_directories]
print("Part 1:")
print(sum([x for x in directory_sizes if x <= 100000]))

total_filesystem_space = 70000000
space_required = 30000000
current_space_used = root_directory.get_size()
directory_size_to_delete = space_required - (total_filesystem_space - current_space_used)
print("Part 2:")
print(min([size for size in directory_sizes if size > directory_size_to_delete]))
