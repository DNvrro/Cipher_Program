import string
from ciphers import Cipher


class Affine(Cipher):

    def __init__(self):
        self.letters = string.ascii_uppercase

        # creates a dict assigning each letter of the alphabet a numeric value
        # from 0 - 25
        # Example {'A' : 0, 'B' : 1, ... .etc
        self.letter_keys = {key: value for key, value in zip(self.letters,
                                                             range(26))}

    def introduction(self):
        """
        This function gives the user a brief introduction of the cipher
        and then calls the cipher_choice function
        """
        print("This is the Affine Cipher. It is a mono-alphabetic cipher that "
              "requires you to provide TWO keys (alpha & beta). \nPlease "
              "make sure that your alpha key has a Greatest Common Divisor"
              " (GCD) of 1 with the number 26.\n")
        Affine().cipher_choice()

    def cipher_choice(self):
        """
        This function prompts the user to choose an action  to do w/ the
        the Affine cipher or to return to the main menu
        """
        choice = input("What would you like to do?"
                       "\n1. Encrypt a message."
                       "\n2. Decrypt a message."
                       "\n3. Return to Main Menu."
                       "\nEnter a number..."
                       "\n>")
        if choice == '1':
            alpha = Affine().get_alpha()
            beta = Affine().get_beta()
            while Affine().get_txt() != False:
                txt = Affine().get_txt()
            Affine().encrypt(alpha, beta, txt)
        elif choice == '2':
            alpha = Affine().get_alpha()
            beta = Affine().get_beta()
            txt = Affine().get_txt()
            Affine().decrypt(alpha, beta, txt)
        elif choice == '3':
            return
        else:
            print("That is not a valid option. Please choose an option "
                  "from the menu below:")
            Affine().cipher_choice()

    def get_alpha(self):
        """
        This function checks that the alpha the user chooses is within the
        usable alphas for the size m = 26. It then returns alpha once it
        has met said criteria
        """

        usable_alphas = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

        alpha = int(input("Please choose an appropriate alpha value: \n> "))

        while alpha not in usable_alphas:
            print('That is not a valid alpha. Please choose one '
                  'from the list below: '
                  '\n3, 5, 7, 9, 11, 15, 17, 19, 21, 23')

            alpha = int(input("\n> "))
        return alpha

    def get_beta(self):
        """
        This checks that the user has inputted a beta value w/in the range of
        0 - 25 and returns beta once it has met said criteria
        """
        usable_betas = [i for i in range(26)]

        beta = int(input("Please choose a beta value from 0 - 25: \n> "))

        while beta not in usable_betas:
            print("That is not a valid beta value. Please choose a value from"
                  " 0-25: ")

            beta = int(input("> "))
        return beta

    def get_txt(self):
        """
        This checks that the user's message only contains letters from A - Z
        If the user has entered a message containing any numbers or special
        characters, the user is asked to reenter the message
        """
        valid_txt = False


        while not valid_txt:
            txt = input("What would you like your message to "
                        "be?\n> ").upper().strip()

            for x in txt:
                if x not in self.letters:
                    print("Please make sure your message contains no integers"
                          " or special characters...")
                    Affine().get_txt()

            valid_txt = True
        return txt

    def encrypt(self, alpha, beta, txt):
        """
        Encrypts a string given user supplied values
        for alpha and beta. The encryption follows the
        Affine cipher formula (alpha * x + beta)mod 26. 65 is added to
        the final number to convert the hexadecimal number to base 10
        so the real number can be used to get the corresponding letter

        """

        encrypted_txt = []
        for letter in txt:
            if letter in self.letter_keys.keys():
                (encrypted_txt.append(chr((self.letter_keys[letter]
                                           * alpha + beta) % 26 + 65)))
            else:
                encrypted_txt.append(letter)
        print("Your encrypted message is: \n")
        print("".join(encrypted_txt))

    def decrypt(self, alpha, beta, txt):
        """
        Decrypts a string given user supplied values for alpha & beta.
        the decryption follows the formula alpha^-1*(x - beta)mod 26. 65 is
        added to the final value to obtain the integer base of 10 since the
        values are done via hexadecimal operations
        """

        alpha_inverse = Affine().mod_inverse(alpha)

        decrypted_txt = []

        for letter in txt:
            if letter in self.letter_keys.keys():
                (decrypted_txt.append(chr(((self.letter_keys[letter]
                                            - beta) * alpha_inverse)
                                          % 26 + 65)))
            else:
                decrypted_txt.append(letter)
        print("Your decrypted message is:\n")
        print("".join(decrypted_txt))

    # This function calculates the multiplicative inverse for alpha
    def mod_inverse(self, alpha, m=26):
        a = alpha % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x


