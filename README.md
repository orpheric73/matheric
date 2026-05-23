# Matheric

A modular Python library designed to simplify secure and flexible user input.  

Matheric provides advanced console input utilities with built-in validation, retry systems, type checking and optional confirmation protocols.

## ✅ Features

- Secure and validated user input
- Automatic retry on invalid input
- Built-in type verification
- Integer and float range control
- String length validation
- Optional input confirmation system
- Custom exception messages
- Modular architecture

## 📦 Installation

```bash
Bash

pip install matheric
```

## 💡 Quick Example

```Python
Python

from matheric import secureinput

age = secureinput(
    "Enter your age: ",
    type="int",
    min=0,
    except_msg = Please enter a valid age
)

print(age)
```

### Supported Types

Matheric currently supports:

- "string"
- "int"
- "float"

### String Validation

```Python
Python

name = secureinput(
    "Enter your name : ",
    type="string",
    str_min=3,
    str_max=20
)
```

The **msg** can be ommitted if it is placed first

### Integer Validation

```Python
Python

number = secureinput(
    "Enter a number : ",
    type="int",
    min=1,
    max=10
)
```

### Float Validation

```Python
Python

price = secureinput(
    msg="Enter the price : ",
    type="float",
    min=0
)
```

### Input Confirmation System

```Python
Python

password = secureinput(
    msg="Enter password : ",
    type="string",
    validation=True
)
```

The validation system allows the user to confirm the entered value before final submission.

## ⚙️ Parameters

| Parameter | type | Description | Default Value |
| --- | --- | --- | --- |
| `msg` | `string` | Message displayed before input | "" |
| `type` | `string / int / float` | Expected input type (`string`, `int`, `float`) | string |
| `max` | `int / float` | Maximum allowed numeric value | NotDefined |
| `min` | `int / float` | Minimum allowed numeric value | NotDefined |
| `str_length` | `int` | Exact required string length | Any |
| `str_max` | `int` | Maximum allowed string length | NotDefined |
| `str_min` | `int` | Minimum allowed string length | NotDefined |
| `except_msg` | `string` | Message displayed on invalid input | type ERROR |
| `validation` | `bool` | Enables validation protocol | False |
| `validation_msg` | `string` | Validation confirmation message | Enter 1 to confirm the input |
| `validation_caractere` | `string / int / float` | Value required to validation input | 1 |

## 💡 Example With Validation

```Python
Python

from matheric import secureinput

code = secureinput(
    msg="Enter access code : ",
    type="string",
    str_length=6,
    validation=True,
    validation_msg="Confirm the code [y/N] "
    validation_caractere="y"
)
```

## Project Structure

```text
matheric/
│
├── pyproject.toml
├── README.md
├── LICENSE
│
└── src/
    └── matheric/
        ├── __init__.py
        │
        ├── secure_input/
        │   ├── __init__.py
        │   └── input.py
        │
        └── utils/
            ├── __init__.py
            └── helpers.py
```

## 🖥️ Command Line

After installation:

```bash
Bash

matheric
```

Displays general information about the library.

## 📜 License

This project is licensed under the [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 👨‍💻 Author

Orphéric SANGNIDJO
