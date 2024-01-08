from ecdsa import SECP256k1, numbertheory
import hashlib

curve = SECP256k1
n = curve.order

def recover_private_key(r, s1, s2, z1, z2, k):
    r = int(r, 16)
    k = int(k, 16)

    # Calculate the inverse of r and k
    r_inv = numbertheory.inverse_mod(r, n)
    k_inv = numbertheory.inverse_mod(k, n)

    # Prepare to try both s1 and -s1 mod n, and s2 and -s2 mod n
    s_candidates = [s1, (n - s1) % n, s2, (n - s2) % n]

    # Try all combinations of s1 and s2 (including their negations)
    for s1_candidate in s_candidates[:2]:
        for s2_candidate in s_candidates[2:]:
            # Calculate the private key candidate
            d_candidate = (r_inv * (s1_candidate * k - z1)) % n
            # Verify the candidate by checking the public key
            if verify_private_key(d_candidate):
                return d_candidate  # Return the private key if it's valid

    return None  # Return None if no valid private key was found

def verify_private_key(private_key):
    # Generate the public key from the private key and compare it to the given one
    from ecdsa import SigningKey
    sk = SigningKey.from_secret_exponent(private_key, curve=SECP256k1)
    public_key_derived = sk.get_verifying_key().to_string("compressed")
    return public_key_derived == given_public_key

# Given values (hexadecimal strings)
k_hex = "616d617a6f6e"
r = "CE81B7F00779D7C548447E6124E1D7DDCECE0FE9DA982FA96E1FC5AB2A8CB67E"
s1 = int("133D52F0E4987D9B41B8BC8B341A3956811CF5EBA744D9A34F5B7F906B2A3FC2", 16)
s2 = int("256E1934C4E4539E5BD2879BAB1307E69162A611795D3A7F968E90C1D74E2866", 16)
z1 = int("F537B28432BDC92F289FA8291EA1E443C906A3CD11D7BE5377D994900B268406", 16)
z2 = int("E75B7A2C885D438E9E17535639D147D6DC09AB3F0866D1B7D5ED6CC0C063BF9E", 16)
given_public_key = binascii.unhexlify("03750583297BC97A12D04741A1AE974D0EC95880EC6396C784461DED6E045CBF9E")

# Attempt to recover the private key
private_key = recover_private_key(r, s1, s2, z1, z2, k_hex)
if private_key:
    print("Recovered private key:", format(private_key, '064x'))
else:
    print("Failed to recover the private key.")
