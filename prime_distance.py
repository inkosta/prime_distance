import sys, time
import multiprocessing as mp
import concurrent.futures as cf


NUMBER_OF_PROCESSES = mp.cpu_count()


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def func(num: int, dividers: list[int]) -> bool:
    for div in dividers:
        if num % div == 0:
            return True
    return False


def main(delta):
    primes = [3, 5, 7]
    d = 2
    n = 7

    with cf.ProcessPoolExecutor(max_workers=NUMBER_OF_PROCESSES) as executor:
        while n < 1000:
            # while d < delta:
            n += 2
            print(f"processed: {n}, ", end='')

            futures = []
            sr = int(n**0.5)
            limit = 0
            while limit < len(primes) and (primes[limit] < sr):
                limit += 1
            for chunk in chunks(primes[:limit], NUMBER_OF_PROCESSES):
                w = executor.submit(func, n, chunk)
                futures.append(w)
            for future in cf.as_completed(futures):
                if future.result():
                    # n is not prime
                    print("is not prime")
                    break
            else:
                # n is prime
                primes.append(n)
                print("is prime")


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
    start = time.process_time_ns()
    main(delta)
    elapsed = (time.process_time_ns() - start) / 1_000_000_000
    print(f"elapsed: {elapsed}")
