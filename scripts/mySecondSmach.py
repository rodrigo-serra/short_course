#!/usr/bin/env python

import rospy
import smach
import smach_ros

# Define state FOO
class Foo(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                            outcomes=['outcome1', 'outcome2'], 
                            input_keys=['foo_counter_in'], 
                            output_keys=['foo_counter_out'])

    def execute(self, ud):
        rospy.loginfo('Executing state FOO!')
        if ud.foo_counter_in < 3:
            ud.foo_counter_out = ud.foo_counter_in + 1
            return 'outcome1'
        else:
            return 'outcome2'


# Define state BAR
class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                            outcomes=['outcome2'],
                            input_keys=['bar_counter_in'])

    def execute(self, ud):
        rospy.loginfo("Executing state BAR!")
        rospy.loginfo("Counter = %f" %ud.bar_counter_in)
        return 'outcome2'

if __name__ == '__main__':
    rospy.init_node('my_smach_state_machine')
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome4', 'outcome5'])
    # Create a state machine variable. Notice that is neither an input of this container nor an output
    sm.userdata.sm_counter = 0

    # Open the container
    with sm:
        #Add states to the container
        smach.StateMachine.add('FOO', Foo(), 
                            transitions={'outcome1': 'BAR', 'outcome2': 'outcome4'},
                            remapping={'foo_counter_in':'sm_counter', 'foo_counter_out':'sm_counter'})

        smach.StateMachine.add('BAR', Bar(), transitions={'outcome2': 'FOO'},
                            remapping={'bar_counter_in':'sm_counter'})

    # Execute SMACH plan
    outcome = sm.execute()
    