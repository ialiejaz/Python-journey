n = int(input("Enter a combination: "))

def single_line_output(n):
    if n < 10:
        print(n)
        return
    single_line_output(n // 10)
    print(n % 10)

single_line_output(n)