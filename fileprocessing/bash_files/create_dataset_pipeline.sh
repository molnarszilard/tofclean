#!bin/bash
builddir=$PWD'/../build/'
evaldir=$PWD'/../../dataset/evaluation/'
cd $1
mkdir depth_aug
mkdir pcd_aug
mkdir pcd_aug_filtered
mkdir depth_aug_filtered
mkdir dataset
mkdir dataset/gt
mkdir dataset/noisy
mkdir dataset/gt/test
mkdir dataset/noisy/test
mkdir dataset/gt/train
mkdir dataset/noisy/train

cp depth/* depth_aug/
cd $bashdir
python3 augmentation.py --dir=$1depth_aug/
python3 rename.py --dir=$1depth_aug/ --ext=.png

bash depth2pcd.sh $1depth_aug/ $1pcd_aug/
case $2 in
    sor)
        bash sor.sh $1pcd_aug/ $1pcd_aug_filtered/
        ;;
    voxel)
        bash voxel_filter.sh $1pcd_aug/ $1pcd_aug_filtered/
        ;;
    *)
        bash sor.sh $1pcd_aug/ $1pcd_aug_filtered/
        ;;
esac
bash pcd2depth.sh $1pcd_aug_filtered/ $1depth_aug_filtered/
python3 rename.py --dir=$1depth_aug_filtered/ --ext=.png

cd $1
cp depth_aug/* dataset/noisy/
cp depth_aug_filtered/* dataset/gt/

cd $bashdir
python3 create_train.py --dir=$1dataset/gt/
python3 create_train.py --dir=$1dataset/noisy/