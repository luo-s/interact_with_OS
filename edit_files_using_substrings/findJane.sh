#!/bin/bash

> oldFiles.txt

files=$(grep " jane " list.txt | cut -d ' ' -f 3)
for file in $files; do
    echo "${file}"
	if [ -e "${file}" ]; then 
        echo "File exists"
		echo "${file}" >> oldFiles.txt
    fi
done