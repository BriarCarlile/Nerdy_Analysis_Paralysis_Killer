


def higher_target(value, maximum, minimum):
    return (value - minimum) / (maximum - minimum)

def lower_target(value, maximum, minimum):
    return (maximum - value) / (maximum - minimum)