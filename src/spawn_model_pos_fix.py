#!/usr/bin/env python
# -*- coding: utf-8 -*-
# gazebo world上に指定した物体をランダムな位置に配置するコード

#import sys
import rospy
import rospkg
from gazebo_msgs.srv import DeleteModel
from gazebo_msgs.srv import SpawnModel
#from std_msgs.msg import Header, Float64, Bool, String, Int16
from geometry_msgs.msg import Pose, Quaternion
from __init__ import *
import tf.transformations as tft
import random
#import argparse

class DropModel:
    # @staticmethod
    def __init__(self):
        pass

    def delete_model(self, model_name):
        rospy.loginfo("Delete_model: " + model_name)
        # Delete the old model if it's stil around
        self.delete_model_prox = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
        self.delete_model_prox(model_name)
        rospy.loginfo("Delete_model")

    # @staticmethod
    def spawn_model(self, model_name):
        rospy.loginfo("Spawn_model: " + model_name)

        # 物体の種類を決める
        # pig_doll
        #o = random.randint(0, len(objects)-1)
        o = 2
        

        # 物体の位置を決める (主観)
        ## doll : living, bedroom 
        ## bottle : living, kitchen
        ## cup : kitchen, toilet
        if o == 0 or o == 1 or o == 2:
            i = random.randrange(2)
            if i == 0:
                p = 0
            else:
                p = 2
        
        elif o == 3 or o == 4 or o == 5:
            i = random.randrange(2)
            if i == 0:
                p = 0
            else:
                p = 1
        
        else:
            i = random.randrange(2)
            if i == 0:
                p = 1
            else:
                p = 3

            
        #p = random.randint(0, len(places)-1)
        

        self.initial_pose = Pose()
        self.initial_pose.position.x = places[p][0]
        self.initial_pose.position.y = places[p][1]
        self.initial_pose.position.z = places[p][2]
        roll = places[p][3]
        pitch = places[p][4]
        yaw = places[p][5]
        tmpq = tft.quaternion_from_euler(roll, pitch, yaw)
        q = Quaternion(tmpq[0], tmpq[1], tmpq[2], tmpq[3])
        self.initial_pose.orientation = q

        # Spawn the new model #
        self.model_path = rospkg.RosPack().get_path('nrp_gazebo_worlds')+'/models/{}/'.format(objects[o])
        self.model_xml = ''
        rospy.loginfo(model_name)
        rospy.loginfo(self.model_path)
        rospy.loginfo("FILEPATH: " + self.model_path + model_name + '.sdf')
        with open (self.model_path + model_name + '.sdf', 'r') as xml_file:
            self.model_xml = xml_file.read().replace('\n', '')
        self.spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        self.spawn_model_prox('training_model', self.model_xml, '', self.initial_pose, 'world')
        rospy.loginfo("Spawn_model")


if __name__ == '__main__':
    rospy.init_node('spawn_model_naito')

    drop_model = DropModel()
    #rospy.logwarn("Customer entering the environment")
    #human_action = sys.argv[1]
    drop_model.spawn_model("model")
