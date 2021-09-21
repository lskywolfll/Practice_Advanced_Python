

def suma(num1: int, num2: int) -> int:
    return num1 + num2

def restar(num1: int, num2: int) -> int:
    return num1 - num2

def dividir(num1: int, num2: int) -> float:
    return num1 / num2

def multiplicar(num1: int, num2: int) -> int:
    return num1 * num2

ENUM = ["suma", "restar", "dividir", "multiplicar"]

def get_input_operation(typ: type, message: str, error: str) -> str:
    while True:
        value = typ(input(message))

        if type(value) == str:
            text: str = value

            print(f"value: {text}")

            if text.isspace():
                raise ValueError("No se pueden contener espacios en blanco.")
            elif text.isdigit():
                raise ValueError("No se aceptan numeros para la operacion.")
            else:
                return text
        else:
            return value

opt = {
    "suma": suma,
    "restar": restar,
    "dividir": dividir,
    "multiplicar": multiplicar
}

def run():
    home = """
    ingresa textualmente una de las siguente operaciones:
    1- suma
    2- restar
    3- dividir
    4- multiplicar

    Escogo
    """
    error_msg_number = "Solo se admiten numeros."
    operation = get_input_operation(str, home, "Lo sentimos necesitas unicamente los valores pre-establecidos en la lista")
    num1 = get_input_operation(int, "Ingresa tu primer numero: ", error_msg_number)
    num2 = get_input_operation(int, "Ingresa tu segundo numero: ", error_msg_number)
    print(f"El resultado de la {operation} es: {opt[operation](num1, num2)}")

if __name__ == "__main__":
    run()
