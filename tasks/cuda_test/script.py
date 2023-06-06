import argparse
import torch


def main(args):
    available = torch.cuda.is_available()
    print(f"cuda: {available}")
    if available:
        for i in range(torch.cuda.device_count()):
            print(f"device: {torch.cuda.get_device_name(i)}")
    else:
        exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args())
