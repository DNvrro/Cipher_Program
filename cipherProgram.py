#!/usr/bin/env python3
import os

from affineCipher import Affine
from railFenceCipher import RailFence


def clear_screen():
    """clears screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def quit_program():
    """This quits the application"""

    print("Thank you for your time. Goodbye.")
    exit()


def greeting():
    print("\nWelcome to the Bishop-Navarro Cipher Program!")


def main_menu():
    """
    The main menu of the program that essentially handles the calling
    of the ciphers
    """
    while True:

        print("\nSelect a cipher to learn more about it:")

        cipher_choice = input(
            "1. Affine Cipher"
            "\n2. Rail Fence Cipher"
            "\n3. Quit Program"
            "\nEnter a number..."
            "\n>")
        clear_screen()
        if cipher_choice == '1':
            choice = Affine()
            choice.introduction()
        elif cipher_choice == '2':
            choice = RailFence()
            choice.introduction()
        elif cipher_choice == '3':
            quit_program()
        else:
            print("I'm sorry that is not a valid choice.\nPlease choose"
                  "an option from the menu:")
            clear_screen()
            main_menu()


if __name__ == "__main__":
    greeting()
    main_menu()
