# ===== PROBLEM1 =====
# Exercise 1 - Introduction - Say "Hello, World!" With Python
print("Hello, World!")
# Exercise 2 - Introduction - Python If-Else
# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n >= 20:
        print("Not Weird")
# Exercise 3 - Introduction - Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
# Exercise 4 - Introduction - Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
# Exercise 5 - Introduction - Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
# Exercise 6 - Introduction - Write a function
def is_leap(year):
    # Write your logic here
    leap = False
    if year%4==0 and year%100==0 and year%400==0:
        leap = True
    elif year%4==0 and year%100==0:
        leap = False
    elif year%4==0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))
# Exercise 7 - Introduction - Print Function
if __name__ == '__main__':
    n = int(input())
    i = 0
    while(i<n):
        i = i+1
        print(i, end= "")
# Exercise 8 - Basic data types - List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,w] for i in range(x+1) for j in range(y+1) for w in range(z+1) if i+j+w != n ])
# Exercise 9 - Basic data types - Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst_sort = sorted(arr,reverse = True)
    a = lst_sort[0]
    for x in lst_sort:
        if x < a:
            print(x)
            break
# Exercise 10 - Basic data types - Nested Lists
if __name__ == '__main__':
    lst_est =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst = []
        lst.append(name)
        lst.append(score)
        lst_est.append(lst)
    minimo_score = lst_est[0][1]
    for row in lst_est:
        if row[1] < minimo_score:
            minimo_score = row[1]
    nuova_lst = []
    for row in lst_est:
        if row[1] != minimo_score:
            nuova_lst.append(row)
    secondo_score = nuova_lst[0][1]
    for row in nuova_lst:
        if row[1] < secondo_score:
            secondo_score = row[1]
    ultima_lst = []
    for valore in nuova_lst:
        if valore[1] == secondo_score:
            ultima_lst.append(valore[0])
    ultima_lst.sort()
    for x1 in ultima_lst:
        print(x1)
# Exercise 11 - Basic data types - Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list_score = student_marks.get(query_name)
    mean = 0.0
    total_sum = 0
    for x in list_score:
        total_sum += x
    mean = float(total_sum)/len(list_score)
    print('%.2f' % mean)
# Exercise 12 - Basic data types - Lists
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        arr = input().split()
        if arr[0] == "print":
            print(lst)
        elif arr[0] == "insert":
            lst.insert(int(arr[1]),int(arr[2]))
        elif arr[0]== "remove":
            lst.remove(int(arr[1]))
        elif arr[0] == "append":
            lst.append(int(arr[1]))
        elif arr[0] == "sort":
            lst.sort()
        elif arr[0]== "pop":
            lst.pop()
        elif arr[0]=="reverse":
            lst.reverse()
# Exercise 13 - Basic data types - Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    int_lst = list(integer_list)
    t=tuple(int_lst)
    print(hash(t))
