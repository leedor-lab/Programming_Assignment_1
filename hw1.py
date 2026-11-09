"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data
from math import sqrt


# Part 1: vowel_count
#this function takes in a string and with a loop checks if there are vowels and increases a count for every vowel appearance
#the inputs are a string and the outputs are a count (integer)
def vowel_count(text: str) -> int:
    lower=text.lower()
    count=0
    for char in lower:
        if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
            count=count+1
    return count        


# Part 2: short_lists
#The purpsoe is to select the nested lists that contain a length of 2 and return a new list with those len()==2 lists usig a loop and and if statement
#the inputs are a nested lists, and outputs are a new list of appended lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    l=[]
    for item in items:
        if len(item)==2:
            l.append(item)
    return l

# Part 3: ascending_pairs
# the purpose of this function is to find the nested lisst with len()==2 and make the items in the list go in ascending order usign nested for loops and if logic
# the input is a nested lists, and the output is a new list of ascending length two lists
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    l=[]
    for row in items:
        new_row=[]
        for item in row:
            new_row.append(item)
        if len(new_row)==2 and new_row[0]>new_row[1]:
            temp=new_row[0]
            new_row[0]=new_row[1]
            new_row[1]=temp
        l.append(new_row)  
    return l                            

# Part 4: add_prices
# the purpose of this function is to add two prices using a Price object and return the dollar amount from their sum
# the inputs are two parameters that use data.py and the output is a new Price object
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    dollars = first.dollars + second.dollars
    cents = first.cents + second.cents
    if cents>=100:
        dollars=dollars+1
        cents=cents-100
    return data.Price(dollars,cents)    

# Part 5: rectangle_area
# the purpose is to use a rectangle and Point object to find the legnths of the height and width of a rectangle and find the area
# the inputs are a rectangle class and point object data and the outputs are
def rectangle_area(rectangle: data.Rectangle) -> float:
    height=rectangle.top_left.y-rectangle.bottom_right.y
    width=rectangle.bottom_right.x-rectangle.top_left.x
    return height * width

# Part 6: books_by_author
# the purpose is to search through each book in the books list and check to see if the author is in that specifc book object and if it is append that book to a new list
# inputs are the author and list of books, the output is a new list of books accodring to the authors
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    l=[]
    for book in books:
        if author in book.authors:
            l.append(book)
    return l        


# Part 7: circle_bound
#the purpose of this fucntiuon is to use rectange, point, and circle clsses to center a circle in a rectange and find the radius to be from the edge of the rectangle to the center of the circle
# the inputs are rectangle data and the output is a new circle object 
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    x=(rectangle.top_left.x+rectangle.bottom_right.x)/2
    y=(rectangle.top_left.y+rectangle.bottom_right.y)/2
    center=data.Point(x,y)
    distance=sqrt((rectangle.top_left.x-x)**2+(rectangle.top_left.y-y)**2)
    return data.Circle(center,distance)

# Part 8: below_pay_average
# the purpose of this function is to find the average pay of the employees list object and determine who is lower than that average pay
#  the unputs are the employees object and the outputs is a list of the employees name

def below_pay_average(employees: list[data.Employee]) -> list[str]:
   total=0
   l=[]
   if len(employees)==0:
       return l
   for employee in employees:
       total+=employee.pay_rate
   total=total/len(employees)
   for employee in employees:
       if employee.pay_rate<total:
           l.append(employee.name)
   return l           
       