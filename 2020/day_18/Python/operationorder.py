
def load_string():
    with open("./2020/day_18/input.txt", "r") as file:
        out = file.readlines()
    return out

def answer_sum(part2=False):
    """
    Evaluates all statements first within brackets then left to right. Outputs sum of all answers.
    May choose rules for part 2 instead.
    """
    # Load all problems, one per line
    problems = load_string()
    # evaluate all problems
    answers = [evaluate_string(problem, part2) for problem in problems]
    # return sum
    return sum(answers)

def evaluate_string(problem, part2=False):
    """
    Read a string problem and return its result.
    May choose rules for part 2 instead.
    """
    # Remove spaces and newlines
    problem = problem.replace(" ", "").strip()
    # Create iterator for sequential read between loops and calls
    problem_iter = iter(problem)
    # Translate string to statement
    statement = interpret(problem_iter)
    # In part 2 all addtion is placed in brackets
    if part2:
        statement = bracket_adds(statement)
    # Evaluate statement
    return evaluate(statement)

def interpret(problem_iter):
    """
    Reads a problem string iterator and stores it in the statement list. Symbols are unchanged except for brackets, whose contents become sublists.
    All numbers are assumed to be single digit.
    """
    statement=[]
    # Continue iteration. Not a value type so position is consistent between calls and loops.
    for char in problem_iter:
        # When bracket opens, interpret as sublist until inner function ends at a close bracket
        if char == "(":
            statement.append(interpret(problem_iter))
        # When bracket closes break loop and return
        elif char == ")":
            break
        # Numbers are stored as integers
        elif char in "0123456789":
            statement.append(int(char))
        # All other characters are stored as is
        else:
            statement.append(char)
    return statement

def evaluate(statement):
    """
    Reads a statement list and evaluates it left to right. Sublists are evaluated recursively.
    """
    # Begin by adding first value to 0
    value = 0
    # Adding is true, multiplying is false
    adding = True

    for element in statement:
        # Operators are the only strings in the statement
        if type(element) == str:
            # + is True, * is False
            adding = element == "+"
        else:
            # subevaluate lists
            if type(element) == list:
                element = evaluate(element)
            # add or multiply onto value
            if adding:
                value += element
            else:
                value *= element
    return value

def bracket_adds(statement):
    """
    Forces addition to evaluate first by putting them in sublists
    """
    # this preferentially adds 
    new_statement = []
    substatement = []
    for element in statement:
        # any mulitplication ends a substatement
        if element == "*":
            new_statement = append_substatement(new_statement, substatement)
            # add multiplication
            new_statement.append(element)
            # clear substatement
            substatement = []
        # other elements add to substatement
        else:
            # recursively bracket sublists
            if type(element) == list:
                element = bracket_adds(element)
            substatement.append(element)
    # add remaining substatement
    return append_substatement(new_statement, substatement)

def append_substatement(statement, substatement):
    """
    Appends substatement to statement, or the content of substatement if it is a single element.
    Avoids unnecessary extra brackets when adding auto brackets.
    """
    if len(substatement) < 2:
        statement += substatement
    else:
        statement.append(substatement)
    return statement

if __name__ == "__main__":
    print(answer_sum(part2=True))