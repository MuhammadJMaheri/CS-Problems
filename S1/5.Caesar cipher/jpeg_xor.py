'''XORs a jpeg file'''
file_name = input("enter your file's name, you can also use Sample.jpg:")
enc_key_bytes = int(input("enter encryption key:"))%255
input_file = open(file_name,"rb")
input_bytes = input_file.read()
output = open(file_name.removesuffix(".jpg") + "_XOR.jpg","wb")
for byte in input_bytes:
    output.write((enc_key_bytes^byte).to_bytes(1,"big"))
