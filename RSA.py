import random
import math

def generate_random_number(a, b):
	return random.randrange(a, b)

def check_prime(random_number, k):
	if random_number < 2:
		return False

	if random_number == 2:
		return True

	if random_number % 2 == 0:
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

def euler(p, q):
	return (p - 1) * (q - 1)

def get_euler_e(phi):
	while True:
		e = generate_random_number(2, phi)

		if over_gcd(e, phi):
			return e

def find_inverse(e, euler_n):
	return pow(e, -1, euler_n)

def encrypt(m, e, n):
	return pow(m, e, n)

def decrypt(c, d, n):
	return pow(c, d, n)

def convert_to_ascii(string):
	ascii_values = []
	for char in range(len(string)):
		ascii_values.append(ord(string[char]))

	return ascii_values

def convert_ascii_to_binary(ascii_values):
	string = ""
	for value in ascii_values:
		binary = format(value, '08b')
		string += binary

	return string

def convert_binary_to_decimal(binary):
	return int(binary, 2) # 2 <- znamena ze text je v bin forme
