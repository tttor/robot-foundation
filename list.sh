#!/bin/bash
rootdir=/home/tor/rsc/robot-foundation
dlist[0]=book/ebook
dlist[1]=talk/etalk
dlist[2]=thesis/ethesis
dlist[3]=tool/etool
dlist[4]=write/ewrite

for dir in "${dlist[@]}"
do
    echo '>>> listing: '$dir
    ls -1 -R $rootdir/$dir > $rootdir/$dir/LIST.txt
done

