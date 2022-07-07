#!/bin/bash

basepathO="../../../corpus/synthetic/original/*"
declare -a implementations=("original" "bug" "feature" "djb2" "polynomial" "4b" "refactored" "refactored-4b" "refactored-djb2" "refactored-polynomial" "refactored-4b-djb2" "refactored-4b-polynomial")
echo "algorithm;size;time;iteration;filename" > "ssdeep-runtime-synthetic.csv"
basepath="../../../corpus/synthetic"
declare -a sizes=("1000" "10000" "100000" "1000000" "10000000")
declare -a mods=("insert" "change" "delete")
declare -a types=("first" "second" "third")


for a in ${implementations[@]}; do
	echo $a
	for filename in $basepathO; do
		for ((n=0;n<10;n++)); do 
			ts=$(date +%s%N)
			"/tmp/ssdeep-$a/bin/ssdeep" -s $filename >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			i=$(stat --format=%s $filename)
			echo "ssdeep-$a;$i;$tt;$n;$filename" >> "ssdeep-runtime-synthetic.csv"
		done
	done
done

for d in ${implementations[@]}; do
	echo $d
	for a in ${mods[@]}; do
		for b in ${types[@]}; do
			for c in ${sizes[@]}; do
				tmp="$basepath/$a/$b/$c"
				for filename in "$tmp"/*; do
					for ((n=0;n<10;n++)); do
						ts=$(date +%s%N)
						"/tmp/ssdeep-$d/bin/ssdeep" -s $filename >> "/dev/null"
						tt=$((($(date +%s%N) - $ts)))
						i=$(stat --format=%s $filename)
						echo "ssdeep-$d;$i;$tt;$n;$filename" >> "ssdeep-runtime-synthetic.csv"
					done
				done
			done
		done
	done
done


