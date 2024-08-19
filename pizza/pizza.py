import os
import sys
import csv
from tabulate import tabulate

def start():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
        display_csv(sys.argv[1])

def display_csv(input_file):
    with open(input_file, "r") as csv_data:
        csv_table = csv.DictReader(csv_data, delimiter=",")
        print(tabulate(csv_table, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    start()
