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

	real	0m10,059s
	user	0m9,705s
	sys	0m0,248s

	real	0m9,940s
	user	0m9,615s
	sys	0m0,324s

	real	0m9,933s
	user	0m9,684s
	sys	0m0,248s


# Last segment bug

If the last byte of the input triggers an anchor point, an empty last segment will be appended to the similarity hash value. This can be a critical error if it leads to the selection of a block size that has a much smaller hash of length 32 characters. The fnv hash is initialized to 0x27, which corresponds to the base64 character 'n', as can be seen in the following hash. 

768:6WAU41W2CS9MXcjtKOTiHxC1j/ZDeUl/wC/wmFK9xhFRpoCwi96n:61DbCdcjoD811D3wC//FGxhFryn,"forensic_last_segment.txt"

The error is within the digest construction after processing the input. 

``` 
uint32_t h = roll_sum(&self->roll);
if (h != 0){
    add character to digest
}
else if(last_b64 != '\0'){
    add character to digest
}
``` 

which has been exchanged with:

```
uint32_t h = roll_sum(&self->roll);
if ((h+1)==0 || ((h+1) % SSDEEP_BS(bi))){
    add character to digest
}
``` 
768:6WAU41W2CS9MXcjtKOTiHxC1j/ZDeUl/wC/wmFK9xhFRpoCwi96:61DbCdcjoD811D3wC//FGxhFry,"forensic_last_segment.txt"

# (b,2b) -> (b,4b) + Removal of halfh and halfdigest calculation + Last segment bug

##### GENERAL PROPERTIES
	=> much more efficient runtime 
	=> higher accuracy and higher optinoal range of comparisons
	=> hash values remain limited but larger on average; signatures limited between 32-128 characters
	
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

##### AFTER CHANGES:
 
###### Runtime:
time /tmp/ssdeep/bin/ssdeep -r ../../corpus/t5-corpus/

real	0m9,134s
user	0m8,934s
sys	0m0,200s

real	0m9,335s
user	0m9,079s
sys	0m0,256s

real	0m9,102s
user	0m8,870s
sys	0m0,232s


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

# (b,2b) -> (b,4b) + Removal of halfh and halfdigest calculation + Last segment bug + djb2

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

	real	0m10,298s
	user	0m10,042s
	sys	0m0,256s

	real	0m10,256s
	user	0m9,992s
	sys	0m0,264s

	real	0m10,277s
	user	0m10,053s
	sys	0m0,224s
