from ParseInputFile import *
from Optomize import *

def Main(input_file):
    persons = Parse(input_file)
    Optomize(persons, 0, 1)


if __name__ == '__main__':
    Main()