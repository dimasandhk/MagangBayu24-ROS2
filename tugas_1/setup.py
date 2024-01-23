from setuptools import setup

package_name = 'tugas_1'

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
    maintainer='Dimas Andhika',
    maintainer_email='dimasandhikadiputra@gmail.com',
    description='Mempublish secara random permasalahan matematika sederhana dengan format: (num1) (opr1) (num2) (opr2) (num3)',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = tugas_1.publisher_member_function:main',
            'listener = tugas_1.subscriber_member_function:main'
        ],
    },
)
