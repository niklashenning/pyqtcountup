from setuptools import setup, find_namespace_packages


with open('README.md', 'r') as fh:
    readme = "\n" + fh.read()

setup(
    name='pyqtcountup',
    version='1.0.0',
    author='Niklas Henning',
    author_email='business@niklashenning.com',
    license='MIT',
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'QtPy>=2.4.1'
    ],
    python_requires='>=3.7',
    description='A simple numerical data animation library for PyQt and PySide labels',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/niklashenning/pyqtcountup',
    keywords=['python', 'pyqt', 'qt', 'label', 'animation', 'numerical data'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
    ]
)
