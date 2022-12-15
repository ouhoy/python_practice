fruit = "banana"

counter = 0
if "a" in fruit:
    counter += 1
    print("Found")

print(counter)

stuff = "Hello, world!!"

my_file = open("./my_text.txt", "r")
inp = my_file.read()

for li in inp:
    print(li)
print("read function: ", len(inp))
