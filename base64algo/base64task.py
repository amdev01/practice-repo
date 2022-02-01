import base64
import sys
import os

usage = """\
Usage: base64task.py [-hced] "<file_to_encode>" <n>
  file_to_encode        - <required> path to the file to encode
  n                     - <optional> number of times to encode file
  -e/--encode           - <required> encode <file_to_encode> with base64
  -d/--decode           - <required> decode <file_to_encode> with base64
  -c/--count n          - <optional> specify <n> to encode/decode <file_to_encode>\
"""

def encode_test(p_flag):
    print("Test Base64 encoded once: %s" % base64.b64encode(p_flag)) # print 1st base64 encoding

def decode_test(p_flag):
    print("Test Base64 decoded once: %s" % base64.b64decode(p_flag)) # print 1st base64 decoding

def encode(file_to_encode, encode_count):
    # encoding
    f_s = open(file_to_encode, "r").read() # get text from file and store it as a string
    #b_flag = bytes(f_s, "UTF-8") # convert string to bytes[]
    encoded_flag = base64.b64encode(f_s) # encode flag for the first time
    print("Encoded once")
    if (encode_count > 1):
        for k in range(encode_count):
            encoded_flag = base64.b64encode(encoded_flag) # save encoded string to same var
            # print("Encoded "+ str(k+1) + " times")
            # if (k < 7): # debug print to see if encoding is correct
            #  print(encoded_flag.decode('utf8'))
    
    # create a new file or open existsing one
    try: # try create a new file
        o_encoded_f = open("o_encoded_f.txt", "x")
    except: # open if exists
        o_encoded_f = open("o_encoded_f.txt", "w")
    o_encoded_f.write(str(encoded_flag)) # write to file
    o_encoded_f.close()

# decoding
def decode(file_to_decode, decode_count):
    f_d = open(file_to_decode, "r").read() # get text from file and store it as a string
    #f_s_decode = f_to_decode.read()
    #decoded_flag = bytes(f_s_decode, "UTF-8")

    decoded_flag = base64.b64decode(f_d)
    if (decode_count > 1):
        for k in range(decode_count):
            decoded_flag = base64.b64decode(decoded_flag)
            # print("Decoded "+ str(k+1) + " times")
            # if (k > decode_count-7): # debug print to see if encoding is correct
            #    print(decoded_flag.decode('utf8'))

    #print("Decoded flag: %s " % f_to_decode.decode('utf8'))
    #print("Decoded flag: %s " % f_s_decode)
    try: # try create a new file
        o_decoded_f = open("o_decoded_f.txt", "x")
    except: # open if exists
        o_decoded_f = open("o_decoded_f.txt", "w")
    o_decoded_f.write(str(decoded_flag))
    o_decoded_f.close()

def arg_count():
    if sys.argv[2] in ["-c", "--count"]:
            print(sys.argv[2])
            if len(sys.argv) < 4: # check if correct number or args
               print(usage)
               sys.exit(1)
               check_file_path(sys.argv[3])
            return True
            # pass file name and decode count
    else:
        check_file_path(sys.argv[2])
        return False

def check_file_path(f_name):
    if not os.path.isfile(f_name): # check if file exists
        print("file not found: %s" % f_name)
        sys.exit(1)

def cli():
    # print (sys.argv[1:])
    if len(sys.argv) < 2: # exit if no arguments
        print(usage)
        sys.exit(1)
    if sys.argv[1] in ["-h", "--help"]: # print help menu
        print(usage)
        sys.exit(0)
    if sys.argv[1] in ["-e", "--encode"]: # set encoding vars
        if len(sys.argv) < 3: # check if correct number or args
            print(usage)
            sys.exit(1)
        if (arg_count()): # check if count arg present
            encode(sys.argv[3], int(sys.argv[4])) # call encode N times
        else:
            encode(sys.argv[2], 1) # call encode N times
    if sys.argv[1] in ["-d", "--decode"]: # set decoding vars
        if len(sys.argv) < 3: # check if correct number or args
            print(usage)
            sys.exit(1)
        if (arg_count()): # check if count arg present
            decode(sys.argv[3], int(sys.argv[4])) # call decode N times
        else:
            decode(sys.argv[2], 1) # call encode N times

if __name__ == '__main__':
    cli()
