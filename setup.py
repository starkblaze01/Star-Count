import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="starcount",
    version="0.0.1",
    author="starkblaze01",
    author_email="mp.pathela@gmail.com",
    description="Command Line tool to get total stargazers count of GitHub Repository of any user.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/starkblaze01/Star-Count",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    keywords="GitHub stargazers count stars-count repository",

    entry_points={
        "console_scripts": ['starcount = starcount.starcount:main'],
    },
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.22.0',
        'termcolor>=1.1.0'
    ],
)
