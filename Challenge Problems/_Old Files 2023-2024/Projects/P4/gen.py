"""
Auxiliary function used to generate conditionals.
"""

norm = []
for i in range(65, 91):
    norm.append(chr(i))
for i in range(97, 123):
    norm.append(chr(i))
for i in range(0, 10):
    norm.append(str(i))
norm.append(' ')
norm.append(',')
norm.append('.')
norm.append('!')
norm.append('?')
norm.append('/')
norm.append('-')
# the code before this comment builds an array of plaintext characters
encr = [x for x in 'WheNtHaTG3oAuzQKxDXsSUnvZC7195ckgIF ,/OqLdBJ!.-0ywbE:l;m862YPMRpVr4?f']
# the indexes in the encrypted array match to that of the plaintext array

#for i in range(len(norm)):
#    print(f"""
#if c == \"{norm[i]}\":
#    a = \"{encr[i]}\"""", end="")
    
for i in range(len(norm)):
    print(f"""
if c == "{encr[i]}":
    a = "{norm[i]}\"""", end="")