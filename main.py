# print ("Hello World!")
# print (3 + 2)
# input_string_var = input("Введите данные: ")
# print (input_string_var)

# firstName = input("Enter first name: ")
# lastName = input("Enter last name: ")
# print(f"Hi! {firstName} {lastName}. Nice to meуt you!")

## Lesson 4
# num_1 = input("Enter first number: ")
# num_1 = int (input("Enter first number: "))
# num_2 = input("Enter second number: ")
# result = num_1 + int(num_2);
# print (f"Result ({num_1} + {num_2}) is", result)

## Lesson 5
# if 0:
#     print ("True")
# print("All is OK!")
# num = int(input("Введіть число: "))
# if int(num) > 10:
#     if num < 20:
#         print ("Ваше число більше десяти але меньше 20")
#     else:
#         print ("Ваше число більше двадцяти")
# elif num < 10:
#     print ("Ваше число меньше десяти")
# else:
#     print ("Ваше число рівне десяти")

## Lesson 6

# i = 0 
# while i < 10:
#     print(i)
#     i +=1

# for j in "Hello world!".upper():
#     if "h" == j.lower():
#         continue
#     print(j*2, end="")
#     if "a" == j.lower():
#         break
# else:
#     print("Letter `A` not found in the text")

l = []
numCollection = [1, 23, 43, 5, ['L', 'i', 's', 't'], 7, 87]
print(numCollection)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

l.append(1)
l.append(55)
b = [24, 65]
l.extend(b)
print(f"Append two elements {l}")
l.insert(2, 33)
print(f"Insert element by index {l}")
l.append(88)
print(l)
l.remove(88)
print(f"Remove by element {l}")
l.pop(1)
print(f"Remove by index {l}")
print(f"Show index by element {l.index(24)}")
print(f"Count by element {l.count(24)}")
