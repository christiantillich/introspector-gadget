import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="introspector_gadget", # Replace with your own username
    version="1.0.0",
    author="Christian Tillich",
    author_email="christian.tillich.walker@gmail.com",
    description="A small tool to more helpfully explore objects. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/christiantillich/introspector_gadget",
    #packages=['introspector_gadget'],
    py_modules=['introspector_gadget'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

