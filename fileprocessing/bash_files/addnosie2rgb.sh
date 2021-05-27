#!bin/bash

builddir=$PWD'/../build/'
default_dir=$PWD'/../../dataset_anime/gt/' # path to input file directory
default_iext=.png # find the files with these extension
default_od=$PWD'/../../dataset_anime/noisy/' # 
default_sigma=0.05

if [[ ! -z "$1" ]] 
then 
    default_dir=$1
fi
cd $default_dir

for filename in *.png; do
    cd $builddir
    # input directory, input filename, output directory, output extention, sigma
    ./addnoise2rgb $default_dir $filename $default_od $default_sigma
done