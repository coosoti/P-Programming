def maximum(*args):
    """
    Find the maximum value out of a variable number of arguments.
    """
    if len(args) == 0:
        # if no arguments are given, return None
        return None
    else:
        # initialize the maximum value to the first argument
        max_value = args[0]
        # loop over the rest of the arguments and update the maximum value
        for arg in args[1:]:
            if arg > max_value:
                max_value = arg
        return max_value

print(maximum(8, -99, 8, 6, 99))

