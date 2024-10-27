import math
from secrets import randbelow


class CLEAR_Keys_V1():
    def __init__(self):
        '''Initialises an empty key'''
        self.key = []

    def create_key(self):
        '''Empties the key first,
        then generates a random key containing five elements
        belonging to the range [10, 99]'''
        self.key = []
        for i in range(5):
            self.key.append(randbelow(10**2-10) + 10)

    def enc_poly_1(self, data):
        '''A hexavariable quadratic expression,
        with the key as five variables,
        and the character unicode as the sixth variable,
        is used to encrypt the character'''
        x1, x2, x3, x4, x5 = self.key
        x6 = data
        resultant = x1**2 + x2**2 + x3**2 - (x4**2) - (x5**2) + x6**2 + x1*x4*x6 - (x2*x3*x6) + x1*x2*x4*x5
        return resultant

    def enc_poly_2(self, data):
        '''Another hexavariable quadratic expression,
        encrypts the same character
        into a different value'''
        x1, x2, x3, x4, x5 = self.key
        x6 = data
        resultant = - (x1**2) - (x2**2) + x3**2 + x4**2 - (x5**2) - (x6**2) - (x1*x3*x6) - (x1*x2*x5) + x1*x3*x4*x6
        return resultant

    def dec_poly_1(self, resultant):
        '''A decryption expression is used
        to reverse the encryption
        using the key and encrypted value.
        A tuple of two values is obtained'''
        x1, x2, x3, x4, x5 = self.key
        Z = resultant
        b = x1*x4 - (x2*x3)
        c = x1**2 + x2**2 + x3**2 - (x4**2) - (x5**2) + x1*x2*x4*x5 - Z
        x6 = (- b + math.sqrt(b**2 - (4*c)))/2, (- b - math.sqrt(b**2 - (4*c)))/2
        return x6

    def dec_poly_2(self, resultant):
        '''Another decryption expression is used
        to obtain another tuple'''
        x1, x2, x3, x4, x5 = self.key
        Z = resultant
        b = x1*x3*x4 - (x1*x3)
        c = - (x1**2) - (x2**2) + x3**2 + x4**2 - (x5**2) - (x1*x2*x5) - Z
        x6 = (- b + math.sqrt(b**2 + (4*c)))/(-2), (- b - math.sqrt(b**2 + (4*c)))/(-2)
        return x6

    def encrypt(self, char):
        '''Converts the character to its Unicode value
        and then encrypts using
        the two different expressions.
        Returns a tuple of two encrypted values'''
        code = ord(char)
        enc_codes = (self.enc_poly_1(code), self.enc_poly_2(code))
        return enc_codes

    def decrypt(self, enc_codes):
        '''Decrypts the encrypted values
        using the two different expressions.
        Checks for the common value between
        the two decrypted tuples,
        and returns the character'''
        dec_tuple_1, dec_tuple_2 = (self.dec_poly_1(enc_codes[0]), self.dec_poly_2(enc_codes[1]))
        for val in dec_tuple_1:
            if val == int(dec_tuple_2[0]) or val == int(dec_tuple_2[1]):
                return chr(int(val))


# Sample Code to show the usage of CLEAR_Keys_V1
char = "A"
if __name__ == "__main__":
    ck = CLEAR_Keys_V1()
    ck.create_key()
    enc_codes = ck.encrypt(char)
    decrypted_char = ck.decrypt(enc_codes)
    print(f"Original Character: {char}")
    print(f"Encrypted Codes: {enc_codes}")
    print(f"Decrypted Character: {decrypted_char}")
