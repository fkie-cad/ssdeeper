#!/bin/bash

echo "hash_generation;hash_comparison;mod;section;size;similarity;result" > ssdeep_comparison_synthetic.csv

basepath="../corpus/synthetic"
declare -a sizes=("1000" "10000" "100000" "1000000" "10000000")
declare -a mods=("insert" "change" "delete")
declare -a types=("first" "second" "third")
declare -a hash_generation=("ssdeep-original" "ssdeep-refactored" "ssdeep-refactored-djb2" "ssdeep-refactored-4b-djb2" "ssdeep-4b" "ssdeep-refactored-polynomial" "ssdeep-refactored-4b-polynomial" "ssdeep-refactored-4b")
declare -a hash_comparison=("-opt" "-max" "-opt-max")
for a in ${mods[@]}; do
	for b in ${types[@]}; do
		for c in ${sizes[@]}; do
			for d in ${hash_generation[@]}; do
				echo $d $c
				original_file="../corpus/synthetic/original/original_random_data_$c" 
				/tmp/$d/bin/ssdeep -s $original_file > tmp.txt
				tmp="$basepath/$a/$b/$c"
				for file in "$tmp"/*; do
					tmp2="$(cut -d'/' -f7 <<<"$file")"
					i="$(cut -d'_' -f1 <<<"$tmp2")"
					if [ "$a" = "change" ]; then
						let similarity=100-$i
					elif [ "$a" = "delete" ]; then
						similarity=`echo "scale=5; (100.000-$i)/(100.000)*100"| bc`
					else
						similarity=`echo "scale=5; 100.000/(100.000+$i)*100"| bc`
					fi
					
					/tmp/$d/bin/ssdeep -s $file > tmp2.txt
					
					for e in ${hash_comparison[@]}; do
						if [ "$d" = "ssdeep-refactored-4b-djb2" ] || [ "$d" = "ssdeep-4b" ] || [ "$d" = "ssdeep-refactored-4b-polynomial" ] || [ "$d" = "ssdeep-refactored-4b" ]   ; then
							result=`/tmp/ssdeep-4b$e/bin/ssdeep -s -k tmp.txt tmp2.txt`
						else
							result=`/tmp/ssdeep-original$e/bin/ssdeep -s -k tmp.txt tmp2.txt`
						fi
						
						if [ "$result" = "" ]; then
							result="0"
						else
							result="$(cut -d'(' -f2 <<<"$result")"
							result="$(cut -d')' -f1 <<<"$result")"
						fi
						
						if [ "$d" = "ssdeep-refactored-4b-djb2" ] || [ "$d" = "ssdeep-4b" ] || [ "$d" = "ssdeep-refactored-4b-polynomial" ] || [ "$d" = "ssdeep-refactored-4b" ]   ; then
							echo "$d;ssdeep-4b$e;$a;$b;$c;$similarity;$result" >> ssdeep_comparison_synthetic.csv
						else
							echo "$d;ssdeep-original$e;$a;$b;$c;$similarity;$result" >> ssdeep_comparison_synthetic.csv
						fi	
					done	
					if [ "$d" = "ssdeep-refactored-4b-djb2" ] || [ "$d" = "ssdeep-4b" ] || [ "$d" = "ssdeep-refactored-4b-polynomial" ] || [ "$d" = "ssdeep-refactored-4b" ]   ; then
						result=`/tmp/ssdeep-4b/bin/ssdeep -s -k tmp.txt tmp2.txt`
					else
						result=`/tmp/ssdeep-original/bin/ssdeep -s -k tmp.txt tmp2.txt`
					fi
					
					if [ "$result" = "" ]; then
						result="0"
					else
						result="$(cut -d'(' -f2 <<<"$result")"
						result="$(cut -d')' -f1 <<<"$result")"
					fi
				
					if [ "$d" = "ssdeep-refactored-4b-djb2" ] || [ "$d" = "ssdeep-4b" ] || [ "$d" = "ssdeep-refactored-4b-polynomial" ] || [ "$d" = "ssdeep-refactored-4b" ]   ; then
						echo "$d;ssdeep-4b;$a;$b;$c;$similarity;$result" >> ssdeep_comparison_synthetic.csv
					else
						echo "$d;ssdeep-original;$a;$b;$c;$similarity;$result" >> ssdeep_comparison_synthetic.csv
					fi	
				done
			done
		done
	done
done
