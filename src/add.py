import datetime
import shutil
import sys

import requests


def try_get_input(day: int):
    with open(".cookie") as f:
        session_cookie = f.read()
    r = requests.get(f"https://adventofcode.com/2023/day/{day}/input",
                     cookies={"session": session_cookie})
    with open(f"advent_of_code_2023/day{day:>02}/input.txt", mode="wb") as f:
        f.write(r.content)


def main():
    try:
        day = sys.argv[1].zfill(2)
    except IndexError:
        date = datetime.date.today()
        if date <= datetime.date(2023, 12, 25):
            day = str(date.day).zfill(2)
        else:
            print("You need to say what day to add")
    print("Creating new day")
    print("Did you remember to change branch?")
    print(shutil.copytree("./advent_of_code_2023/_template/", f"./advent_of_code_2023/day{day}/"))
    try_get_input(day=int(day))


if __name__ == '__main__':
    main()
