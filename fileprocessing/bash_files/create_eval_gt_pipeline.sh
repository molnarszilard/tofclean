#!bin/bash
bashdir=$PWD
builddir=$PWD'/../build/'
work_dir=$PWD'/../../dataset/evaluation/'
filter_type='sor'
if [[ ! -z "$1" ]] 
then 
    work_dir=$1
    if [[ ! -z "$2" ]] 
    then 
        filter_type=$2
    fi
fi
cd $work_dir
mkdir pcd
mkdir pcd_filtered
mkdir depth3/
mkdir depthgt/
cd $bashdir
python3 rename.py --dir=$work_dir'depth/' --ext=.png
bash depth2pcd.sh $work_dir'depth/' $work_dir'pcd/'
case $filter_type in
    sor)
        bash sor.sh $work_dir'pcd/' $work_dir'pcd_filtered/'
        ;;
    voxel)
        bash voxel_filter.sh $work_dir'pcd/' $work_dir'pcd_filtered/'
        ;;
    *)
        bash sor.sh $work_dir'pcd/' $work_dir'pcd_filtered/'
        ;;
esac
bash pcd2depth.sh $work_dir'pcd_filtered/' $work_dir'depthgt/'

python3 rename.py --dir=$work_dir'depthgt/' --ext=.png
python3 rename.py --dir=$work_dir'pcd_filtered/' --ext=.pcd
python3 rename.py --dir=$work_dir'pcd/' --ext=.pcd

bash depth3.sh $work_dir'depth/' $work_dir'depth3/'
python3 rename.py --dir=$work_dir'depth3/' --ext=.png
bash create_mask.sh $work_dir'depthgt/' $work_dir'maskgt/'