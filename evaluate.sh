#!bin/bash
bashdir=$PWD'/fileprocessing/bash_files/'
builddir=$PWD'/fileprocessing/build/'
evaldir=$PWD'/dataset/evaluation/'

rm -rf $evaldir'depth_pred/'
mkdir $evaldir'depth_pred'
python eval.py

cd $evaldir

rm -rf pcd_pred/
mkdir pcd_pred/

rm -rf mask/
mkdir mask/

rm -rf mask_diff/
mkdir mask_diff/

# rm -rf pcd_pred_mask/
# mkdir pcd_pred_mask/

cd $bashdir
# python rename.py --dir=$evaldir'depth_pred/' --ext=.png
bash depth2pcd.sh $evaldir'depth_pred/' $evaldir'pcd_pred/'
# python rename.py --dir=$evaldir'pcd_pred/' --ext=.pcd
bash create_mask.sh $evaldir'depth_pred/' $evaldir'mask/'
# python rename.py --dir=$evaldir'mask/' --ext=.png
# bash depthmask2pcd.sh $evaldir'depth/' $evaldir'mask/' $evaldir'pcd_pred_mask/'
# python rename.py --dir=$evaldir'pcd_pred_mask/' --ext=.pcd

echo Prediction
# bash pw_compare.sh own depth
bash maskcompare.sh $evaldir'maskgt/' $evaldir'mask/' $evaldir'mask_diff/'