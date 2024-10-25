from setuptools import setup

setup(name="hwo_sci_eng",
      version="0.1.5",
      description="HWO Science Engineering Interface", 
      author="Breann Sitarski, NASA/GSFC, Jason Tumlinson, STScI", 
      author_email=" ",
      license="CC",
      keywords=["simulation", "astronomy", "astrophysics"],
      url="https://github.com/HWO-GOMAP-Working-Groups/Sci-Eng-Interface", 
      packages=["hwo_sci_eng/obs_config", "hwo_sci_eng/json", "hwo_sci_eng/utils"], 
      package_data={'':['*.yaml', '*.json', 'json/*json', 'hwo_sci_eng/obs_config/*.yaml', 'hwo_sci_eng/obs_config/CI/*yaml', 'hwo_sci_eng/obs_config/Detectors/*yaml', 'hwo_sci_eng/obs_config/HRI/*yaml', 'hwo_sci_eng/obs_config/Tel/*yaml', 'hwo_sci_eng/obs_config/UVI/*yaml']}, 
      include_package_data=True,
      classifiers=[
          "Programming Language :: Python :: 3.6",
      ],
      install_requires=[
            "setuptools>=61.0", 
      ],
)
