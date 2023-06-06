import argparse

def main(args):
  with open(args.output, "w") as out_file:
    handles = []
    for input in args.inputs:
      handles.append(open(input))
    for lines in zip(*handles):
      lines = map(lambda x: x.strip(), lines)
      out_file.write(args.delimiter.join(lines) + "\n")
    for h in handles:
      h.close()

if __name__ == "__main__":
  parser = argparse.ArgumentParser("Stack files")
  parser.add_argument("inputs", nargs="+", type=str, help="input file(s)")
  parser.add_argument("-o", "--out_file", dest="output", required=True, type=str, help="output file")
  parser.add_argument("-d", "--delimiter", default=",", type=str, help="delimiter")
  args = parser.parse_args()
  main(args)