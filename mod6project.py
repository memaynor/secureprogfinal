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
        with open(fileE, "r") as encryptFile:
            with open(fileOE, "w") as outputFile: 
                #for loop to encrypt and add to output file
                for line in encryptFile:
                    encrypt = []
                    for item in line:
                        code = str(ord(item)-line.index(item))
                        encrypt.append(code)
                    e = ".".join(encrypt)
                    outputFile.write(e+"\n")
            print("Encrypted passwords wrote to", fileOE)
    except FileNotFoundError: 
        print("Input file not found, try again.")
    except Exception as e:
        print("Error, try again")

#Function used to decrypt a file
def decrypt():
    #get file names
    fileD = input("Enter file to decrypt:")
    fileOD = input("Enter output file:")
    #open files
    try:
        with open(fileD, "r") as decryptFile:
            with open(fileOD, "w") as outputFile:
                #for loop to decrypt and add to output file
                for line in decryptFile:
                    decrypt = line.split(".")
                    for item in line:
                        code = chr(int(item)+decrypt.index(item))
                        outputFile.write(code)
            print("Decrypted passwords wrote to", fileOD)
    except FileNotFoundError:
        print("Input file not found, try again")
    except ValueError:
        print("File is not encrypted, try again")
    except Exception as e:
        print("Error: try again")

if __name__ == "__main__":
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
            
        choice = input("Options:\n< e for encryption >\n< d for decryption >\n< q to exit >\n").lower()

    #final message
    print("Thank you for using our program!")
