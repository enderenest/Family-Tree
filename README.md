# 🌳 Family Tree Relationships in Python

## 📝 Project Overview

This project is a Python implementation to analyze family tree relationships represented as a tree structure using nested lists.

---

## 🏛️ Key Features

Tree Representation: Family members are organized hierarchically using a list-based tree structure.

Relationships Identified:

Parent of a person.

Siblings, Brothers, Sisters.

Uncles, Aunts.

Cousins.

Supports Case Sensitivity: Lowercase letters represent males, uppercase represent females.

---

## 🛠️ Key Functions

parent(tree, name) – Finds the parent of name.

brothers(tree, name) – Finds the brothers of name.

sisters(tree, name) – Finds the sisters of name.

siblings(tree, name) – Finds all siblings of name.

uncles(tree, name) – Finds the uncles of name.

aunts(tree, name) – Finds the aunts of name.

cousins(tree, name) – Finds the cousins of name.

---

## ▶️ How to Run

from family_tree import parent, brothers, sisters, uncles, aunts, cousins

family_tree = ['A', ['b', ['c'], ['D']], ['e', ['F']]]
print("Parent of 'c':", parent(family_tree, 'c'))
print("Brothers of 'c':", brothers(family_tree, 'c'))
print("Sisters of 'c':", sisters(family_tree, 'c'))
print("Uncles of 'c':", uncles(family_tree, 'c'))

---

## 📤 Sample Output

Parent of 'c': b
Brothers of 'c': []
Sisters of 'c': ['D']
Uncles of 'c': ['e']

---

## 🧑‍💻 Dependencies

Python 3.x

---

## 📫 Contact

Feel free to reach out for questions or contributions!
