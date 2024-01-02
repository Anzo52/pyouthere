from setuptools import setup, find_packages

setup(
    name='pyouthere',
    version='0.1.0',
    description='A Python application to detect human presence in images',
    author='Anzo52',  # Replace with your name
    author_email='andy@zollnersolutions.com',  # Replace with your email
    url='https://github.com/Anzo52/pyouthere',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[
        'numpy>=1.26.2',
        'opencv-python>=4.9.0.80',
        'simple-term-menu>=1.6.4'
    ],
    entry_points={
        'console_scripts': [
            'pyyouthere=main:main',  # Change this line
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
