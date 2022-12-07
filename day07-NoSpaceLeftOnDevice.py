class Folder:
    def __init__(self, name, parent):
        self._name = name
        self._parent = parent
        self._files = {}
        self._folders = {}

    def add_file(self, file_name, size):
        self._files[file_name] = size

    def add_folder(self, folder_name):
        self._folders[folder_name] = Folder(folder_name, self)
        return self._folders[folder_name]

    def size(self):
        total = 0
        for folder in self._folders.values():
            total += folder.size()
        for file in self._files.keys():
            total += self._files[file]
        return total

    def get_folders(self):
        return self._folders.values()

    def get_folder(self, folder_name):
        if folder_name in self._folders.keys():
            return self._folders[folder_name]
        return None

    def get_parent(self):
        return self._parent


def parse_input_into_folder_tree(lines):
    root = Folder('/', None)
    current_folder = root

    for line in lines:
        tokens = line.strip().split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    current_folder = current_folder.get_parent()
                elif tokens[2] == '/':
                    current_folder = root
                else:
                    current_folder = current_folder.get_folder(tokens[2])
            elif tokens[1] == "ls":
                pass
            else:
                raise Exception("unsupported command {0} in line:\n   {1}".format(tokens[1], line))
        else:
            if tokens[0] == "dir":
                if current_folder.get_folder(tokens[1]) is None:
                    current_folder.add_folder(tokens[1])
            else:
                current_folder.add_file(tokens[1], int(tokens[0]))

    return root


def main():
    f = open("day07.txt")
    lines = f.readlines()

    root = parse_input_into_folder_tree(lines)
    sum_of_most_100000 = 0
    folders_queue = [root]
    while len(folders_queue) > 0:
        folder = folders_queue.pop()
        folder_size = folder.size()
        if folder_size <= 100000:
            sum_of_most_100000 += folder_size
        for f in folder.get_folders():
            folders_queue.append(f)
    print(sum_of_most_100000)


if __name__ == '__main__':
    main()
