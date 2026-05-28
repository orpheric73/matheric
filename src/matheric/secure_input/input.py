def secureinput(msg = "",   type = "string",    max = "NotDefined",    min = "NotDefined",   str_length = "Any",    str_max = "NotDefined",    str_min = "NotDefined",   except_msg = "Type ERROR",    validation = False,    validation_msg = "Enter 1 to confirm the input",   validation_caractere = "1",    language = "EN"):
    """
    Improve safety in input by auto-verification of specified parameter without error.

    msg
        Can be used to define the message that will be print before asking for input.
        The default is nothing.
    type
        Can be used to specified the type of data that must be input.

        POSSIBLE VALUES :
        - "string" 
        - "int" 
        - "float"

        The default is string.
    max
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
    validation
        Can be used to do a input validation at end
        
        POSSIBLE VALUES :
        - True
        - False

        The default is False.
    validation_msg
        Can be used to modify the validation sentence.
        The default is : "Enter 1 to confirm the input"
        ONLY IF VALIDATE IS TRUE
    validation_caractere
        Can be used to set the caracter that will be used to validation the input.
        The default value is 1
        ONLY IF VALIDATE IS TRUE
    language
        Can be used to set output language used for the automatic responses
        
        POSSIBLE VALUES :
        - EN
        - FR

        The default is EN.

                            ALL PARAMETER ARE OPTIONOUS
                secureinput act like simple input when no parameter is setted

    """
    
    # PARAMETER VALIDATION
    # Parameter type checking

    if(type != "string" and type != "int" and type != "float"):
        raise ValueError(f"Expected 'string' or 'int' or 'float' for type but '{type}'")

    # Parameter max checking

    if (max == "NotDefined"):
        max = "ND"
    else:
        try:
            max = int(max)
        except ValueError:
            raise TypeError(f"Expected int value for the parameter max but '{max}'")

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
        except TypeError:
            raise TypeError(f"Expected int value for the parameter str_min but '{str_min}'")
        if (str_min < 0):
            raise ValueError(f"Expected positive value for the parameter str_min but '{str_min}'")
    
    # Language checking

    if(language != "EN" and language != "FR"):
        raise ValueError(f"Expected 'EN' or 'FR' for language but '{language}'")

    # String logic checking

    if ((max != "ND" or min != "ND") and type == "string"):
        raise SyntaxError("The parameters max or min can not be used with 'string'. Set type to int or float")
    if(str_length != "ND" and (str_max != "ND" or str_min != "ND")):
        raise SyntaxError("The parameter str_length should not be used with another string parameter")

    if ((str_length != "ND" or str_min != "ND" or str_max != "ND") and (type == "int" or type == "float")):
        raise SyntaxError("The string parameter can not be used with 'int' or 'float' value")
    
    if(str_min != "ND" and str_max != "ND"):
        if(str_min > str_max):
            raise ValueError(f"The parameter 'str_max' should be high than 'str_min' but {str_min} > {str_max}")
    
    if(min != "ND" and max != "ND"):
        if(min > max):
            raise ValueError(f"The parameter 'max' should be high than 'min' but {min} > {max}")

    if validation:
        validation_caractere = str(validation_caractere)
        if(validation_caractere != "1" and validation_msg == "Enter 1 to confirm the input"):
            raise ValueError("The parameter 'validation_msg' must be changed when 'validation_caractere' is modified")
    else:
        if(validation_msg != "Enter 1 to confirm the input" or validation_caractere != "1"):
            raise SyntaxError("Validation protocol must be activated (with validation = True) before setting validation parameter")
    
    # Input according to type

    if (type == "string"):
        if(validation_caractere != "0"):
            C = "0"
        else:
            C = "1"
        while (C != validation_caractere):
            while True:
                value = input(msg)
                if(str_length == "ND" and str_max == "ND" and str_min == "ND"):
                    break
                else:
                    if (str_length != "ND"):
                        if (len(value) == str_length):
                            break
                        else:
                            if language == "EN":
                                print(f"The string must contains {str_length} caracteres")
                            else:
                                print(f"La chaine doit contenir {str_length} caractêres")
                    else:
                        if(str_min != "ND" and str_max != "ND"):
                            if (len(value) >= str_min and len(value) <= str_max):
                                break
                            else:
                                if language == "EN":
                                    print(f"The string length must be between {str_min} and {str_max}")
                                else:
                                    print(f"La longueur de la chaine doit être comprise entre {str_min} et {str_max}")
                        elif(str_max != "ND" and str_min == "ND"):
                            if (len(value) <= str_max):
                                break
                            else:
                                if language == "EN":
                                    print(f"The string length must be less than or equal to {str_max}")
                                else:
                                    print(f"La longueur de la chaine doit être inférieure ou égale á {str_max}")
                        elif(str_min != "ND" and str_max == "ND"):
                            if (len(value) >= str_min):
                                break
                            else:
                                if language == "EN":
                                    print(f"The string length must be greater than or equal to {str_min}")
                                else:
                                    print(f"La longueur de la chaine doit être supérieure ou égale á {str_max}")
            if validation :
                C = input(validation_msg)
            else :
                C = validation_caractere
        return value
    elif (type == "int"):
        if(validation_caractere != "0"):
            C = "0"
        else:
            C = "1"
        while (C != validation_caractere):
            while True:
                try:
                    value = int(input(msg))
                except ValueError:
                    print(except_msg)
                    continue
                if(max == "ND" and min == "ND"):
                    break
                else:
                    if(min != "ND" and max != "ND"):
                        if (value >= min and value <= max):
                            break
                        else:
                            if language == "EN":
                                print(f"The number must be between {min} and {max}")
                            else:
                                print(f"La longueur de la chaine doit être comprise entre {min} et {max}")
                    elif(max != "ND" and min == "ND"):
                        if (value <= max):
                            break
                        else:
                            if language == "EN":
                                print(f"The number must be less than or equal to {max}")
                            else:
                                print(f"Le nombre doit être inférieure ou égale á {max}")
                    elif(min != "ND" and max == "ND"):
                        if (value >= min):
                            break
                        else:
                            if language == "EN":
                                print(f"The number must be greater than or equal to {min}")
                            else:
                                print(f"Le nombre doit être supérieure ou égale á {min}")
            if validation :
                C = input(validation_msg)
            else:
                C = validation_caractere
        return value
    elif(type == "float"):
        if(validation_caractere != "0"):
            C = "0"
        else:
            C = "1"
        while (C != validation_caractere):
            while True:
                try:
                    value = float(input(msg))
                except ValueError:
                    print(except_msg)
                    continue
                if(max == "ND" and min == "ND"):
                    break
                else:
                    if(min != "ND" and max != "ND"):
                        if (value >= min and value <= max):
                            break
                        else:
                            if language == "EN":
                                print(f"The number must be between {min} and {max}")
                            else:
                                print(f"La longueur de la chaine doit être comprise entre {min} et {max}")
                    elif(max != "ND" and min == "ND"):
                        if (value <= max):
                            break
                        else:
                            if language == "EN":
                                print(f"The number must be less than or equal to {max}")
                            else:
                                print(f"Le nombre doit être inférieure ou égale á {max}")
                    elif(min != "ND" and max == "ND"):
                        if (value >= min):
                            break
                        else:
                            if language == "EN":
                                print(f"The number must be greater than or equal to {min}")
                            else:
                                print(f"Le nombre doit être supérieure ou égale á {min}")
            if validation :
                C = input(validation_msg)
            else:
                C = validation_caractere
        return value