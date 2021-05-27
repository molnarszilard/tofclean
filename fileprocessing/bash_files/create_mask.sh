#!bin/bash
builddir=$PWD'/../build/'
ddir=$PWD'/../../dataset/evaluation/depth/'
mdir=$PWD'/../../dataset/evaluation/mask/'

if [[ ! -z "$1" ]] 
then 
    ddir=$1
    if [[ ! -z "$2" ]] 
    then 
        mdir=$2
    fi
fi
cd $ddir

for filename in *.png; do
    cd $builddir
    # depth directory, mask directory, filename
    ./create_mask $ddir $mdir $filename 0.5
done