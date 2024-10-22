from setuptools import setup

setup(name="hwo_sci_eng",
      version="0.1.2",
      description="HWO Science Engineering Interface", 
      author="Breann Sitarski, NASA/GSFC, Jason Tumlinson, STScI", 
      author_email=" ",
      license="CC",
      keywords=["simulation", "astronomy", "astrophysics"],
      url="https://github.com/HWO-GOMAP-Working-Groups/Sci-Eng-Interface", 
      packages=["obs_config", "json", "utils"], 
      package_data={'':['*.yaml', '*.json', 'json/*json', 'obs_config/*.yaml']}, 
      include_package_data=True,
      classifiers=[
          "Programming Language :: Python :: 3.6",
      ],
      install_requires=[
            "setuptools>=61.0", 
      ],
)
