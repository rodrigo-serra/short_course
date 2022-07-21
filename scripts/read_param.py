#!/usr/bin/env python

import rospy

def sectionIdToName(argument):
    switcher = {
        0: "left_panels",
        1: "central_corridor",
        2: "right_panels",
    }
    return switcher.get(argument, "nothing")

def paramsToCoordinates(section_id, x, y):
    name  = sectionIdToName(section_id)
    # Central corridor has no columns
    if section_id == 1:
        wp_str = "/evora_map/" + name + "/row/" + str(x)
    else:
        wp_str = "/evora_map/" + name + "/row/" + str(x) + "/column/" + str(y)

    wp_param = rospy.get_param(wp_str)
    coord = wp_param.split(",")
    return float(coord[0]), float(coord[1])

def readMultiParameter(section_id, x):
    name  = sectionIdToName(section_id)
    if section_id == 1:
        wp_str = "/evora_map/" + name + "/row/"
    else:
        wp_str = "/evora_map/" + name + "/row/" + str(x)

    wp_list = rospy.get_param(wp_str)
    print(wp_list)
    print(len(wp_list))
    print(wp_list['16'])

def checkParameterExist(section_id, x):
    name  = sectionIdToName(section_id)
    if section_id == 1:
        wp_str = "/evora_map/" + name + "/row/"
    else:
        wp_str = "/evora_map/" + name + "/row/" + str(x)
    
    print(rospy.has_param(wp_str))

def getFirstParameter(section_id, x):
    name  = sectionIdToName(section_id)
    if section_id == 1:
        wp_str = "/evora_map/" + name + "/row/"
    else:
        wp_str = "/evora_map/" + name + "/row/" + str(x)

    wp_list = rospy.get_param(wp_str)
    print((wp_list.keys()))
    print(min(list(map(int, wp_list.keys()))))

if __name__ == '__main__':
    rospy.init_node('read_param_evora_topmap')
    lat, lon = paramsToCoordinates(2, 15, 3)
    print(lat, lon)
    print(lon)
    # readMultiParameter(1, 0)
    # checkParameterExist(1, 0)
    # getFirstParameter(1, 0)
    rospy.spin()
