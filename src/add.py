import shutil
import sys


def main():
    day = sys.argv[1].zfill(2)
    print("Creating new day")
    print("Did you remember to change branch?")
    print(shutil.copytree("./advent_of_code_2023/_template/", f"./advent_of_code_2023/day{day}/"))


if __name__ == '__main__':
    main()
