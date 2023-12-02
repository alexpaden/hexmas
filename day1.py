def compute_lagrange_interpolation(x_values, y_values, mod):
    """
    Compute Lagrange Interpolation at a specific point (here x=0) to reconstruct the secret.
    :param x_values: List of x-coordinates (IDs).
    :param y_values: List of y-coordinates (magic numbers).
    :param mod: The modulus for the computation.
    :return: The secret number obtained by interpolation.
    """
    secret = 0
    n = len(x_values)
    for i in range(n):
        # Start with the y-value for this iteration
        term = y_values[i]

        # Calculate the Lagrange basis polynomial for the i-th term
        for j in range(n):
            if i != j:
                # (x - x_values[j]) / (x_values[i] - x_values[j])
                # Since we're evaluating at x=0, this simplifies to -x_values[j] / (x_values[i] - x_values[j])
                term *= -x_values[j] * pow(x_values[i] - x_values[j], -1, mod)
                term %= mod

        secret += term
        secret %= mod

    return secret


# Using the provided input data
ids_and_magic_numbers = [
    [1, 1686753191], [2, 90544604], [3, 589632252], [4, 1521719331],
    [5, 124228412], [6, 275018904], [7, 905751694], [8, 1595122963],
    [9, 1719647061], [10, 1751923029]
]
modulus = 2147483647

# Extract IDs and magic numbers
x_values = [pair[0] for pair in ids_and_magic_numbers]
y_values = [pair[1] for pair in ids_and_magic_numbers]

# Run the interpolation to find the secret
secret_number = compute_lagrange_interpolation(x_values, y_values, modulus)
print("The secret number is:", secret_number)
