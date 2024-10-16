def fibonacci_sequence():
    # Ask the user for the number of terms
    terms = int(input("Enter the number of terms: "))
    
    # Starting values of the sequence
    n1, n2 = 0, 1
    count = 0
    
    # Handle case for number of terms less than 1
    if terms <= 0:
        print("Please enter a positive integer.")
    elif terms == 1:
        print(f"Fibonacci sequence up to {terms} term: {n1}")
    else:
        print("Fibonacci sequence:")
        while count < terms:
            print(n1)
            nth = n1 + n2
            # Update values
            n1 = n2
            n2 = nth
            count += 1

# Call the function
fibonacci_sequence()
