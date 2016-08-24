from setuptools import setup

setup(
    name="giffer",
    version="0.1",
    py_modules=['giffer'],
    install_requires=[
        'Click',
        'moviepy',
        'Pillow==2.1.0',
    ],
    entry_points='''
        [console_scripts]
        giffer=giffer:cli
    ''',
)
