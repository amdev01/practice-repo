import base64
import sys
import os

usage = """\
Usage: base64task.py "<file_to_encode>" [-hc] <n>
  file_to_encode        - <required> path to the file to encode
  n                     - <optional> number of times to encode file
  -c/--count n          - <required> if in multi encode mode, <file_to_encode> will be encoded <n> number of times\
"""

def encode_test(p_flag):
    print("Test Base64 encooded once: %s" % base64.b64encode(p_flag)) # print 1st base64 encoding

def encode(file, encode_count):
    # encoding
    f_s = open(file, "r").read() # get text from file and store it as a string
    #b_flag = bytes(f_s, "UTF-8") # convert string to bytes[]
    encoded_flag = base64.b64encode(f_s) # encode flag for the first time
    print("Encoded once")
    if (encode_count > 1):
        for k in range(encode_count):
            encoded_flag = base64.b64encode(encoded_flag)
            print("Encoded "+ str(k+1) + " times")
            if (k < 7):
              print(encoded_flag.decode('utf8'))
    # create a new file or open existsing one
    try: # try create a new file
        o_encoded50_f = open("o_encoded50_f.txt", "x")
    except: # open if exists
        o_encoded50_f = open("o_encoded50_f.txt", "w")
    o_encoded50_f.write(str(encoded_flag))
    o_encoded50_f.close()

# decoding
def decode():
    f_to_decode = open("base64algo/o_encoded50_f.txt")
    f_s_decode = f_to_decode.read()
    #decoded_flag = bytes(f_s_decode, "UTF-8")

    for k in range(50):
        f_s_decode = base64.b64decode(f_s_decode)

    #print("Decoded flag: %s " % f_to_decode.decode('utf8'))
    print("Decoded flag: %s " % f_s_decode)


def cli():
    print (sys.argv[1:])

    if len(sys.argv) < 2:
        print(usage)
        sys.exit(1)
    if sys.argv[1] in ["-h", "--help"]:
        print(usage)
        sys.exit(0)
    if sys.argv[1] in ["-c", "--count"]:
        print(sys.argv[1])
        if len(sys.argv) < 3:
            print(usage)
            sys.exit(1)
        print(sys.argv[1])
        file_name = sys.argv[2]
        encode_count = int(sys.argv[3])
    else:
        file_name = sys.argv[1]
        encode_count = 1
    if not os.path.isfile(file_name):
        print("file not found: %s" % file_name)
        sys.exit(1)
    encode(file_name, encode_count)

if __name__ == '__main__':
    cli()
