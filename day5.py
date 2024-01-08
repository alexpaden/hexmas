from ecdsa import SECP256k1, VerifyingKey
import binascii

# Initialize the curve globally as it's used across multiple functions
curve = SECP256k1

def compute_point_for_choice_1(box_point_hex, scalar_hex):
    box_point_bytes = binascii.unhexlify(box_point_hex)
    scalar_bytes = binascii.unhexlify(scalar_hex)

    your_scalar = int.from_bytes(scalar_bytes, 'big')
    your_point = your_scalar * curve.generator

    box_verifying_key = VerifyingKey.from_string(box_point_bytes, curve=curve)
    box_point = box_verifying_key.pubkey.point

    point_for_choice_1 = your_point + box_point
    point_for_choice_1_hex = binascii.hexlify(VerifyingKey.from_public_point(point_for_choice_1, curve=curve).to_string("compressed"))

    return point_for_choice_1_hex

def generate_your_key(box_point_hex, scalar_hex):
    box_point_bytes = binascii.unhexlify(box_point_hex)
    your_scalar = int(scalar_hex, 16)

    box_verifying_key = VerifyingKey.from_string(box_point_bytes, curve=curve)
    box_point = box_verifying_key.pubkey.point

    your_key_point = your_scalar * box_point
    your_key_hex = binascii.hexlify(VerifyingKey.from_public_point(your_key_point, curve=curve).to_string("compressed"))

    return your_key_hex

def xor_hex_strings(hex_str1, hex_str2):
    bytes_str1 = binascii.unhexlify(hex_str1)
    bytes_str2 = binascii.unhexlify(hex_str2)

    xor_result = bytes(a ^ b for a, b in zip(bytes_str1, bytes_str2))
    return binascii.hexlify(xor_result).decode()

# Input data
point_from_box = "027e74e89dff93105654ad4b7339f3d0e6e22fe368e04543e820bc5c0e73294a3d"
your_scalar = "8aedf236663c160916df7d6caad94d7a83271fa4d86cb55780d7827f6ba68018"
scrambled_message = "4131b0cb29bbb91ec672d498c1f5d1dd530443517c8070bd817c8d10ad0bcf597a"

# Compute the point for choice 1
point_for_choice_1 = compute_point_for_choice_1(point_from_box, your_scalar)
print("Send this compressed point for choice 1:", point_for_choice_1)

# Generate your key
your_key = generate_your_key(point_from_box, your_scalar)
print("Your key (scalar multiplied by the box point):", your_key)

# Unscramble the message
unscrambled_message = xor_hex_strings(your_key, scrambled_message)
print("Unscrambled message:", unscrambled_message)
