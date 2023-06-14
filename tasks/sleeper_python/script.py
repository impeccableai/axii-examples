import argparse
import time


def main(args):
    print(f'starting long running python for {args.duration}', flush=True)
    for s in range(args.duration // args.step_duration):
        for v in range(args.step_duration):
            print(f'{s}:{v}', flush=True)
            time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=int, default=900)
    parser.add_argument("--step_duration", type=int, default=60)
    main(parser.parse_args())
