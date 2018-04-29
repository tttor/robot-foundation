# [ROS](http://ros.org/)
## Cmd
* system
  * `catkin_create_pkg beginner_tutorials std_msgs rospy roscpp`
  * `catkin_make`
  * `catkin_make --pkg <package A> <package B>` # warn: not robust, see [this](https://answers.ros.org/question/54178/how-to-build-just-one-package-using-catkin_make/)
  * `rostopic list | grep -o -P '^.*(?=/feedback)'` # list action servers from [this](https://answers.ros.org/question/222748/list-action-servers/)
* controller
    * `rosrun controller_manager controller_manager list`
    * `rosservice call /controller_manager/list_controller_types`
* tf
  * `rosrun tf tf_echo <source_frame> <target_frame>`
  * `rosrun tf tf_monitor <source_frame> <target_target>`
  * `rosrun tf view_frames` # generate a pdf
  
## With Gazebo
* `roslaunch gazebo_worlds empty_world.launch` 
* `gzsdf print urdfname.urdf > newname.sdf` # from [here](http://answers.gazebosim.org/question/2282/convert-urdf-to-sdf-or-load-urdf/)

## Best practices
* topics vs services vs actionlib
  * https://answers.ros.org/question/11834/when-should-i-use-topics-vs-services-vs-actionlib-actions-vs-dynamic_reconfigure/
  * http://wiki.ros.org/ROS/Patterns/Communication#Communication_via_Topics_vs_Services_vs_X
* clean_catkin_ws
```
#!/bin/bash
# http://wiki.ros.org/catkin/Tutorials/using_a_workspace#Cleaning_up
# https://answers.ros.org/question/66366/how-to-catkin_make-clean-just-one-package/
rm -rf build devel install
```
* programming guide:
  * http://wiki.ros.org/PyStyleGuide,
  * http://wiki.ros.org/CppStyleGuide
* ref:
  * https://github.com/ethz-asl/ros_best_practices/wiki
    
## Tutorials
* http://wiki.ros.org/ROS/Tutorials
* http://www.clearpathrobotics.com/assets/guides/ros/index.html
* http://jbohren.com/tutorials/2014-02-10-roscpp-hello-world/
* http://jbohren.com/tutorials/2014-02-12-gentle-catkin-intro/
 
## Tools
* Visualize quarternion: http://quaternions.online/
