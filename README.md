# Key = Hash init 
Using a key in the hash initialisation of the FNV hash values and within the rolling hash function to determine trigger points optimizes the ssdeep algorithms obfuscation resistance. It is infeasible to efficiently manipulate an input without knowing how to enforce trigger points and segment initialisations. On the contrary sharing a hash value database requires identical keys. 


##### GENERAL PROPERTIES
	=> identical runtime, accuracy and compression rate
	
##### SECURITY PROPERTIES
	=> more robust 
	=> full coverage
	

##### ORIGINAL:

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


##### KEY:
 
###### Runtime:
time /tmp/ssdeep/bin/ssdeep -r ../../corpus/t5-corpus/

	real	0m11,922s
	user	0m11,633s
	sys	0m0,288s

	real	0m11,918s
	user	0m11,674s
	sys	0m0,244s
	
	real	0m11,825s
	user	0m11,573s
	sys	0m0,252s


