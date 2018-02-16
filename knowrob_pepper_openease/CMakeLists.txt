cmake_minimum_required(VERSION 2.8.3)
project(knowrob_pepper_openease)

find_package(catkin REQUIRED COMPONENTS rospy roscpp tf roslib geometry_msgs rospack knowrob_pepper_openease_msgs knowrob_common knowrob_vis knowrob_mongo knowrob_cram)

catkin_package(CATKIN_DEPENDS roscpp roslib message_runtime rospack geometry_msgs knowrob_pepper_openease_msgs)

find_package(PkgConfig)
pkg_check_modules(SWIPL REQUIRED swipl)
message(STATUS "SWIPL found.")

include_directories(include ${SWIPL_INCLUDE_DIRS} ${catkin_INCLUDE_DIRS})
add_library(pepper_openease_client SHARED src/pepper_openease_client.cpp)
target_link_libraries(pepper_openease_client ${SWIPL_LIBRARIES} ${catkin_LIBRARIES})
add_dependencies(pepper_openease_client knowrob_pepper_openease_msgs_gencpp)

install(DIRECTORY prolog/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/prolog)