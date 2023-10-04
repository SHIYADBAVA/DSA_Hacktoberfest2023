import random

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find modular inverse using Extended Euclidean Algorithm
def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x1, y1 = gcd_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)

# Function to generate RSA key pair
def generate_rsa_keys(bits):
    # Generate two distinct prime numbers
    p, q = random_prime(bits), random_prime(bits)

    # Calculate modulus (n) and totient (phi)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose public exponent (e)
    e = 65537  # Commonly used public exponent

    # Calculate private exponent (d)
    _, d, _ = gcd_extended(e, phi)
    d = d % phi

    # Public key: (e, n), Private key: (d, n)
    return ((e, n), (d, n))

# Function to encrypt a message using RSA
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message using RSA
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Function to generate a random prime number of given bits
def random_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Example usage
bits = 2048  # Number of bits for the key length
public_key, private_key = generate_rsa_keys(bits)
message = "Hello, RSA!"

# Encryption
encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

# Decryption
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
