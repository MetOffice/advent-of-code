import numpy as np

def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()

def id_by_minutes(estimate, buses):
    """ compute the best bus iteratively"""
    best_bus = 0
    best_wait = np.inf
    for i in buses:
        if i.isdigit():
            wait = -estimate % int(i)
            if wait < best_wait:
                best_wait = wait
                best_bus = int(i)
    return best_bus * best_wait

def first_timestamp(buses):
    """
    this can be solved iteratively or using some number theory, noting all the inputs are prime

    taking the example, we are required to solve the following system of equations:
    t = 0 (mod 7)
    t = -1 (mod 13)
    t = -4 (mod 59)
    t = -6 (mod 31)
    t = -7 (mod 19)

    by the chinese remainder theorem, there is a unique solution to the system:

    x = a_1 mod (m_1)
    .
    .
    .
    x = a_n mod (m_n)

    for m_i coprime mod M=m_1 * m_2 * ... * m_n given by x = \sum_{i}^{n} a_i b_i c_i, where  b_i = M/m_i and c_i = b_i^(-1) mod (m_i)
    """

    a=[]
    m=[]
    b=[]
    c=[]

    for i in range(len(buses)):
        if buses[i].isdigit():
            a.append(-i)
            m.append(int(buses[i]))

    M = np.prod(m)
    t = 0
    for j in range(len(a)):
        b.append(int(M/m[j]))
        c.append(pow(b[j], m[j]-2, m[j]))  # only works if m's prime
        t = (t + a[j]*b[j]*c[j]) % M

    return t









def main():
    input = read_input("../input.txt")
    estimate = int(input[0])
    buses = input[1].split(',')
    print(id_by_minutes(estimate, buses))
    print(first_timestamp(buses))

if __name__ == "__main__":
    main()
