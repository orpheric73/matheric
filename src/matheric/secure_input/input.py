from ..utils.helpers import is_int, is_float
def secureinput(msg = "",   Type = "string",    Max = "NotDefined",    min = "NotDefined",   str_length = "Any",    str_max = "NotDefined",    str_min = "NotDefined",   except_msg = "Type ERROR",    validate = False,    validate_msg = "Enter 1 to confirm the input",   validation_caractere = 1,   validation_caractere_type = "int",   validate_except_msg = "Must be an integer"):
    
    # Help section

    """
    Improve safety in input by auto-verification of specified parameter without error.

    msg
        Can be used to define the message that will be print before asking for input.
        The default is nothing.
    Type
        Can be used to specified the type of data that must be input.

        POSSIBLE VALUES :
        - "string" 
        - "int" 
        - "float"

        The default is string.
    Max
        Can be used to define the maximum value that can be input.
        The default is "NotDefined".
        ONLY FOR "int" or "float"
    min
        Can be used to define the minimum value that can be input.
        The default is "NotDefined".
        ONLY FOR "int" or "float"
    str_length
        Can be used to define the string length.
        The default is "Any".
        ONLY FOR "string"
    str_max
        Can be used to define the max length of the string.
        The default is "NotDefined".
        ONLY FOR "string" and can not be used with str_length
    str_min
        Can be used to define the min length of the string.
        The default is "NotDefined".
        ONLY FOR "string" and can not be used with str_length
    except_msg
        Can be used to modify the printed sentence in case of except.
        The default is "Type ERROR"
    validate
        Can be used to do a input validation at end
        
        POSSIBLE VALUES :
        - True
        - False

        The default is False.
    validate_msg
        Can be used to modify the validation sentence.
        The default is : "Enter 1 to confirm the input"
        ONLY IF VALIDATE IS TRUE
    validate_caractere
        Can be used to set the caracter that will be used to validate the input.
        The default value is 1
        ONLY IF VALIDATE IS TRUE
    validate_caractere_type
        Can be used to set the caracter that will be used to validate the input.

        POSSIBLE VALUES :
        - "string" 
        - "int" 
        - "float"

        The default value is 1
        ONLY IF VALIDATE IS TRUE
    validate_except_msg
        Can be used to modify the printed sentence in case of except(for validation)
        The default is "Must be an integer"
        ONLY IF VALIDATE IS TRUE

                            ALL PARAMETER IS OPTIONOUS
                secureinput act like simple input when no parameter is setted

    """
    
    # PARAMETER VALIDATION
    # Parameter Type checking

    if(Type != "string" and Type != "int" and Type != "float"):
        raise ValueError(f"Expected 'string' or 'int' or 'float' for Type but '{Type}'")

    # Parameter Max checking

    if (Max == "NotDefined"):
        Max = "ND"
    else:
        try:
            Max = int(Max)
        except ValueError:
            raise TypeError(f"Expected int value for the parameter Max but '{Max}'")

    # Parameter min checking

    if (min == "NotDefined"):
        min = "ND"
    else:
        try:
            min = int(min)
        except ValueError:
            raise TypeError(f"Expected int value for the parameter min but '{min}'")
   
    # Parameter str_length checking

    if (str_length == "Any"):
        str_length = "ND"
    else:
        try:
            str_length = int(str_length)
        except ValueError:
            raise TypeError(f"Expected int value for str_length but '{str_length}'")
        if (str_length <= 0):
            raise ValueError(f"Expected positive value for str_length but '{str_length}'")
        
    # Parameter str_max checking

    if (str_max == "NotDefined"):
        str_max = "ND"
    else:
        try:
            str_max = int(str_max)
        except ValueError:
            raise TypeError(f"Expected int value for the parameter str_max but '{str_max}'")
        if (str_max <= 0):
            raise ValueError(f"Expected positive value for the parameter str_max but '{str_max}'")
        
    # Parameter str_min checking

    if (str_min == "NotDefined"):
        str_min = "ND"
    else:
        try:
            str_min = int(str_min)
        except ValueError:
            raise TypeError(f"Expected int value for the parameter str_min but '{str_min}'")
        if (str_min < 0):
            raise ValueError(f"Expected positive value for the parameter str_min but '{str_min}'")
    
    # Parameter validation_caractere_type checking

    if(validation_caractere_type != "string" and validation_caractere_type != "int" and validation_caractere_type != "float"):
        raise ValueError(f"Expected 'string' or 'int' or 'float' for validation_caractere_type but '{validation_caractere_type}'")
    
    # String logic checking

    if ((Max != "ND" or min != "ND") and Type == "string"):
        raise SyntaxError("The parameters Max or min can not be used with 'string'. Set Type to int or float")
    if(str_length != "ND" and (str_max != "ND" or str_min != "ND")):
        raise SyntaxError("The parameter str_length should not be used with another string parameter")

    if ((str_length != "ND" or str_min != "ND" or str_max != "ND") and (Type == "int" or Type == "float")):
        raise SyntaxError("The string parameter can not be used with 'int' or 'float' value")
    
    if(str_min != "ND" and str_max != "ND"):
        if(str_min > str_max):
            raise ValueError(f"The parameter 'str_max' should be high than 'str_min' but {str_min} > {str_max}")
    
    if(min != "ND" and Max != "ND"):
        if(min > Max):
            raise ValueError(f"The parameter 'Max' should be high than 'min' but {min} > {Max}")

    if validate:
        if(validate_msg != "Enter 1 to confirm the input" or validation_caractere != 1 or validation_caractere_type != "int" or validate_except_msg == "Must be an integer"):
            if(validation_caractere != 1 and validate_msg == "Enter 1 to confirm the input"):
                raise ValueError("The parameter 'validation_msg' must be changed when 'validation_caractere' is modified")
            elif(validation_caractere_type != "int" and (validate_except_msg == "Must be an integer" or validate_msg == "Enter 1 to confirm the input" or validation_caractere == 1)):
                raise ValueError("The parameter 'validate_except_msg', 'validate_msg' and 'validation_caractere' must be changed when 'validation_caractere_type' is modified")
    else:
        if(validate_msg != "Enter 1 to confirm the input" or validation_caractere != 1 or validation_caractere_type != "int" or validate_except_msg != "Must be an integer"):
            raise SyntaxError("Validation protocol must be activated (with validate = True) before setting validate parameter")
    

    if(validation_caractere_type == "int"):
        if(is_int(validation_caractere) == False):
            raise TypeError(f"The 'validation_caractere_type' must be compatible to 'validation_caractere'. Expect an integer but '{validation_caractere}'")
    elif(validation_caractere_type == "float"):
        if(is_float(validation_caractere) == False):
            raise TypeError(f"The 'validation_caractere_type' must be compatible to 'validation_caractere'. Expect a float but '{validation_caractere}'")

    # Input according to Type

    if (Type == "string"):
        while True:
            if(validation_caractere != 0):
                C = 0
            else:
                C = 1
            while (C != validation_caractere):
                value = input(msg)
                if validate :
                    C = secureinput(msg = validate_msg, Type = validation_caractere_type, except_msg = validate_except_msg)
                else:
                    C = validation_caractere
            if(str_length == "ND" and str_max == "ND" and str_min == "ND"):
                return value
            else:
                if (str_length != "ND"):
                    if (len(value) == str_length):
                        return value
                    else:
                        print(f"The string must contains {str_length} caracteres")
                else:
                    if(str_min != "ND" and str_max != "ND"):
                        if (len(value) >= str_min and len(value) <= str_max):
                            return value
                        else:
                            print(f"The input length must be between {str_min} and {str_max}")
                    elif(str_max != "ND" and str_min == "ND"):
                        if (len(value) <= str_max):
                            return value
                        else:
                            print(f"The input length must be equal or less than {str_max}")
                    elif(str_min != "ND" and str_max == "ND"):
                        if (len(value) >= str_min):
                            return value
                        else:
                            print(f"The input length must be at least {str_min}")
    elif (Type == "int"):
        while True:
            if(validation_caractere != 0):
                C = 0
            else:
                C = 1
            while (C != validation_caractere):
                try:
                    value = int(input(msg))
                except ValueError:
                    print(except_msg)
                    continue
                if validate :
                    C = secureinput(msg = validate_msg, Type = validation_caractere_type, except_msg = validate_except_msg)
                else:
                    C = validation_caractere
            if(Max == "ND" and min == "ND"):
                return value
            else:
                if(min != "ND" and Max != "ND"):
                    if (value >= min and value <= Max):
                        return value
                    else:
                        print(f"The number must be between {min} and {Max}")
                elif(Max != "ND" and min == "ND"):
                    if (value <= Max):
                        return value
                    else:
                        print(f"The number must be equal or less than {Max}")
                elif(min != "ND" and Max == "ND"):
                    if (value >= min):
                        return value
                    else:
                        print(f"The number must be equal or more than {min}")
    elif(Type == "float"):
        while True:
            if(validation_caractere != 0):
                C = 0
            else:
                C = 1
            while (C != validation_caractere):
                try:
                    value = float(input(msg))
                except ValueError:
                    print(except_msg)
                    continue
                if validate :
                    C = secureinput(msg = validate_msg, Type = validation_caractere_type, except_msg = validate_except_msg)
                else:
                    C = validation_caractere
            if(Max == "ND" and min == "ND"):
                return value
            else:
                if(min != "ND" and Max != "ND"):
                    if (value >= min and value <= Max):
                        return value
                    else:
                        print(f"The number must be between {min} and {Max}")
                elif(Max != "ND" and min == "ND"):
                    if (value <= Max):
                        return value
                    else:
                        print(f"The number must be equal or less than {Max}")
                elif(min != "ND" and Max == "ND"):
                    if (value >= min):
                        return value
                    else:
                        print(f"The number must be equal or more than {min}")