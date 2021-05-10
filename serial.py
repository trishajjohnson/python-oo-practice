"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create a new serial number generator with given start number."""
        
        self.start = self.next = start

    def __repr__(self):
        """Makes a more clear representation of instance serial number generator."""
        
        return f"<SerialGenerator start = {self.start} next = {self.next}>"

    def generate(self):
        """returns next serial number"""

        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Resets serial number back to original start number."""

        self.next = self.start

