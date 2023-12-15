message = 12
exponent = 65537
p = 17
q = 23

modulus = p * q 

decrypt = pow(message, exponent, modulus)
print(decrypt)