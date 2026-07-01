#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.logging import logging
def generate_launch_description() -> LaunchDescription:
    pkg_dir = get_package_share_directory('h3l_s_description')
    urdf_file = os.path.join(pkg_dir, 'urdf', 'omnihand_3_lite_right.urdf')
    rviz_file = os.path.join(pkg_dir, 'rviz', 'display.rviz')

    with open(urdf_file, 'r', encoding='utf-8') as f:
        robot_description = f.read()
    return LaunchDescription(
        [
            Node(
                package='joint_state_publisher_gui',
                executable='joint_state_publisher_gui',
                name='joint_state_publisher_gui',
                output='screen',
                parameters=[
                    {
                        'robot_description': robot_description
                    }
                ]
            ),
            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                name='robot_state_publisher',
                output='screen',
                parameters=[
                    {
                        'robot_description': robot_description,
                        'use_sim_time': False,
                    }
                ]
            ),
            Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                output='screen',
                arguments=[
                    '-d',
                    rviz_file
                ]
            )

        ]
    )