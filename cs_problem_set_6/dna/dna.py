import csv
import sys


def main():

    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    people = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            person = {}
            person["name"] = row[0]
            for i in range(1, len(header)):
                person[header[i]] = int(row[i])
            people.append(person)

    with open(sys.argv[2]) as file:
        sequence = file.read()

    counts = {}
    for i in range(1, len(header)):
        STR = header[i]
        counts[STR] = longest_match(sequence, STR)

    for person in people:
        match = True
        for STR in counts:
            if person[STR] != counts[STR]:
                match = False
                break
        if match:
            print(person["name"])
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subse
