import enum
import string
import re

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
        lowercase_t = character("t", 20, "001010000")
        uppercase_T = character("T", 82, "001010001")
        lowercase_u = character("u", 21, "101010000")
        uppercase_U = character("U", 83, "101010001")
        lowercase_v = character("v" ,22, "011010000")
        uppercase_V = character("V", 84, "011010001")
        lowercase_w = character("w", 23, "111010000")
        uppercase_W = character("W", 85, "111010001")
        lowercase_x = character("x", 24, "000110000")
        uppercase_X = character("X", 86, "000110001")
        lowercase_y = character("y", 25, "100110000")
        uppercase_Y = character("Y", 87, "100110001")
        lowercase_z = character("z", 26, "010110000")
        uppercase_Z = character("Z", 88, "010110001")
        newline = character("\n", 27, "110110000")
        tab = character("\n", 28, "001110000")
        whitespace = character(" ", 29, "101110000")
        period = character(".", 30, "011110000")
        comma = character(",", 31, "111110000")
        forward_slash = character("/", 32, "000001000")
        semicolon = character(";", 33, "100001000")
        colon = character(":", 34, "010001000")
        apostrophy = character("\'", 35, "110001000")
        at = character("@", 36, "001001000")
        question_mark = character("?", 37, "101001000")
        more_than = character(">", 38, "011001000")
        less_than = character("<", 39, "111001000")
        open_curly_brace = character("{", 40, "000101000")
        close_curly_brace = character("}", 41, "100101000")
        open_square_bracket = character("[", 42, "010101000")
        close_square_bracket = character("]", 43, "110101000")
        hashtag = character("#", 44, "001101000")
        tilde = character("~", 45, "101101000")
        pipe = character("|", 46, "011101000")
        back_slash = character("\\", 47, "111101000")
        backtick = character("`", 48, "000011000")
        logical_not = character("¬", 49, "100011000")
        equals = character("=", 50, "010011000")
        plus = character("+", 51, "110011000")
        minus = character("-", 52, "001011000")
        underscore = character("_", 53, "101011000")
        exclamation = character("!", 54, "011011000")
        quote_marks = character("\"", 55, "111011000")
        GBP_sterling_pound_symbol = character("£", 56, "000111000")
        percent_symbol = character("%", 57, "100111000")
        exponent = character("^", 58, "010111000")
        ampersand = character("&", 59, "110111000")
        asterisk = character("*", 60, "001111000")
        close_bracket = character(")", 61, "101111000")
        open_bracket = character("(", 62, "011111000")
        dollar_sign = character("$", 89, "110110001")
        euro_sign = character("€", 90, "001110001")
        # number_1 = character("1", 91, "110110100")
        # number_2 = character("2", 92, "001110100")
        # number_3 = character("3", 93, "101110100")
        # number_4 = character("4", 94, "011110100")
        # number_5 = character("5", 95, "111110100")
        # number_6 = character("6", 96, "000001100")
        # number_7 = character("7", 97, "100001100")
        # number_8 = character("8", 98, "010001100")
        # number_9 = character("9", 99, "110001100")
        # number_0 = character("0", 100, "001001100")
        # numbers as is due to 1's and 0's


    def encode(self, mesg: str):
        nospace = mesg.replace(self.chars.whitespace.value.charform, f"{self.chars.whitespace.value.binform} ")
        a = nospace
        for i in self.chars:
            a.replace()
        return a
    def decode(self, mesg:str):
        nospace = re.sub(self.chars.whitespace.value.binform + " ", f"{self.chars.whitespace.value.charform}", mesg)
        a = nospace
        for i in self.chars:
            try:
                a = re.sub(f"{i.value.binform} ", f"{i.value.charform}", a)
            except re.PatternError:
                pass
        return a



# access example
#for i in Binlang.chars:
#    print(i.value.charform)
a = Binlang()
b = input("Mesg: ")
print(f"Mesg out: {a.encode(b)}")
print(f"decode: {a.decode(a.encode(b))}")