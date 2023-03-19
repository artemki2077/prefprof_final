from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'packages': ['PySide6', 'requests'],
    'plist': {
        'CFBundleDevelopmentRegion': 'English',
        'CFBundleIdentifier': "com.ballesta.xxx",
        'CFBundleVersion': "1.0.0",
        'NSHumanReadableCopyright': u"Copyright © 2020, Serge Ballesta, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)