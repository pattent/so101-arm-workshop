from glob import glob

from setuptools import find_packages, setup

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Exercise 4: install the launch files, so `ros2 launch my_robot ...` can find them.
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@example.com',
    description='My own nodes and launch files for the SO-101 workshop',
    license='MIT',
    entry_points={
        'console_scripts': [
            'hello = my_robot.hello:main',
            # Exercise 3: `ros2 run my_robot safety_monitor` runs main() in safety_monitor.py.
            'safety_monitor = my_robot.safety_monitor:main',
        ],
    },
)
