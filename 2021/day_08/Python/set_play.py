from random import shuffle

def crappy_debug_print(location, digits, cmp_val):
    print("================================")
    print(location)
    print(f"digit_0 is : {digits[0]}")
    print(f"digit_1 is : {digits[1]}")
    print(f"digit_2 is : {digits[2]}")
    print(f"digit_3 is : {digits[3]}")
    print(f"digit_4 is : {digits[4]}")
    print(f"digit_5 is : {digits[5]}")
    print(f"digit_6 is : {digits[6]}")
    print(f"digit_7 is : {digits[7]}")
    print(f"digit_8 is : {digits[8]}")
    print(f"digit_9 is : {digits[9]}")
    if cmp_val == digits[0]:
        print("** WTF it's become the checked value ***")
    
# The 'seven' segment labels by original diagram.
segment_names = ["a","b","c","d","e","f","g"]
print(f"List of segment names (in original order )                       :"
      f" {segment_names}")

# The randomizer....
shuffle(segment_names)
print(f"List of segment names (in original order but with random labels) :"
      f" {segment_names}")

a = segment_names[0]
b = segment_names[1]
c = segment_names[2]
d = segment_names[3]
e = segment_names[4]
f = segment_names[5]
g = segment_names[6]

# For convenience : Sets of the 10 'digits' by size using the
# original/correct labelling
digit_8 = set([a,b,c,d,e,f,g])
digit_0 = set([a,b,c,e,f,g])
digit_9 = set([a,b,c,d,f,g])
digit_6 = set([a,b,d,e,f,g])
digit_5 = set([a,b,d,f,g])
digit_3 = set([a,c,d,f,g])
digit_2 = set([a,c,d,e,g])
digit_4 = set([b,c,d,f])
digit_7 = set([a,c,f])
digit_1 = set([c,f])

print(f"digit_0 is : {digit_0}")
print(f"digit_1 is : {digit_1}")
print(f"digit_2 is : {digit_2}")
print(f"digit_3 is : {digit_3}")
print(f"digit_4 is : {digit_4}")
print(f"digit_5 is : {digit_5}")
print(f"digit_6 is : {digit_6}")
print(f"digit_7 is : {digit_7}")
print(f"digit_8 is : {digit_8}")
print(f"digit_9 is : {digit_9}")

# Note - this could be a 'random' list of all the numbers.
full_list = [digit_0, digit_1, digit_2, digit_3, digit_4,
             digit_5, digit_6, digit_7, digit_8, digit_9]
# e.g.
shuffle(full_list)

crappy_debug_print("==== pre defs ====",
                   [digit_0, digit_1, digit_2, digit_3, digit_4,
                    digit_5, digit_6, digit_7, digit_8, digit_9],
                    digit_6 & digit_9 & digit_0 )

def find_segment_by_difference(A, B):
    return (A - B).pop()

def find_segment_by_intersection(A, B):
    return (A & B).pop()

def get_intersection_of_list(list_of_sets):
    set_intersection = list_of_sets[0].copy()
    for next_set in list_of_sets[1:]:
        set_intersection &= next_set
    return set_intersection

def filt_list_by_size(full_list, size):
    return [x for x in full_list if len(x) == size]

def get_one_number(parent_list, size):
    sub_list = filt_list_by_size(parent_list, size)
    if len(sub_list) != 1:
        raise ValueError(f"Got more than 1 result of size {size} from list :"
                         f" {parent_list}")
    return sub_list[0]

def remap_to_rand_segment_labels(set_of_segments, segment_maps):
    remapped_digit = set()
    for segment in set_of_segments:
        remapped_digit.add(segment_maps[segment])
    return remapped_digit

def print_translated_readouts(readout_rand, known_nos):
    readout=""
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

print("================================")
crappy_debug_print("==== post defs ====",
                   [digit_0, digit_1, digit_2, digit_3, digit_4,
                    digit_5, digit_6, digit_7, digit_8, digit_9],
                    digit_6 & digit_9 & digit_0 )

print("================================")

known_nos = {}
known_letters = {}

S1 = get_one_number(full_list, 2)
S4 = get_one_number(full_list, 4)
S7 = get_one_number(full_list, 3)
S8 = get_one_number(full_list, 7)

known_nos["1"] = S1
known_nos["4"] = S4
known_nos["7"] = S7
known_nos["8"] = S8

print("================================")
crappy_debug_print("==== pre intersections ====",
                   [digit_0, digit_1, digit_2, digit_3, digit_4,
                    digit_5, digit_6, digit_7, digit_8, digit_9],
                    digit_6 & digit_9 & digit_0 )

all_5s = filt_list_by_size(full_list, 5)
all_6s = filt_list_by_size(full_list, 6)

print("================================")
crappy_debug_print("==== mid intersections ====",
                   [digit_0, digit_1, digit_2, digit_3, digit_4,
                    digit_5, digit_6, digit_7, digit_8, digit_9],
                    digit_6 & digit_9 & digit_0 )

intersection_5s = get_intersection_of_list(all_5s)
# {a, d, g}
print("================================")
crappy_debug_print("==== Mid II intersections ====",
                   [digit_0, digit_1, digit_2, digit_3, digit_4,
                    digit_5, digit_6, digit_7, digit_8, digit_9],
                    digit_6 & digit_9 & digit_0 )

