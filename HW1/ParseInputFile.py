from Person import *

def Parse(input_file):
    """Parse the file, returns back all the people at the table

    inputs:
        (string) file name in given format
    returns:
        (list of People) all the people in the dinner table initialized
    """
    people = []
    try:
        with open(input_file) as file:
            num_people = int(file.readline())
            # First half of people are hosts
            for i in range(1, int(num_people / 2) + 1):
                person = Person(i, "H")
                person.SetPosition(i)
                people.append(person)
            # Second half of people are guests
            for i in range(int(num_people / 2) + 1, num_people + 1):
                person = Person(i, "G")
                person.SetPosition(i)
                people.append(person)

            # Set the first half of the people on the top row (looking top-down)
            for i in range(0, int(num_people / 2) - 1):
                people[i].SetAdjRight(people[i + 1])
            for i in range(1, int(num_people / 2)):
                people[i].SetAdjLeft(people[i - 1])
            for i in range(0, int(num_people / 2)):
                people[i].SetDown(people[i + int(num_people / 2)])

            # Set the second half of the people on the bottom row (looking top-down)
            for i in range(int(num_people / 2), num_people - 1):
                people[i].SetAdjRight(people[i + 1])
            for i in range(1 + int(num_people / 2), num_people):
                people[i].SetAdjLeft(people[i - 1])
            for i in range(int(num_people / 2), num_people):
                people[i].SetUp(people[i - int(num_people / 2)])

            # Set the relation between each person
            person_num = 0
            for line in file:
                relations = line.strip("\n").split()
                relationship_num = 0
                for relation in relations:
                    if person_num != relationship_num:
                        people[person_num].SetRelationTo(people[relationship_num], int(relation))
                    relationship_num += 1
                person_num += 1

        return people
    except:
        print(input_file + " not found")
        exit()

