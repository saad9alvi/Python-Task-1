#Q1.Declare and initialize two variables, num1 and num2, with integer values. Calculate and print
#their sum.
num1 = 5
num2 = 10
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)

#Q2.Create a variable, message, and assign it a string value. Append another string, " World!", to it
#and print the result.
Name = "Hello"
Name += " World!"
print(Name)

#Q3.Define a variable, is_python_fun, and assign it a boolean value. Print a statement based on
#whether Python is considered fun.
is_python_fun = True 
if is_python_fun:print("Python is fun!")
else:print("Python may not be as fun for everyone.")

#Q4.Create a list, fruits, with three different fruit names. Print the list and then add a new fruit to it.
#Print the updated list.
fruits = ["Apple", "Banana", "Orange"]
print("Original list of fruits:", fruits)
fruits.append("Grapes")
print("Updated list of fruits:", fruits)

#Q5.Declare a variable, price, with a floating-point value. Convert it to an integer and print both the
#original and converted values.
price = 17.15
price_int = int(price)
print("Original price:", price)
print("Converted price to integer:", price_int)

#Q6.Create a dictionary, student_info, with keys for 'name', 'age', and 'grade'. Assign corresponding
#values and print the dictionary.
student_info = {'name': 'Areeb Alvi','age': 15,'grade': 'A'}
print("Student Information:")
print("Name:", student_info['name'])
print("Age:", student_info['age'])
print("Grade:", student_info['grade'])

#Q7.Combine two strings using string concatenation, and then use string interpolation to include the
#length of the resulting string in a print statement.
string1 = "Python"
string2 = "Learner!"
combined_string = string1 + " " + string2
print(f"The combined string is: {combined_string}, and its length is: {len(combined_string)}")

#Q8.Create a tuple, days_of_week, with the names of the days. Access and print the third day of the
#week.
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
third_day = days_of_week[2]
print("The third day of the week is:", third_day)
