#!/usr/bin/env python
import rospy
from robotnik_msgs.msg import inputs_outputs
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class VerticalLaser:

    def callback_hw(self, data):
        if(data.digital_inputs[self.io_left_laser] == True or data.digital_inputs[self.io_right_laser] == True):
	    #The robot is not able to move
            self.stop = True
        else:
	    #The robot is able to move
            self.stop = False
        
    def callback_cmd(self, data):
        if(not self.stop):
            self.pub.publish(data)
        else:
            self.pub.publish(self.cmd_vel_zero)
    
    def __init__(self):
        rospy.loginfo("Front vertical laser initialize")

        self.prefix = rospy.get_param('~prefix', 'robot_')
        self.io_left_laser = rospy.get_param("~io_left_laser", 3)
        self.io_right_laser = rospy.get_param("~io_right_laser", 4)
        self.topic_in = rospy.get_param('~topic_in', '/robot/robotnik_base_hw/io')
        self.topic_cmd_unsafe = rospy.get_param('~topic_cmd_unsafe', 'move_base/cmd_vel_unsafe')
        self.topic_cmd_safe = rospy.get_param('~topic_cmd_safe', 'move_base/cmd_vel')
        self.stop = False
        self.cmd_vel_zero = Twist()

        rospy.init_node('front_vertical_laser_security', anonymous=False)        

        rospy.Subscriber(self.topic_in, inputs_outputs, self.callback_hw)
        rospy.Subscriber(self.topic_cmd_unsafe, Twist, self.callback_cmd)

        self.pub = rospy.Publisher(self.topic_cmd_safe, Twist, queue_size=10)

        rospy.spin()

if __name__ == '__main__':
    vertical_laser = VerticalLaser()
