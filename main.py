from datetime import datetime
import csv
import random

def main():

    choice = input(f"\n\n[1] Add [2] Read [3] Random [4] Exit\n")

    if choice == "1":
        addEntry()

    elif choice == "2":
        readEntry()
    
    elif choice == "3":
        randomEntry()

    elif choice == "4":
        print(f"exit")


def addEntry():
    month = datetime.today().month
    day = datetime.today().day
    year = datetime.today().year
    
    title = input(f"Title: ")
    season = input(f"Season: ")
    episode = input(f"Episode: ")

    entry = [title,season,episode,month,day,year]
    
    with open("watchlog.csv", "a")  as f:
        f.write(f"{entry}\n")

    readEntry()

def readEntry():
    entries = []
    with open("watchlog.csv", newline='') as f:
        read = csv.reader(f)
        for row in read:    
            entries.append(", ".join(row))
    for entry in entries:
        row = entry.split(",")
        

def randomEntry():
    print(f"Random Entry display here")

main()
