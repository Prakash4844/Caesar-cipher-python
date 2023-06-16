import Art

print(Art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_Continue = True

while should_Continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caeser(input_text, shift_amount, algo_direction):
        if shift_amount > 26:
            shift_amount %= 26
        output_text = ""
        is_invalid = False
        for letters in input_text:
            if letters not in alphabet:
                output_text += letters
            else:
                new_index = alphabet.index(letters)
                if algo_direction == "encode":
                    output_text += str(alphabet[new_index + shift_amount])
                elif algo_direction == "decode":
                    output_text += str(alphabet[new_index - shift_amount])
                else:
                    print("Invalid Input")
                    is_invalid = True
                    break
        if is_invalid:
            pass
        else:
            print(f"The {direction}d text is {output_text}")


    caeser(input_text=text, shift_amount=shift, algo_direction=direction)

    should_restart = int(input("Restart Cipher Program? type 1 to continue and 0 to quit: "))

    if should_restart == 1:
        should_Continue = True
    else:
        should_Continue = False
        print("Goodbye!")


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the
#  shift amount and print the encrypted text. e.g. plain_text = "hello" shift = 5 cipher_text = "mjqqt"
#  print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'? Fixed!🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and
#  encrypt a message.


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the
#  shift amount and print the decrypted text. e.g. cipher_text = "mjqqt" shift = 5 plain_text = "hello"
#  print output: "The decoded text is hello"

# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#  Then call the correct function based on that 'direction' variable. You should be able to test the code to
#  encrypt *AND* decrypt a message

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# TODO-3: What happens if the user enters a number/symbol/space?
#   Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#    e.g. start_text = "meet me at 3"
#   end_text = "•••• •• •• 3"

# TODO-1: Import and print the logo from art.py when the program starts.

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#   e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#   If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#   Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.


# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet? Try
#  running the program and entering a shift number of 45. Add some code so that the program continues to
#  work even if the user enters a shift number greater than 26. Hint: Think about how you can use the
#  modulus (%).
