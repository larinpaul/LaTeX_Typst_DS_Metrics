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

### Python OS
os.access(path, mode) # check if the specified path has the specified access permissions
os.chdir(path)
os.chflags(path, flags)
os.chmod
os.chown(path,uid,gid) # uid - идентификатор пользователя gid - идентификатор группы 
os.chroot(path) # change the root directory of the current process
os.close(fd)
os.dup(fd)
os.fchdir(id)
os.fstat(fd)
os.fsync(fd)
os.getcwd()
os.lchmod(path,mode) # Change the permissionof a symbolic link itself
os.lchown(path, uid,gid)
os.link(src,dst)# create a hard link
os.listdir(path)
os.istat(path)
os.openpty() # create a pseudo-terminal
os.pathconf(path,name)
os.pipe()
os.readlink(path)
os.remove(path)
os.removedirs(path) # recursively remove directories
os.rename(src,dst)
os.renames(old, new)
os.mdir(path)# remove an empty directory
os.stat(path) # get information of the file or directory at the specified path
os.statvis(path) # get information of the file system at the specified path
os.symlink(src,dst) # crate a symbolic link
os.ttyname(df) # return a string representing the name of the terminal device
os.unllink(path) # delete a file at the specified path
os.utime(path,times) # set the last modification and access time of specified path file
os.pardir() # get the parent directory of the current directory
os.replace() # Rename a file or directory
os.startfile() # open a file or launch an application on windows

### Python File

file.close() 
file.flush # flush the internal I/O buffer of a file object
file.fileno() # returns the underlying file descriptor corresponding to the file object
file.isarry() # check whether the file object is connected to a terminal device
file.read([size]) # read specified number of bytes from a file
file.readline([size]) # read a single line of data from a file
fle.write(str)
file.writelines(sequence) # write a sequence of strings to a file

### Python Random

seed() # initialize the random number generator
getstate()# get the internal state of the random number generator
random() # generate a random floating-point number in the range [0.0, 1.0]
uniform() # generate a random floating-point number within a given range
betavariate() # generate a random number from the beta distribution # бета-распределение - это семейство непрерывных распределений вероятностей. ограниченных интервалом от 0 до 1. Бета-распределение идеально подходит для моедлирования процентов, долей или вероятностей чего-либо, например какова реальная конверсия сайта? с помощью параметров alpha (успехи = 10) и beta (неудачи = 5) бета-распределение покажет вам наиболее вероятный диапазон вашей конверсии
random.betavariate(alpha, beta)
expovariate() # generate a random number from the exponential distribution
gammavariate() # generate a randomnumber from the gamma distribution
gauss()# generate a random number from the normal (Gaussian) distribution
lognormvariate()  # Generate a random number from the log-normal distribution
paretovariate() # Generate a random number from the Pareto distribution
weibuillivariate() # Generate a random number from the Weibull distribution

### Python Data Type Conversion

int()
float()
str()
bool()
list()
tuple()
set()
dict()
complex()
bytes()
chr() # covert a value to a character

### Python List

len(list) # return the number of elements in the list
max(list)
min(lint)
list(seg) # convert a tuple to a list
list.append(obj) # append a new object to the end of the list
list.count(obj) # count the number of times an element appears in the list
list.index(obj) # find the index position of the first math for a value from the list 
list.insert(index, obj) # insert the object into the list
list.pop([index=-1]) # Remove an element from the list (the last element by default)
list.remove(obj) # Remove the first match for a value in the list 
list.reverse() # Reverse the order of elements in the list
list.clear() # Clear the list
list.copy # Copy the list
