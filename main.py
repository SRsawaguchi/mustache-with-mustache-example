import argparse
import yaml
import pystache

parser = argparse.ArgumentParser()
parser.add_argument(
    "-t",
    "--template",
    default="./template.html",
    dest="path_to_template",
)
parser.add_argument(
    "-v",
    "--values",
    default="./values.yaml",
    dest="path_to_values",
)

args = parser.parse_args()

with open(args.path_to_values, "r") as f:
    values = yaml.safe_load(f)

with open(args.path_to_template, "r") as f:
    template = f.read()

output = pystache.render(template, values)
print(output)
