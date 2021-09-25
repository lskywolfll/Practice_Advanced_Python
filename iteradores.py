
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# print(next(my_iter))

# iterator propio para usar con un iterable reference line 3 my_iter o bien mas abajo line 28
class EvenNumbers:

    def __init__(self, max=int):
        self.max = max
    
    def __iter__(self):
        self.num = 2
        return self
    
    def __next__(self) -> int:
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration

# Ventajas
# Un iterador ahorra recursos en memoria y incluso la capacidad de guardar todos los numeros pares, por que ahorran mucha memoria en la computadora

my_evenNumber15 = EvenNumbers(16)
for number in my_evenNumber15:
    print(f"iterator: {number}")