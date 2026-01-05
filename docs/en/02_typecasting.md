````md
# Lesson 02: Type Casting

🌐 Language: English | [বাংলা](../bn/02_typecasting.md)

---

## 📘 Topic Overview

In this lesson you will learn:

- What **type casting** means in Python  
- How to check the data type of a variable using `type()`  
- How to convert between basic data types:
  - string ↔ integer
  - integer ↔ float
  - number ↔ string
  - string ↔ boolean  
- Common mistakes and important rules when converting types  

The examples below are taken from the file `02_typecasting.py`.

---

## 💻 Full source code (original)

```python
# converting one type to another type

name = "Ashraful"
age = 25
gpa = 3.25
is_student = True

````

---

## 🔍 Checking variable types with `type()`

The `type()` function is used to find the data type of a variable.

```python
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))
```

**Output:**

```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Explanation:

* `"Ashraful"` → `str`
* `25` → `int`
* `3.25` → `float`
* `True` → `bool`

---

## 🔄 What is Type Casting?

**Type casting** means converting one data type into another.

Python provides built-in functions for this:

* `int()` → convert to integer
* `float()` → convert to float
* `str()` → convert to string
* `bool()` → convert to boolean

---

## 🔢 Converting float to int

```python
gpa = int(gpa)
print(gpa)
```

**Output:**

```
3
```

Important:

* Converting a float to an integer **removes the decimal part** (it does not round).
* `3.25` becomes `3`.

---

## 🔸 Converting int to float

```python
age = float(age)
print(age)
```

**Output:**

```
25.0
```

Explanation:

* The integer `25` becomes the float `25.0`.

---

## 🔤 Converting number to string

```python
age = str(age)
age = age + "1"
print(age)
print(type(age))
```

**Output:**

```
25.01
<class 'str'>
```

Explanation:

* After converting `age` to a string, `"25.0" + "1"` results in string concatenation.
* Python does **not** perform numeric addition on strings.

---

## ✅ Converting string to boolean

```python
name = bool(name)
print(name)
```

**Output:**

```
True
```

Rules for `bool()`:

* Any **non-empty string** → `True`
* Empty string `""` → `False`

Example:

```python
bool("")      # False
bool("Hi")    # True
```

---

## 🛠 Common mistakes & tips

* **Converting invalid strings to numbers** causes errors:

  ```python
  int("abc")   # ❌ ValueError
  ```
* **String addition is not numeric addition**:

  ```python
  "2" + "3"    # "23"
  ```
* **Order matters** when casting:

  ```python
  int("25")    # ✅
  int(25.9)    # ✅
  int("25.9")  # ❌ ValueError
  ```
* Always check types using `type()` when debugging.

---

## 🔁 How to run this file locally

If you cloned the repository, run:

```bash
python 02_typecasting.py
```

This will print the data types and converted values.

---

## 🔗 View the original Python file on GitHub

[View `02_typecasting.py` on GitHub](../../02_typecasting.py)

---

## 📝 Practice exercises

1. Convert an integer `x = 10` into a float and print its type.
2. Convert a float `y = 7.8` into an integer and print the result.
3. Convert a number into a string and concatenate it with `"Python"`.
4. Test `bool()` with:

   * an empty string
   * a non-empty string
   * the number `0`
   * the number `5`

---

⬅️ **[Previous: Printing & Variables](01_printing_n_variables.md)** | ➡️ **[Next: User Input](03_input.md)**

🎉 You now understand how Python converts data between different types!

```
```
