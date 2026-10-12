soldier_name = "Jack Reacher"
reversed_soldier_name = ""

for char in soldier_name:
    reversed_soldier_name = char + reversed_soldier_name
print("using for loop",'=',reversed_soldier_name)

reversed_soldier_name = ""

for i in range(len(soldier_name)-1,-1,-1):
    reversed_soldier_name += soldier_name[i]
print("using indexing",'=',reversed_soldier_name)  

reversed_soldier_name = ""

reverse_in_slicing = soldier_name[::-1]
print("reverse using slicing",'=',reverse_in_slicing)