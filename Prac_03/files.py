name_file = open('name.txt', 'w')
name_file.write(input("Name: "))
name_file.close()
name_file = open('name.txt', 'r')
print("Your name is ", name_file.read())
name_file.close()
numbers_file = open('numbers.txt', 'w')
numbers_file.write("17" + "\n")
numbers_file.write("42" + "\n")
numbers_file.write("200" + "\n")
numbers_file.close()
numbers_file = open('numbers.txt', 'r')
first_number = numbers_file.read(2)
second_number = numbers_file.read(3)
first_number_1 = int(first_number)
second_number_2 = int(second_number)
total = first_number_1 + second_number_2
print(f"The total of {first_number_1} and {second_number_2} is {total}.")
numbers_file.close()
numbers_file = open('numbers.txt', 'r')
print(numbers_file.read())
numbers_file.close()