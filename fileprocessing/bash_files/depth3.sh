#!bin/bash
builddir=$PWD'/../build/'
ddir=$PWD'/../../dataset/evaluation/depth/'
d3dir=$PWD'/../../dataset/evaluation/depth3/'


if [[ ! -z "$1" ]] 
then 
    ddir=$1
    if [[ ! -z "$2" ]] 
    then 
        d3dir=$2
    fi
fi
cd $ddir

for filename in *.png; do
    cd $builddir
    # depth directory, mask directory, filename
    ./depth3 $ddir $d3dir $filename
done