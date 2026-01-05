
# Lesson 01: Printing & Variables

🌐 Language: English | [বাংলা](../bn/01_printing_n_variables.md)

---

## 📘 Topic Overview

In this lesson you will learn:

- How to print text to the screen with `print()`.  
- How to create and use variables.  
- Basic Python data types: **string**, **integer**, **float**, **boolean**.  
- How to insert variables into strings using **f-strings**.  
- A few common mistakes to avoid.

The examples below are taken from the file `01_printing_n_variables.py`.

---

## 💻 Full source code (original)

```python
print("I love pizza!")
print("Pizza is the best food ever!")
````

---

## 🖨️ Printing text with `print()`

The `print()` function outputs text (or other values) to the console.

```python
print("I love pizza!")
print("Pizza is the best food ever!")
```

**Expected output:**

```
I love pizza!
Pizza is the best food ever!
```

Notes:

* Text values (strings) must be surrounded by quotes: either double `"` or single `'`.
* `print()` can be called many times; each call prints on a new line by default.

---

## 🧾 Comments

Lines that start with `#` are comments. They are ignored by Python and used to explain code for humans.

```python
#this is my first python program
#variables as strings
```

Use comments to describe what code does — it helps other readers and your future self.

---

## 🧑‍💻 Strings and string variables

A **string** is text stored in a variable.

```python
first_name = "Ashraful"
print(first_name)
print(f"Hello {first_name}")
```

* `first_name` now holds the text `"Ashraful"`.
* `print(first_name)` prints the value of the variable.
* `f"Hello {first_name}"` is an **f-string** (formatted string literal). The expression inside `{}` is evaluated and inserted into the string.

**Output:**

```
Ashraful
Hello Ashraful
```

Tip: f-strings are available in Python 3.6+ and are a convenient, readable way to combine text and variables.

---

## 🔢 Integers (whole numbers)

Integers are numbers without decimals.

```python
age = 25
quantity = 3
print(f"You are buying {quantity} houses")
```

**Output:**

```
You are buying 3 houses
```


```python
quantity = 3
print(f"You are buying {quantity} houses")
```

Variable naming rules (short summary):

* Use letters, numbers, and underscores (`_`), but cannot start with a number.
* Use descriptive names (`quantity` better than `q`).
* Avoid typos in names — they are a common source of bugs.

---

## 🔸 Floats (decimal numbers)

Floats are numbers with a decimal point.

```python
price = 19.99
print(price)
```

**Output:**

```
19.99
```

Floats are used when you need fractional values (money, measurements, etc.).

---

## ✅ Booleans (True / False)

Booleans represent truth values.

```python
is_student = True
print(f"Are you a student? {is_student}")
```

**Output:**

```
Are you a student? True
```

Boolean values are `True` or `False` (capitalized). They are useful for conditions and logic (e.g., `if is_student:`).

---

## 🛠 Common mistakes & tips

* **Missing quotes** around strings will cause errors:

  ```python
  name = Ashraful   # ❌ NameError (Ashraful is not defined)
  name = "Ashraful" # ✅
  ```
* **Typo in variable name**: `quanity` vs `quantity` — if you use `quantity` in one place and `quanity` in another, Python treats them as different variables.
* **Spacing and readability**: follow a consistent style (PEP 8). Example:

  ```python
  price = 19.99   # good
  price=19.99     # also valid, but spacing improves readability
  ```
* **Boolean capitalization**: use `True` and `False` (not `true`/`false`).

---

## 🔁 How to run this file locally

If you cloned the repository, run:

```bash
python 01_printing_n_variables.py
```

This runs the program and prints the output in your terminal.

---

## 🔗 View the original Python file on GitHub

[View `01_printing_n_variables.py` on GitHub](../../01_printing_n_variables.py)

---

## 📝 Practice exercises

1. Change the `first_name` variable to your name and print a greeting.
2. Fix the variable typo `quanity` → `quantity` and print a sentence using it.
3. Add a new float variable `tax_rate = 0.05` and calculate a simple tax on `price`:

   ```python
   tax = price * tax_rate
   print(f"Tax: {tax}")
   ```
4. Add a boolean `has_coupon = False` and print a sentence that uses it.

---

⬅️ **[Back to English Overview](index.md)** | ➡️ **[Next: Type Casting](02_typecasting.md)**

```
```
