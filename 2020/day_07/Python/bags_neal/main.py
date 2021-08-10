import read_input
import build_matrix
import solve
import sys

def main():
    # read from the puzzle input
    filename = sys.argv[1]
    file_contents = read_input.read_input(filename)
    # build the matrix for the graph
    bag_matrix = build_matrix.build_matrix(file_contents, "shiny gold")

    # use the giant matrix to solve for parts 1 and 2
    part1_sol, part2_sol = solve.solve_parts1_and_2(bag_matrix)

    print(f"Part 1 solution: {part1_sol}")
    print(f"Part 2 solution: {part2_sol}")

if __name__ == "__main__":
    main()