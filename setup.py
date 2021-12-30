from pathlib import Path
from setuptools import setup, find_packages

CURRENT_DIR = Path(__file__).parent
LONG_DESCRIPTION = (CURRENT_DIR / "README.md").read_text(encoding="utf-8")

setup(
    name="musttyping",
    version='0.0.1',
    description="Force you (or your user) annotate function types.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="zkonge",
    author_email="zkonge@outlook.com",
    url="https://github.com/zkonge/musttyping",
    packages=find_packages(),
    license="MIT",
    keywords="typing",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",

    ],
)
