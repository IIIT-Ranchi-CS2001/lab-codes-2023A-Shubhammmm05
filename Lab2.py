#1......................



S1 = "Maha Bharat"


result_1 = S1.swapcase()


result_2 = S1.split()[1]


result_3 = result_2 * 3


result_4 = S1.replace("Maha", "Mera")


result_5 = result_4 + " Mahan"


print("Generated Strings:")
print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)




#Output.....................

"""
Generated Strings:
mAHA bHARAT
Bharat
BharatBharatBharat
Mera Bharat
Mera Bharat Mahan

"""


#2.................................



S = "Ba Ba Black Sheep"


length_of_S = len(S)


first_occurrence_e = S.find('e')


total_occurrences_a = S.count('a')


modified_S = S.replace("Ba", "Ta", 2)  



print("Results:")
print(f"Length of the string: {length_of_S}")
print(f"First occurrence of the letter 'e': {first_occurrence_e}")
print(f"Total number of occurrences of 'a': {total_occurrences_a}")
print(f"Modified string: {modified_S}")



#Output.....................
"""
Results:
Length of the string: 18
First occurrence of the letter 'e': 14
Total number of occurrences of 'a': 4
Modified string: Ta Ta Black Sheep

"""


#3........................


def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]


input_string = input("Enter any string: ")


if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")



#Output.....................

"""
Enter any string: Madam
'Madam' is a palindrome.

"""


#4................................................


def calculate_grade_point_and_remark(marks):
    if marks >= 90:
        return 10, "OUTSTANDING"
    elif marks >= 80:
        return 9, "VERY GOOD"
    elif marks >= 70:
        return 8, "GOOD"
    elif marks >= 60:
        return 7, "AVERAGE"
    elif marks >= 50:
        return 6, "PASS"
    else:
        return 0, "FAIL"


name = input("Enter the student's name: ")
roll_number = input("Enter the student's roll number: ")
marks = float(input("Enter the marks secured in Mathematics (out of 100): "))


if marks < 0 or marks > 100:
    print("Invalid input! Marks should be between 0 and 100.")
else:
    
    grade_point, remark = calculate_grade_point_and_remark(marks)
    
    
    print("\nStudent Details:")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Marks: {marks}")
    print(f"Grade Point: {grade_point}")
    print(f"Remark: {remark}")





#Output..................
"""
Enter the student's name: Alice
Enter the student's roll number: 12345
Enter the marks secured in Mathematics (out of 100): 85

Student Details:
Name: Alice
Roll Number: 12345
Marks: 85.0
Grade Point: 9
Remark: VERY GOOD

"""


#5..................................


import math


def find_roots(a, b, c):
    
    discriminant = b**2 - 4*a*c

    if discriminant > 0: 
        R1 = (-b + math.sqrt(discriminant)) / (2 * a)
        R2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The equation has two distinct real roots:")
        print(f"Root 1: {R1:.2f}")
        print(f"Root 2: {R2:.2f}")
    elif discriminant == 0:
       
        R = -b / (2 * a)
        print(f"The equation has one real repeated root:")
        print(f"Root: {R:.2f}")
    else:
        
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"The equation has two complex roots:")
        print(f"Root 1: {real_part:.2f} + {imaginary_part:.2f}i")
        print(f"Root 2: {real_part:.2f} - {imaginary_part:.2f}i")


a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))


if a == 0:
    print("Invalid input! Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    
    find_roots(a, b, c)




#Output............................

"""
Enter coefficient a: 1
Enter coefficient b: -3
Enter coefficient c: 2
The equation has two distinct real roots:
Root 1: 2.00
Root 2: 1.00

"""