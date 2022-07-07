#!/bin/bash

echo "hash_generation;hash_comparison;mod;section;similarity;result;datatype" > ssdeep_comparison_real.csv

basepath="../corpus/real-data/t5-corpus-roussev"
declare -a mods=("insert" "change" "delete")
declare -a types=("first" "second" "third")
declare -a hash_generation=("ssdeep-original" "ssdeep-refactored" "ssdeep-refactored-djb2" "ssdeep-refactored-4b-djb2" "ssdeep-4b" "ssdeep-refactored-polynomial" "ssdeep-refactored-4b-polynomial" "ssdeep-refactored-4b")
declare -a hash_comparison=("-opt" "-max" "-opt-max")
for file1 in "$basepath"/*; do
	echo $file1
	for a in ${mods[@]}; do
		for b in ${types[@]}; do
			for d in ${hash_generation[@]}; do 
				`python3 ../corpus/scripts/real_data.py $file1 $b $a`
				/tmp/$d/bin/ssdeep -s $file1 > tmp.txt
				tmp1="$(cut -d'/' -f5 <<<"$file1")"
				datatype="$(cut -d'.' -f2 <<<"$tmp1")"
				file2path="real/$a/$b"
				
				for file2 in "$file2path"/*; do
					i="$(cut -d'/' -f4 <<<"$file2")"
					if [ "$a" = "change" ]; then
						let similarity=100-$i
					elif [ "$a" = "delete" ]; then
						similarity=`echo "scale=5; (100.000-$i)/(100.000)*100"| bc`
					else
						similarity=`echo "scale=5; 100.000/(100.000+$i)*100"| bc`
					fi
					
					/tmp/$d/bin/ssdeep -s $file2 > tmp2.txt
					
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
							echo "$d;ssdeep-4b$e;$a;$b;$similarity;$result;$datatype" >> ssdeep_comparison_real.csv
						else
							echo "$d;ssdeep-original$e;$a;$b;$similarity;$result;$datatype" >> ssdeep_comparison_real.csv
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
						echo "$d;ssdeep-4b;$a;$b;$similarity;$result;$datatype" >> ssdeep_comparison_real.csv
					else
						echo "$d;ssdeep-original;$a;$b;$similarity;$result;$datatype" >> ssdeep_comparison_real.csv
					fi	
				done
				rm -r "real/$a/$b"
				rm -r "real/$a/"
			done
		done
	done
done
rm -r "real/"
