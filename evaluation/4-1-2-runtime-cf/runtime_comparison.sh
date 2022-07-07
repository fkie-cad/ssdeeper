#!/bin/bash

basepath="../../../corpus/200/*"
declare -a implementations=("ssdeep-original" "ssdeep-original-opt" "ssdeep-original-max" "ssdeep-original-pa" "ssdeep-original-opt-max" "ssdeep-original-opt-pa" "ssdeep-original-pa-max" "ssdeep-original-opt-pa-max")

echo "algorithm;time;size;iteration;filename" > "ssdeep-runtime-comparison.csv"

for a in ${implementations[@]}; do
	echo $a

	for filename in $basepath; do
		/tmp/$a/bin/ssdeep -s $filename > tmp.txt
		for ((n=0;n<10;n++)); do 
			ts=$(date +%s%N)
			/tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100-original.txt" tmp.txt >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			echo "$a;$tt;100;$n;$filename" >> "ssdeep-runtime-comparison.csv"

			ts=$(date +%s%N)
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-1000-original.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;1000;$n;$filename" >> "ssdeep-runtime-comparison.csv"

			ts=$(date +%s%N)
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-10000-original.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;10000;$n;$filename" >> "ssdeep-runtime-comparison.csv"
		        
		        ts=$(date +%s%N)
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100000-original.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;100000;$n;$filename" >> "ssdeep-runtime-comparison.csv"
		done
	done
done

declare -a implementations=("ssdeep-4b" "ssdeep-4b-opt" "ssdeep-4b-max" "ssdeep-4b-pa" "ssdeep-4b-opt-max" "ssdeep-4b-opt-pa" "ssdeep-4b-pa-max" "ssdeep-4b-opt-pa-max")

for a in ${implementations[@]}; do
	echo $a

	for filename in $basepath; do
		/tmp/$a/bin/ssdeep -s $filename > tmp.txt

		for ((n=0;n<10;n++)); do
			ts=$(date +%s%N)
			/tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100-4b.txt" tmp.txt >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			echo "$a;$tt;100;$n;$filename" >> "ssdeep-runtime-comparison.csv"

			ts=$(date +%s%N)
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-1000-4b.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;1000;$n;$filename" >> "ssdeep-runtime-comparison.csv"

			ts=$(date +%s%N)
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-10000-4b.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;10000;$n;$filename" >> "ssdeep-runtime-comparison.csv"
		        
		        ts=$(date +%s%N)
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100000-4b.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;100000;$n;$filename" >> "ssdeep-runtime-comparison.csv"
		done
	done
done
