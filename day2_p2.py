import random


def generate_shares(secret, k, n, mod):
    """
    Generate 'n' shares for a secret, where any 'k' shares can be used to reconstruct the secret.

    :param secret: The secret number to be shared.
    :param k: The minimum number of shares required to reconstruct the secret.
    :param n: The total number of shares to generate.
    :param mod: The modulus for the computation.
    :return: A list of shares in the format [elf ID, magic number].
    """
    # Random coefficients for the polynomial, with a_0 as the secret
    coefficients = [secret] + [random.randint(0, mod - 1) for _ in range(k - 1)]

    # Function to evaluate the polynomial at a given x
    def poly(x):
        return sum(coeff * (x ** i) for i, coeff in enumerate(coefficients)) % mod

    # Generating the shares
    shares = [[i + 1, poly(i + 1)] for i in range(n)]
    return shares


# Input parameters
secret_number = 347040376
modulus = 2147483647
num_shares = 10
# min_shares_to_reconstruct = 5
min_shares_to_reconstruct = 5
min_shares_to_reconstruct = 1
#min_shares_to_reconstruct = 0


# Generate the shares
generated_shares = generate_shares(secret_number, min_shares_to_reconstruct, num_shares, modulus)
print(generated_shares)
