# (b,2b) -> (b,4b)
The algorithm has to calculate signatures for only at most half of the amount of block sizes. This improves the algorithm in runtime for the hash value generation, the hash value length and therefore the accuracy and the range of comparisons that remain possible for inputs that strongly differ in length. More hash value comparisons and larger hash values however increase the runtime in a comparison with a hash value database. 

##### GENERAL PROPERTIES
	=> more efficient runtime 
	=> higher accuracy and higher optinoal range of comparisons
	=> hash values remain limited; signatures limited between 32-128 characters
	
##### SECURITY PROPERTIES
	=> more robust, longer hash values, higher range in comparisons
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


##### (b,4b):
 
###### Runtime:
time /tmp/ssdeep/bin/ssdeep -r ../../corpus/t5-corpus/

	real	0m10,932s
	user	0m10,727s
	sys	0m0,205s

	real	0m10,935s
	user	0m10,658s
	sys	0m0,276s
	
	real	0m10,890s
	user	0m10,691s
	sys	0m0,197s

