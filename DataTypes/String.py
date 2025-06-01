#String in Python

Name = "Goutham"
Name1 = "Sankar"
Country = "India"

Message = '''Hello this is 
python multi line string'''

print(Name[2])

#Concatnation

full_name = Name+Name1
length = len(full_name)
print(length)

#Slicing

print(full_name[2:4])
print(full_name[4:9])
print(full_name[-1:])
print(full_name[:])

#String functions

My_name="Goutham sankar"
small="goutham sankar"
print(My_name.upper())
print(My_name.lower())
print(small.capitalize())

#strip

str1="      Goutham sankar"
print(str1.strip())


#Replace
text = "I am learning Python."
print(text.replace("I am", "We are"))



print("Hello \n Goutham")


print("Hello \" goutham \"")


