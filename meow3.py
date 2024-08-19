import argparse 

parser = argparse.ArgumentParser(description="cat say meow")
parser.add_argument("-n", default=1, help="this is meow")
args = parser.parse_args()

for _ in range(int(int(args.n))):
    print("meow")