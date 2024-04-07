def operations(userInput):
    try:
        result = eval(userInput)
        print(result)
    except Exception as e:
        print(e)


