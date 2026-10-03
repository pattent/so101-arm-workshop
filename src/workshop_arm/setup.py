from glob import glob

from setuptools import setup

package_name = 'workshop_arm'


setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pattent LLC',
    maintainer_email='jeffreypattison@pattentllc.com',
    description='Beginner-friendly Python helper for moving the SO-101 arm through MoveIt.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'demo = workshop_arm.demo:main',
            'sim_camera = workshop_arm.sim_camera:main',
            'block_detector = workshop_arm.block_detector:main',
            'spawn_blocks = workshop_arm.spawn_blocks:main',
            'vision_demo = workshop_arm.vision_demo:main',
        ],
    },
)
