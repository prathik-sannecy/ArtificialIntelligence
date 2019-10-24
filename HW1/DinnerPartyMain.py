from ParseInputFile import *
from Optimize import *
import sys


def Main(input_file):
    """Finds the optimized seating arrangement for the dinner table for the highest possible score

    The "score" of a table is determined by the following criteria:

    1 point for every adjacent pair (seated next to each other) of people with one a host and the other a guest. 2
    points for every opposite pair (seated across from each other) of people with one a host and the other a guest.
    h(p1, p2) + h(p2, p1) points for every adjacent or opposite pair of people p1, p2 where h(p1,2) is the preference
        function between two people

    inputs:
        File name for initializing the dinner table
    returns:
        None

    """
    # Increase the recursion limit max (used for the optomization function)
    sys.setrecursionlimit(100000)
    # Get all the people at the dinner table
    persons = Parse(input_file)
    # Optimize the seating arrangements for the highest score
    score, people = Optimize(persons, 0, 1, float("-inf"))
    # Print the result in the desired format
    print(score)
    people.sort(key=lambda x: x.GetNumber())
    for person in people:
        print(str(person.GetNumber()) + " " + str(person.GetPosition()))


if __name__ == '__main__':
    print("Enter Path to file")
    # Get the input file (to initialize dinner table)
    file_path = input()
    Main(file_path)
