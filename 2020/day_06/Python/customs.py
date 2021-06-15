from common.loaders import load_string


def count_unique_group_answers(answers):
    """
    Return a count of unique answers within a group.

    Parameters
    ----------
    answers : list[str]
        A list of strings containing the answers from a group.

    Returns
    -------
    int
        The number of unique questions answered with a "yes".

    """
    unique_answers = set()
    for answer in answers:
        for char in answer:
            unique_answers.add(char)

    return len(unique_answers)

def count_common_group_answers(answers):
    """
    Return a count of common answers within a group.

    Parameters
    ----------
    answers : list[str]
        A list of strings containing the answers from a group.

    Returns
    -------
    int
        The number of unique questions answered by everyone
        with a "yes".

    """
    common_answers = set(answers[0])
    for answer in answers:
        common_answers = common_answers & set(answer)
    return len(common_answers)

def get_group_answers(file_contents):
    """
    Return a list of answers from each group member.

    Parameters
    ----------
    file_contents : list[str]
        The raw lines from input.txt.

    Yields
    -------
    list[str]
        List of answers from each group.
    """
    group = []
    for line in file_contents:
        if line == "":
            yield group
            group = []
        else:
            group.append(line)
    
    if group:
        # if file contents don't end in a newline, then yield the final
        # group
        print("nooo :(")
        yield group

def part1(file_contents):
    sum_of_unique_answers = 0
    for answers in get_group_answers(file_contents):
        sum_of_unique_answers += count_unique_group_answers(answers)
    print(f"Solution to part 1: {sum_of_unique_answers}")

def part2(file_contents):
    sum_of_common_answers = 0
    for answers in get_group_answers(file_contents):
        sum_of_common_answers += count_common_group_answers(answers)
    print(f"Solution to part 2: {sum_of_common_answers}")

if __name__ == "__main__":
    file_contents = load_string()
    part1(file_contents)
    part2(file_contents)
