'''XORs a jpg file/any file with a key'''
file_name = input("enter your file's name, you can also use Sample.jpg:")
enc_key_bytes = int(input("enter encryption key:"))%255
input_file = open(file_name,"rb")
input_bytes = input_file.read()
output_name = file_name.removesuffix(".jpg") + "[XORed with key" + str(enc_key_bytes) + "].jpg"
output = open(output_name,"wb")
for byte in input_bytes:
    output.write((enc_key_bytes^byte).to_bytes(1,"big"))
print(output_name,"generated")
