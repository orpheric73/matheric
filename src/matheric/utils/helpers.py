def info():
    print("""
    ╔══════════════════════════════════╗
                MATHERIC LIB
    ╚══════════════════════════════════╝

    Matheric is a modular Python library designed 
    to simplify secure and flexible console input.

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    AVAILABLE MODULES

    • secureinput
        Advanced and safe user input handling

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          
    Features :
          
        - Automatic type validation
        - Min/Max value control
        - String length verification
        - Input confirmation system
    
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    Github :  
        https://github.com/orpheric73/matheric
          
    Author  : Orphéric
    Version : 0.1.1
    License : MIT
    
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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