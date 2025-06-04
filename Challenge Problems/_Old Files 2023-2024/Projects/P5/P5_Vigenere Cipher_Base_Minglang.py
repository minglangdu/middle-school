orig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,?!'-"
# list of ciphers to encrypt the code
ciphers = [
       "86Y?2OP9,AG1ZV5SN7M'JEBTIHCX.KW0FQ- DU!34LR",
       "J5E!MWNOPQF24?7,ZYUX9G6K381 HLRI0T'DCBV-AS.",
       "5QZKBDG' AP-802UW.3!EH7VI,JC9RLX?TN61FOY4MS",
       "L?XUEDTRBQNJHS2!1.F6 MC3IZ4Y5K'AVP0O-978W,G",
       "PBCRNH!JW3M17Q0US2KTOL'EA4.XV, 9D6-IF8GY5Z?"
]

# return the encoded string by looping through
# ciphers and characters in the string
def encode(string):
    newstr = ""
    for i in range(len(string)):
        idx = -1
        for j in range(len(orig)):
            if (orig[j] == string[i]):
                idx = j
                break
        newstr += ciphers[i % len(ciphers)][idx]
    return newstr

# return the decrypted string by looping through
# ciphers instead of the original alphabet
def decode(string):
    newstr = ""
    for i in range(len(string)):
        idx = -1
        ciph = ciphers[i % len(ciphers)]
        for j in range(len(ciph)):
            if (ciph[j] == string[i]):
                idx = j
                break
        newstr += orig[idx]
    return newstr
# output

def output(string):
    string = string.upper()
    print("Original String:", string, end="\n\n")
    print("Encrypted String:", encode(string), end="\n\n")
    print("Decrypted String:", decode(encode(string)), end="\n\n")
    print("-" * 70)

print("""_Project #5: Vigènere Cipher_\n""")
print("-" * 70, "\n")
output("Look at a stone cutter hammering away at his rock, perhaps a hundred times without as much as a crack showing in it. Yet at the hundred-and-first blow it will split in two, and I know it was not the last blow that did it, but all that had gone before. -- Jacob Riis")
output("SPHINX OF BLACK QUARTZ, JUDGE MY VOW! Waxy and quivering, jocks fumble the pizza. Is it the job of the wizard to vex the chumps quickly in fog?")
output("ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.!?'- ")

while 1:
    string = input("Input the string to encode: ")
    string = string.upper()
    if (string == "QUIT"):
        break
    output(string)