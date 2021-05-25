#!bin/bash
builddir=$PWD'/../build/'
evaldir=$PWD'/../../dataset/evaluation/'

# path, leaf size, meanK, StddevMulThresh
histo=histogram_$1.txt
start=0
end=1449
gtdir=$evaldir$2gt/

case $1 in
    base) # original noisy data
    echo BASE
        preddir=$evaldir$2/
        ;;
    own) # toffilter prediction
        echo ToFFilter
        preddir=$evaldir$2_pred/
        ;;
    ownmask) # toffilter prediction with mask
        echo ToFFilterMask
        preddir=$evaldir'pcd_pred_mask/'
        ;;
    *) # toffilter
        echo Undefined, ToFFilter
        preddir=$evaldir$2_pred/
        ;;    
esac
# echo $preddir
cd $builddir
step=1
case $2 in
    depth)
        echo depth
        gtending=.png
        predending=.png
        ./pw_depthcompare $gtdir $preddir $gtending $predending $start $end $step
        ;;
    pcd)
        echo pcd
        predending=.pcd
        ./pw_pcdcompare $gtdir $preddir $gtending $predending $start $end $step nyu 480 640
        ;;
    *)
        predending=.png
        gtending=.png
        ./pw_depthcompare $gtdir $preddir $gtending $predending $start $end $step
        ;;
esac