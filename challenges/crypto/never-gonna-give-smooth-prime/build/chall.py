from Crypto.Util.number import getStrongPrime, bytes_to_long
from Crypto.Util.Padding import pad
from secret import flag

print("Never gonna give smooth prime~")

assert len(flag) < 77

x = bytes_to_long(pad(flag, 256))

# p = 2 p0 - 1
# Never gonna give smooth prime
p = getStrongPrime(1024)
g = 2
y = pow(g, x, p)

print(f"{p = }")
print(f"{g = }")
print(f"{y = }")
