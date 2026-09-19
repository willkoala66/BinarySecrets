import enum
import string

class character:
        binform: str 
        intform: int 
        charform: str 
        def __init__(self, charform: str, intform: int, binform: str):
            self.binform = binform
            self.charform = charform
            self.intform = intform


class Binlang:
    
    class chars(enum.Enum):
        # append the last 7 bits to the binform later
        lowercase_a = character("a", 1, "100000000")
        uppercase_A = character("A", 63, "100000001")
        lowercase_b = character("b", 2, "010000000")
        uppercase_B = character("B", 64, "010000001")
        lowercase_c = character("c", 3, "110000000")
        uppercase_C = character("C", 65, "110000001")
        lowercase_d = character("d", 4, "001000000")
        uppercase_D = character("D", 66, "001000001")
        lowercase_e = character("e", 5, "101000000")
        uppercase_E = character("E", 67, "101000001")
        lowercase_f = character("f",  6, "011000000")
        uppercase_F = character("F", 68, "011000001")
        lowercase_g = character("g", 7, "111000000")
        uppercase_G = character("G", 69, "111000001")
        lowercase_h = character("h", 8, "000100000")
        uppercase_H = character("H", 70, "000100001")
        lowercase_i = character("i", 9, "100100000")
        uppercsae_I = character("I", 71, "100100001")
        lowercase_j = character("j", 10, "010100000")
        uppercase_J = character("J", 72, "010100001")
        lowercase_k = character("k", 11, "110100000")
        uppercase_K = character("K", 73, "110100001")
        lowercase_l = character("l", 12, "001100000")
        uppercase_L = character("L", 74, "001100001")
        lowercase_m = character("m", 13, "101100000")
        uppercase_M = character("M", 75, "101100001")
        lowercase_n = character("n", 14, "011100000")
        uppercase_N = character("N", 76, "011100001")
        lowercase_o = character("o", 15, "111100000")
        uppercase_O = character("O", 77, "111100001")
        lowercase_p = character("p", 16, "000010000")
        uppercase_P = character("P", 78, "000010001")
        lowercase_q = character("q", 17, "100010000")
        uppercase_Q = character("Q", 79, "100010001")
        lowercase_r = character("r", 18, "010010000")
        uppercase_R = character("R", 80, "010010001")
        lowercase_s = character("s", 19, "110010000")
        uppercase_S = character("S", 81, "110010001")