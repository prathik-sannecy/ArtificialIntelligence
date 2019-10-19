from Optomize import *
from Person import *

def Parse(input_file):
    """Parse the file, returns back all the people at the table

    inputs:
        (string) file name in given format
    returns:
        (list of People) all the people in the dinner table initialized
    """
    people = []
    with open(input_file) as file:
        num_people = file.readline()
        for i in range(0, num_people):
            person = Person()
        people.append()