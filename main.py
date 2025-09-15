import csv
import random

def main():
    choice = input(f"\n\n[1] Add [2] Remove [3] Display [4] Random\n")
    if choice == "1":
        addEntry()
    elif choice == "2":
        removeEntry()
    elif choice == "3":
        displayEntry()
    elif choice == "4":
        randomEntry()


def addEntry():
    title = input(f"Title: ")
    season = input(f"Season: ")
    episode = input(f"Episode: ")
    entry = [title,season,episode3]
    with open("watchlog.csv", "a", newline='')  as f:
        f.write(f"{entry}\n")
    displayEntry()


def removeEntry():
    displayEntry()
    fullList = csvToMemory()
    entryNum = input(f"Which entry should be removed? [1-{len(fullList)}] [0] Cancel\n")
    if entryNum == '0':
        print(f"No entry deleted.")
    else:
        n = 0
        while n < len(fullList):
            if n != (entryNum-1):
                with open("watchlog.csv", "a",newline='') as f:
                    f.write(f"{fullList[n]}")
                    n =+ 1
                    continue
            else:
                n =+ 1
                continue


def displayEntry():
    with open("watchlog.csv", newline='') as f:
        read = csv.reader(f)
        for item in read:
            print(f"════════════════════════════════════════════════════════════════")
            print(f"  {item[0].ljust(45).replace("[", "").replace("'", "")}", end="")
            print(f"   Se {item[1].replace("'", "")}", end="")
            print(f"  Ep {item[2].replace("]", "").replace("'", "")}")
            print(f"════════════════════════════════════════════════════════════════")


def csvToMemory():
    fullList = []
    with open("watchlog.csv", newline='') as f:
        read = csv.reader(f)
        for item in read:
            fullList.append(item)
    return fullList


def randomEntry():
    fullList = csvToMemory()

    pick = random.randint(0,(len(fullList))-1)
    print(f"════════════════════════════════════════════════════════════════")
    print(f"  {fullList[pick][0].ljust(45)}   Se {fullList[pick][1]}   Ep {fullList[pick][2]}")
    print(f"════════════════════════════════════════════════════════════════")


main()
