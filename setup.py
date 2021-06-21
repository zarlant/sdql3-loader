from setuptools import setup

setup(
  name="sdql-load",
  description="CLI to load SDQL data",
  author="Zacharias Thompson",
  author_email="zarlant@gmail.com",
  package_dir={"": "src"},
  packages=[""],
  install_requires=[
    "requests"
  ],
  entry_points={
    "console_scripts": [
      "sdql-load=cli:main"
    ]
  }
)
