import sys
import multiprocessing as mp
import concurrent.futures as cf


def main(delta):
    pass


if __name__ == '__main__':
    mp.freeze_support()
    delta = 2
    if len(sys.argv) > 1:
        print(sys.argv)
        try:
            delta = int(sys.argv[1])
            print(f"delta = {delta}")
        except ValueError:
            print("Неверный аргумент! Используется значение по умолчанию: 2.")
    main(delta)
