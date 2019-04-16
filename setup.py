import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="encdecpy",
    version="0.0.1",
    author="Atharva Kulkarni",
    author_email="amk11@iitbbs.ac.in",
    description="Python Package to encode and decode strings using ciphers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='encode decode cryptography ciphers encryption decryption',
    url="https://github.com/IronVenom/encdecpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)