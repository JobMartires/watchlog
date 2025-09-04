from datetime import datetime
import random

def main():
    choice = input(f"[1] Add [2] Read [3] Random [4] Exit")

    if choice == "1":
        list = addEntry()

    elif choice == "2":
        #display watchlog here
    
    elif choice == "3":
        #random here

    elif choice == "4":
        #exit here

def addEntry():
    month = datetime.today().month
    day = datetime.today().day
    year = datetime.today().year
    
    title = input(f"Title: ")
    season = input(f"Season: ")
    episode = input(f"Episode: ")

    entry = [title,season,episode,month,day,year]
    
    with open("watchlog.csv", "w")  as f:
        f.write(f"{entry}\n")


main()
