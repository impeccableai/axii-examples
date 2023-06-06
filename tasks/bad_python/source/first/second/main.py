from source.first.second.functions import f
from source.first.second_b.functions import b
import os


def main():
    p = os.environ.get("PYTHONPATH")
    print(f'PYTHONPATH={p}')
    f()
    b()


if __name__ == "__main__":
    main()
