"""
44-141 Computer Programming
Author: Max Maynor
Date: 11/22
Description: Project for Mod 6
"""


def encrypt():
    #get file names
    fileE = input("Enter file to encrypt:")
    fileOE = input("Enter output file:")
    #open files
    outputFile = open(fileOE,"w")
    encryptFile = open(fileE,"r")
    encrypt = []
    e = ""
    #for loop to encrypt and add to output file
    for line in encryptFile:
        encrypt.extend(line)
        for item in encrypt:
            code = str(ord(item)-encrypt.index(item))
            e += code+"."   
        outputFile.write(e+"\n")
        e = ""
        encrypt.clear()
    print("Encrypted passwords wrote to", fileOE)
    
#Function used to decrypt a file
def decrypt():
    #get file names
    fileD = input("Enter file to decrypt:")
    fileOD = input("Enter output file:")
    #open files
    outputFile = open(fileOD,"w")
    decryptFile = open(fileD,"r")
    decrypt = []
    e = ""
    #for loop to encrypt and add to output file
    for line in decryptFile:
        decrypt= line.split(".")
        for item in decrypt:
            code = chr(int(item)+decrypt.index(item))
            e += code
        outputFile.write(e)
        e = ""
        decrypt.clear()
    print("Decrypted passwords wrote to", fileOD)


#Welcome message
print("Welcome to the password encryption program")
choice = input("Options:\n< e for encryption >\n< d for decryption >\n< q to exit >\n")

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

#close files
fileOE.close()
fileOD.close()
