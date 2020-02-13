from ciphers import Cipher


class RailFence(Cipher):

    def __init__(self):
        pass

    def introduction(self):

        print("The Rail Fence cipher (also know as the Zigzag Cipher) is "
              "a form of transposition cipher. This requires the user to pick"
              " a key 'x' that satisfies the condition  1 < x <= 3.\n")
        RailFence().cipher_choice()
        pass

    def cipher_choice(self):
        pass

    def get_key(self):
        pass

    def encrypt(self):
        pass

    def decrypt(self):
        pass