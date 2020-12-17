#!/usr/bin/env python
import rospy
from robotnik_msgs.msg import inputs_outputs

class VerticalLaser:
    def pantalla(self, data):
        print(data)

    def callback(self, data):
        print("Se recibio' algo\n")
        rospy.loginfo("Input 2 %b", data.digital_inputs[2])
        rospy.loginfo("Input 3 %b", data.digital_inputs[3])
    
    def __init__(self):
        rospy.loginfo("Nodo ejecutado correctamente")
        self.topic = rospy.get_param('~topic', '/rb1_base/robotnik_base_hw/io')
        self.frame_id = rospy.get_param('~frame_id', 'front_vertical_laser')


        rospy.init_node('front_vertical_laser_driver', anonymous=False)

        rospy.Subscriber(self.topic, inputs_outputs, self.callback)
        rospy.spin()

if __name__ == '__main__':
    vertical_laser = VerticalLaser()