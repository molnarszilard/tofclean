#!bin/bash
bashdir=$PWD
builddir=$PWD'/../build/'
evaldir=$PWD'/../../dataset/evaluation/'
cd $1
mkdir pcd
mkdir pcd_filtered
mkdir depth_filtered
mkdir evaluation
mkdir evaluation/depth3/
mkdir evaluation/depthgt/
mkdir evaluation/depth/
mkdir evaluation/depth_pred/
mkdir evaluation/pcdgt
mkdir evaluation/pcd
cp depth/* evaluation/depth/
cd $bashdir
python3 rename.py --dir=$1evaluation/depth/ --ext=.png
bash depth2pcd.sh $1depth/ $1pcd/
case $2 in
    sor)
        bash sor.sh $1pcd/ $1pcd_filtered/
        ;;
    voxel)
        bash voxel_filter.sh $1pcd/ $1pcd_filtered/
        ;;
    *)
        bash sor.sh $1pcd/ $1pcd_filtered/
        ;;
esac
bash pcd2depth.sh $1pcd_filtered/ $1depth_filtered/

python3 rename.py --dir=$1depth_filtered/ --ext=.png
python3 rename.py --dir=$1pcd_filtered/ --ext=.pcd
python3 rename.py --dir=$1pcd/ --ext=.pcd

bash depth3.sh $1evaluation/depth/ $1evaluation/depth3/
python3 rename.py --dir=$1evaluation/depth3/ --ext=.png

cd $1
cp depth_filtered/* evaluation/depthgt/
cp pcd_filtered/* evaluation/pcdgt/
cp pcd/* evaluation/pcd/