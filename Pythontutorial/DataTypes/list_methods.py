marks1  = [5, 2, 21, 5, 10]
extra_marks1 = [3,4,6,7]

print(marks1)
marks1.append(63)

 #This will change the original list.
marks1.extend(extra_marks1)
marks1.pop(2)
print(marks1)