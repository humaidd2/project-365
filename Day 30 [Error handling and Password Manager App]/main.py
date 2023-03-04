# FileNotFound

# try:
#     file = open("a_file.txt")
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# else:
#     content = file.readline()
#     print(content)
# finally:
#     file.close()
#     print("file closed")

height = float(input("Height: "))
weight = float(input("weight: "))

if height > 30:
    raise ValueError("Height too much")

bmi = weight / height ** 2
print(bmi)