# OmniHand 3 Lite S description

ROS 2 description package for the OmniHand 3 Lite S (H3L-S) hand. It contains independent left-
and right-hand URDF models and meshes, joint-name references and an RViz2
display launch file.

The distal finger joints are represented by URDF `mimic` joints. The left-hand
model mirrors its mesh geometry in its visual and collision elements, while
retaining its own kinematics and inertial parameters.

## Layout

```text
config/           Left- and right-hand joint-name references
launch/           ROS 2 display launch file
meshes/left/      Left-hand meshes
meshes/right/     Right-hand meshes
rviz/             RViz2 configuration
urdf/             Left- and right-hand URDF models
```

## Build

```bash
colcon build --packages-select h3l_s_description
source install/setup.bash
```

## Display

```bash
ros2 launch h3l_s_description display.launch.py hand_type:=right
ros2 launch h3l_s_description display.launch.py hand_type:=left
```
