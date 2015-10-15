from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


# also update in nsq/version.py
version = '0.6.8'

PY3 = sys.version_info >= (3, 0)

TESTS_REQUIRE = [
    'pytest',
    'simplejson',
    'python-snappy',
]

if not PY3:
    TESTS_REQUIRE.append('mock')


setup(
    name='pynsq',
    version=version,
    description='official Python client library for NSQ',
    keywords='python nsq',
    author='Matt Reiferson',
    author_email='snakes@gmail.com',
    url='https://github.com/nsqio/pynsq',
    download_url=(
        'https://s3.amazonaws.com/bitly-downloads/nsq/pynsq-%s.tar.gz' %
        version
    ),
    packages=['nsq'],
    install_requires=['tornado'],
    include_package_data=True,
    zip_safe=False,
    tests_require=TESTS_REQUIRE,
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
