from tqdm import trange

def load_data(file_path: str) -> list:
    with open(file_path, 'r') as file:
        data = file.readlines()

    springs = []
    instructions = []
    for dat in data:
        dat = dat.strip()
        spring, instr = dat.split(" ")
        springs.append(spring)
        instructions.append(instr)

    return springs, instructions

def calculate_arrangements(string: str, arrangement_idx: int, N_quest: int) -> str:
    
    arrangement_idx = bin(arrangement_idx)[2:].zfill(N_quest)
    qidx = 0
    result = ""
    for char in string:
        if char == "?":
            if arrangement_idx[qidx] == "1":
                result += "#"
            else:
                result += "."
            qidx += 1
        else:
            result += char

    return result

if __name__ == "__main__":
    springs, instructions = load_data("input.txt")

    spring = springs[0]
    instr = instructions[0]

    count_q = spring.count("?")
    results = []
    for arr_idx in trange(0, 2**instr.count("?")):
        results.append(calculate_arrangements(spring, arr_idx, count_q))
    print(len(results))

# Note for next time: Sorry
# We have a function to replace ? with stuff
# This slow method gives us every possible case
# Filter by obeying instructions
# Get money