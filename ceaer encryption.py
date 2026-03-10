text = input("Enter message: ")
shift = int(input("Enter shift number: "))

result = ""

for char in text:
    if char.isalpha():
        new_char = chr((ord(char) + shift - 97) % 26 + 97)
        result += new_char
    else:
        result += char

print("Encrypted message:", result)




 
            
            
            
            
            
            