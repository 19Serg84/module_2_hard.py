def generate_password(n):
    password = ""

    # Перебираем все возможные числа от 1 до 20 для формирования пар
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j

            if n % pair_sum == 0:
                password += f"{i}{j}"

    return password


# Пример использования функции
for n in range(3, 21):
    result = generate_password(n)
    print(f"{n} - {result}")