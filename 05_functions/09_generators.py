# # limit = 20

# def even_finder(limit):
#     for i in range(2,limit+1,2):
#         print(i)
# print(even_finder(10))

# def even_checker(limit):
#     for i in range(2,limit+2,2):
#         yield i

# for num in even_checker(10):
#     print(num)

# def letters():
#     for i in range(65,91):
#         yield chr(i)

# my_letters = letters()

# for letter in my_letters:
#     print(letter,end = ' ')

list = [1,2,3,4,5]

list_iter = iter(list)

# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))

# def list_generator():
#     fruits = ['apple','mango','strawberry']
#     for item in fruits:
#         yield item
# iter_obj = list_generator()

# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# def lower_case():
#     for char in range(97,101):
#         yield chr(char)

# iter_obj = lower_case()
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

def multiples():
    i=1
    while True:
        yield i * 5
        i+=1

multiple5 = multiples()

print(next(multiple5))
print(next(multiple5))
print(next(multiple5))
