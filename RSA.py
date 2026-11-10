import random
import math

range_low = pow(10, 14)
range_high = pow(10, 15)

bit_size = 8

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
	binary_text = ""
	for block in blocks:
		ascii_text = convert_to_ascii(block)
		binary_array = convert_ascii_to_binary(ascii_text)
		m = convert_binary_to_decimal(binary_array)
		binary_text += "".join(str(binary_array)) + " "
		ciphered_text += str(pow(m, e, n)) + " "


	if binary_text[-1] == " ":
		binary_text = binary_text[:-1]

	if ciphered_text[-1] == " ":
		ciphered_text = ciphered_text[:-1]

	return ciphered_text, private_key, public_key, binary_text

def decrypt(cipher_text, d, n):
	blocks = get_blocks(cipher_text)

	for block in blocks:
		decrypted_block = decrypt_block(block, d, n)
		binary_text = convert_to_ascii(decrypted_block)


def split_into_blocks(plain_text):
	blocks = []
	index = 0
	count = 0
	new_text = ""
	while index < len(plain_text):
		if count < bit_size:
			new_text += plain_text[index]
			count += 1
			index += 1
		else:
			blocks.append(new_text)
			new_text = ""
			count = 0

	if new_text:
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

	if len(string) != bit_size*bit_size:
		l = bit_size*bit_size - len(string)
		string += "0" * l

	return string

def convert_binary_to_decimal(binary):
	return int(binary, 2) # 2 <- znamena ze text je v bin forme



def convert_binary_to_ascii(binary):
	ascii_values = []

	count = 0
	index = 0
	ascii_text = ""
	while index < len(binary):
		if count < bit_size:
			ascii_text += binary[index]
			count += 1
			index += 1
		else:
			ascii_values.append(ord(ascii_text))
			count = 0

def get_blocks(cipher_text):
	blocks = []

	block_text = ""
	for i in cipher_text:
		if i == " ":
			blocks.append(block_text)
			block_text = ""
		else:
			block_text += i

	if block_text:
		blocks.append(block_text)

	return blocks

def decrypt_block(ciphered_block, d, n):
	return pow(ciphered_block, d, n)

def convert_decimal_to_binary(decimal):
	return format(decimal, 'b')

