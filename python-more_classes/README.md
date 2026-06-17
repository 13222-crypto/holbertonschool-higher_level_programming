# Python - More Classes and Objects

This project dives deeper into Object-Oriented Programming (OOP) in Python 3. It covers class methods, static methods, class vs. instance attributes, and special methods like `__str__`, `__repr__`, and `__del__`.

## Requirements

* **OS/Environment:** Ubuntu 20.04 LTS interpreted with `python3` (version 3.8.5).
* **Style Guide:** Code strictly follows `pycodestyle` (version 2.7.*).
* **Executables:** All Python scripts must be executable (`chmod +x`).
* **Documentation:** Mandatory full docstrings for every module, class, and method.

## Tasks Summary

| Task | File | Description |
| --- | --- | --- |
| **0. Simple rectangle** | `0-rectangle.py` | Defines an empty class `Rectangle` with basic structural documentation. |
| **1. Real definition of a rectangle** | `1-rectangle.py` | Implements private `width` and `height` attributes with property getters and setters. |
| **2. Area and Perimeter** | `2-rectangle.py` | Adds public instance methods `area` and `perimeter` to perform geometric calculations. |
| **3. String representation** | `3-rectangle.py` | Implements the `__str__` magic method to print the rectangle visually using `#`. |
| **4. Eval is magic** | `4-rectangle.py` | Implements the `__repr__` magic method to recreate instances using `eval()`. |
| **5. Detect instance deletion** | `5-rectangle.py` | Overloads the `__del__` destructor method to handle and announce instance deletion. |
| **6. How many instances** | `6-rectangle.py` | Uses a class attribute `number_of_instances` to dynamically track active objects. |
| **7. Change representation** | `7-rectangle.py` | Introduces a customizable `print_symbol` class attribute for flexible rendering. |
| **8. Compare rectangles** | `8-rectangle.py` | Employs a `@staticmethod` to compare two rectangle objects based on area values. |
| **9. A square is a rectangle** | `9-rectangle.py` | Implements a `@classmethod` factor method to generate square-proportioned instances. |
