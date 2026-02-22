
---

# 📘 Assignment 5 – Python Tasks

This repository contains solutions for **Assignment 5**, which includes two Python tasks demonstrating dictionary usage and list operations.

---

## 📝 Task 1: Student Marks Lookup

### 🔹 Description

This program stores student names and their marks in a dictionary.
It prompts the user to enter a student's name and displays the corresponding marks if the student exists in the dictionary.
If the student is not found, it prints an appropriate message.

### 🔹 Code

```python
Student = {'Alice': 89, 'john': 79, 'Amar': 45, 'Ram': 90, 'Afzal': 66}

name = input("Enter the Student's name:")

if name in Student:
    print(f"{name}'s marks: {Student[name]}")
else:
    print('Student not found.')
```

### 🔹 How It Works

* A dictionary named `Student` stores student names as keys and marks as values.
* The program checks whether the entered name exists in the dictionary.
* If found, it prints the marks.
* Otherwise, it displays `"Student not found."`

### 🔹 Example Output

```
Enter the Student's name: Ram
Ram's marks: 90
```

---

## 📝 Task 2: List Creation and Manipulation

### 🔹 Description

This program:

1. Creates a list of numbers from 1 to 10.
2. Extracts the first five elements.
3. Reverses the extracted elements.
4. Displays all results.

### 🔹 Code

```python
numlist = []

for i in range(1, 11):
    numlist.append(i)

print(f"Original list: {numlist}")

extracted_list = numlist[0:5]
print(f"Extracted first five elements: {extracted_list}")

extracted_list.reverse()
print("Reversed extracted elements:", extracted_list)
```

### 🔹 How It Works

* A loop generates numbers from 1 to 10 and stores them in `numlist`.
* Slicing (`numlist[0:5]`) extracts the first five elements.
* The `.reverse()` method reverses the extracted list.
* All results are printed to the console.

### 🔹 Example Output

```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
```

---

## 🚀 Requirements

* Python 3.x

---

## ▶️ How to Run

1. Save the code in a Python file (e.g., `assignment5.py`).
2. Open a terminal or command prompt.
3. Run the program using:

```
python assignment5.py
```

---

## 📌 Concepts Used

* Dictionaries
* Conditional Statements (`if-else`)
* Lists
* For Loops
* List Slicing
* List Methods (`reverse()`)

---


