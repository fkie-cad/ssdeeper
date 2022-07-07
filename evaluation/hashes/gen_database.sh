#!/bin/bash

declare -a implementations=("original" "bug" "feature" "djb2" "polynomial" "4b" "refactored" "refactored-4b" "refactored-djb2" "refactored-polynomial" "refactored-4b-djb2" "refactored-4b-polynomial")

for a in ${implementations[@]}; do
	echo $a
	"/tmp/ssdeep-$a/bin/ssdeep" -r ../corpus/100 >> "database/hashes-100-$a.txt"
	"/tmp/ssdeep-$a/bin/ssdeep" -r ../corpus/1000 >> "database/hashes-1000-$a.txt"
	"/tmp/ssdeep-$a/bin/ssdeep" -r ../corpus/10000 >> "database/hashes-10000-$a.txt"
	"/tmp/ssdeep-$a/bin/ssdeep" -r ../corpus/100000 >> "database/hashes-100000-$a.txt"
done

