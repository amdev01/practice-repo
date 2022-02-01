A file has been base64 encoded 50 times - write a script to retrieve the flag. Here is the general process to do this:
read input from the file
use function to decode the file
do process in a loop
Try do this in both Bash and Python!

https://www.sentinelone.com/blog/guide-encode-decoded-base64/

https://en.wikipedia.org/wiki/Base64

https://base64.guru/learn/base64-algorithm/encode

https://stackoverflow.com/questions/49650847/determine-if-string-is-base64-encoded-twice


encode :
Text file flag664.txt with word “flag” in it
>flag
>ZmxhZw==
>Wm14aFp3PT0=
>V20xNGFGcDNQVDA9
>VjIweE5HRkdjRE5RVkRBOQ==
>VmpJd2VFNUhSa2RqUkU1UlZrUkJPUT09
>Vm1wSmQyVkZOVWhTYTJScVVrVTFVbFpyVWtKUFVUMDk=
>Vm0weGQxTnRVWGxXYTFwUFZsZG9WRmxVU2xOalZsWnlWbFJHVm1KR2NIbFdWM1JMVlVaV1ZVMUVhejA9

https://www.base64encode.org/

Exception has occurred: Error
Invalid base64-encoded string: number of data characters (19554449) cannot be 1 more than a multiple of 4
  File "/home/amdev01/Documents/GitHub/practice-repo/base64algo/base64task.py", line 32, in <module>
    f_s_decode = base64.b64decode(f_s_decode)

Given encoded string is too long to be decoded, how can I tackle that?

The encoding is right so it can't be a corrupt base64 string

Once running extra challenges:

[] Implement own base64 decode and encode class algorithm and use within project
