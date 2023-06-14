import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_counts_plot(name, type1, type2):
  x = np.arange(len(type1.index))  # the label locations
  width = 0.35  # the width of the bars

  fig, ax = plt.subplots(figsize=(8, 6))
  rects1 = ax.bar(x - width/2, type1["Name"], width, label='Type1')
  rects2 = ax.bar(x + width/2, type2["Name"], width, label='Type2')

  # Add some text for labels, title and custom x-axis tick labels, etc.
  ax.set_ylabel('Count')
  ax.set_title('Counts by type')
  ax.set_xticks(x, type1.index, rotation=45)
  ax.legend()

  ax.bar_label(rects1, padding=3)
  ax.bar_label(rects2, padding=3)

  fig.tight_layout()

  plt.savefig(name)


def create_cross_plot(name, title, both):
  fig, axs = plt.subplots(5, 4, figsize=(30, 45))
  for i, t in enumerate(both.index.levels[0]):
    x = np.arange(len(both.loc[t]["Name"].index))  # the label locations

    ax = axs[i // 4, i % 4]
    rects1 = ax.bar(x, both.loc[t]["Name"])

    # Add some text for labels, title and custom x-axis tick labels, etc.

    ax.set_title(t)
    ax.set_xticks(x, both.loc[t]["Name"].index, rotation=45)

    ax.bar_label(rects1, padding=3)

    fig.tight_layout()
    fig.suptitle(title, fontsize=20, y=1)

    plt.savefig(name)

def main(args):
  print(args)
  with open(os.path.join(args.dataset, "pokemon.csv")) as f:
    classes = pd.read_csv(f)
    type1 = classes[["Name", "Type1"]].groupby(["Type1"]).count()
    type2 = classes[["Name", "Type2"]].groupby(["Type2"]).count()
    both = classes.groupby(["Type1", "Type2"]).count()
    both2 = classes.groupby(["Type2", "Type1"]).count()

    create_counts_plot(os.path.join(args.plots, "counts.png"), type1, type2)
    create_cross_plot(os.path.join(args.plots, "type1_type2.png"), "Type1 x Type2", both)
    create_cross_plot(os.path.join(args.plots, "type2_type1.png"), "Type2 x Type1", both2)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("dataset")
  parser.add_argument("plots")
  args = parser.parse_args()
  main(args)