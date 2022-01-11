import os

starterTemplate = "print('Enter your operation.')\nop = input('> ')\nparsed = op.split(' ')\nnum1 = int(parsed[0])\nnum2 = int(parsed[2])\noperator = parsed[1]\n\n"

def cls():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def IfStatement(conditions, runIfTrue): 
    current = "if "
    for i, condition in enumerate(conditions):
        current += condition
        try: 
            if conditions[i+1] != None:
                current += " and "
        except IndexError:
            pass
            
    current += ":\n    "        
    current += runIfTrue
    return current
        

    
    