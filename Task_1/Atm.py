mypin = 1234
total = 50000

def transaction():
    pin = int(input("Please Enter your Secret Number: "))
    if pin == mypin:
        amnt = int(input("Please Enter the amount: "))
        if amnt <= total:
            print("Please wait while your transaction is processing...")
            print("\nAvailable Balance is", total - amnt)
            print("Thank you for Banking with Us")
        else:
            print("Insufficient Balance")
    else:
        print("Incorrect PIN")

def balance():
    pin = int(input("Please Enter your Secret Number: "))
    if pin == mypin:
        print("Your total balance is", total)
    else:
        print("Incorrect PIN")

def main():
    print("Welcome to GC Bank")
    print("Please select your Account type")
    print("1. Savings\n2. Current")

    try:
        en = int(input())
        if en in [1, 2]:
            print("1. Cash Withdrawal\n2. Balance Enquiry")
            n = int(input())

            if n == 1:
                transaction()
            elif n == 2:
                balance()
            else:
                print("Invalid option")
        else:
            print("Please Enter a valid option")
    except ValueError:
        print("Invalid Input. Please enter numbers only.")

if __name__ == "__main__":
    main()
