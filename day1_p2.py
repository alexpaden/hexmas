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
    [5, 124228412], [6, 275018904]#, [7, 905751694], [8, 1595122963],
    #[9, 1719647061], [10, 1751923029]
]

# trad 6 needed version
#ids_and_magic_numbers = [[1, 1667996414], [2, 639855478], [3, 37761658], [4, 353287111], [5, 1137893104], [6, 198907410], [7, 1385436292], [8, 899440017], [9, 1524095781], [10, 1082356870]]

# new 5 needed version
#ids_and_magic_numbers = [[1, 1409279932], [2, 1373157670], [3, 438442932], [4, 46265733], [5, 731633114]]#, [6, 2123429142], [7, 796931263], [8, 1011228537], [9, 1824319756], [10, 1388080738]]

# only 1 needed version
#ids_and_magic_numbers = [[1, 347040376]]#, [2, 347040376]]#, [3, 347040376], [4, 347040376], [5, 347040376], [6, 347040376], [7, 347040376], [8, 347040376], [9, 347040376], [10, 347040376]]

# only 0? needed version // doesn't work
ids_and_magic_numbers = [[1,0]]#[[1, 347040376], [2, 347040376], [3, 347040376], [4, 347040376], [5, 347040376], [6, 347040376], [7, 347040376], [8, 347040376], [9, 347040376], [10, 347040376]]


modulus = 2147483647

# Extract IDs and magic numbers
x_values = [pair[0] for pair in ids_and_magic_numbers]
y_values = [pair[1] for pair in ids_and_magic_numbers]

# Run the interpolation to find the secret
secret_number = compute_lagrange_interpolation(x_values, y_values, modulus)
print("The secret number is:", secret_number)
