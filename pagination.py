# Import Pagination
from django.core.paginator import Paginator

user_list = [1,2,3,4,5,6,7,8,90,87,467,235,76,34,53,23,67,8,346,7987,345,4,876,4,645,77,697,346,231,124,67,689,80,567,86,57687,547587,2346457,234645867,45876978]

# Create Pagination Object
paginator = Paginator(user_list, 10)
print(paginator)

# Count of values
print(paginator.count)

# Number of pages
print(paginator.num_pages)

# Range of Pages
print(paginator.page_range)

# Page Number Selecting
print(paginator.page(2))



# Lets Make a object to get data

users = paginator.page(2)

# Pages
print(users)

# Checking if next page is available
print(users.has_next())

# Checking if previous page is available
print(users.has_previous())

# Checking is other pages ar4e avaliable
print(users.has_other_pages())

# Checking Next page number
print(users.next_page_number())

# Checking Previous page number
print(users.previous_page_number())

# Starting index
print(users.start_index())

# Ending Index
print(users.end_index())


# Getting Data Value
for u in users:
	print(u)
