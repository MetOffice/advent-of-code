from typing import Dict, List, Set, Tuple
from common.loaders import load_string


def parse_display_code(display_code: str) -> Tuple[List[Set[str]], List[str]]:
    """

    Parameters
    ----------
    display_code: str

    Returns
    -------
    tuple: (list, list)

    """
    definition_string, four_digits_string = display_code.split("|")

    four_digits = four_digits_string.split()
    definition = [set(string) for string in definition_string.split()]

    return definition, four_digits


def count_unique_segments(four_digits):
    segment_numbers_for_each_digit = {"1": 2, "4": 4, "7": 3, "8": 7}

    unique_digits = [
        digit
        for digit in four_digits
        if len(digit) in segment_numbers_for_each_digit.values()
    ]

    return len(unique_digits)


def main_part_1(display_codes):
    count = 0

    for display_code in display_codes:
        definition, four_digits = parse_display_code(display_code)

        number_of_unique_segments = count_unique_segments(four_digits)

        count += number_of_unique_segments

    return count


def find_a(S7, S1):
    # a = S7 intersection S1
    return find_segment_by_difference(S7, S1)


def find_b(S4, known_letters):
    return find_segment_by_difference(S4, set(known_letters.values()))


def find_c(S1, known_letters):
    return find_segment_by_difference(S1, set(known_letters.values()))


def find_d(intersection_5s, intersection_6s):
    return find_segment_by_difference(intersection_5s, intersection_6s)


def find_e(S8, known_letters):
    return find_segment_by_difference(S8, set(known_letters.values()))


def find_f(intersection_6s, S7, known_letters):
    return find_segment_by_difference(
        (intersection_6s & S7), set(known_letters.values())
    )


def find_g(intersection_5s, known_letters):
    return find_segment_by_difference(intersection_5s, set(known_letters.values()))


def main_part_2(display_codes: List[str]):
    """
      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

    5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg

    """

    total = 0
    for display_code in display_codes:
        definition, four_digits = parse_display_code(display_code)

        # 1 is only definition with 2 elements
        # 7 is only definition with 3 elements
        # 4 is only definition with 4 elements
        # 8 is only definition with 7 elements

        # decoding_definitions = set([char for char in definition])

        S1 = get_one_number(definition, 2)
        S4 = get_one_number(definition, 4)
        S7 = get_one_number(definition, 3)
        S8 = get_one_number(definition, 7)
        S0 = set(["a", "b", "c", "e", "f", "g"])
        S9 = set(["a", "b", "c", "d", "f", "g"])
        S6 = set(["a", "b", "d", "e", "f", "g"])
        S5 = set(["a", "b", "d", "f", "g"])
        S3 = set(["a", "c", "d", "f", "g"])
        S2 = set(["a", "c", "d", "e", "g"])

        # Lists of all digits using 5 or 6 segments (5 segments for 2, 5 and 3;
        # 6 for 0, 6 and 9).
        all_5s = filt_list_by_size(definition, 5)
        all_6s = filt_list_by_size(definition, 6)

        # Common segments for digits using 5 or 6 segments (a, d and g for 5
        # segments; a, b, f, g for 6 segments)
        intersection_5s = get_intersection_of_list(all_5s)
        intersection_6s = get_intersection_of_list(all_6s)

        known_letters = {}
        known_letters["a"] = find_a(S7, S1)
        known_letters["f"] = find_f(intersection_6s, S7, known_letters)
        known_letters["c"] = find_c(S1, known_letters)
        known_letters["d"] = find_d(intersection_5s, intersection_6s)
        known_letters["b"] = find_b(S4, known_letters)
        known_letters["g"] = find_g(intersection_5s, known_letters)
        known_letters["e"] = find_e(S8, known_letters)

        known_nos = {}
        known_nos[1] = S1
        known_nos[4] = S4
        known_nos[7] = S7
        known_nos[8] = S8
        known_nos[0] = remap_to_rand_segment_labels(S0, known_letters)
        known_nos[2] = remap_to_rand_segment_labels(S2, known_letters)
        known_nos[3] = remap_to_rand_segment_labels(S3, known_letters)
        known_nos[5] = remap_to_rand_segment_labels(S5, known_letters)
        known_nos[6] = remap_to_rand_segment_labels(S6, known_letters)
        known_nos[9] = remap_to_rand_segment_labels(S9, known_letters)

        def lookup_digit(digit: Set[str]):
            matches = [
                num for num, ref_digit in known_nos.items() if digit == ref_digit
            ]
            if len(matches) != 1:
                raise ValueError
            return matches[0]

        total += int("".join([str(lookup_digit(set(digit))) for digit in four_digits]))
    return total


def find_segment_by_difference(A, B):
    return (A - B).pop()


def find_segment_by_intersection(A, B):
    return (A & B).pop()


def get_intersection_of_list(list_of_sets: List[Set[str]]):
    set_intersection = list_of_sets[0].copy()
    for next_set in list_of_sets[1:]:
        set_intersection &= next_set
    return set_intersection


def filt_list_by_size(full_list, size):
    return [x for x in full_list if len(x) == size]


def get_one_number(parent_list: List[Set[str]], size):
    sub_list = filt_list_by_size(parent_list, size)
    if len(sub_list) != 1:
        raise ValueError(
            f"Got more than 1 result of size {size} from list :" f" {parent_list}"
        )
    return sub_list[0]


def remap_to_rand_segment_labels(set_of_segments, segment_maps):
    remapped_digit = set()
    for segment in set_of_segments:
        remapped_digit.add(segment_maps[segment])
    return remapped_digit


def print_translated_readouts(readout_rand, known_nos):
    readout = ""
    for digit in readout_rand:
        print(f"got digit as : {digit}")
        readout += which_no(digit, known_nos) + "."
        print(f"Which which_no claims is {which_no(digit, known_nos)}")
    return readout


def which_no(no, all_nos):
    for name, contents in all_nos.items():
        if contents == no:
            return name
    return ""


if __name__ == "__main__":
    display_codes = load_string()

    count = main_part_1(display_codes)

    print(f"Part 1: {count}")

    answer = main_part_2(display_codes)
    print(f"Part 2: {answer}")
