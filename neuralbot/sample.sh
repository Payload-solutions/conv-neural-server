#!/bin/bash

# content=$(ls -l file_test_dirs/ | wc -l)

# echo "${content}"

for i in {1..10000}
do
	echo hello > "file_test_dirs/file_$i.txt"
done
