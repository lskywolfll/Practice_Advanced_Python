
def is_par(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False

def run():
    num = int(input("Ingresa un numero: "))
    print(is_par(num))

if __name__ == "__main__":
    run()