print(f"All_6s is : {all_6s}")
intersection_6s = get_intersection_of_list(all_6s)
print(f"Intersection_6s is : {intersection_6s}")
#intersection_6s = set([a, b, g, f])
#print(f"Intersection_6s is : {intersection_6s}")
# {a, b, g, f}

print("================================")
crappy_debug_print("==== post intersections ====",
                   [digit_0, digit_1, digit_2, digit_3, digit_4,
                    digit_5, digit_6, digit_7, digit_8, digit_9],
                    digit_6 & digit_9 & digit_0 )

print("================================")

# a = S7 intersection S1
known_letters['a'] = find_segment_by_difference(S7, S1)
# print(f"'a' maps onto {known_letters['a']}")

# f = (S(intersection_6s) intersection S7) difference S('a')
known_letters['f'] = find_segment_by_difference((intersection_6s & S7),
                                             set(known_letters.values()))
# print(f"'f' maps onto {known_letters['f']}")

print("================================")
crappy_debug_print("==== post a & f ====",
                   [digit_0, digit_1, digit_2, digit_3, digit_4,
                    digit_5, digit_6, digit_7, digit_8, digit_9],
                    digit_6 & digit_9 & digit_0 )

# c = S1 difference S(known_letters)
known_letters['c'] = find_segment_by_difference(S1, set(known_letters.values()))
# print(f"'c' maps onto {known_letters['c']}")

# d = intersection_5s difference intersection_6s
# print(f"Intersaection 5s = {intersection_5s}")
# print(f"Intersaection 6s = {intersection_6s}")
known_letters['d'] = find_segment_by_difference(intersection_5s, intersection_6s)
# print(f"'d' maps onto {known_letters['d']}")

# b = S4 difference S(known_letters)
known_letters['b'] = find_segment_by_difference(S4, set(known_letters.values()))
# print(f"'b' maps onto {known_letters['b']}")

# g = intersection_5s difference S(known_letters)
known_letters['g'] = find_segment_by_difference(intersection_5s,
                                             set(known_letters.values()))
# print(f"'g' maps onto {known_letters['g']}")

# e = S8 difference S(known_letters)
known_letters['e'] = find_segment_by_difference(S8, set(known_letters.values()))
# print(f"'e' maps onto {known_letters['e']}")

print("================================")
# Print out what we think we know...
print(f"'a' maps onto {known_letters['a']}")
print(f"'b' maps onto {known_letters['b']}")
print(f"'c' maps onto {known_letters['c']}")
print(f"'d' maps onto {known_letters['d']}")
print(f"'e' maps onto {known_letters['e']}")
print(f"'f' maps onto {known_letters['f']}")
print(f"'g' maps onto {known_letters['g']}")

print("================================")

print(f"digit_0 is : {digit_0}")
print(f"digit_1 is : {digit_1}")
print(f"digit_2 is : {digit_2}")
print(f"digit_3 is : {digit_3}")
print(f"digit_4 is : {digit_4}")
print(f"digit_5 is : {digit_5}")
print(f"digit_6 is : {digit_6}")
print(f"digit_7 is : {digit_7}")
print(f"digit_8 is : {digit_8}")
print(f"digit_9 is : {digit_9}")

print("================================")

S0 = set(["a","b","c","e","f","g"])
S9 = set(["a","b","c","d","f","g"])
S6 = set(["a","b","d","e","f","g"])
S5 = set(["a","b","d","f","g"])
S3 = set(["a","c","d","f","g"])
S2 = set(["a","c","d","e","g"])

known_nos["0"] = remap_to_rand_segment_labels(S0, known_letters)
known_nos["2"] = remap_to_rand_segment_labels(S2, known_letters)
known_nos["3"] = remap_to_rand_segment_labels(S3, known_letters)
known_nos["5"] = remap_to_rand_segment_labels(S5, known_letters)
known_nos["6"] = remap_to_rand_segment_labels(S6, known_letters)
known_nos["9"] = remap_to_rand_segment_labels(S9, known_letters)

for digit in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    print(f"The digit {digit} is made of segments {known_nos[digit]}")

print("================================")

print(f"digit_0 is : {digit_0}")
print(f"digit_1 is : {digit_1}")
print(f"digit_2 is : {digit_2}")
print(f"digit_3 is : {digit_3}")
print(f"digit_4 is : {digit_4}")
print(f"digit_5 is : {digit_5}")
print(f"digit_6 is : {digit_6}")
print(f"digit_7 is : {digit_7}")
print(f"digit_8 is : {digit_8}")
print(f"digit_9 is : {digit_9}")

print("================================")

# Make up some numbers using the randomised segements....

readout_1803 = [known_nos["1"], known_nos["8"], known_nos["0"], known_nos["3"]]
print(f"{readout_1803} translates to ")
print(f"     {print_translated_readouts(readout_1803, known_nos)} ")

print(f"digit_0 is : {digit_0}")
print(f"digit_1 is : {digit_1}")
print(f"digit_2 is : {digit_2}")
print(f"digit_3 is : {digit_3}")
print(f"digit_4 is : {digit_4}")
print(f"digit_5 is : {digit_5}")
print(f"digit_6 is : {digit_6}")
print(f"digit_7 is : {digit_7}")
print(f"digit_8 is : {digit_8}")
print(f"digit_9 is : {digit_9}")

print("================================")

readout_1803 = [digit_1, digit_8, digit_0, digit_3]
print(f"{readout_1803} translates to ")
print(f"     {print_translated_readouts(readout_1803, known_nos)} ")
