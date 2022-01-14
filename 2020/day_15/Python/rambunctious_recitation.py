import numpy as np




def reciter(input, upto):
    """ function to perform and store recitation

        dictionary data:
            keys: spoken numbers
            values: index of when number last spoke

        list sequence: the full sequence, though we don't actually need to store the whole thing
        int next: the next integer to be inserted into the sequence - we calculate the one following this first before doing so
        int next_next: the integer following next in the sequence

        use 1-indexing throughout to match problem
    """

    data=dict()
    sequence = input[:-1]
    #initialise dict with input data, omitting the last entry

    for i in range(len(input)-1):
        data[input[i]]=i+1

    next = input[-1]
    for i in range(len(input)-1, upto):

        if next in data:
            next_next = i + 1 - data[next] #since next will be inserted into the sequence at position i+1
        else:
            next_next = 0

        sequence.append(next)

        data[next] = i+1 #next inserted at i+1
        next = next_next #next iterated

    return sequence[-1]



def main():
    input = [14,3,1,0,9,5]

    result = reciter(input,2020)
    result2 = reciter(input,30000000)
    print(result)
    print(result2)

if __name__ == "__main__":
    main()
