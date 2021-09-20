

from typing import Generic, TypeVar
def make_repeater_of(n: int) -> str:
    def repeater(string: str) -> str:
        assert type(string) == str, "Solo se aceptan cadenas de caracteres"
        return string * n
    return repeater

def run():
    test = "hola"
    repeat_5 = make_repeater_of(5)
    repeat_3 = make_repeater_of(3)
    print(repeat_5(test))

run()