def get_user_name():
    name = input('Please enter your name: ')
    return name


def get_user_age():
    age = input('Please enter your age: ')
    return age


name = get_user_name()
age = get_user_age()



def print_all_data(age,name):
  print(f'your age is {age}')
  print(f'your name is {name}')


def number_of_decades(age):
   """
  Get the number of decades from a number of years.

  Args:
    years: The number of years.

  Returns:
    The number of decades.
  """
   print(f'the amount of decades that you have is: {int(float(age)// 10)}') 

print_all_data(age,name)
number_of_decades(age)