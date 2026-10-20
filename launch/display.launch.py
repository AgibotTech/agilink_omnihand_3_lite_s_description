import os

import launch
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):
    del args, kwargs
    hand_type = LaunchConfiguration('hand_type').perform(context)
    if hand_type not in ('left', 'right'):
        raise RuntimeError("hand_type must be 'left' or 'right'")

    package_dir = get_package_share_directory('h3l_s_description')
    urdf_path = os.path.join(
        package_dir, 'urdf', f'h3l_s_{hand_type}.urdf')
    rviz_path = os.path.join(package_dir, 'rviz', 'h3l_s.rviz')
    with open(urdf_path, 'r', encoding='utf-8') as urdf_file:
        robot_description = {'robot_description': urdf_file.read()}

    return [
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            parameters=[robot_description],
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[robot_description],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_path],
            output='screen',
        ),
    ]


def generate_launch_description():
    return launch.LaunchDescription([
        DeclareLaunchArgument(
            'hand_type',
            default_value='right',
            description="Hand type: 'left' or 'right'",
        ),
        OpaqueFunction(function=launch_setup),
    ])
