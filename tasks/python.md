# 💡 Python Practice Problems

This repository contains multiple beginner to intermediate Python programs focused on logic building, user input handling, matrix manipulation, number theory, string processing, database connection, and more.

---

## 🧠 Problem List

---

### 1. ✅ Prime Number Matrix Input

**Question:**
Write a program to take a 2x2 matrix as input from the user where each value must be a **prime number**. If the input is not a prime number, prompt the user again.

**Code:**

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

matrix = []
for i in range(2):  
    row = []
    for j in range(2):  
        while True:
            val = int(input(f"enter the number({i+1},{j+1}):"))
            if is_prime(val):
                row.append(val)
                break
            else:
                print("Not a prime number")
matrix.append(row)
print(matrix)
```

---

### 2. 🗓️ Leap Year Check

**Question:**
Write a program to check whether a given year is a **leap year**.

**Code:**

```python
n = int(input("enter the number"))
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print("leap year")
else:
    print("not leap year")
```

---

### 3. 🔁 Matrix Symmetry Check

**Question:**
Take a 2x2 matrix input and check whether the matrix is **equal to its transpose** (i.e., it's symmetric).

**Code:**

```python
matrix = []
for i in range(2):  
    row = []
    for j in range(2):  
        value = int(input(f"Enter the number ({i+1},{j+1}): "))
        row.append(value)
    matrix.append(row)
print(f"matrix{matrix}")
inverse_matrix = list(map(list, zip(*matrix)))
print(f"InverseMatrix:{inverse_matrix}")
if matrix == inverse_matrix:
    print("Both are Same")
else:
    print("Both are Not Same")
```

---

### 4. 🔢 Decimal to Binary Conversion

**Question:**
Convert a given decimal number into its **binary equivalent** and pad it with zeros to a minimum of 2 digits.

**Code:**

```python
n = int(input())
b = ""
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(f"Binary: {b.zfill(2)}")
```

---

### 5. 🔠 Longest Common Prefix

**Question:**
Write a function that takes a list of strings and returns the **longest common prefix** among them.

**Code:**

```python
def longest_prefix(words):
    pre = min(words, key=len)
    for s in words:
        while not s.startswith(pre):
            pre = pre[:-1]
            if pre == "":
                return ""
    return pre

words = input().split()
print(longest_prefix(words))
```

---

### 6. 🎯 Generate Combinations

**Question:**
Given a list of numbers and a value `k`, print all **combinations of size `k`** using Python's `itertools`.

**Code:**

```python
import itertools
nums = list(map(int, input().split()))
size = int(input())
res = list(itertools.combinations(nums, size))
print(res)
```

---

### 7. ⭐ Wildcard Match

**Question:**
Check if either of the input strings contains a `*` or `.*`, indicating the presence of a **wildcard pattern**.

**Code:**

```python
a = input()
b = input()
if '*' in a or '*' in b or '.*' in a or '.*' in b:
    print('True')
else:
    print('False')
```

---

### 8. ➖ Minimum Difference Between Adjacent Elements

**Question:**
Find the **minimum absolute difference** between adjacent elements in a list.

**Code:**

```python
l1 = [3, 8, -10, 23, 19, -4, -14, 27]
minn = abs(abs(l1[1] - l1[0]))
for i in range(len(l1) - 1):
    diff = abs(l1[i] - l1[i + 1])
    if diff < minn:
        minn = diff
print(minn)
```

---

### 9. ➕️ Sum and Product Difference

**Question:**
Given a list of integers, calculate the **absolute difference** between their **sum** and their **product**.

**Code:**

```python
n = list(map(int, input().split()))
sum = 0
mul = 1
for i in n:
    sum += i
    mul *= i
print(abs(sum - mul))
```


### 10. 🚩 Divide Array into Sets of K Consecutive Numbers

**Question:**
Check if an array can be divided into sets of `k` consecutive numbers.

**Code:**

```python
from collections import Counter

def canDivide(nums, k):
    if len(nums) % k != 0:
        return False

    freq = Counter(nums)
    keys = sorted(freq)

    for num in keys:
        count = freq[num]
        if count > 0:
            for i in range(1, k):
                if freq[num + i] < count:
                    return False
                freq[num + i] -= count
    return True

nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))
print(canDivide(nums, k))
```

---

### 11. 🔢 Most Frequent Element

**Question:**
Find the most frequently occurring element in a list.

**Code:**

```python
def most_frequent(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_count = 0
    most_common = None
    for key, value in d.items():
        if value > max_count:
            max_count = value
            most_common = key
    return most_common

lst = [1, 2, 3, 4, 5, 2, 3, 4]
print(most_frequent(lst))
```

---

### 11.1. ⚡ Most Frequent Elements (All with Max Count)

**Question:**
Return all elements that have the highest frequency.

**Code:**

```python
def most_frequent(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_count = max(d.values())
    most_common = [key for key, value in d.items() if value == max_count]
    return most_common

lst = [1, 2, 3, 4, 5, 2, 3, 4]
print(most_frequent(lst))
```

---

### 12. 📆 Pair with Given Target Sum

**Question:**
Find a pair in a list whose sum equals the target value.

**Code:**

```python
def pairs_target(lst, target):
    seen = set()
    for n in lst:
        if target - n in seen:
            return (target - n, n)
        seen.add(n)
    return None

lst = [1, 2, 3, 4, 5, 6]
target = 8
print(pairs_target(lst, target))
```

---

### 13. 💡 Insertion Sort Logic (Partial)

**Question:**
Perform a partial step of insertion sort to sort a list.

**Code:**

```python
lst = [2, 4, 5, 3, 1, 6]
for i in range(1, len(lst)):
    key = lst[i]
    j = i - 1
    if lst[i] > lst[j]:
        lst[i], lst[j] = lst[j], lst[i]
print(lst)
```

---

### 14. 👨‍💼 MySQL Stored Procedure Call

**Question:**
Call a stored procedure from MySQL that takes an employee ID and returns their name.

**Code:**

```python
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Yashwanth@7',
    database='sample'
)

cursor = conn.cursor()
create_proc = """
CREATE PROCEDURE GetEmployeeName(IN emp_id INT, OUT emp_name VARCHAR(100))
BEGIN
    SELECT ename INTO emp_name
    FROM employee
    WHERE empno = emp_id;
END
"""
cursor.execute(create_proc)
conn.commit()

emp_id = int(input())
emp_name = ''
result_args = cursor.callproc('GetEmployeeName', [emp_id, emp_name])
print("Employee Name:", result_args[1])

cursor.close()
conn.close()
```

---



### 15. ⚠️ Custom Exception: Negative Value

**Question:**
Create a custom exception class and raise it if the user enters a **negative number** while computing the square root.

**Code:**

```python
class NegativeValueError(Exception):
    def __init__(self, value):
        super().__init__(f"Negative value not allowed: {value}")
        self.value = value

def square_root(x):
    if x < 0:
        raise NegativeValueError(x)
    return x ** 0.5

try:
    result = square_root(int(input()))
    print(result)
except NegativeValueError as e:
    print("Caught custom exception:", e)
```

---

### 16. 🔹 Decorator Function

**Question:**
Use a **decorator** to print messages before and after a function is called.

**Code:**

```python
def decorator_function(func):
    def result():
        print("Before function call")
        func()
        print("After function call")
    return result

@decorator_function
def say_hello():
    print("Hello!")

say_hello()
```

---

### 17. 🔮 Default Mutable Argument Pitfall

**Question:**
Demonstrate unexpected behavior using **mutable default arguments** and a fix.

**Code:**

```python
def append_to_list(value, lst=[]):
    lst = value
    return lst

print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))
```

Also includes lambda closure behavior:

```python
funcs = [lambda x: x+i for i in range(3)]
results = [f(10) for f in funcs]
print(results)  # Output: [10+2, 10+2, 10+2] => [12, 12, 12]
```

---

### 18. 🔄 Sort and Move Zeros to End

**Question:**
Sort the non-zero elements in a list and move all zeros to the **end**.

**Code:**

```python
a = [1, 0, 5, 0, 6, 2, 0, 9]
b = []
c = []
for i in a:
    if i == 0:
        c.append(i)
    else:
        b.append(i)

for i in range(len(b)):
    for j in range(len(b)):
        if b[i] < b[j]:
            b[i], b[j] = b[j], b[i]
