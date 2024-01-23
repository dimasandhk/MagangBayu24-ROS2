from setuptools import setup

package_name = 'tugas_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Dimas Andhika Diputra',
    maintainer_email='dimasandhikadiputra@gmail.com',
    description='2 publisher yang mempublish boolean (true, false) secara bergantian',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = tugas_2.publisher_member_function:main',
            'listener = tugas_2.subscriber_member_function:main'
        ],
    },
)
