numbers = input("Enter the numbers separated by comma: ")
numbers_list = numbers.split(',')
numbers_tuple = tuple(numbers_list)
print(f'The list of numbers is: {numbers_list} \nThe tuple of numbers is: {numbers_tuple}')
