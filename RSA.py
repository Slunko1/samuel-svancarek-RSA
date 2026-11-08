import random

def generate_random_number():
    return random.randrange(pow(10, 25), pow(10, 30))

def check_prime(random_number, k):
    if random_number == 2:
        return True

    if random_number < 0:
        return False

    n = random_number - 1

    count = 0
    while n % 2 == 0:
        n = n // 2
        count += 1

    d = n
    s = count

    for i in range(k):
        # 2 <= x <= num
        a = random.randrange(2, random_number - 1)

        x = pow(a, d, random_number)

        if x == 1 or x == random_number - 1:
            continue

        for j in range(s - 1):
            x = pow(x, 2, random_number)

            if x == random_number - 1:
                break
        else:
            return False
    return True


a = generate_random_number()
print(a)
print(check_prime(a, 40))