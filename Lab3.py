#...........................1.........................


def display_squares(n):
    print("Number\tSquare")
    number = 1
    while number <= n:
        square = number ** 2
        print(f"{number}\t{square}")
        number += 1


n = int(input("Enter the value of n: "))


display_squares(n)


#Output....................
"""
Enter the value of n: 5
Number	Square
1	1
2	4
3	9
4	16
5	25

"""



#...........................2................................


def sum_of_digits(number):
    total_sum = 0
    while number > 0:
        
        digit = number % 10
        
        total_sum += digit
       
        number //= 10
    return total_sum


number = int(input("Enter a number: "))


if number < 0:
    print("Please enter a non-negative number.")
else:
   
    result = sum_of_digits(number)
    
    
    print(f"Number: {number}")
    print(f"Sum of the digits: {result}")




#Output...............................................
"""
Enter a number: 1234
Number: 1234
Sum of the digits: 10

"""



#3..................................................................


def print_fibonacci(n):
    
    a, b = 0, 1
    count = 0

    
    while count < n:
        print(a, end=' ')
       
        a, b = b, a + b
        count += 1
    print()  


n = int(input("Enter the number of terms in the Fibonacci series: "))


print_fibonacci(n)




#Output...............
"""
Enter the number of terms in the Fibonacci series: 10
0 1 1 2 3 5 8 13 21 34

"""






#4......................................................



def print_multiplication_table(number, limit):
    print(f"Multiplication table for {number} up to {limit}:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


number = int(input("Enter the number for the multiplication table: "))
limit = int(input("Enter the limit up to which the table should be printed: "))


print_multiplication_table(number, limit)




#Output:......................................
"""
Enter the number for the multiplication table: 5
Enter the limit up to which the table should be printed: 12
Multiplication table for 5 up to 12:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
5 x 11 = 55
5 x 12 = 60

"""











#5................................................................

def are_all_characters_alphanumeric(s):
    
    for char in s:
        
        if not char.isalnum():
            return False
    return True


input_string = input("Enter a string: ")


result = are_all_characters_alphanumeric(input_string)


print(result)




#Output:..................................
"""
Enter a string: Hello123
True

"""


#6..........................................................




def count_character_occurrences(s, char_to_count):
    count = 0
    
    for char in s:
        
        if char == char_to_count:
            count += 1
    return count


input_string = input("Enter the string: ")
character = input("Enter the character to count: ")


if len(character) != 1:
    print("Please enter exactly one character to count.")
else:
    
    occurrences = count_character_occurrences(input_string, character)
    
    
    print(f"The character '{character}' occurs {occurrences} times in the string.")




#Output:.....................................................
"""
Enter the string: hello world
Enter the character to count: o
The character 'o' occurs 2 times in the string.

"""