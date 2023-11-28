"""
44-141 Computer Programming
Author: Max Maynor
Date: 11/22
Description: Project for Mod 6
"""


def encrypt():
    #get file names
    fileE = input("Enter file to encrypt:")
    fileOE = input("Enter output file (Will create file if not created):")
    try:
        with open(fileE, "r") as encryptFile, open(fileE, "w") as outputFile:
            #for loop to encrypt and add to output file
            for line in encryptFile:
                encrypt = []
                for item in encrypt:
                    code = str(ord(item)-encrypt.index(item))
                    encrypt.append(code)
                e = ".".join(encrypt)
                outputFile.write(e+"\n")
        print("Encrypted passwords wrote to", fileOE)
    except FileNotFoundError: 
        print("File not found, Try again.")
    except Exception as e:
        print("Error, try again")
    
#Function used to decrypt a file
def decrypt():
    #get file names
    fileD = input("Enter file to decrypt:")
    fileOD = input("Enter output file:")
    #open files
    try:
        with open(fileD, "r") as decryptFile, open(fileOD, "w") as outputFile:
            #for loop to decrypt and add to output file
            for line in decryptFile:
                decrypt = line.split(".")
                for item in decrypt:
                    code = chr(int(item)+decrypt.index(item))
                    outputFile.write(code)
        print("Decrypted passwords wrote to", fileOD)
    except FileNotFoundError:
        print("File not found, Try again")
    except Exception as e:
        print("Error, try again")


#Welcome message
print("Welcome to the password encryption program\nUse this program to encrypt and decrypt your text files!")
choice = input("Options:\n< e for encryption >\n< d for decryption >\n< q to exit >\n").lower()

#While loop for choice
while(choice!="q"):
    #encrypt choice
    if(choice == "e"):
        encrypt()
    #decrypt choice
    elif(choice == "d"):
        decrypt()
    #invalid choice
    else:
        print("Invalid input")
        
    choice = input("Options:\n< e for encryption >\n< d for decryption >\n< q to exit >\n")

#final message
print("Thank you for using our program!")
