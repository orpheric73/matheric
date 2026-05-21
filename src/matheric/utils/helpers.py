def info():
    print("""
    Matheric Lib
    ==================

    Matheric is a modular Python library designed 
    to simplify secure and flexible user input.

    Modules:
    - secure_input  : advanced and safe user input 

    Author : Orphéric
    Version: 0.1.0
    """)

def is_int(n):
    try:
        if(int(n) == n):
            return True
    except ValueError:
        return False
    return False
def is_float(n):
    try:
        float(n) == n
    except ValueError:
        return False
    return True