print(b + c)
```

---

### 19. ❌ Modify List While Iterating

**Question:**
Demonstrate what happens when you **remove elements** from a list while iterating.

**Code:**

```python
nums = [1,2,3,4,5,6,7,8,9,10,12,13,16]
for num in nums:
    if num % 2 == 0:
        nums.remove(num)
print(nums)
```

---

### 20. 🤖 Index Error and Multiplication

**Question:**
What is the result of multiplying a string with 0 and accessing an **out-of-bound index** in a list?

**Code:**

```python
print("abc" * 0)
a = [1, 2, 3]
print(a[3])  # Will raise IndexError
```

---

### 21. 🛏️ Inner Class Usage

**Question:**
Demonstrate how to define and use an **inner class** within an outer class.

**Code:**

```python
class Outer:
    class Inner:
        def greet(self):
            return "Hello from the Inner class!"

    def __init__(self):
        self.inner = Outer.Inner()

    def outer_greet(self):
        return self.inner.greet()

o = Outer()
print(o.outer_greet())
```

---

### 22. 🔄 Shallow vs Deep Copy

**Question:**
Demonstrate the difference between **shallow copy** and **deep copy** in Python.

**Code:**

```python
import copy

original = [[1, 2], [3, 4]]
original1 = [[1, 2], [3, 4]]

shallow = copy.copy(original)
shallow[0][0] = 'X'
print(original)  # Affected

deep = copy.deepcopy(original1)
deep[0][0] = 'X'
print(original1)  # Not affected
```

---

### 23. ❌ Unbound Local Variable Example

**Question:**
Show how modifying a variable inside a nested function can lead to an **UnboundLocalError**.

**Code:**

```python
def outer():
    x = 10
    def inner():
        x += 5
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
```

---

### 24. 🤔 Anagram Grouping

**Question:**
Group all anagrams in a list of words.

**Code:**

```python
def anagrams(words):
    dict = {}
    for word in words:
        key = ''.join(sorted(word))
        if key in dict:
            dict[key].append(word)
        else:
            dict[key] = [word]
    return list(dict.values())

print(anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
```

---

### 25. ⏱ Longest Substring Without Repeating Characters

**Question:**
Find the **length of the longest substring** with all unique characters.

**Code:**

```python
def substring(word):
    seen = set()
    j = 0
    maxx = 0
    for i in range(len(word)):
        while word[i] in seen:
            seen.remove(word[j])
            j += 1
        seen.add(word[i])
        maxx = max(maxx, i - j + 1)
    return maxx

print(substring(input()))
```

### 26. 🤷️ Isomorphic Strings

**Question:**
Check if two strings are **isomorphic** (characters map one-to-one).

**Code:**

```python
def isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False
    map_s1_to_s2 = {}
    map_s2_to_s1 = {}
    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        if c1 in map_s1_to_s2:
            if map_s1_to_s2[c1] != c2:
                return False
        else:
            map_s1_to_s2[c1] = c2
        if c2 in map_s2_to_s1:
            if map_s2_to_s1[c2] != c1:
                return False
        else:
            map_s2_to_s1[c2] = c1
    return True

print(isomorphic(s1=input(), s2=input()))
```

---

### 27. 📏 Diagonal Sum in Matrix

**Question:**
Calculate the **sum of diagonals** in a 3x3 matrix, avoiding double count of the middle.

**Code:**

```python
n = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]
d1 = 0
d2 = 0
for i in range(len(n)):
    d1 += n[i][i]
    d2 += n[i][len(n) - 1 - i]
if len(n) % 2 != 0:
    d2 -= n[len(n)//2][len(n)//2]
print(d1 + d2)
```

---

### 28. 🎭 Parse Encoded String

**Question:**
Parse a string formatted as "FirstName000LastName000ID" into a dictionary.

**Code:**

```python
import re

def parse_encoded_string(s):
    parts = re.split('0+', s)
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }

print(parse_encoded_string(s="Robert000Smith000123"))
```

---

### 29. 🄠 Find Non-Matching Character

**Question:**
Find the first character in the first string that doesn’t appear in the second string.

**Code:**

```python
def same_char(s1, s2):
    for i in s1:
        if i not in s2:
            return i

