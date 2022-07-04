# Notes from Corey Schafer's Python Course
# https://www.youtube.com/c/Coreyms

# List, Tuples, and Sets
from operator import index

#__________________
#Lists []

courses = ['History', 'Math', 'Physics', 'CompSci']

#Print list
print(courses)
# ['History', 'Math', 'Pysics', 'CompSci']

#Get length
print(len(courses))
#4

#get data at index, starts at 0
print(courses[2])
#Physics

#Last Index
print(courses[-1])
#CompSci

#Range - print 0 - 1, starts a zero, does not include 2

print(courses[0:2])
#['History', 'Math'] 
# Can leave off 0 since its first (slicing)
print(courses[:2])
#['History', 'Math']

# Can leave off end when going to the full end (slicing)
print (courses[2:])
# ['Physics', 'CompSci']

# Add to list, 3 ways
# Way 1
# Add item to list at the end (append)
# courses.append('Art')

# Way 2
# Adds to targeted index of list (insert)
# inserts, not overrides
# courses.insert(0 , 'Art')
# print (courses)
# ['Art', 'History', 'Math', 'Physics', 'CompSci']

#Way 3
courses2 = ['Art', 'Education']

# add via insert (not the expected output)
#courses.insert(0, courses2)
# print(courses)
# [['Art', 'Education'], 'Art', 'History', 'Math', 'Physics', 'CompSci']
# produces list in list at Index 0
# not what we wanted, need to use extend method

# Extend list ( adds courses2 to courses)
courses.extend(courses2)
print( courses )
# ['Art', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']

#Remove values

# Remove via name
courses.remove("Math")
print (courses)
# ['Art', 'History', 'Physics', 'CompSci', 'Art', 'Education']

# Remove via pop (by default will remove the last value on the list)
# Can set var and get return value that is popped off
print(courses)
popped = courses.pop()
print(popped)
print(courses)

## Output
# ['Art', 'History', 'Physics', 'CompSci', 'Art', 'Education']
# Education
# ['Art', 'History', 'Physics', 'CompSci', 'Art']

# Sort a list
# Reverse
courses.reverse()
print(courses)
#['Art', 'CompSci', 'Physics', 'History']

# Sort
nums = [ 1, 5, 4, 3]
nums.sort()
courses.sort()
print(courses)
print(nums)
#['Art', 'CompSci', 'History', 'Physics']
#[1, 3, 4, 5]

# To reverse sort, pass argument to sort method (reverse = True)
nums = [ 1, 5, 4, 3]
nums.sort(reverse = True)
courses.sort(reverse = True)
print(courses)
print(nums)
#['Physics', 'History', 'CompSci', 'Art']
#[5, 4, 3, 1]

# To sort without changing the original, use the sorted function rather than the sort method
courses = ['History', 'Math', 'Physics', 'CompSci']
print(sorted(courses))
print(courses)
['CompSci', 'History', 'Math', 'Physics']
['History', 'Math', 'Physics', 'CompSci']

# MIN, MAX, SUM, built in functions
nums = [ 1, 5, 4, 3]
print(min(nums))
# 1
print(max(nums))
# 5
print(sum(nums))
# 15

# Find values in List
#Search for index number of name
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('CompSci'))
# 3

# Search and get a true or false result
print('Art' in courses)
print('Math' in courses)
# False
# True

# Using for loop
for item in courses:
    print(item)

# output
# History
# Math
# Physics
# CompSci

# To get index and value use the enumerate
for item in enumerate(courses):
    print(item)
# Output
# (0, 'History')
# (1, 'Math')
# (2, 'Physics')
# (3, 'CompSci')

# To get index and value use the enumerate
for index, course in enumerate(courses):
    print(index, course)
# Output
# 0 History
# 1 Math
# 2 Physics
# 3 CompSci

# if you wanted to start at 1 vs 0 pass in value into the fuction
courses = ['History', 'Math', 'Physics', 'CompSci']
for index, course in enumerate(courses, start = 1):
    print(index, course)

#Output
# 1 History
# 2 Math
# 3 Physics
# 4 CompSci


# Convert list into string sep by value
# string method used, Join

course_str = ", ".join(courses)
print(course_str)
# Output
# History, Math, Physics, CompSci

# Reverse, string back to list via split
new_list = course_str.split(",")
print(new_list)
# Output
# ['History', ' Math', ' Physics', ' CompSci']

# _________________
# Tuples 
# Tuples are immutable

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

# ['History', 'Math', 'Physics', 'CompSci']
# ['History', 'Math', 'Physics', 'CompSci']

# Added Art to list 1, but they are both the same mutuable object...so both change
list_1[0] = 'Art'

print(list_1)
print(list_2)
['Art', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']

# To prevent this ( if needed) use a tuple ()
tuple_1 = ('History', 'Math', 'Physics', 'Compsci')
tuple_2 = tuple_1

#tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# creates error on tuple_1[0] = 'Art
# tuples cannot change, append, remove

# ___________
# Sets
# Sets are unordered and no duplicates {}
# the order can change,sets do not care about order
# Uses
# 1) Test if a value is part of a set (sets are optimized for this)
# 2) Used to remove duplicate values, sets throw away duplicates

cs_course = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_course)
# Output 
# run 1 {'History', 'Math', 'Physics', 'CompSci'}
# run 2 {'CompSci', 'Physics', 'Math', 'History'}
# run 3 {'History', 'Physics', 'Math', 'CompSci'}

# Example of duplicate removal...Math is listed twice
cs_course = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_course)
# output
# {'Math', 'CompSci', 'Physics', 'History'}

# Example of value check in set
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print('Math' in cs_course)
# output
# True

#Check to sets for shared values via the intersection method

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

#shared
print(cs_courses.intersection(art_courses))

#Output
# {'History', 'Math'}

# Courses in cs_courses and not the art_courses use diffence methdod
print(cs_courses.difference(art_courses))

#output
# {'CompSci', 'Physics'}

# use the union method to list all courses offered
print(cs_courses.union(art_courses))

#output
#{'Design', 'Physics', 'CompSci', 'Art', 'Math', 'History'}

#Empty Lists 
# 1 - brackets
# 2 - list class
empty_lists = []
empty_list = list()

#Empty Tuples
# 1 - parentheses
# 2 - tuple class
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
# 1 - use set class
# This does not work:
empty_set = {} # does not work..this will create an empty dictionary
empty_set = set()