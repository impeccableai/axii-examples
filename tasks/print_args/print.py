import argparse

def main(args):
  for inp in args.inputs:
    print("input:", inp)
  print("arg:", args.arg)

if __name__ == "__main__":
  parser = argparse.ArgumentParser("Print args")
  parser.add_argument("inputs", nargs="+", type=str, help="inputs")
  parser.add_argument("--arg", type=str, help="parameters")
  args = parser.parse_args()
  main(args)