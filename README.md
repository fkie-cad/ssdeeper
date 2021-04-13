# Removal of halfh and halfdigest calculation.
The limitation requires an additional fnv hash value calculation at each step and truncates information about the original file. Without using the limitation, the second half of the hash value can have more characters but remains being limited by at most 64 characters. The removal achieves a much faster calculation and some comparisons happen to be more precise due to a larger hash length. Additionally, the robustness of ssdeep is enhanced; the truncation makes it easier to shift the actual information of the file into the last base64 character by modifications that insert segments into the file. 

##### GENERAL PROPERTIES
	=> much more efficient runtime
	=> some comparisons have a higher accuracy
	=> larger hash values but still limited to 2x64 characters
	
##### SECURITY PROPERTIES
	=> more robust against the described kind of manipulations
	=> full coverage property remained


##### ORIGINAL:
###### Example hash:
768:6MHqHqHqHqHqHqHqHqHqHqHqHqHqHqHqHqHqHeAU41W2CS9MXcjtKOTiHxC1j/ZK:6MHqHqHqHqHqHqHqHqHqHqHqHqHqHqHJ,"forensic.txt"

###### Runtime:
time /tmp/ssdeep/bin/ssdeep -r ../../corpus/t5-corpus/

	real	0m12,018s
	user	0m11,742s
	sys	0m0,276s

	real	0m12,011s
	user	0m11,723s
	sys	0m0,288s

	real	0m12,322s
	user	0m12,093s
	sys	0m0,229s


##### AFTER REMOVAL:
###### Example hash: 
768:6MHqHqHqHqHqHqHqHqHqHqHqHqHqHqHqHqHqHeAU41W2CS9MXcjtKOTiHxC1j/ZK:6MHqHqHqHqHqHqHqHqHqHqHqHqHqHqHqHqHqHNDbCdcjoD811D3wC//FGxhFrb,"forensic.txt"
 
###### Runtime:
time /tmp/ssdeep/bin/ssdeep -r ../../corpus/t5-corpus/

	real	0m10,059s
	user	0m9,705s
	sys	0m0,248s

	real	0m9,940s
	user	0m9,615s
	sys	0m0,324s

	real	0m9,933s
	user	0m9,684s
	sys	0m0,248s

