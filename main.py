from datetime import datetime
import csv
import random

def main():
    choice = input(f"\n\n[1] Add [2] Read [3] Random [4] Remove\n")
    if choice == "1":
        addEntry()
    elif choice == "2":
        readEntry()
    elif choice == "3":
        randomEntry()
    elif choice == "4":
        removeEntry()

# adds entry to the csv file
def addEntry():
    month = datetime.today().month
    day = datetime.today().day
    year = datetime.today().year
    title = input(f"Title: ")
    season = input(f"Season: ")
    episode = input(f"Episode: ")
    entry = (f"{title},{season},{episode},{month},{day},{year}")
    with open("watchlog.csv", "a")  as f:
        f.write(f"{entry.replace("'","")}\n")
    readEntry()

# access the csv and display each entry per row
def readEntry():
    with open("watchlog.csv", newline='') as f:
        read = csv.reader(f)
        for item in read:
            print(f"════════════════════════════════════════════════════════════════")
            print(f"  {item[0].ljust(45)}   Se{item[1]}   Ep{item[2]}")
            print(f"════════════════════════════════════════════════════════════════")


def removeEntry():
    print(f"Remove entry function here")

def randomEntry():
    print(f"Random Entry display here")

main()
