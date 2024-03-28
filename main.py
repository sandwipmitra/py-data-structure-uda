age = 10
if (age >= 18):
  print("You can learn driving")
print("You can not learn driving")


eclipse_dates = [
    'June 21, 2001', 'December 4, 2002', 'November 23, 2003', 'March 29, 2006',
    'August 1, 2008', 'July 22, 2009', 'July 11, 2010', 'November 13, 2012',
    'March 20, 2015', 'March 9, 2016'
]

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])


list_of_random_things = [1, 3.4, 'a string', True]
# print(list_of_random_things[-1])
list_of_random_things = len(list_of_random_things) -2
print(list_of_random_things)

q1 = 'this' in 'this is a string'
print(q1)
#True
q2 = 'in' in 'this is a string'
print(q2)
#True
q3 = 'isa' in 'this is a string'
print(q3)
#False
q4 = 5 not in [1, 2, 3, 4, 6]
print(q4)
#True
q5 = 5 in [1, 2, 3, 4, 6]
print(q5)
#False

#Mutable
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)
#['one', 2, 3, 4, 5]

#Immutable
#does not work
greeting = "Hello there"
greeting[0] = 'M'



month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
# num_days = days_in_month[7]
num_days = days_in_month[month - 1] 
print(num_days)