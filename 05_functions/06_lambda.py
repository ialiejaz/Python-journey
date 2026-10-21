# Usually use for single line function

students = [('ali',22),('usman',20),('umer',21),]

students.sort(key=lambda students:students)

print(students)

# numbers = [1,2,3,4,5,6,7,8,9,0]
odd_num = list(filter(lambda x: x%2  != 0 ,range(0,19)))
print(odd_num)

cube = lambda x : x**3

print(cube(5))