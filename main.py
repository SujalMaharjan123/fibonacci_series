import fibonacci

def main():
    number=input("Enter the number:")
    if not number.isdigit():
        print("Invalid input!!")
        return None
        exit()
    result=fibonacci.fibo(int(number))
    if result is None:
        print("Invalid input!! Please enter valid number")
    print(result)
main()
