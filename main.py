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

i = 0 
while i < 10:
    print(i)
    i +=1

for j in "Hello world!".upper():
    if "h" == j.lower():
        continue
    print(j*2, end="")
    if "a" == j.lower():
        break
else:
    print("Letter `A` not found in the text")