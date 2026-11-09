import random
import math

range_low = pow(10, 14)
range_high = pow(10, 15)

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

def encrypt(plain_text):
	p, q = 0, 0
	while p == 0 or q == 0:
		random_number = generate_random_number(range_low, range_high)
		if check_prime(random_number, 40):
			if p == 0:
				p = random_number
			elif random_number != p:
				q = random_number

	n = multiply(p, q)
	phi = euler(p, q)
	e = get_euler_e(phi)
	d = find_inverse(e, phi)

	private_key = (n, d)
	public_key = (n, e)


	blocks = split_into_blocks(plain_text)

	ciphered_text = ""
	for block in blocks:
		ascii_text = convert_to_ascii(block)
		binary_array = convert_ascii_to_binary(ascii_text)
		m = convert_binary_to_decimal(binary_array)
		ciphered_text += str(pow(m, e, n))

	return ciphered_text, private_key, public_key, binary_array

def decrypt(c, d, n):
	return pow(c, d, n)

def split_into_blocks(plain_text):
	blocks = []
	index = 0
	count = 0
	new_text = ""
	while index < len(plain_text):
		if count < 8:
			new_text += plain_text[index]
			count += 1
			index += 1
		else:
			blocks.append(new_text)
			new_text = ""
			count = 0

	if new_text:
		if len(new_text) < 8:
			c = 8 - len(new_text)
			new_text += c * "0"

		blocks.append(new_text)

	return blocks

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
