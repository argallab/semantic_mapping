from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package = "tf2_ros", 
            executable = "static_transform_publisher",
            arguments = ["0", "0", "0", "0", "0", "0", "base_camera", "camera_link"]
        ),

        Node(
            package='landmark_manager',
            executable='semantic_labeling',
            name='semantic_labeling'
        )
    ])