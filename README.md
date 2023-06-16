# Caesar cipher in python
The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to 
his allies. It works by shifting the letters in the plaintext message by a certain number of positions, 
known as the “shift” or “key”.

# Screenshots

#### Encode
![Screenshot](Screenshots/Encode)

#### Decode
![Screenshot](Screenshots/Decode)

# Working 

The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique. It’s simply a
type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of 
positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so
on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his 
officials

Thus, to cipher a given text we need an integer value, known as a shift which indicates the number of 
positions each letter of the text has been moved down. 

The encryption can be represented using modular arithmetic by first transforming the letters into numbers, 
according to the scheme, A = 0, B = 1,…, Z = 25. Encryption of a letter by a shift n can be described 
mathematically as. 

For example, if the shift is 3, then the letter A would be replaced by the letter D, B would become E, C would
become F, and so on. The alphabet is wrapped around so that after Z, it starts back at A.

Here is an example of how to use the Caesar cipher to encrypt the message “HELLO” with a shift of 3:

1. Write down the plaintext message: HELLO
2. Choose a shift value. In this case, we will use a shift of 3.
3. Replace each letter in the plaintext message with the letter that is three positions to the right in the 
alphabet.

```
         H becomes K (shift 3 from H)

         E becomes H (shift 3 from E)

         L becomes O (shift 3 from L)

         L becomes O (shift 3 from L)

         O becomes R (shift 3 from O)
```
4. The encrypted message is now “KHOOR”.

To decrypt the message, you simply need to shift each letter back by the same number of positions. In this 
case, you would shift each letter in “KHOOR” back by 3 positions to get the original message, “HELLO”.