# Exercise 14 - Strings - sWAP cASE
def swap_case(s):
    r=""
    for x in s:
        if str.isalpha(x):
            if str.islower(x):
                z = str.upper(x)
                r=r+z
            elif str.isupper(x):
                z = str.lower(x)
                r=r+z
        else:
            r = r+x
    return r


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
# Exercise 15 - Strings - String Split and Join
def split_and_join(line):
    # write your code here
    nline = line.split()
    nline = "-".join(nline)
    return nline

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
# Exercise 16 - Strings - What's Your Name?
def print_full_name(a, b):
    print("Hello",a,b+"! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
# Exercise 17 - Strings - Mutations
def mutate_string(string, position, character):
    list_char = list(string)
    list_char[position] = character
    string = ''.join(list_char)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
# Exercise 18 - Strings - Find a string
def count_substring(string, sub_string):
    len_sub = len(sub_string)
    len_str = len(string)
    cnt = 0
    for i in range(len_str - len_sub + 1):
        if string[i:i + len_sub] == sub_string:
            cnt += 1
    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
# Exercise 19 - Strings - String Validators
if __name__ == '__main__':
    s = input()
    n_l = 0
    n_n = 0
    for x in range(len(s)):
        if (s[x].isalpha() == True):
            n_l += 1
        elif (s[x].isdigit() == True):
            n_n += 1
    if (n_n > 0 and n_l > 0):
        print(True)
    elif (n_n >= 0 and n_l > 0):
        print(True)
    elif (n_n > 0 and n_l >= 0):
        print(True)
    else:
        print(False)
    for x in range(len(s)):
        if (s[x].isalpha() == True):
            print(True)
            break
        elif x != len(s)-1:
            continue
        else:
            print (False)
    for x in range(len(s)):
        if (s[x].isdigit() == True):
            print(True)
            break
        elif x != len(s)-1:
            continue
        else:
            print(False)
    for x in range(len(s)):
        if (s[x].islower() == True):
            print(True)
            break
        elif x != len(s)-1:
            continue
        else:
            print (False)
    for x in range(len(s)):
        if (s[x].isupper() == True):
            print(True)
            break
        elif x != len(s)-1:
            continue
        else:
            print(False)
# Exercise 20 - Strings - Text Alignment
#Replace all ______ with rjust, ljust or center.
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
# Exercise 21 - Strings - Text Wrap
import textwrap
def wrap(string, max_width):
    x = len(string)
    c = 1
    j = 0
    for i in range(x):
        if i == (c*max_width)-1:
            print(string[j:i+1])
            c=c+1
            j=i+1
            if x-i <= max_width:
                print(string[i+1:])
    return ""

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
# Exercise 22 - Strings - Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = [int(x) for x in input().split()]
d = 1
c = (m-3*d)//2
f = (m-6)//2
for i in range(n):
    if i < n//2:
        print(("-")*c + (".|.")*d + ("-")*c)
        d = d+2
        c = (m-3*d)//2
    elif i == n//2:
        print(("-")*f + "WELCOME" + ("-")*f)
        d = d-2
        c = (m-3*d)//2
    elif i > n//2:
        print(("-")*c + (".|.")*d + ("-")*c)
        d = d-2
        c = (m-3*d)//2
# Exercise 23 - Strings - String Formatting
def print_formatted(number):
    # your code goes here
    for j in range(1, number + 1):
        x = '{:b}'.format(j)
    n = len(x)

    for i in range(1, number + 1):
        print(repr(i).rjust(n), end = " "),
        print('{:o}'.format(i).rjust(n), end = " "),
        print('{:x}'.format(i).rjust(n).upper(), end = " "),
        print('{:b}'.format(i).rjust(n))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
# Exercise 24 - Strings - Alphabet Rangoli
# Exercise 25 - Strings - Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    for i in range(len(s)):
        if i == 0:
            s = s[0].upper() + s[1:]
        elif s[i-1] == " " and s[i] != " ":
            s = s[:i] + s[i].upper() + s[i+1:]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
# Exercise 26 - Strings - The Minion Game
# Exercise 27 - Strings - Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    lst = []
    i = 0
    n = len(string)
    while i < n:
        lst.append(string[:k])
        string = string[k:]
        i+=k
    for parola in lst:
        s = ""
        for carattere in parola:
            if carattere not in s:
                s = s + carattere
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
# Exercise 28 - Sets - Introduction to Sets
def average(array):
    # your code goes here
    ins = set(array)
    j = sum(ins)
    i = len(ins)
    media = j / i
    return media


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
# Exercise 29 - Sets - No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
x = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int,input().split()))
happy = 0
for i in x:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1
    else:
        happy = happy
print (happy)
# Exercise 30 - Sets - Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
a=set(list(map(int,input().split())))
t=input()
b=set(list(map(int,input().split())))
c=a.symmetric_difference(b)
d=sorted(c)
for x in d:
    print(x)
# Exercise 31 - Sets - Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
ins=set()
x=int(input())
for i in range(0,x):
    y=input()
    if y not in ins:
        ins.add(y)
print(len(ins))
# Exercise 32 - Sets - Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
t = int(input())
for _ in range(t):
    arr = input().split(" ")
    if arr[0] == "pop":
        s.pop()
    elif arr[0]== "remove":
        s.remove(int(arr[1]))
    elif arr[0] == "discard":
        s.discard(int(arr[1]))
sm=0
for x in s:
    sm=sm+x
print(sm)
# Exercise 33 - Sets - Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
a=set(list(map(int,input().split())))
t=input()
b=set(list(map(int,input().split())))
c = set()
for valore in b:
    c.add(valore)
for valore1 in a:
    c.add(valore1)
