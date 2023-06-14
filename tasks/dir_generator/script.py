import argparse


def main(args):
    for i in range(args.count):
        with open(f'{args.output}/{i}', 'w') as f:
            f.write(f'test line: {i}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--output", type=str, required=True)
    main(parser.parse_args())
