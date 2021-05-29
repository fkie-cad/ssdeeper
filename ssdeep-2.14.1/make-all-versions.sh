#!/bin/bash

# hash generation implementations:

git checkout master
./configure --prefix=/tmp/ssdeep-original
make
make install

git checkout anchor-bug
./configure --prefix=/tmp/ssdeep-bug
make
make install

git checkout ssdeep-halfh-removal
./configure --prefix=/tmp/ssdeep-feature
make
make install

git checkout ssdeep-djb2
./configure --prefix=/tmp/ssdeep-djb2
make
make install

git checkout ssdeep-polynomial
./configure --prefix=/tmp/ssdeep-polynomial
make
make install

git checkout 2bTo4b
./configure --prefix=/tmp/ssdeep-4b
make
make install

git checkout ssdeep-refactored
./configure --prefix=/tmp/ssdeep-refactored
make
make install

git checkout ssdeep-refactored-2bTo4b
./configure --prefix=/tmp/ssdeep-refactored-4b
make
make install

git checkout ssdeep-refactored-djb2
./configure --prefix=/tmp/ssdeep-refactored-djb2
make
make install

git checkout ssdeep-refactored-polynomial
./configure --prefix=/tmp/ssdeep-refactored-polynomial
make
make install

git checkout ssdeep-refactored-4b-djb2
./configure --prefix=/tmp/ssdeep-refactored-4b-djb2
make
make install

git checkout ssdeep-refactored-4b-polynomial
./configure --prefix=/tmp/ssdeep-refactored-4b-polynomial
make
make install

# hash comparison implemenations 		
#		ssdeep-original       
#		ssdeep-original-opt	    
#		ssdeep-original-max	   
#		ssdeep-original-pa	    
#		ssdeep-original-opt-max    
#		ssdeep-original-opt-pa     
#		ssdeep-original-pa-max     
#		ssdeep-original-opt-pa-max

git checkout rm-substring-opt
./configure --prefix=/tmp/ssdeep-original-opt
make
make install

git checkout rm-max-score
./configure --prefix=/tmp/ssdeep-original-max
make
make install

git checkout rm-parray-opt
./configure --prefix=/tmp/ssdeep-original-pa
make
make install

git checkout rm-substring-opt-max
./configure --prefix=/tmp/ssdeep-original-opt-max
make
make install

git checkout rm-substring-opt-pa
./configure --prefix=/tmp/ssdeep-original-opt-pa
make
make install

git checkout rm-parray-opt-max
./configure --prefix=/tmp/ssdeep-original-pa-max
make
make install

git checkout rm-substring-opt-pa-max
./configure --prefix=/tmp/ssdeep-original-opt-pa-max
make
make install

# hash comparison 4b implemenations 		
#		ssdeep-4b       
#		ssdeep-4b-opt	    
#		ssdeep-4b-max	   
#		ssdeep-4b-pa	  
#		ssdeep-original-opt-max    
#		ssdeep-original-opt-pa     
#		ssdeep-original-pa-max     
#		ssdeep-original-opt-pa-max


git checkout rm-substring-opt-4b
./configure --prefix=/tmp/ssdeep-4b-opt
make
make install

git checkout rm-max-score-4b
./configure --prefix=/tmp/ssdeep-4b-max
make
make install

git checkout rm-parray-opt-4b
./configure --prefix=/tmp/ssdeep-4b-pa
make
make install

git checkout rm-substring-opt-max-4b
./configure --prefix=/tmp/ssdeep-4b-opt-max
make
make install

git checkout rm-substring-opt-pa-4b
./configure --prefix=/tmp/ssdeep-4b-opt-pa
make
make install

git checkout rm-parray-opt-max-4b
./configure --prefix=/tmp/ssdeep-4b-pa-max
make
make install

git checkout rm-substring-opt-pa-max-4b
./configure --prefix=/tmp/ssdeep-4b-opt-pa-max
make
make install

