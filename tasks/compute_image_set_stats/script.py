import argparse
import os
from PIL import Image
import numpy as np

class OnlineVariance(object):
    """
    Welford's algorithm computes the sample variance incrementally.
    """

    def __init__(self, iterable=None, ddof=1):
        self.ddof, self.n, self.mean, self.M2 = ddof, 0, 0.0, 0.0
        if iterable is not None:
            for datum in iterable:
                self.include(datum)

    def include(self, datum):
        self.n += 1
        self.delta = datum - self.mean
        self.mean += self.delta / self.n
        self.M2 += self.delta * (datum - self.mean)

    def get_mean(self):
        return self.mean

    def get_variance(self):
        return self.M2 / (self.n - self.ddof)

    def get_std(self):
        return np.sqrt(self.get_variance())

def main(args):
  ov = OnlineVariance()
  n = 0
  for img_name in os.listdir(args.images):
    img = Image.open(os.path.join(args.images, img_name)).convert('RGB')
    img = np.array(img, dtype=float)
    img = img / 255.0
    ov.include(np.mean(img, axis=(0, 1)))
    n += 1

  print(f"computed statistics of {n} images")
  with open(args.stats, "w") as sf:
    sf.write("name,value\n")
    sf.write(f"mean,{ov.get_mean()}\n")
    sf.write(f"std,{ov.get_std()}\n")


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("images")
  parser.add_argument("stats")
  args = parser.parse_args()
  main(args)