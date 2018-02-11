cmake_minimum_required(VERSION 2.8.3)
project(knowrob_pepper_openease_msgs)

find_package(catkin REQUIRED COMPONENTS
    message_generation std_msgs geometry_msgs
)

add_service_files(
  FILES
  PepperSay.srv
  PepperPointAt.srv
)

generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS std_msgs geometry_msgs)
