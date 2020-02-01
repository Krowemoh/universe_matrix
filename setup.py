import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="universe_matrix",
        version="0.0.1",
        author="Nivethan Thiyagarajah",
        author_email="nivethant@asynchronsystems.com",
        description="Wrapper for Multivalue Data",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/Krowemoh/universe_matrix",
        packages=["universe_matrix"],
        )
