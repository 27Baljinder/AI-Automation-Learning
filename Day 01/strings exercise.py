first_name = "Baljinder"
last_name = "Singh"
country = "India"
full_name = first_name + " " + last_name
print(f"My name is {first_name} {last_name} and i am from {country} and my full name has length of {len(full_name)}")

#string indexing
word = "Python"
print(word[0])
print(word[2])
print(word[5])

#experiment with string indexing
print(f"this word string have different characters at each spot for example, at 0 its {word[0]} and at 2 its {word[2]} and at 5 its {word[5]}")

#negative indexing
print(word[-1])
print(word[-3])
print(word[-6])

#string slicing
word = "Python"

print(word[0:3]) #pyt
print(word[2:5]) #tho
print(word[1:4]) #yth

print(word[:2])
print(word[3:])
print(word[-4:])
print(word[:-2])

#step
word = "Python"

print(word[::-1])