def calculator(expression):

    try:
        result = eval(expression)
        return result
    except:
        return "Error in calculation"