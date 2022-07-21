#!/usr/bin/env python

import rospy
import rospkg
import sys

def findPkg(pkg_name):
    rp = rospkg.RosPack()
    try:
        rp.get_path(pkg_name)
    except:
        rospy.logerr("The package " + pkg_name + " does not exist")
        sys.exit()

    print("Success!")


if __name__ == '__main__':
    rospy.init_node('find_pkg_path')
    findPkg('evora_topological_map')
    # findPkg('meh')
    print("Sucess 2!")
    rospy.spin()

