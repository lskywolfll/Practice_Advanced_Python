
def is_palindromo(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]

def run():
    testing_string = "ana"
    print(is_palindromo(testing_string))

if __name__ == "__main__":
    run()