from functools import wraps
#https://stackoverflow.com/questions/7108193/frequently-repeated-try-except-in-python
#https://stackoverflow.com/questions/11186422/reducing-the-number-of-try-except-in-python
#https://www.quora.com/Is-there-an-elegant-way-to-reduce-the-numbers-of-try-except-in-Python-programming


def may_exist(func):
   @wraps(func):
   def wrapper(*args, **kwds):
       try:
           return func(*args, **kwds)
       except OSError:
           pass
   return wrapper

def df

may_exist()
