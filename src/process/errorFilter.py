from .operations import operations

def errorFilter(userInput):
    try:
        errorCases = ['+', '-', '*', '/', '(', ')', ' ', '', '()', '[]']
        if userInput in errorCases:
            print('ERROR! EXPRESION INGRESADA NO VALIDA')
        if userInput[0] != '(' and userInput[-1] != ')':
            print('ERROR! EXPRESION INGRESADA NO VALIDA')

        operations(userInput)
    except Exception as e:
        print('ERROR! EXPRESION INGRESADA NO VALIDA')