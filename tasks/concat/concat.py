import argparse

def main(args):
  with open(args.output, "w") as out_file:
    for input in args.inputs:
      with open(input) as input_file:
        for line in input_file:
          out_file.write(line)

if __name__ == "__main__":
  parser = argparse.ArgumentParser("Concat files")
  parser.add_argument("inputs", nargs="+", type=str, help="input file(s)")
  parser.add_argument("-o", "--out_file", dest="output", required=True, type=str, help="output file")
  args = parser.parse_args()
  main(args)