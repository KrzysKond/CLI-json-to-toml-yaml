Command Line interpreter running on Docker that converts json files to TOML/YAML.

To run docker use the following lines:

docker build -t my_image --rm .

docker run -it --name my_app --rm my_image

1. Converting to TOML file:
   convert_json_to_toml [source] [destination]
2. Converting to YAML file:
   convert_json_to_yaml [source] [destination]

If the destination file doesn't exist, a new file with the argument's name is created. Providing adequate file extensions (.yaml, .toml), in the destination argument, is vital for the program to work properly.
