import os
import sys
import csv

def start():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
        cleanse_data(sys.argv[1], sys.argv[2])

def cleanse_data(input_file, output_file):

    with open(input_file, "r") as read_csv_file:
        csv_reader = csv.DictReader(read_csv_file, delimiter=",")

        with open(output_file, "w") as write_csv_file:
            fieldnames = ["first", "last", "house"]
            csv_writer = csv.DictWriter(write_csv_file, fieldnames=fieldnames)

            csv_writer.writeheader()

            for row in csv_reader:
                last, first = row["name"].split(",")
                house = row["house"]

                csv_writer.writerow(
                    {"first": first.strip(), "last": last, "house": house}
                )

if __name__ == "__main__":
    start()
