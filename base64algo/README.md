#### A file has been base64 encoded 50 times - write a script to retrieve the flag.
Here is the general process to do this:

- read input from the file
- use function to decode the file
- do process in a loop

Try do this in both Bash and Python!

#### Research

[Encoding guide](https://www.sentinelone.com/blog/guide-encode-decoded-base64/) \
[base64 wiki](https://en.wikipedia.org/wiki/Base64) \
[base64 algorithm encoding algorithm](https://base64.guru/learn/base64-algorithm/encode) \
[Check if string is base64 encoded twice php stackoverflow](https://stackoverflow.com/questions/49650847/determine-if-string-is-base64-encoded-twice)

I was doing my best not to find a straight answer

#### Manual encoding:
Text file flag664.txt with word “flag” in it:
``` 
 flag
 ZmxhZw==
 Wm14aFp3PT0=
 V20xNGFGcDNQVDA9
 VjIweE5HRkdjRE5RVkRBOQ==
 VmpJd2VFNUhSa2RqUkU1UlZrUkJPUT09
 Vm1wSmQyVkZOVWhTYTJScVVrVTFVbFpyVWtKUFVUMDk=
 Vm0weGQxTnRVWGxXYTFwUFZsZG9WRmxVU2xOalZsWnlWbFJHVm1KR2NIbFdWM1JMVlVaV1ZVMUVhejA9
```
[online encoder/decoder](https://www.base64encode.org/)

```
 Exception has occurred: Error
 Invalid base64-encoded string: number of data characters (19554449) cannot be 1 more than a multiple of 4
  File "/home/amdev01/Documents/GitHub/practice-repo/base64algo/base64task.py", line 32, in <module>
 f_s_decode = base64.b64decode(f_s_decode)
```
Given encoded string is too long to be decoded, how can I tackle that?
The encoding is right so it can't be a corrupt base64 string
> I thought because file encoded 50 times is too long I will have to make a function
> that splits it into max len strings array, decodes each element, then join string back
> into the file and repeat untill flag is achieved. This is not an issue with this implementation,
> not sure why

UPDATE: The reason this happened is because I used "o_encoded50.txt" to try decoding on,
this file was previously encoded with my program but it was bytes not a string so encoded string
was wrapped in b'xxx'. Updated program to 

Program output:
```
~$ rm -rf o_*
~$ python base64task.py -e -c flagb64.txt 50
['-e', '-c', 'flagb64.txt', '50']
-c
Encoded once
Encoded 1 times
Wm14aFp3PT0=
Encoded 2 times
V20xNGFGcDNQVDA9
Encoded 3 times
VjIweE5HRkdjRE5RVkRBOQ==
Encoded 4 times
VmpJd2VFNUhSa2RqUkU1UlZrUkJPUT09
Encoded 5 times
Vm1wSmQyVkZOVWhTYTJScVVrVTFVbFpyVWtKUFVUMDk=
Encoded 6 times
Vm0xd1NtUXlWa1pPVldoVFlUSlNjVlZyVlRGVmJGcHlWV3RLVUZWVU1Eaz0=
Encoded 7 times
Vm0weGQxTnRVWGxXYTFwUFZsZG9WRmxVU2xOalZsWnlWbFJHVm1KR2NIbFdWM1JMVlVaV1ZVMUVhejA9
Encoded 8 times
Encoded 9 times
Encoded 10 times
Encoded 11 times
Encoded 12 times
Encoded 13 times
Encoded 14 times
Encoded 15 times
Encoded 16 times
Encoded 17 times
Encoded 19 times
Encoded 20 times
Encoded 21 times
Encoded 22 times
Encoded 23 times
Encoded 24 times
Encoded 25 times
Encoded 26 times
Encoded 27 times
Encoded 28 times
Encoded 29 times
Encoded 30 times
Encoded 31 times
Encoded 32 times
Encoded 33 times
Encoded 34 times
Encoded 35 times
Encoded 36 times
Encoded 37 times
Encoded 38 times
Encoded 39 times
Encoded 40 times
Encoded 41 times
Encoded 42 times
Encoded 43 times
Encoded 44 times
Encoded 45 times
Encoded 46 times
Encoded 47 times
Encoded 48 times
Encoded 49 times
Encoded 50 times
~$ python base64task.py -d -c o_encoded_f.txt 50
['-d', '-c', 'o_encoded_f.txt', '50']
-c
Decoded 1 times
Decoded 2 times
Decoded 3 times
Decoded 4 times
Decoded 5 times
Decoded 6 times
Decoded 7 times
Decoded 8 times
Decoded 9 times
Decoded 10 times
Decoded 11 times
Decoded 12 times
Decoded 13 times
Decoded 14 times
Decoded 15 times
Decoded 16 times
Decoded 17 times
Decoded 18 times
Decoded 19 times
Decoded 20 times
Decoded 21 times
Decoded 22 times
Decoded 23 times
Decoded 24 times
Decoded 25 times
Decoded 26 times
Decoded 27 times
Decoded 28 times
Decoded 29 times
Decoded 30 times
Decoded 31 times
Decoded 32 times
Decoded 33 times
Decoded 34 times
Decoded 35 times
Decoded 36 times
Decoded 37 times
Decoded 38 times
Decoded 39 times
Decoded 40 times
Decoded 41 times
Decoded 42 times
Decoded 43 times
Decoded 44 times
Decoded 45 times
VmpJd2VFNUhSa2RqUkU1UlZrUkJPUT09
Decoded 46 times
VjIweE5HRkdjRE5RVkRBOQ==
Decoded 47 times
V20xNGFGcDNQVDA9
Decoded 48 times
Wm14aFp3PT0=
Decoded 49 times
ZmxhZw==
Decoded 50 times
flag
~$ ls
base64task.py  flag64.txt  flagb64.txt  o_decoded_f.txt  o_encoded_f.txt
~$ cat flagb64.txt 
flag
~$ cat o_decoded_f.txt 
flag 
```

Once running extra challenges:
- [ ] Implement own base64 decode and encode class algorithm and use within project
