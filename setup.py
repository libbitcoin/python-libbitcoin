import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-libbitcoin",
    version = "1.2.05",
    author = "DarkWallet",
    author_email = "policeterror@dyne.org",
    description = ("Python client side library for libbitcoin-server."),
    license = "AGPL",
    keywords = "bitcoin libbitcoin blockchain library",
    url = "https://github.com/rojavacrypto/python-libbitcoin",
    packages=["libbitcoin"],
    install_requires=["pyzmq", "ecdsa"],
    #long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ],
)

