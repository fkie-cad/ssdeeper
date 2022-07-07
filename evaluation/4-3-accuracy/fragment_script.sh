#!/bin/bash

echo "hash_generation;hash_comparison;size;result;datatype;section" > ssdeep_fragment.csv

basepath="../corpus/t5-corpus-roussev"
declare -a sizes=("025" "050" "075" "090" "095")
declare -a types=("first" "second" "third")
declare -a hash_generation=("ssdeep-original" "ssdeep-refactored" "ssdeep-refactored-djb2" "ssdeep-refactored-4b-djb2" "ssdeep-4b" "ssdeep-refactored-polynomial" "ssdeep-refactored-4b-polynomial" "ssdeep-refactored-4b")
declare -a hash_comparison=("-opt" "-max" "-opt-max")
for b in ${types[@]}; do
	for c in ${sizes[@]}; do
		for d in ${hash_generation[@]}; do
			for file1 in "$basepath"/*; do
				tmp2="$(cut -d'/' -f4 <<<"$file1")"
				datatype="$(cut -d'.' -f2 <<<"$tmp2")"
				
				frag_size=`echo $c | sed 's/^0*//'`
				file2="../corpus/t5-fragments/$frag_size/"$b"_"$c"_delete_"$tmp2
		
				/tmp/$d/bin/ssdeep -s $file1 > tmp.txt 
				/tmp/$d/bin/ssdeep -s $file2 > tmp2.txt
				
				for e in ${hash_comparison[@]}; do
					if [ "$d" = "ssdeep-refactored-4b-djb2" ] || [ "$d" = "ssdeep-4b" ] || [ "$d" = "ssdeep-refactored-4b-polynomial" ] || [ "$d" = "ssdeep-refactored-4b" ]   ; then
						result=`/tmp/ssdeep-4b$e/bin/ssdeep -s -k tmp.txt tmp2.txt`
					else
						result=`/tmp/ssdeep-original$e/bin/ssdeep -s -k tmp.txt tmp2.txt`
					fi
					echo $result
					if [ "$result" = "" ]; then
						result="0"
					else
						result="$(cut -d'(' -f2 <<<"$result")"
						result="$(cut -d')' -f1 <<<"$result")"
					fi
					if [ "$d" = "ssdeep-refactored-4b-djb2" ] || [ "$d" = "ssdeep-4b" ] || [ "$d" = "ssdeep-refactored-4b-polynomial" ] || [ "$d" = "ssdeep-refactored-4b" ]; then
						echo "$d;ssdeep-4b$e;$frag_size;$result;$datatype;$b" >> ssdeep_fragment.csv
					else
						echo "$d;ssdeep-original$e;$frag_size;$result;$datatype;$b" >> ssdeep_fragment.csv
					fi	
				done	
				if [ "$d" = "ssdeep-refactored-4b-djb2" ] || [ "$d" = "ssdeep-4b" ] || [ "$d" = "ssdeep-refactored-4b-polynomial" ] || [ "$d" = "ssdeep-refactored-4b" ]; then
					result=`/tmp/ssdeep-4b/bin/ssdeep -s -k tmp.txt tmp2.txt`
				else
					result=`/tmp/ssdeep-original/bin/ssdeep -s -k tmp.txt tmp2.txt`
				fi
				#echo $result
				if [ "$result" = "" ]; then
					result="0"
				else
					result="$(cut -d'(' -f2 <<<"$result")"
					result="$(cut -d')' -f1 <<<"$result")"
				fi
				if [ "$d" = "ssdeep-refactored-4b-djb2" ] || [ "$d" = "ssdeep-4b" ] || [ "$d" = "ssdeep-refactored-4b-polynomial" ] || [ "$d" = "ssdeep-refactored-4b" ]; then
					echo "$d;ssdeep-4b;$frag_size;$result;$datatype;$b" >> ssdeep_fragment.csv
				else
					echo "$d;ssdeep-original;$frag_size;$result;$datatype;$b" >> ssdeep_fragment.csv
				fi
			done
		done
	done
done
