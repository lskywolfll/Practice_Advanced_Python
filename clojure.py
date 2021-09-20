
def main():
    a = 5
    def nested():
        print(a)
    
    return nested

my_func = main()

del main

my_func()