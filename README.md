# Exchanging adler32 checksum with djb2
The djb2 algorithm is a more efficient alternative to the alder32 checksum as a rolling hash function and has an excellent distribution. Less operations are required to update the polynomial djb2 hash with the new incoming byte when processing the window. If a high distribution is necessary for the rolling hash function is evaluated in another branch, in which a polynomial is used as a rolling hash function. In theory the distrubtion is not of importance, for any rolling hash specific words in a document or sequences of bytes determine a segment; Which words or byte sequences trigger anchor points is or rather should not be significant.  

##### GENERAL PROPERTIES
    => much more efficient runtime
    => expected to have a similar accuracy and hash length

##### SECURITY PROPERTIES
    => coverage and obfuscation resistance remain unchanged

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


##### WITH DJB2:
###### Runtime:
time /tmp/ssdeep/bin/ssdeep -r ../../corpus/t5-corpus/

	real	0m10,671s
	user	0m10,443s
	sys	0m0,228s

	real	0m10,680s
	user	0m10,476s
	sys	0m0,205s

	real	0m10,744s
	user	0m10,479s
	sys	0m0,264s

