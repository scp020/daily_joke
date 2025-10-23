from setuptools import setup, find_packages

setup(
    name='dailyjoke',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'daily-joke=dailyjoke.main:run',
        ],
    },
    author='your_name',
    author_email='your_email',
    description='一个每日一笑的Python小程序',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_user_name/daily-joke',
)
