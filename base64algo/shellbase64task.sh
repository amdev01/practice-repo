#!/bin/bash
#set -euo pipefail
#IFS=$'\n\t'

count=1 # pre set count to 1 to always decode once
while getopts f:c: flag
do
    case "${flag}" in # handle flags
        f) filename=${OPTARG};;
        c) count=${OPTARG};;
        *) echo "Invalid flags try again";;
    esac
done

if [[ -e $filename ]] # check if filename exists
then
    read -r one_line < "$filename" # read line from file name to one_line var
    decoded=$(echo "$one_line" | base64 --decode) # decode once
    if [[ $count -gt 1 ]] # if count flag used
    then
        for (( i=0; i < count-1; i++)); do # execute count-1 times because we already decoded file once 
            decoded=$(echo "$decoded" | base64 --decode) # decode back to decoded var
        done
    fi
    echo "Decoded: ${decoded}" # print flag to terminal
    exit 0
else
    echo "File ${filename} does not exist!" # exit on error
    exit 1
fi