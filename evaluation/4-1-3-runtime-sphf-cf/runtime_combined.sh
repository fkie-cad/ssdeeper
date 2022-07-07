#!/bin/bash

basepath="../../../corpus/200/*"
declare -a implementations=("ssdeep-original" "ssdeep-original-opt" "ssdeep-original-max" "ssdeep-original-opt-max")

echo "algorithm;time;size;iteration;filename" > "ssdeep-runtime-combined-sphf-cf.csv"

# SPHF = ssdeep-original         CF -opt max -opt-max

for a in ${implementations[@]}; do
	echo $a

	for filename in $basepath; do
		for ((n=0;n<10;n++)); do
			ts=$(date +%s%N)
			/tmp/$a/bin/ssdeep -s $filename > tmp.txt
			/tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100-original.txt" tmp.txt >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			echo "$a;$tt;100;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/$a/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-1000-original.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;1000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/$a/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-10000-original.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;10000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		        
		        ts=$(date +%s%N)
		        /tmp/$a/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100000-original.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;100000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		done
	done
done

declare -a implementations=("ssdeep-4b" "ssdeep-4b-opt" "ssdeep-4b-max" "ssdeep-4b-opt-max")

for a in ${implementations[@]}; do
	echo $a

	for filename in $basepath; do
		for ((n=0;n<10;n++)); do
			ts=$(date +%s%N)
			/tmp/$a/bin/ssdeep -s $filename > tmp.txt
			/tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100-4b.txt" tmp.txt >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			echo "$a;$tt;100;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/$a/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-1000-4b.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;1000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/$a/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-10000-4b.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;10000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		        
		        ts=$(date +%s%N)
		        /tmp/$a/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100000-4b.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a;$tt;100000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		done
	done
done

declare -a implementations=("ssdeep-original" "ssdeep-original-opt" "ssdeep-original-max" "ssdeep-original-opt-max")

for a in ${implementations[@]}; do
	echo $a

	for filename in $basepath; do
		for ((n=0;n<10;n++)); do
			ts=$(date +%s%N)
			/tmp/ssdeep-refactored/bin/ssdeep -s $filename > tmp.txt
			/tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100-refactored.txt" tmp.txt >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			echo "$a-refactored;$tt;100;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-1000-refactored.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-refactored;$tt;1000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-10000-refactored.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-refactored;$tt;10000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		        
		        ts=$(date +%s%N)
		        /tmp/ssdeep-refactored/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100000-refactored.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-refactored;$tt;100000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		done
	done
done

declare -a implementations=("ssdeep-4b" "ssdeep-4b-opt" "ssdeep-4b-max" "ssdeep-4b-opt-max")

for a in ${implementations[@]}; do
	echo $a

	for filename in $basepath; do
		for ((n=0;n<10;n++)); do
			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-4b/bin/ssdeep -s $filename > tmp.txt
			/tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100-refactored-4b.txt" tmp.txt >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			echo "$a-refactored-4b;$tt;100;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-4b/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-1000-refactored-4b.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-refactored-4b;$tt;1000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-4b/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-10000-refactored-4b.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-refactored-4b;$tt;10000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		        
		        ts=$(date +%s%N)
		        /tmp/ssdeep-refactored-4b/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100000-refactored-4b.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-refactored-4b;$tt;100000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		done
	done
done

















declare -a implementations=("ssdeep-original" "ssdeep-original-opt" "ssdeep-original-max" "ssdeep-original-opt-max")

for a in ${implementations[@]}; do
	echo $a

	for filename in $basepath; do
		for ((n=0;n<10;n++)); do
			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-polynomial/bin/ssdeep -s $filename > tmp.txt
			/tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100-refactored-polynomial.txt" tmp.txt >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			echo "$a-polynomial;$tt;100;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-polynomial/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-1000-refactored-polynomial.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-polynomial;$tt;1000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-polynomial/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-10000-refactored-polynomial.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-polynomial;$tt;10000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		        
		        ts=$(date +%s%N)
		        /tmp/ssdeep-refactored-polynomial/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100000-refactored-polynomial.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-polynomial;$tt;100000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		done
	done
done

declare -a implementations=("ssdeep-4b" "ssdeep-4b-opt" "ssdeep-4b-max" "ssdeep-4b-opt-max")

for a in ${implementations[@]}; do
	echo $a

	for filename in $basepath; do
		for ((n=0;n<10;n++)); do
			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-4b-polynomial/bin/ssdeep -s $filename > tmp.txt
			/tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100-refactored-4b-polynomial.txt" tmp.txt >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			echo "$a-4b-polynomial;$tt;100;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-4b-polynomial/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-1000-refactored-4b-polynomial.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-4b-polynomial;$tt;1000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-4b-polynomial/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-10000-refactored-4b-polynomial.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-4b-polynomial;$tt;10000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		        
		        ts=$(date +%s%N)
		        /tmp/ssdeep-refactored-4b-polynomial/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100000-refactored-4b-polynomial.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-4b-polynomial;$tt;100000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		done
	done
done

declare -a implementations=("ssdeep-original" "ssdeep-original-opt" "ssdeep-original-max" "ssdeep-original-opt-max")

for a in ${implementations[@]}; do
	echo $a

	for filename in $basepath; do
		for ((n=0;n<10;n++)); do
			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-djb2/bin/ssdeep -s $filename > tmp.txt
			/tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100-refactored-djb2.txt" tmp.txt >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			echo "$a-djb2;$tt;100;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-djb2/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-1000-refactored-djb2.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-djb2;$tt;1000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-djb2/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-10000-refactored-djb2.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-djb2;$tt;10000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		        
		        ts=$(date +%s%N)
		        /tmp/ssdeep-refactored-djb2/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100000-refactored-djb2.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-djb2;$tt;100000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		done
	done
done

declare -a implementations=("ssdeep-4b" "ssdeep-4b-opt" "ssdeep-4b-max" "ssdeep-4b-opt-max")

for a in ${implementations[@]}; do
	echo $a

	for filename in $basepath; do
		for ((n=0;n<10;n++)); do
			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-4b-djb2/bin/ssdeep -s $filename > tmp.txt
			/tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100-refactored-4b-djb2.txt" tmp.txt >> "/dev/null"
			tt=$((($(date +%s%N) - $ts)))
			echo "$a-4b-djb2;$tt;100;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-4b-djb2/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-1000-refactored-4b-djb2.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-4b-djb2;$tt;1000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"

			ts=$(date +%s%N)
			/tmp/ssdeep-refactored-4b-djb2/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-10000-refactored-4b-djb2.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-4b-djb2;$tt;10000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		        
		        ts=$(date +%s%N)
		        /tmp/ssdeep-refactored-4b-djb2/bin/ssdeep -s $filename > tmp.txt
		        /tmp/$a/bin/ssdeep -s -k "../hashes/database/hashes-100000-refactored-4b-djb2.txt" tmp.txt >> "/dev/null"
		        tt=$((($(date +%s%N) - $ts)))
		        echo "$a-4b-djb2;$tt;100000;$n;$filename" >> "ssdeep-runtime-combined-sphf-cf.csv"
		done
	done
done


