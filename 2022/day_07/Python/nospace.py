import abc
from abc import ABC


class Node(ABC):
    """
    A single node in a filetree
    """
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        self._size = None

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
        return f"- {self.name} (file)"

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
        self._size = None

    def __str__(self) -> str:
        return f"- {self.name} (dir, size={self.size()})"

    def size(self):
        self._size = sum([child[1].size() for child in self.children.items()])
        return self._size
    
    def add_child(self, child: Node):
        self.children[child.name] = child
        child.parent = self
        self.size()

    def get_child(self, name):
        for child_name, child in self.children.items():
            if child_name == name:
                target = child
                return target
            else:
                if isinstance(child, Directory):
                    target = child.get_child(name)
                    return target
        return None
    
    def pretty_print(self, indent=0):
        print("  " * indent + str(self))
        for child in self.children.values():
            child.pretty_print(indent=indent + 1)
    
    
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


def main():
    tree = TreeBuilder.build("../test_input.txt")
    tree.pretty_print()


if __name__ == "__main__":
    main()