print(len(c))
# Exercise 34 - Sets - Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
a=set(list(map(int,input().split())))
t=input()
b=set(list(map(int,input().split())))
print(len(a.intersection(b)))
# Exercise 35 - Sets - Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
a=set(list(map(int,input().split())))
t=input()
b=set(list(map(int,input().split())))
print(len(a.difference(b)))
# Exercise 36 - Sets - Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
a=set(list(map(int,input().split())))
t=input()
b=set(list(map(int,input().split())))
print(len(a.symmetric_difference(b)))
# Exercise 37 - Sets - Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
ins = set(list(map(int,input().split())))
y = int(input())
for _ in range(y):
    arr = input().split(" ")
    ins1 = set(list(map(int,input().split())))
    if arr[0]== "update":
        ins.update(ins1)
    elif arr[0]== "intersection_update":
        ins.intersection_update(ins1)
    elif arr[0] == "symmetric_difference_update":
        ins.symmetric_difference_update(ins1)
    elif arr[0] == "difference_update":
        ins.difference_update(ins1)
sm = 0
for p in ins:
    sm= sm + p
print(sm)
# Exercise 38 - Sets - The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
lst = list(map(int,input().split()))
d = {}
for a in lst:
    d[a] = d.get(a, 0)+1
for k,v in d.items():
    if v!= x:
        print(k)
# Exercise 39 - Sets - Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
for _ in range(x):
    t = int(input())
    ins = set(map(int, input().split()))
    y = int(input())
    ins1 = set(map(int, input().split()))
    if ins.issubset(ins1):
        print(True)
    else:
        print(False)
# Exercise 40 - Sets - Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = set(map(int, input().split()))
n = int(input())
b = True
for _ in range(n):
    s1 = set(map(int, input().split()))
    if s.issuperset(s1):
        continue
    else:
        b=False
        break
print(b)
# Exercise 41 - Collections - collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
lst = list(map(int,input().split()))
y = int(input())
p = 0
for _ in range(y):
    arr = list(map(int,input().split()))
    if arr[0] in lst:
        p = p + arr[1]
        lst.remove(arr[0])
    else:
        continue
print(p)

# Exercise 42 - Collections - DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int,input().split())
A = defaultdict(list)
B = []
cnt = 1
for i in range(n):
    A[input()].append(cnt)
    cnt+= 1
for j in range(m):
    B.append(input())
for k in B:
    if k in A.keys():
        print (' '.join( map(str,A[k]) ))
    else:
        print(-1)
# Exercise 43 - Collections - Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
sum_scores = 0
student = namedtuple("student",input())
for i in range(n):
    lst = input().split()
    student1 = student(lst[0],lst[1],lst[2],lst[3])
    x = int(student1.MARKS)
    sum_scores += x
media = round(sum_scores/n,2)
print(media)
# Exercise 44 - Collections - Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
d = OrderedDict()
for i in range(n):
    lst = input().split()
    x = lst[-1:]
    t = int(x[0])
    n_lst = lst[:-1]
    lungh = len(n_lst)
    if lungh > 1:
        val = " ".join(n_lst)
    else:
        val = n_lst[0]
    d[val] = d.get(val, 0)+ t
for x,y in d.items():
  print(x, end = " ")
  print(y)
# Exercise 45 - Collections - Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = {}
for i in range(n):
  a = input()
  d[a] = d.get(a, 0) + 1
print(len(d))
for x in d.values():
  print(x, end = " ")
# Exercise 46 - Collections - Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
lst = []
for i in range(n):
    lst = input().split()
    if len(lst) == 1:
        if lst[0] == "pop":
            d.pop()
        else:
            d.popleft()
    else:
        if lst[0] == "append":
            d.append(int(lst[1]))
        else:
            d.appendleft(int(lst[1]))
for x in d:
    print(x, end = " ")
# Exercise 47 - Collections - Company Logo
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    d = {}
    d1 = {}
    lst = []
    lst1 = []
    lst2 = []
    for a in s:
        d[a] = d.get(a,0) +1
        d1 = sorted(d.items(), key = lambda t: t[1],reverse= True)
    max1 = d1[0][1]
    for i in range(len(d1)):
        if d1[i][1] == max1:
            lst.append(d1[i])
    if len(lst) < 3:
        max1 = d1[len(lst)][1]
        for i in range(len(lst),len(d1)):
            if d1[i][1] == max1:
                lst1.append(d1[i])
    if len(lst+lst1) < 3:
        max1 =d1[len(lst)+len(lst1)][1]
        for i in range(len(lst)+len(lst1),len(d1)):
            if d1[i][1] == max1:
                lst2.append(d1[i])
    lst.sort(key = lambda t: t[0])
    lst1.sort(key = lambda t: t[0])
    lst2.sort(key = lambda t: t[0])
    lst4 = lst+lst1+lst2
    for i in range(3):
        print(lst4[i][0], end = " ")
        print(lst4[i][1])
