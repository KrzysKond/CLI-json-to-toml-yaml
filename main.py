import cmd
import json
import toml
import yaml
import os


class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to CLI converting JSON files to YAML OR TOML. Type "help" for available commands.'

    def do_convert_json_to_yaml(self, args):
        """CONVERT JSON FILE TO NEW YAML FILE: TAKES TWO ARGUMENTS, SOURCE OF JSON AND DESTINATION"""
        source, output_file = args.split()
        try:
            with open(source, "r") as json_file:
                data = json.load(json_file)

            with open(output_file, "w") as yaml_file:
                yaml.dump(data, yaml_file)

            print(f"'{output_file}' created in '{os.getcwd()}'")
        except Exception as e:
            print(f"Error: {e}")

    def do_convert_json_to_toml(self, args):
        """CONVERT JSON FILE TO NEW TOML FILE: TAKES TWO ARGUMENTS, SOURCE OF JSON AND DESTINATION"""
        source, output_file = args.split()
        try:
            with open(source, "r") as json_file:
                data = json.load(json_file)

            with open(output_file, "w") as toml_file:
                toml.dump(data, toml_file)

            print(f"'{output_file}' created in '{os.getcwd()}'")
        except Exception as e:
            print(f"Error: {e}")

    def do_exit(self, line):
        """Exit the CLI."""
        return True


if __name__ == '__main__':
    MyCLI().cmdloop()
