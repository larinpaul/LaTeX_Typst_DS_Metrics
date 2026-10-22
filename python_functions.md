# 2026 10 22 # 10:00

## Python

### Python Time Datetime

time.time()
time localtime(time.time())
time.asctime()
time.perf_counter()
datetime.timedelta()
datetime.now(tz=None)
datetime.fromisocalendar(year.week.day)
datetime.strptime(date_string format)

### Python Statistics

statistics.harmonic_mena()
statistics.mean()
statistics.median()
statistics.median_grouped()
statistics.median_high()
statistics.median_low()
statistics.mode()
statistics.stdev()
statistics.variance()
statistics.quanties()
capitalize()
isainum()
isapha()
isdigit()
len(string)
lower()
upper()
max(str)
min(str)

### Python Set

set.add()
set.clear()
set.copy() # shallow copy of an existing set
set.difference() # return the difference of multiple sets
set.intersection()
set.isdsjoint()
set.issubset()
set.symmetric_difference() # return the set of non-repeated elements from two sets
set.discard(element) # конкретный элемент, переданный в аргументе
set.pop() # случайный элемент (так как множества не упорядочены)
set.remove(element) # строгий аналог discard. remove вызывает ошибку если элемента нет
set.union()

### Python Tuple

len(tuple)
max(tuple)
min(tuple)
tuple(iterable) # convert an iterable series to a tuple

### Python Dictionary

len(dict) # the number of elements in the dictionary
str(dit)
type(variable) # return the type of the input variable # <class 'dict'>
dict.clear() # clear all the elements
dict.copy() # return the shallow copy
; import copy; copied_dict = copy.deepcopy(original_dict)
dict.keys() # return a view object (dict_keys), which is kinda like a set, but looks like dict_keys(['a', 'b', 'c'])
dict.popitem() return and remove the last key-value pair from the dictionary


### Python Math

math.cos(x)
math.sin(x)
math.tan(x)
math.acos(x)
math.asin(x)
math.atan(x)
math.acosh(x)
math.asinh(x) # inverse hyperbolic sine of x
math.atanh(x) # hyperboic tangent of x
math.ceil(x) # smallest integer not less than x
math.degrees(x) # convert angle x from radians to degrees
math.erf(x) # return the error function of a value # функция ошибок Гаусса или интеграл вероятности # вероятность того, что значение попадет в определенный диапазон вокруг среднего значения
math.exp(x) # return e raised to the power of x
math.fabs(x) # return the absolute value of x # fabs() in float, while abs() in int # abs() works with complex too, while fabs() works with float and throws error with complex
math.gamma(x) # Return the gamma function value at x # главная идея гамма-функции - это расширение понятия факториала на вещественные (дробные) числа. Для любого положительного целого числа значение math.gamma(n) всегда равно (n - 1)! # нельзя передать отрицательные числа и ноль # является базой для целого семейства распределений (гамма-распределение, распределение Стьюдента, Хи-квадрат) 
math.lgamma(x)
math.gcd(x) # return the greatest common divisor of the integer argument x









