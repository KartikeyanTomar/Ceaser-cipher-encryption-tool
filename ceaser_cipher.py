def encrypt(text, shift):
    if shift == 26:
        return text[::-1] #i am using this to reverse the string
    
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            result += char
    return result[::-1]

def decrypt(ciphertext, shift):
    # reversed_ciphertext = ciphertext[::-1]
    a=encrypt(ciphertext, -shift)
    return a

def main():
    while True:
        choice = input("Press (e) to Encrypt and (d) to Decrypt or type (quit) to quit the program: ").lower()
        
        if choice == 'exit':
                break

        elif choice == 'e':
            plaintext = input("Enter the message to encrypt: ")
            shift_amount = int(input("Enter the shift amount: "))
            ciphertext = encrypt(plaintext, shift_amount)
            print("Encrypted:", ciphertext)

        elif choice == 'd':
            ciphertext = input("Enter the message to decrypt: ")
            shift_amount = int(input("Enter the shift amount: "))
            decrypted_text = decrypt(ciphertext, shift_amount)
            print("Decrypted:", decrypted_text)

        else:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
