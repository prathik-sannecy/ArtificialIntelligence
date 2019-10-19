from src.ParseInputFile import *
from src.Optomize import *
import sys


def Main(input_file) :
    sys.setrecursionlimit(10000)
    persons = Parse(input_file)
    score, people = Optomize(persons, 0, 1)
    print(score)
    people.sort(key=lambda x: x.GetNumber())
    for person in people:
        print(str(person.GetNumber()) + " " + str(person.GetPosition()))


if __name__ == '__main__':
    print("Enter Path to file")
    file_path = input()
    Main(file_path)
