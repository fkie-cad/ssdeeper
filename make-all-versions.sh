#!/bin/bash

# hash generation implementations:

git checkout master
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-original
make
make install
cd ..

git checkout anchor-bug
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-bug
make
make install
cd ..

git checkout ssdeep-halfh-removal
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-feature
make
make install
cd ..

git checkout ssdeep-djb2
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-djb2
make
make install
cd ..

git checkout ssdeep-polynomial
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-polynomial
make
make install
cd ..

git checkout 2bTo4b
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-4b
make
make install
cd ..

git checkout ssdeep-refactored
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-refactored
make
make install
cd ..

git checkout ssdeep-refactored-2bTo4b
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-refactored-4b
make
make install
cd ..

git checkout ssdeep-refactored-djb2
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-refactored-djb2
make
make install
cd ..

git checkout ssdeep-refactored-polynomial
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-refactored-polynomial
make
make install
cd ..

git checkout ssdeep-refactored-4b-djb2
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-refactored-4b-djb2
make
make install
cd ..

git checkout ssdeep-refactored-4b-polynomial
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-refactored-4b-polynomial
make
make install
cd ..

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
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-original-opt
make
make install
cd ..

git checkout rm-max-score
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-original-max
make
make install
cd ..

git checkout rm-parray-opt
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-original-pa
make
make install
cd ..

git checkout rm-substring-opt-max
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-original-opt-max
make
make install
cd ..

git checkout rm-substring-opt-pa
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-original-opt-pa
make
make install
cd ..

git checkout rm-parray-opt-max
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-original-pa-max
make
make install
cd ..

git checkout rm-substring-opt-pa-max
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-original-opt-pa-max
make
make install
cd ..

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
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-4b-opt
make
make install
cd ..

git checkout rm-max-score-4b
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-4b-max
make
make install
cd ..

git checkout rm-parray-opt-4b
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-4b-pa
make
make install
cd ..

git checkout rm-substring-opt-max-4b
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-4b-opt-max
make
make install
cd ..

git checkout rm-substring-opt-pa-4b
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-4b-opt-pa
make
make install
cd ..

git checkout rm-parray-opt-max-4b
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-4b-pa-max
make
make install
cd ..

git checkout rm-substring-opt-pa-max-4b
cd ssdeep-2.14.1
./configure --prefix=/tmp/ssdeep-4b-opt-pa-max
make
make install
cd ..
