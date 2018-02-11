#include "pepper_openease_client.h"

#include <stdlib.h>

#include <ros/ros.h>
#include <ros/package.h>

#include <std_msgs/String.h>
#include <std_msgs/Int8.h>
#include <geometry_msgs/PointStamped.h>

#include "knowrob_pepper_openease_msgs/PepperPointAt.h"
#include "knowrob_pepper_openease_msgs/PepperSay.h"

ros::ServiceClient clientPoint;
ros::ServiceClient clientSay;

PREDICATE(ros_init_pepper, 0) {
  int argc=0;
  ros::start();
  ros::init(argc, (char**)NULL, std::string("pepper_server"));
  ros::NodeHandle nh;
  clientPoint = nh.serviceClient<knowrob_pepper_openease_msgs::PepperPointAt>("pepper_point_at");
  clientSay = nh.serviceClient<knowrob_pepper_openease_msgs::PepperSay>("pepper_say");
  return TRUE;
}

// pepper_point_at(xPosition,yPosition,zPosition,frameID,Description)
PREDICATE(pepper_point_at,5) {
  knowrob_pepper_openease_msgs::PepperPointAt srv;
  srv.request.point.header.frame_id = (char*)PL_A4;
  srv.request.point.header.stamp = ros::Time::now();
  srv.request.point.pose.position.x = (double)PL_A1;
  srv.request.point.pose.position.y = (double)PL_A2;
  srv.request.point.pose.position.z = (double)PL_A3;
  if((char*)PL_A5){
    srv.request.description = (char*)PL_A5;
  }

  ros::service::waitForService("pepper_point_at");

  if (!clientPoint.call(srv))
  {
    return FALSE;
  }

  return TRUE;
}

// pepper_say(description)
PREDICATE(pepper_say,1) {
    ROS_ERROR("%s\n", "Starting1");

  knowrob_pepper_openease_msgs::PepperSay srv;
    ROS_ERROR("%s\n", "Starting2");

  srv.request.message = (char*)PL_A1;
    ROS_ERROR("%s\n", "Starting3");


  //ros::service::waitForService("pepper_say");
    ROS_ERROR("%s\n", "Starting4");


  if (!clientSay.call(srv))
  {
    return FALSE;
  }

  return TRUE;

}