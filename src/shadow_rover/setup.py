import os
from glob import glob
from setuptools import setup

package_name = 'shadow_rover'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
data_files=[
            ('share/ament_index/resource_index/packages',
                ['resource/' + package_name]),
            ('share/' + package_name, ['package.xml']),
            (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
            (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
            # THESE ARE THE CRITICAL LINES:
            (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
            (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
        ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='The Shadow Rover System',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # We will add scripts here later
        ],
    },
)