# Exercise 48 - Collections - Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
for i in range(n):
    m = int(input())
    lst = list(map(int,input().split()))
    d = deque(lst)
    while True:
        if len(d) == 1:
            print("Yes")
            break
        elif d[0] >= d[1]:
            d.popleft()
        elif d[-1] >= d[-2]:
            d.pop()
        else:
            print("No")
            break
# Exercise 49 - Date time - Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
data = list(map(int,(input().split())))
y = datetime.datetime(data[2],data[0],data[1])
x=y.weekday()
if x == 0:
    print("MONDAY")
elif x == 1:
    print("TUESDAY")
elif x == 2:
    print("WEDNESDAY")
elif x == 3:
    print("THURSDAY")
elif x == 4:
    print("FRIDAY")
elif x == 5:
    print("SATURDAY")
elif x == 6:
    print("SUNDAY")
# Exercise 50 - Date time - Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    date_object = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date_object1 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    date = (date_object-date_object1)
    return (str(abs(int(date.total_seconds()))))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
# Exercise 51 - Exceptions -
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    arr = input().split()
    try:
        a=arr[0]
        b=arr[1]
        print (int(a)//int(b))
    except ZeroDivisionError as t:
        print("Error Code:",t)
    except ValueError as e:
        print("Error Code:",e)
# Exercise 52 - Built-ins - Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
ls = list(map(int,(input().split())))
t=[]
media=0
val=0
for p in range(ls[1]):
    z = list(map(float,(input().split())))
    t.append(z)
x = zip(*t)
for tupla in x:
    mean = sum(tupla)/len(tupla)
    print(round(mean,1))
# Exercise 53 - Built-ins - Athlete Sort
#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key = lambda l:l[k])
    for valore in arr:
        for j in valore:
            print(j,end = " ")
        print()
# Exercise 54 - Built-ins - Ginorts
# Enter your code here. Read input from STDIN. Print output to STDOUT
string = input()
lower_val = ""
upper_val = ""
odd_val = ""
even_val = ""
stampa = ""
for x in string:
    if x.islower():
         lower_val += x
for x in string:
    if x.isupper():
         upper_val += x
for x in string:
    if x.isdigit() and int(x)%2!=0:
         odd_val += x
for x in string:
    if x.isdigit() and int(x)%2==0:
         even_val += x
lower_val = "".join(sorted(lower_val))
upper_val = "".join(sorted(upper_val))
odd_val = "".join(sorted(odd_val))
even_val = "".join(sorted(even_val))
stampa = lower_val + upper_val + odd_val + even_val
print(stampa)
# Exercise 55 - Map and lambda function
cube = lambda x: x**3 # complete the lambda function
def fibonacci(n):
    # return a list of fibonacci numbers
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
# Exercise 56 - Regex - Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    m = re.match("([0-9]*\.[0-9]+$)|(-[0-9]*\.[0-9]+$)|(\+[0-9]*\.[0-9]+$)",input())
    if m:
        print(True)
    else:
        print(False)
# Exercise 57 - Regex - Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
# Exercise 58 - Regex - Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
w = input()
m = re.search("(11+)|(22+)|(33+)|(44+)|(55+)|(66+)|(77+)|(88+)|(99+)|(aa+)|(bb+)|(cc+)|(dd+)|(ee+)|(ff+)|(gg+)|(hh+)|(ii+)|(jj+)|(kk+)|(ll+)|(mm+)|(nn+)|(oo+)|(pp+)|(qq+)|(rr+)|(ss+)|(tt+)|(uu+)|(vv+)|(ww+)|(xx+)|(yy+)|(zz+)", w)
if m:
    n = m.group()
    print(n[0])
else:
    print(-1)
# Exercise 59 - Regex - Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
n = re.findall("(?=([qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]{1,1}[aeiouAEIOU]{2,}[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]+))",s)
if n:
    for stri in n:
        p = re.search("[aeiouAEIOU]+",stri)
        print(p.group())
else:
    print(-1)
# Exercise 60 - Regex - Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = input()
c = input()
m = "(?=("+c+"))"
l = len(c)-1
lst = re.findall(m,n)
if lst == []:
    print((-1,-1))
else:
    for match in re.finditer(m, n):
        print (tuple([match.start(),match.start()+l]))
# Exercise 61 - Regex - Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    t = input()
    t = re.sub(" &&(?= )"," and",t)
    t = re.sub(" \|\|(?= )"," or",t)
    print(t, end = " ")
    print()
# Exercise 62 - Regex - Validating Roman Numerals
# Exercise 63 - Regex - Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    m = input()
    p = re.fullmatch("[789]{1,1}[0-9]{9,9}", m)
    if p:
        print("YES")
    else:
        print("NO")
# Exercise 64 - Regex - Validating and Parsing Email Addresses
# Exercise 65 - Regex - Hex Color Code
# Exercise 66 - Regex - HTML Parser - Part 1
# Exercise 67 - Regex - HTML Parser - Part 2
# Exercise 68 - Regex - Detect HTML Tags, Attributes and Attribute Values
# Exercise 69 - Regex - Validating UID
# Exercise 70 - Regex - Validating Credit Card Numbers
# Exercise 71 - Regex - Validating Postal Codes
# Exercise 72 - Regex - Matrix Script
# Exercise 73 - Xml - XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    x = 0
    for child in root.iter():
        x += len(child.attrib.values())
    return x

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
# Exercise 74 - Xml - XML 2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
# Exercise 75 - Closures and decorators - Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        prex = "+91"
        l1 = []
        l2 = []
        l3 = []
        for x in l:
            x = str(x)
            x1 = x[::-1]
            l1.append(x1)
        for y in l1:
            y1 = y[:10]
            y1 = y1[::-1]
            l2.append(y1)
        for i in range(len(l2)):
            l[i] = (l2[i])
        for i in l:
            l3.append(prex + " " + i[:5] + " " + i[5:])
        for i in range(len(l3)):
            l[i] = (l3[i])
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
# Exercise 76 - Closures and decorators - Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        people = sorted(people,key = lambda l: int(l[2]))
        l1 = []
        for person in people:
            l1.append(f(person))
        return l1
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
# Exercise 77 - Numpy - Arrays
import numpy
def arrays(arr):
    # complete this function
    # use numpy.array
    st1 = arr[::-1]
    b = numpy.array(st1,float)
    return b

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
# Exercise 78 - Numpy - Shape and Reshape
import numpy
lst = []
lst = list(map(int,input().split()))
my_array = numpy.array(lst)
my_array.shape = (3, 3)
print(my_array)
# Exercise 79 - Numpy - Transpose and Flatten
import numpy
number_row_column = input().split()
number_row = number_row_column[0]
row = []
matrix=[]
for x in range(int(number_row)):
    row = list(map(int,input().split()))
    matrix.append(row)
arr = numpy.array(matrix)
print(numpy.transpose(arr))
print(arr.flatten())
# Exercise 80 - Numpy - Concatenate
import numpy
number_row_column = input().split()
number_row_1 = number_row_column[0]
number_row_2 = number_row_column[1]
row_1= []
matrix_1=[]
row_2= []
matrix_2=[]
for x in range(int(number_row_1)):
    row_1 = list(map(int,input().split()))
    matrix_1.append(row_1)
arr_1 = numpy.array(matrix_1)
for x in range(int(number_row_2)):
    row_2 = list(map(int,input().split()))
    matrix_2.append(row_2)
arr_2 = numpy.array(matrix_2)
print(numpy.concatenate((arr_1, arr_2),axis = 0))
# Exercise 81 - Numpy - Zeros and Ones
import numpy
row = list(map(int,input().split()))

print (numpy.zeros(row,dtype = numpy.int))
print(numpy.ones(row,dtype = numpy.int))
# Exercise 82 - Numpy - Eye and Identity
import numpy
numpy.set_printoptions(sign= " ")
n,m = map(int,input().split())
print (numpy.eye(n, m))
# Exercise 83 - Numpy - Array Mathematics
import numpy
x,v = map(int,input().split())
lst = []
lst1 = []
lst2 = []
for i in range(2*x):
    lst = list(map(int,input().split()))
    if i < x:
        lst1.append(lst)
        a = numpy.array(lst1)
    else:
        lst2.append(lst)
        b = numpy.array(lst2)
print (numpy.add(a, b))
print (numpy.subtract(a, b))
print (numpy.multiply(a, b))
print(a//b)
print (numpy.mod(a, b))
print (numpy.power(a, b))
# Exercise 84 - Numpy - Floor, Ceil and Rint
import numpy
lst = list(map(float,(input().split())))
numpy.set_printoptions(sign=' ')
my_arr = numpy.array(lst)
print(numpy.floor(my_arr))
print(numpy.ceil(my_arr))
print(numpy.rint(my_arr))
# Exercise 85 - Numpy - Sum and Prod
import numpy
n_m = []
n_m = list(map(int,input().split()))
lst1 = []
lst2 = []
for i in range(n_m[0]):
    lst1 = list(map(int,input().split()))
    lst2.append(lst1)
arr = numpy.array(lst2)
arr1 = numpy.sum(arr, axis = 0)
print(numpy.prod(arr1))
# Exercise 86 - Numpy - Min and Max
import numpy
n_m = []
n_m = list(map(int,input().split()))
lst1 = []
lst2 = []
for i in range(n_m[0]):
    lst1 = list(map(int,input().split()))
    lst2.append(lst1)
arr = numpy.array(lst2)
arr1 = numpy.min(arr, axis = 1)
print(numpy.max(arr1))
# Exercise 87 - Numpy - Mean, Var, and Std
import numpy
numpy.set_printoptions(legacy='1.13')
n,m = map(int,input().split())
lst1 = []
lst2 = []
for i in range(n):
    lst1 = list(map(int,input().split()))
    lst2.append(lst1)
arr = numpy.array(lst2)
print(numpy.mean(arr,axis = 1))
print(numpy.var(arr, axis = 0))
print(numpy.std(arr))
# Exercise 88 - Numpy - Dot and Cross
import numpy
x = int(input())
A = []
B  = []
lst = []
for i in range(2*x):
    lst = list(map(int,input().split()))
    if i < x:
        A.append(lst)
    else:
        B.append(lst)

print(numpy.dot(A,B))
# Exercise 89 - Numpy - Inner and Outer
import numpy
A = []
B = []
for i in range(2):
    lst = list(map(int,input().split()))
    if i < 1:
        A.append(lst)
    else:
        B.append(lst)
X = numpy.inner(A,B)
for i in X:
    for j in i:
        print(j)
print(numpy.outer(A,B))
# Exercise 90 - Numpy - Polynomials
import numpy
lst = list(map(float,input().split()))
x = float(input())
print(numpy.polyval(lst,x))
# Exercise 91 - Numpy - Linear Algebra
import numpy
numpy.set_printoptions(legacy='1.13')
x = int(input())
lst2 =[]
for i in range(x):
    lst = list(map(float,input().split()))
    lst2.append(lst)
print(numpy.linalg.det(lst2))

# ===== PROBLEM2 =====

# Exercise 92 - Challenges - Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    # Complete the birthdayCakeCandles function below.
    x = max(ar)
    c = 0
    for i in ar:
        if i==x:
            c=c+1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
# Exercise 93 - Challenges - Kangaroo
# !/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    # Complete the kangaroo function below.
    for p in range(1, 10001):
        if x1 + p * v1 == x2 + p * v2:
            return ("YES")
        else:
            continue
    return ("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
# Exercise 94 - Challenges - Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    recipients = 5
    cumulative = 0
    like = 0
    for i in range(1,n+1):
        like = math.floor(recipients/2)
        cumulative = cumulative+like
        recipients = like*3
    return cumulative




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
# Exercise 95 - Challenges - Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    n1 = 0
    for i in n:
        n1 += int(i)
    n1 = n1*k
    if n1 < 10:
        return n1
    else:
        return superDigit(str(n1),1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
# Exercise 96 - Challenges - Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    x = arr[n-1]
    while n-2>=0:
        if x < arr[n-2]:
            if n-2>0:
                arr[n-1] = arr[n-2]
                n = n-1
                for t in arr:
                    print (t,end=" ")
                print ("")
            else:
                arr[n-1]=arr[n-2]
                for t in arr:
                    print (t,end=" ")
                print("")
                arr[n-2]=x
                n = n-1
                for t in arr:
                    print (t,end=" ")
                return arr
        else:
           arr[n-1]=x
           for p in arr:
               print(p,end=" ")
           return arr
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
# Exercise 97 - Challenges - Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        for u in arr:
            print(u,end=" ")
        print()

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
