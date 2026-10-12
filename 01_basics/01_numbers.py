binary_num = 0b1101011
print(binary_num)

octal_num = 0o16
print(octal_num)

hexal_num = 0xFB
print(hexal_num)

# Converting integers into different numbers:

int_number = 100

binary_base = bin(int_number)
octal_base = oct(int_number)
hexadecimal_base = hex(int_number)

# Converting different_base numbers into integers:

binary_to_int = int(binary_base,2)
octal_to_int = int(octal_base,8)
hexadecimal_to_int = int(hexadecimal_base,16)

# String Conversion

int_to_binary = f"{int_number:b}"
int_to_octal = f"{int_number:o}"
int_to_hexadecimal = f"{int_number:x}"

#  Type conversion

complex_num = 3+5j

# print(complex_num)

