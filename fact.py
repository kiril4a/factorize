def factorize_sync(*numbers):
    factors_list = []
    for num in numbers:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        factors_list.append(factors)
    return factors_list

import multiprocessing

def factorize_single(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(*numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        factors_list = pool.map(factorize_single, numbers)
    
    return factors_list

if __name__ == "__main__":
    import time
    start_time = time.time()

    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
    end_time = time.time()

    print("Synchronous execution time:", end_time - start_time, "seconds")
    start_time = time.time()
    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
    end_time = time.time()

    print("Parallel execution time:", end_time - start_time, "seconds")
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
