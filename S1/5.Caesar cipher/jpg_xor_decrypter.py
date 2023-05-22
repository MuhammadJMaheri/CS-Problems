'''determines the key using magic bytes and decrypts XORed jpg files'''
file_name = input("enter your file's name, you can also use Sample_XOR.jpg:")
input_file = open(file_name,"rb")
input_bytes = input_file.read()
enc_key = input_bytes[0]^255
print("enc key is:",enc_key)
output_name = file_name.removesuffix(".jpg") + "decrypted.jpg"
output = open(output_name,"wb")
for byte in input_bytes:
    output.write((enc_key^byte).to_bytes(1,"big"))
print(output_name,"generated")
