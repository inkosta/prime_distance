import sys, time
from sys import stdout as so
import multiprocessing as mp
from threading import BrokenBarrierError
from typing import Any

NUMBER_OF_PROCESSES = mp.cpu_count()


def split_on_chunks(lst: list[Any], chunks_cnt: int) -> list[list[Any]]:
    """Splits lst into n successive chunks."""
    div, mod = divmod(len(lst),  chunks_cnt)
    step = div + int(bool(mod))
    return [lst[i:i + step] for i in range(0, len(lst), step)]


# проверяет, является какое-нибудь число из списка dividers делителем num
def worker(num: int, dividers: list[int], barrier: mp.Barrier) -> bool:
    # print(f"n: {num}, dividers: {dividers}")
    for div in dividers:
        if num % div == 0:
            # print(f"\t{div} is divider of {num}")
            barrier.abort()
            return True
    # print(f"{dividers} are not dividers of {num}")
    try:
        barrier.wait()
    except BrokenBarrierError:
        # print("process aborted")
        pass

    return False


def main(delta):
    primes = [3, 5, 7]
    d = 2
    n = 7
    limit = 0
    while primes[limit] ** 2 <= n:
        limit += 1
    while n < 500:
        # while d < delta:
        n += 2
        # print(f"processed: {n}, ")
        # so.flush()
        while (limit < len(primes)) and (primes[limit]**2 < n):
            limit += 1
        chunks = split_on_chunks(primes[:limit + 1], NUMBER_OF_PROCESSES)
        barrier = mp.Barrier(len(chunks) + 1)
        workers = []
        for chunk in chunks:
            # print(f"worker({n}, {chunk}, barrier) ", end='...')
            # so.flush()
            w = mp.Process(target=worker, args=(n, chunk, barrier))
            # print("created", end='...')
            # so.flush()
            w.start()
            # print("started", end='...')
            # so.flush()
            workers.append(w)
            # print("append to workers")
            # so.flush()

        try:
            barrier.wait()
        except BrokenBarrierError:
            # print(f"number {n} is not prime")
            [w.terminate() for w in workers]
        else:
            # print(f"number {n} is prime")
            primes.append(n)
            [w.join() for w in workers]


if __name__ == '__main__':
    # p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
    # print(split_on_chunks(p, 3))
    # exit(0)
    delta = 2
    if len(sys.argv) > 1:
        print(sys.argv)
        try:
            delta = int(sys.argv[1])
            print(f"delta = {delta}")
        except ValueError:
            print("Неверный аргумент! Используется значение по умолчанию: 2.")
    start = time.time_ns()
    print(f"start time: {start}")
    main(delta)
    elapsed = (time.time_ns() - start) / 1_000_000_000
    print(f"elapsed: {elapsed}")
