from setuptools import setup

package_name = 'workshop_arm'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
        ],
    },
)
