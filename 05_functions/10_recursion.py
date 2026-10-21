def countdown(n):
    # 1. The Base Case: Stop when n hits 0
    if n <= 0:
        print("Blast off! 🚀")
        return
    
    # Do some work
    print(n)
    
    # 2. The Recursive Step: Call the function again with a smaller number
    countdown(n - 1)

# Calling the function
countdown(3)