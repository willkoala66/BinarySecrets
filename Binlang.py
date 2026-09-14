import enums
import string

class Binlang:
    class character:
        binform: str 
        intform: int 
        charform: str 
        def __init__(self, charform: str, intform: int, binform: str):
            self.binform = binform
            self.charform = charform
            self.intform = intform
    
    class chars(enums.Enum):
        lowercase_a = character("a", 1, "1000000000000000")
        uppercase_A = character("A", 63, "1000000010000000")
        lowercase_b = character("b", 2, "0100000000000000")
        uppercase_B = character("B", 64, "0100000010000000")
        lowercase_c = character("c", 3, "1100000000000000")
        uppercase_C = character("C", 65, "1100000010000000")
        lowercase_d = character("d", 4, "0010000000000000")
        uppercase_D = character("D", 66, "0010000010000000")
        lowercase_e = character("e", 5, "1010000000000000")
        uppercase_E = character("E", 67, "1010000010000000s")