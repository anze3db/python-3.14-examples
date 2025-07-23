import argparse

prameters = argparse.ArgumentParser(description="A simple test script.")
prameters.add_argument("--name", type=str, help="Name of the person to greet.")
args = prameters.parse_args()
