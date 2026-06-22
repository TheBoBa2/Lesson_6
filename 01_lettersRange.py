import string

a, b = input().split('-')

alphabet = string.ascii_letters

start = alphabet.index(a)
end = alphabet.index(b)

print(alphabet[start:end + 1])
