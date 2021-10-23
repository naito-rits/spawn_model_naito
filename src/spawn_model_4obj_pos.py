#!/usr/bin/env python
# -*- coding: utf-8 -*-
# gazebo world上に指定した位置に指定した4つ物体を配置するコード

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

        # 物体の種類を決める (pig_doll)
        #o = random.randint(0, len(objects)-1)
        o = 2

        # 物体の位置の候補数
        #p = random.randint(0, len(places)-1)
        p = 0
        self.initial_pose_0 = Pose()
        self.initial_pose_0.position.x = places[p][0]
        self.initial_pose_0.position.y = places[p][1]
        self.initial_pose_0.position.z = places[p][2]
        roll = places[p][3]
        pitch = places[p][4]
        yaw = places[p][5]
        tmpq = tft.quaternion_from_euler(roll, pitch, yaw)
        q = Quaternion(tmpq[0], tmpq[1], tmpq[2], tmpq[3])
        self.initial_pose_0.orientation = q

        # Spawn the new model #
        self.model_path = rospkg.RosPack().get_path('nrp_gazebo_worlds')+'/models/{}/'.format(objects[o])
        self.model_xml = ''
        rospy.loginfo(model_name)
        rospy.loginfo(self.model_path)
        rospy.loginfo("FILEPATH: " + self.model_path + model_name + '.sdf')
        with open (self.model_path + model_name + '.sdf', 'r') as xml_file:
            self.model_xml = xml_file.read().replace('\n', '')
        self.spawn_model_prox_0 = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        self.spawn_model_prox_0('training_model_0', self.model_xml, '', self.initial_pose_0, 'world')
        rospy.loginfo("Spawn_model")
        
        #######
        p = 1
        self.initial_pose_1 = Pose()
        self.initial_pose_1.position.x = places[p][0]
        self.initial_pose_1.position.y = places[p][1]
        self.initial_pose_1.position.z = places[p][2]
        roll = places[p][3]
        pitch = places[p][4]
        yaw = places[p][5]
        tmpq = tft.quaternion_from_euler(roll, pitch, yaw)
        q = Quaternion(tmpq[0], tmpq[1], tmpq[2], tmpq[3])
        self.initial_pose_1.orientation = q

        # Spawn the new model #
        self.model_path = rospkg.RosPack().get_path('nrp_gazebo_worlds')+'/models/{}/'.format(objects[o])
        self.model_xml = ''
        rospy.loginfo(model_name)
        rospy.loginfo(self.model_path)
        rospy.loginfo("FILEPATH: " + self.model_path + model_name + '.sdf')
        with open (self.model_path + model_name + '.sdf', 'r') as xml_file:
            self.model_xml = xml_file.read().replace('\n', '')
        self.spawn_model_prox_1 = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        self.spawn_model_prox_1('training_model_1', self.model_xml, '', self.initial_pose_1, 'world')
        rospy.loginfo("Spawn_model")

        #######
        p = 2
        self.initial_pose_2 = Pose()
        self.initial_pose_2.position.x = places[p][0]
        self.initial_pose_2.position.y = places[p][1]
        self.initial_pose_2.position.z = places[p][2]
        roll = places[p][3]
        pitch = places[p][4]
        yaw = places[p][5]
        tmpq = tft.quaternion_from_euler(roll, pitch, yaw)
        q = Quaternion(tmpq[0], tmpq[1], tmpq[2], tmpq[3])
        self.initial_pose_2.orientation = q

        # Spawn the new model #
        self.model_path = rospkg.RosPack().get_path('nrp_gazebo_worlds')+'/models/{}/'.format(objects[o])
        self.model_xml = ''
        rospy.loginfo(model_name)
        rospy.loginfo(self.model_path)
        rospy.loginfo("FILEPATH: " + self.model_path + model_name + '.sdf')
        with open (self.model_path + model_name + '.sdf', 'r') as xml_file:
            self.model_xml = xml_file.read().replace('\n', '')
        self.spawn_model_prox_2 = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        self.spawn_model_prox_2('training_model_2', self.model_xml, '', self.initial_pose_2, 'world')
        rospy.loginfo("Spawn_model")

        ######
        p = 3
        self.initial_pose_3 = Pose()
        self.initial_pose_3.position.x = places[p][0]
        self.initial_pose_3.position.y = places[p][1]
        self.initial_pose_3.position.z = places[p][2]
        roll = places[p][3]
        pitch = places[p][4]
        yaw = places[p][5]
        tmpq = tft.quaternion_from_euler(roll, pitch, yaw)
        q = Quaternion(tmpq[0], tmpq[1], tmpq[2], tmpq[3])
        self.initial_pose_3.orientation = q

        # Spawn the new model #
        self.model_path = rospkg.RosPack().get_path('nrp_gazebo_worlds')+'/models/{}/'.format(objects[o])
        self.model_xml = ''
        rospy.loginfo(model_name)
        rospy.loginfo(self.model_path)
        rospy.loginfo("FILEPATH: " + self.model_path + model_name + '.sdf')
        with open (self.model_path + model_name + '.sdf', 'r') as xml_file:
            self.model_xml = xml_file.read().replace('\n', '')
        self.spawn_model_prox_3 = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        self.spawn_model_prox_3('training_model_3', self.model_xml, '', self.initial_pose_3, 'world')
        rospy.loginfo("Spawn_model")


if __name__ == '__main__':
    rospy.init_node('spawn_model_naito')

    drop_model = DropModel()
    #rospy.logwarn("Customer entering the environment")
    #human_action = sys.argv[1]
    drop_model.spawn_model("model")
