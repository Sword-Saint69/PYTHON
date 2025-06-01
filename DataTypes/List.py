#Creatig a list

Students = ["Goutham","Krishna","Rene"]
print(Students)

print(type(Students))


#Using constructor method

list4 = list(Students)
print(list)

list2 = list("Goutham")
print(list2)

list3 = list((3,4,"goutham"))
print(list3)

#Accesing Elements of List

l1 = [1,2,4,5,67,8,3,22]

print(l1[3])
print(l1[5])

#Inserting Elements in a List

arr = [3,32,2,12,14,55,565,34,21]
arr.append(11)
print(arr)

#Inserting multiple elements in a array
arr = [3, 32, 2, 12, 14, 55, 565, 34, 21]
arr.insert(2, (23, 23, 121))  # Insert tuple at index 2
print(arr)


l1 = [1,2]
l2 = ["Goutham","Sankar"]
l1.extend(l2)
print(l1)

#Removing Element
arr1 = [3,5,2,23,23,32,21]

arr1.remove(2)
print(arr1)


arr1.pop()
print(arr1)


#Reversing a List
arr1.reverse()
print(arr1)

#Copy

l1_copy = l1.copy()
print(l1_copy)

#sort
arr1.sort()
print(arr1)