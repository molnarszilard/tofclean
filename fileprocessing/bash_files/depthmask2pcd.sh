#!bin/bash
builddir=$PWD'/../build/'
ddir=$PWD'/../../dataset/evaluation/depth_depth/'
mdir=$PWD'/../../dataset/evaluation/mask/'
pcddir=$PWD'/../../dataset/evaluation/pcd_pred_mask/'

if [[ ! -z "$1" ]] 
then 
    ddir=$1
    if [[ ! -z "$2" ]] 
    then 
        mdir=$2
        if [[ ! -z "$3" ]] 
        then 
            pcddir=$3
        fi
    fi
fi
cd $ddir

declare -a arrD
for file in *.png
do
    arrD=("${arrD[@]}" "$file")
done

cd $mdir
declare -a arrM
for file in *.png
do
    arrM=("${arrM[@]}" "$file")
done

cd $builddir

for i in "${!arrD[@]}"; do
    dfilename="${arrD[i]}"
    mfilename="${arrM[i]}"
    ./depthmask2pcd $ddir $mdir $pcddir $dfilename $mfilename nyu
done