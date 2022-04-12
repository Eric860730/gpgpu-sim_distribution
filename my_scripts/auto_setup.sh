#!/bin/bash

#
# Copy the gpu configuration files to all benchmark.
#
# All arch name:
#   SM6_TITANX
#   SM7_QV100
#   SM7_TITANV
#   SM75_RTX2060

dirlist=$(find ./ -mindepth 1 -maxdepth 1 -type d)
#gpu_arch_list=$(find ./my_result/ -mindepth 1 -maxdepth 1 -type d)

#for g_arch in $gpu_arch_list
for k in {1}:
do
    gpu_arch="SM6_TITANX"
    echo $gpu_arch
    for dir in $dirlist
    do
        cd $dir
        cp ~/gpgpu-sim_distribution/configs/tested-cfgs/$gpu_arch/* ./
        make clean
        echo "make ${dir:2}"
        make
        for i in {1..10};
        do
            echo "run ${dir:2} with ${gpu_arch} - $i"
            ./run > ../my_result/${gpu_arch}/${dir:2}_${gpu_arch}_output_$i.txt
            echo "done ${dir:2} $i"
        done
        cd ../
    done
    exit
done
