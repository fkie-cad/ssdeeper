#!/bin/bash

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

git checkout ssdeep-2bTo4b
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



git checkout master
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-original-opt
make
make install
git merge --abort

git checkout anchor-bug
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-bug-opt
make
make install
git merge --abort

git checkout ssdeep-halfh-removal
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-feature-opt
make
make install
git merge --abort

git checkout ssdeep-djb2
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-djb2-opt
make
make install
git merge --abort

git checkout ssdeep-polynomial
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-polynomial-opt
make
make install
git merge --abort

git checkout ssdeep-2bTo4b
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-4b-opt
make
make install
git merge --abort

git checkout ssdeep-refactored
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-refactored-opt
make
make install
git merge --abort

git checkout ssdeep-refactored-2bTo4b
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-refactored-4b-opt
make
make install
git merge --abort

git checkout ssdeep-refactored-djb2
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-refactored-djb2-opt
make
make install
git merge --abort

git checkout ssdeep-refactored-polynomial
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-refactored-polynomial-opt
make
make install
git merge --abort

git checkout ssdeep-refactored-4b-djb2
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-refactored-4b-djb2-opt
make
make install
git merge --abort

git checkout ssdeep-refactored-4b-polynomial
git merge --no-commit rm-substring-opt
./configure --prefix=/tmp/ssdeep-refactored-4b-polynomial-opt
make
make install
git merge --abort
