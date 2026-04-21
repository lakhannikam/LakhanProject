#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main()
{

    VideoCapture cap(0);

    if (!cap.isOpened())
    {
        cout << "Camera not opened" << endl;
        return -1;
    }

    Mat frame;

    while (true)
    {
        cap >> frame;

        if (frame.empty())
            break;

        Mat hsv, mask;
        cvtColor(frame, hsv, COLOR_BGR2HSV);

        Scalar lower_green(35, 50, 50);
        Scalar upper_green(85, 255, 255);

        inRange(hsv, lower_green, upper_green, mask);

        int green = countNonZero(mask);
        int total = frame.rows * frame.cols;

        double percent = (double)green / total * 100;

        cout << "Green %: " << percent << endl;

        if (percent > 30)
        {
            imwrite("plant.jpg", frame);
            cout << "Photo Captured!" << endl;
            break;
        }
    }

    return 0;
}