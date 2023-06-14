import argparse
import shutil
import os

def main(args):
  src_path = os.path.join(args.in_dir, args.name)
  for f in os.listdir(src_path):
    shutil.copy2(os.path.join(src_path, f), args.out)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("in_dir")
  parser.add_argument("out")
  parser.add_argument("--name")
  args = parser.parse_args()
  main(args)