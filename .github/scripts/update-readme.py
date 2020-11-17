#!/usr/bin/env python3
import argparse
import os
import subprocess

def countTpl(path):
	return len(os.listdir(path))

def command(args, start=None, end=None):
	return "\n".join(subprocess.run(args, text=True, capture_output=True).stdout.split("\n")[start:end])[:-1]

if __name__ == "__main__":
	version = command(["git", "describe", "--tags", "--abbrev=0"])
	template = eval(open('.github/scripts/README.tmpl', 'r').read())

	print(template)
	f = open("README.md", "w")
	f.write(readme)
	f.close()