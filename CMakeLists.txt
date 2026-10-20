cmake_minimum_required(VERSION 3.8)
project(h3l_s_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  config
  launch
  meshes
  rviz
  urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

