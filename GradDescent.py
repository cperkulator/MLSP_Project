from ShortTermEnergy import ShortTermEnergy


def cost(data, n, x, expected):
    predicted = ShortTermEnergy.CountWords(data, x)

    return (expected-predicted)


def gradient_descent(data, previous_x, learning_rate, expected, iterations=100,
                     precision=0.0001):
    for i in range(iterations):
        current_x = previous_x - learning_rate * \
            cost(data, 1, previous_x, expected)

        if abs(previous_x - current_x) <= precision:
            break

        previous_x = current_x

    return current_x
