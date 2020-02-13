from ciphers import Cipher


class RailFence(Cipher):

    def __init__(self):
        pass

    def introduction(self):

        print("The Rail Fence cipher (also know as the Zigzag Cipher) is "
              "a form of transposition cipher. \nThis requires the user to pick"
              " a key 'x' that cannot be greater than the length of the "
              "message.\n")
        RailFence().cipher_choice()


    def cipher_choice(self):
        choice = input("What would you like to do?"
                       "\n1. Encrypt a message."
                       "\n2. Decrypt a message."
                       "\n3. Return to Main Menu."
                       "\nEnter a number..."
                       "\n>")
        if choice == '1':
            txt = RailFence().get_txt()
            key = RailFence().get_key(txt)
            RailFence().encrypt(txt, key)
        elif choice == '2':
            txt = RailFence().get_txt()
            key = RailFence().get_key(txt)
            RailFence().decrypt(txt, key)
        elif choice == '3':
            return
        else:
            print("That is not a valid option. Please choose an option "
                  "from the menu below:\n")
            RailFence().cipher_choice()

    def get_txt(self):
        txt = input("What would you like your message to "
                    "be? \n> ").upper().strip()
        txt = txt.replace(" ",'')

        return txt


    def get_key(self, txt):

        invalid_key = True

        while invalid_key:
            key = int(input("Please enter a key value: \n> "))

            if key > len(txt):
                print()




    def encrypt(self, txt, key):
        pass

    def decrypt(self, txt, key):
        pass