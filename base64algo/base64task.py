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

def encode_test(test_str):
    print("Test Base64 encoded once: %s" % base64.b64encode(test_str)) # print 1st base64 encoding

def decode_test(test_str):
    print("Test Base64 decoded once: %s" % base64.b64decode(test_str)) # print 1st base64 decoding

def encode(file_to_encode, encode_count):
    # encoding
    file_str = open(file_to_encode, "r").read() # get text from file and store it as a string
    file_bytes = bytes(file_str, "UTF-8") # convert string to bytes[]
    encoded_str = base64.b64encode(file_bytes) # encode flag for the first time
    print("Encoded once")
    if (encode_count > 1):
        for k in range(encode_count-1):
            encoded_str = base64.b64encode(encoded_str) # save encoded string to same var
            # print("Encoded "+ str(k+1) + " times")
            # if (k < 7): # debug print to see if encoding is correct
            #  print(encoded_flag.decode('utf8'))
    
    # create a new file or open existsing one
    try: # try create a new file
        encoded_file_out = open("encoded_file_out.txt", "x")
    except: # open if exists
        encoded_file_out = open("encoded_file_out.txt", "w")
    encoded_file_out.write(encoded_str.decode('utf-8')) # write to file
    encoded_file_out.close()

# decoding
def decode(file_to_decode, decode_count):
    file_str = open(file_to_decode, "r").read() # get text from file and store it as a string
    #f_s_decode = f_to_decode.read()
    #decoded_flag = bytes(f_s_decode, "UTF-8")

    decoded_str = base64.b64decode(file_str)
    if (decode_count > 1):
        for k in range(decode_count-1):
            decoded_str = base64.b64decode(decoded_str)
            # print("Decoded "+ str(k+1) + " times")
            # if (k > decode_count-7): # debug print to see if encoding is correct
            #    print(decoded_flag.decode('utf8'))

    #print("Decoded flag: %s " % f_to_decode.decode('utf8'))
    #print("Decoded flag: %s " % f_s_decode)
    try: # try create a new file
        decoded_file_out = open("decoded_file_out.txt", "x")
    except: # open if exists
        decoded_file_out = open("decoded_file_out.txt", "w")
    decoded_file_out.write(decoded_str.decode('utf-8'))
    decoded_file_out.close()

# check if file specified in args exists
def check_file_path(f_name):
    if not os.path.isfile(f_name): # check if file exists
        print("file not found: %s" % f_name)
        sys.exit(1)

# check if arg "-c is used"
# TODO
# Add validation to arguments
def count_arg():
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

# define ability to use arguments
# TODO
# Add validation to arguments
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
        if (count_arg()): # check if count arg present
            encode(sys.argv[3], int(sys.argv[4])) # call encode N times
        else:
            encode(sys.argv[2], 1) # call encode N times
    if sys.argv[1] in ["-d", "--decode"]: # set decoding vars
        if len(sys.argv) < 3: # check if correct number or args
            print(usage)
            sys.exit(1)
        if (count_arg()): # check if count arg present
            decode(sys.argv[3], int(sys.argv[4])) # call decode N times
        else:
            decode(sys.argv[2], 1) # call encode N times

if __name__ == '__main__':
    cli()
