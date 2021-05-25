#!bin/bash
builddir=$PWD'/../build/'
ddir=$PWD'/../../dataset/evaluation/depth_pred/'
pcddir=$PWD'/../../dataset/evaluation/pcd_pred/'

if [[ ! -z "$1" ]] 
then 
    ddir=$1
    if [[ ! -z "$2" ]] 
    then 
        pcddir=$2
    fi
fi
cd $ddir

for filename in *.png; do
    cd $builddir
    # path
    ./depth2pcd $ddir $pcddir $filename nyu
done