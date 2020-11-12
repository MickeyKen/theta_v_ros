#!/usr/bin/env python
import os
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import datetime

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "dummy"

def operator():
    rospy.init_node('operator', anonymous=True)
    pub = rospy.Publisher('camera/color/image_raw', Image, queue_size=10)

    # make bridge
    bridge = CvBridge()

    rate = rospy.Rate(20) # 1hz
    vcap = cv2.VideoCapture("http://127.0.0.1:8000/")
    while not rospy.is_shutdown():
        ret,frame = vcap.read()
        msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        operator()
    except rospy.ROSInterruptException:
        pass
