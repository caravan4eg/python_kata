import sys


def main():
    print("Привет, " + sys.argv[1] + "!")
    print("Количество аргументов: ", len(sys.argv))


if __name__ == "__main__":
    main()
