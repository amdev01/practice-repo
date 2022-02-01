import base64

# encoding

f_s = open("base64algo/flagb64.txt", "r").read() # get text from file and store it as a string
b_flag = bytes(f_s, "UTF-8") # convert string to bytes[]
print("Base64 encooded once: %s" % base64.b64encode(b_flag)) # print 1st base64 encoding

encoded_flag = base64.b64encode(b_flag) # encode flag for the first time
print("Encoded once")
for k in range(50):
    encoded_flag = base64.b64encode(encoded_flag)
    print("Encoded "+ str(k+1) + " times")
    if (k < 7):
        print(encoded_flag.decode('utf8'))

# create a new file or open existsing one
try: 
    o_encoded50_f = open("base64algo/o_encoded50_f.txt", "x")
except:
    o_encoded50_f = open("base64algo/o_encoded50_f.txt", "w")

o_encoded50_f.write(str(encoded_flag))
o_encoded50_f.close()

# decoding
f_to_decode = open("base64algo/o_encoded50_f.txt")
f_s_decode = f_to_decode.read()
#decoded_flag = bytes(f_s_decode, "UTF-8")

for k in range(50):
    f_s_decode = base64.b64decode(f_s_decode)

#print("Decoded flag: %s " % f_to_decode.decode('utf8'))
print("Decoded flag: %s " % f_s_decode)
    


