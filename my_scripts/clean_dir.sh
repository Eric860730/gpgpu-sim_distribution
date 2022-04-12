#!/bin/bash

dirlist=$(find ./ -mindepth 1 -maxdepth 1 -type d)

for dir in $dirlist
do
    cd $dir
    rm *
    cd ../
done
