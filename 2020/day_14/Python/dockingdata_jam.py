from loaders import load_string
import numpy as np

class Dock:
    """
    Reads commands in the list and keeps the memory and mask values
    """
    def __init__(self):
        self.mask = ""
        # avoid allocating missing addresses
        self.memory = dict()

    def execute_commands_v1(self, commands):
        """
        Reads and executes all commands in the supplied list according to v1 spec.
        """
        for command in commands:
            # interpret string
            mask, address, argument = self.read_command(command)
            if mask:
                # update mask
                self.mask = argument
            else:
                # mask value
                masked = self.mask_value(argument, "X")
                # string to int
                value = int(masked, base=2)
                # store value
                self.memory[address] = value

    def execute_commands_v2(self, commands):
        """
        Reads and executes all commands in the supplied list according to v2 spec.
        """
        for command in commands:
            # interpret string
            mask, address, argument = self.read_command(command)
            if mask:
                # update mask
                self.mask = argument
            else:
                # mask value
                masked = self.mask_value(address, "0")
                # fill with all possible combinations
                masked_addresses = self.multi_fill(masked)
                # write value to all computed addresses
                for masked_address in masked_addresses:
                    self.memory[int(masked_address, base=2)] = int(argument)

    def read_command(self, command):
        """
        Reads a command string and returns a mem or mask bit plus arguments
        """
        # remove spaces
        command = command.replace(" ", "")
        # get left and right of equals sign
        action, argument = command.split("=")
        
        if action == "mask": # mask command
            # address isn't used in this case but we need consistent return
            mask = True
            address = None
        else: # mem command
            mask = False
            # ignore first 4 and last 1 character 
            address = action[4:-1]
        
        return mask, address, argument
        
    def mask_value(self, value:str, maskchar):
        """
        maskchar in the mask are replaced with the value in the same position in the value.
        For v1, maskchar is X, for v2 maskchar is 0.
        Returns a string.
        """
        # convert to binary string
        binary = f"{int(value):b}"
        # pad the string to be 36 characters
        padded = binary.zfill(36)
        # keep padded values if position is X in the mask, else take mask values
        masked = [padded[i] if self.mask[i] == maskchar else self.mask[i] for i in range(len(padded))]
        # join list into string
        return "".join(masked)

    def multi_fill(self, fillee):
        """
        Fill all X places with each combination of 0 and 1, returning list of resulting ints.
        Use for v2.
        """
        # For recursion we need a single element list
        if type(fillee) == str:
            fillee = [fillee]
        # if any x in any string in list
        if any(["X" in s for s in fillee]):
            # return a double copy where first X is replaced with 0 and then 1
            fillee = [s.replace("X", "0", 1) for s in fillee] + [s.replace("X", "1", 1) for s in fillee]
            # recursively fill all X occurences
            fillee = self.multi_fill(fillee)
        # Return recursive result or identity if no X occurences
        return fillee

        
    def memory_sum(self):
        """
        Return the sum of all values in memory
        """
        return sum(self.memory.values())

def dockingdata(commands):
    """
    Create a Dock and execute command list, returning the sum of all values in memory.
    Follows version 1.
    """
    dock = Dock()
    dock.execute_commands_v1(commands)
    return dock.memory_sum()

def dockingdata2(commands):
    """
    Create a Dock and execute command list, returning the sum of all values in memory.
    Follows version 2.
    """
    dock = Dock()
    dock.execute_commands_v2(commands)
    return dock.memory_sum()


if __name__ == "__main__":
    commands = load_string()
    sum = dockingdata2(commands)
    print(sum)