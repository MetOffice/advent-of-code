import abc
from abc import ABC


class Node(ABC):
    """
    A single node in a filetree
    """
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None

    def __repr__(self) -> str:
        return self.__str__()

    @abc.abstractmethod
    def size(self):
        pass

    @abc.abstractmethod
    def pretty_print(self, indent=0):
        pass
        

class File(Node):
    """
    A leaf node of the tree
    """
    def __init__(self, size, name) -> None:
        super().__init__(name)
        self._size = int(size)

    def __str__(self) -> str:
        return f"- {self.name} (file, size={self.size()})"

    def size(self):
        return self._size
    
    def pretty_print(self, indent=0):
        print("  " * indent + str(self))


class Directory(Node):
    """
    A node that can contain other nodes
    """
    def __init__(self, name) -> None:
        super().__init__(name)
        self.children = {}

    def __str__(self) -> str:
        return f"- {self.name} (dir, size={self.size()})"

    def size(self):
        return sum([child.size() for child in self.children.values()])
    
    def add_child(self, child: Node):
        self.children[child.name] = child
        child.parent = self

    def get_child(self, name):
        return self.children[name]
    
    def pretty_print(self, indent=0):
        print("  " * indent + str(self))
        for child in self.children.values():
            child.pretty_print(indent=indent + 1)

    def get_all_dirs(self):
        """
        Returns an iterator of all subdirectories, including itself
        """
        yield self
        for child in self.children.values():
            if isinstance(child, Directory):
                for dir in child.get_all_dirs():
                    yield dir
    
    
class TreeBuilder:
    """
    Builds trees
    """
    def __init__(self) -> None:
        self.root = Directory("/")
        self.cwd = None

    @staticmethod
    def build(path):
        builder = TreeBuilder()
        input_string = builder.load_txt(path)
        commands = builder.get_commands(input_string)
        for command in commands:
            builder.execute_command(command)
        return builder.root

    @staticmethod
    def load_txt(path):
        """
        Reads the file at path as a single string
        """
        with open(path) as file:
            return file.read()
        
    @staticmethod
    def get_commands(input_string: str):
        """
        Extract a list of commands from an input string
        """
        commands = input_string.split("$")
        return [command.strip() for command in commands if command]

    def execute_command(self, command: str):
        """
        Executes a single command from a string
        """
        words = command.split()
        command_name = words[0]
        command_args = words[1:]

        match command_name:
            case "cd":
                self.execute_cd(command_args[0])
            case "ls":
                self.execute_ls(command_args)
            case _:
                raise "aaah"
        
    def execute_cd(self, destination):
        """
        Execute a cd command to the destination
        """
        match destination:
            case "/":
                self.cwd = self.root
            case "..":
                self.cwd = self.cwd.parent
            case _:
                self.cwd = self.cwd.get_child(destination)

    def execute_ls(self, content_list):
        """
        Execute ls command, populating hte cwd with the content_list.
        content_list is alternately filesize/dir and names.
        """
        # Interpret as a list of (dir/size, name)
        pairs = zip(content_list[::2], content_list[1::2])
        for content, name in pairs:
            match content:
                case "dir":
                    self.cwd.add_child(Directory(name))
                case _:
                    self.cwd.add_child(File(content, name))


def part1(tree:Directory):
    """
    Find the total size of all directories smaller than 100,000
    """
    return sum([dir.size() for dir in tree.get_all_dirs() if dir.size() <= 100000])

def part2(tree:Directory):
    """
    Find the size of the smallest directory that would, if deleted, free up enough space
    """
    space_total = 7e7
    space_needed = 3e7
    space_used = tree.size()
    space_spare = space_total - space_used
    minimal_deletion = space_needed - space_spare

    best_deletion = space_total
    for dir in tree.get_all_dirs():
        if minimal_deletion <= dir.size() < best_deletion:
            best_deletion = dir.size()

    return best_deletion

def main():
    tree = TreeBuilder.build("../input.txt")
    tree.pretty_print()

    print(f"Part 1 solution: {part1(tree)}")
    print(f"Part 2 solution: {part2(tree)}")


if __name__ == "__main__":
    main()
