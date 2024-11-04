try:
    number = input("Please enter a number: ")
    print(f"You entered: {number}")
except KeyboardInterrupt:
    print("\nInput canceled by user.")