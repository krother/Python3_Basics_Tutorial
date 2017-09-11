

class StringAdder(object):
    """
    Can concatenate parameters.
    """
    def __init__(self):
        """Constructor defining an empty string."""
        self.result = ""

    def add(self, value):
        """Converts value to string and adds it."""
        self.result += str(value)


if __name__ == '__main__':
    """
    Python convention for main code block.
    (looks strange, but the Java expression

    public static void main (String argv[]) {}

    ... looks a little weird for such a siple thing, too :-)
    """
    adder = StringAdder()
    adder.add(3)
    adder.add(4)
    print(adder.result)

