
#include <fstream>
#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <string>

using namespace std;
using namespace cv;

int main(int argc, char **argv)
{
    std::string ddir = argv[1];
    std::string d3dir = argv[2];
    std::string dfilename = argv[3];
    char file_depth[200];
    sprintf(file_depth, "%s%s", ddir.c_str(), dfilename.c_str());
    char file_depth3[200];
    sprintf(file_depth3, "%s%s", d3dir.c_str(), dfilename.c_str());

    cv::Mat mat_depth = cv::imread(file_depth, CV_LOAD_IMAGE_UNCHANGED);
    cv::Mat zerochannel = cv::Mat::zeros(cv::Size(mat_depth.rows, mat_depth.cols), CV_16U);
    cv::Mat output = cv::Mat::zeros(mat_depth.rows, mat_depth.cols, CV_16UC3);
    cv::Mat images[3] = {mat_depth, mat_depth, mat_depth};
    int dims[3] = {2, mat_depth.rows, mat_depth.cols};
    cv::Mat joined(3, dims, CV_16U);
    for (int i = 0; i < 3; i++)
    {
        uint16_t *ptr = &joined.at<uint16_t>(i, 0, 0);                            // pointer to first element of slice i
        cv::Mat destination(mat_depth.rows, mat_depth.cols, CV_32S, (void *)ptr); // no data copy, see documentation
        images[i].copyTo(destination);
    }

    for (int x = 0; x < images[0].rows; x++)
    {
        for (int y = 0; y < images[0].cols; y++)
        {
            output.at<cv::Vec3s>(x, y)[2] = images[0].at<unsigned short>(x, y);
            output.at<cv::Vec3s>(x, y)[1] = images[1].at<unsigned short>(x, y);
            output.at<cv::Vec3s>(x, y)[0] = images[2].at<unsigned short>(x, y);
        }
    }
    cv::imwrite(file_depth3, output);

    return (0);
}
