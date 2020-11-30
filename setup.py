# default to setuptools so that 'setup.py develop' is available,
# but fall back to standard modules that do the same
try:
    from setuptools import setup

    scripts = []
except ImportError:
    from distutils.core import setup

    scripts = ["bin/sipeed_ikernel"]

setup(
    name="sipeed_ikernel",
    version="1.4.6",
    description="Running IPython kernels through batch queues",
    author="Tom Daff",
    author_email="junhuanchen@qq.com",
    license="BSD",
    url="https://github.com/junhuanchen/sipeed_ikernel",
    packages=["sipeed_ikernel"],
    scripts=scripts,
    entry_points={"console_scripts": ["sipeed_ikernel = sipeed_ikernel.__main__:main"]},
    install_requires=["jupyter_client", "pexpect", "tornado"],
    tests_requires=["pytest", "scripttest"],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Framework :: IPython",
        "License :: OSI Approved :: BSD License",
    ],
)
