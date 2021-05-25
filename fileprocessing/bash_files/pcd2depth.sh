#!bin/bash
builddir=$PWD'/../build/'
input_dir=$PWD'/../../dataset/evaluation/pcd/'
output_dir=$PWD'/../../dataset/evaluation/depth/'

if [[ ! -z "$1" ]] 
then 
    input_dir=$1
    if [[ ! -z "$2" ]] 
    then 
        output_dir=$2
    fi
fi
cd $input_dir

for filename in *.pcd; do
    cd $builddir
    # path, height, width, cameratype
    ./pcd2depth $input_dir $output_dir $filename 480 640 nyu
done