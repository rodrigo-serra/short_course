#!/usr/bin/env python

import rospy
import smach

# Define state FOO
class Foo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1', 'outcome2'])
        self.counter = 0

    def execute(self, ud):
        rospy.loginfo('Executing state FOO!')
        if self.counter < 3:
            self.counter += 1
            return 'outcome1'
        else:
            return 'outcome2'


# Define state BAR
class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome2'])

    def execute(self, ud):
        rospy.loginfo("Executing state BAR!")
        return 'outcome2'

if __name__ == '__main__':
    rospy.init_node('my_smach_state_machine')
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome4', 'outcome5'])
    # Open the container
    with sm:
        #Add states to the container
        smach.StateMachine.add('FOO', Foo(), transitions={'outcome1': 'BAR', 'outcome2': 'outcome4'})
        smach.StateMachine.add('BAR', Bar(), transitions={'outcome2': 'FOO'})

    # Execute SMACH plan
    outcome = sm.execute()
