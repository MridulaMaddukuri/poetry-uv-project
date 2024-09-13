# poetry-to-uv-project

Efficiently switch from Poetry to uv in your Python project

## Instructions

1. In the root folder of your poetry project with `pyproject.toml` file, run the following commands
   `wget https://raw.githubusercontent.com/MridulaMaddukuri/poetry-uv-project/master/poetry-to-uv.sh` to download the bash script 
   `bash poetry-to-uv.sh` to modify the pyproject.toml file to be uv compatible
2. To update your project to uv
   `uv sync`
   This will create a `uv.lock` file in your root folder

## References
1. `poetry-to-uv.sh` script is from [this amazing guide](https://dev.to/abbazs/transform-poetry-based-pyprojecttoml-to-uv-compatible-format-with-a-bash-script-3hem), only slightly modified