import torch
import toml
import pprint


def main():
    print("Hello from sd-scripts!")

    path = "/home/radius5/workspace/namai/sd-scripts/pyproject.toml"

    t = toml.load(path)
    pprint.pprint(t)


if __name__ == "__main__":
    main()