print(same_char(input(), input()))
```

---

### 30. 🌑 Shadow Words Check

**Question:**
Check if two sentences are of the same length and corresponding words share no common letters.

**Code:**

```python
def shadow(s1, s2):
    if len(s1) != len(s2):
        return False
    w1 = s1.split()
    w2 = s2.split()
    for w1, w2 in zip(w1, w2):
        if len(w1) != len(w2):
            return False
        if set(w1) & set(w2):
            return False
    return True

print(shadow(input(), input()))
```

---

### 31. 🔠 Unique Characters in Sentence

**Question:**
Return `False` if any word in the sentence has all unique characters.

**Code:**

```python
def sentence(s1):
    words = s1.split()
    for word in words:
        if len(set(word)) == len(word):
            return False
    return True

print(sentence(input()))
```

---

### 32. 🌫️ ASCII to Hexadecimal

**Question:**
Convert each character in the input string to its hexadecimal equivalent.

**Code:**

```python
def asci_to_hex(s1):
    result = ''
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7',
                  '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for char in s1:
        asc_val = ord(char)
        hex_val = ""
        while asc_val > 0:
            rem = asc_val % 16
            hex_val = hex_digits[rem] + hex_val
            asc_val = asc_val // 16
        result += hex_val + " "
    return result

print(asci_to_hex(input()))
```

---

### 33. 📅 Friday the 13th Check

**Question:**
Check if the 13th day of a given month and year is a Friday.

**Code:**

```python
import datetime

def is_friday(month, year):
    d = datetime.date(year, month, 13)
    return d.weekday() == 4

print(is_friday(int(input()), int(input())))
```

---

### 34. 📳 Morse Code Converter

**Question:**
Convert a given message into Morse code.

**Code:**

```python
def morse_code(s):
    s = s.upper()
    result = []
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', "'": '.----.', ':': '---...'
    }
    for i in s:
        if i in morse_dict.keys():
            result.append(morse_dict[i])
        elif i == " ":
            result.append("//")
    return " ".join(result)

print(morse_code(s="Hi, Tom!"))
```

---

### 35. ⚠️ Custom Exception for Negative Input

**Question:**
Create a custom exception if the input is negative while calculating square root.

**Code:**

```python
class NegativeError(Exception):
    def __init__(self, number):
        super().__init__(f"The number must be positive: {number}")
        self.number = number

def squareroot(x):
    if x < 0:
        raise NegativeError(x)
    return x ** 0.5

try:
    result = squareroot(int(input("Enter a number: ")))
    print(result)
except NegativeError as e:
    print(e)
```

---

### 36. 📄 Text Wrap

**Question:**
Wrap a string every `w` characters.

**Code:**

```python
s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = 4
for i in range(0, len(s), w):
    print(s[i:i + w])
```

---

### 37. 🔹 Rangoli Pattern

**Question:**
Print the alphabet rangoli pattern of given size.

**Code:**

```python
def print_rangoli(size):
    width = 4 * size - 3
    lines = []
    for i in range(size):
        left = [chr(ord('a') + j) for j in range(size - 1, i, -1)]
        right = [chr(ord('a') + j) for j in range(i, size)]
        row = '-'.join(left + right)
        lines.append(row.center(width, '-'))
    for row in reversed(lines[:-1]):
        print(row)
    for row in lines:
        print(row)

# Example
print_rangoli(3)
```

---

### 38. 🌐 Day of the Week from Date

**Question:**
Given a date (month, day, year), print the day of the week in uppercase.

**Code:**

```python
import calendar

month, day, year = map(int, input().split())
day_name = calendar.day_name[calendar.weekday(year, month, day)]
print(day_name.upper())
```

---

### 39. ✖️ Symmetric Difference of Sets

**Question:**
Given two sets, print elements present in only one of the sets (symmetric difference).

**Code:**

```python
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
result = sorted(a ^ b)
for num in result:
    print(num)
```

---

### 40. 🧰 Set Intersection

**Question:**
Find common elements between two lists using set intersection.

**Code:**

```python
l1 = [1, 3, 6, 78, 35, 55]
l2 = [12, 24, 35, 24, 88, 120, 155]
res = set(l1).intersection(set(l2))
print(res)
```

---
