import time

def fibo_gen2(limit: int) -> int:
    a,b = 0, 1
    while a <= limit:
        yield a
        a,b = b, a + b

def fibo_gen(limit: int):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1

            if aux >= limit:
                break
            else:
                yield aux

if __name__ == "__main__":
    limit = 15
    fibonacci = fibo_gen2(limit)
    for element in fibonacci:
        print(element)
        time.sleep(1)