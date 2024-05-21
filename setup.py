from setuptools import setup, find_packages

setup(
    name='talk-document',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'langchain==1.0.0',   
        'numpy==1.21.2',     
        'requests==2.26.0',  
    ],
    entry_points={
        'console_scripts': [
            'talk-document = talkdocument:main',
        ],
    },
    author='Prakshaal Jain',
    author_email='prakshaal@gmail.com',
    description='A Python script for processing and interacting with documents, embeddings, and question-answering chains.',
    url='https://github.com/prakshaaljain/Talk-Document',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
