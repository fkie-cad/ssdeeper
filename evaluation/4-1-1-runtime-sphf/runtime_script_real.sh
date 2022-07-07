#!/bin/bash

basepath="../corpus/100000/*"
declare -a implementations=("original" "bug" "feature" "djb2" "polynomial" "4b" "refactored" "refactored-4b" "refactored-djb2" "refactored-polynomial" "refactored-4b-djb2" "refactored-4b-polynomial")
	
echo "algorithm;size;time;iteration;filename;datatype" > "ssdeep-runtime-100k.csv"
for a in ${implementations[@]}; do
	echo $a
	for filename in $basepath; do
		tmp="$(cut -d'/' -f4 <<<"$filename")"
		datatype="$(cut -d'.' -f2 <<<"$tmp")"
		for ((n=0;n<10;n++)); do 
			ts=$(date +%s%N)
			"/tmp/ssdeep-$a/bin/ssdeep" -s $filename >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			i=$(stat --format=%s $filename)
			echo "ssdeep-$a;$i;$tt;$n;$filename;$datatype" >> "ssdeep-runtime-100k.csv"
		done
	done
done

