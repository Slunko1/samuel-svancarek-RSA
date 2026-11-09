import random
import math

def generate_random_number(a, b):
	return random.randrange(a, b)

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

def multiply(p, q):
	return p * q

def over_gcd(n, i):
	return math.gcd(n, i) == 1

def euler(n):
	count = 0

	for i in range(1, n + 1):
		if not over_gcd(n, i):
			count += 1

	while True:
		e = generate_random_number(1, count)

		if over_gcd(e, count):
			return e, count

def find_inverse(e, euler_n):
	for d in range(1, euler_n):
		if (e * d) % euler_n == 1:
			return d

	return None

def encrypt(m, e, n):
	return pow(m, e, n)

def decrypt(c, d, n):
	return pow(c, d, n)

p = generate_random_number(pow(10, 20), pow(10, 30))
q = generate_random_number(pow(10, 20), pow(10, 30))
print(p)
print(check_prime(p, 40))
print(q)
print(check_prime(q, 40))

print(euler(1000))