from setuptools import setup
import os
from glob import glob

package_name = 'px4_ros_visualizer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'px4_ros_visualizer.px4_visualizer'
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Atar Babgei',
    maintainer_email='atarbabgei@gmail.com',
    description='A package to visualize PX4 data in ROS 2',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'px4_visualizer = px4_ros_visualizer.px4_visualizer:main'
        ],
    },
)
