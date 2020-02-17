from ciphers import Cipher


class RailFence(Cipher):

    def __init__(self):
        pass

    def introduction(self):

        print("The Rail Fence cipher (also know as the Zigzag Cipher) is "
              "a form of transposition cipher. \nThis requires the user to pick"
              " a key 'x' that cannot be greater than the length of the "
              "message.\nThe key determines the number of 'rails' in the "
              "\ncipher.")
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
        repeat = False
        while invalid_key:
            key = int(input("Please enter a key value: \n> "))

            if key > len(txt) or key == 1:
                print("Your key cannot be larger than the size "
                      "of your message. Please choose a smaller key.")
                repeat = True
            if repeat:
                repeat = False
            else:
                invalid_key = False
        return key



    def encrypt(self, txt, key):

        txt = txt.replace(" ", "")
        result = ""
        increment = 1
        row = 0
        col = 0

        # Create an array of lists
        rails = [["" for i in range(len(txt))] for j in range(key)]

        # place characters in array of lists
        for x in txt:
            if row + increment < 0 or row + increment >= len(rails):
                increment = increment * -1

            rails[row][col] = x

            row += increment
            col += 1

        for rail in rails:
            result += "".join(rail)

        print(result)

    def decrypt(self, txt, key):

        result = ""
        indx = 0
        increment = 1

        rails = [["" for i in range(len(txt))] for j in range(key)]

        for selectedRow in range(0, len(rails)):
            row = 0

            for col in range(0, len(rails[row])):
                if row + increment < 0 or row + increment >= len(rails):
                    increment = increment * -1

                if row == selectedRow:
                    rails[row][col] += txt[indx]
                    indx += 1
                row += increment

        rails = self.transpose(rails)

        for rail in rails:
            result += "".join(rail)
        print(result)

    def transpose(self, m):

        result = [[0 for y in range(len(m))] for x in range(len(m[0]))]

        for i in range(len(m)):
            for j in range(len(m[0])):
                result[j][i] = m[i][j]

        return result