import base64
import codecs


x = "63 6q 6p 75 5n 32 52 68 62 47 6p 75 5n 79 42 69 5n 57 78 73 49 48 4r 76 64 57 35 6o 63 77 3q 3q"
x_list = list(x)
ascii = [ord(v) if v for v in x_list]
print(ascii)

for y in range(10):
    print([z >> y for z in ascii])