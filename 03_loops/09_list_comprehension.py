even_numbers = [num for num in range(1,51) if num%2 == 0]
print(even_numbers)

word = input("Enter a word: ")
vowels = "aeiou"

Check = [char for char in word if char in vowels]

print (f"The vowel in {word} is {Check}.")