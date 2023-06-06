import argparse
import os
import shutil
import numpy as np
import pandas as pd
import csv

import torch
import torchvision
import torchvision.transforms as transforms

import torch.nn as nn
import torch.nn.functional as F

import torch.optim as optim
from torch.nn.utils import parameters_to_vector

from PIL import Image

class PokemonsDataset(torch.utils.data.Dataset):
    def __init__(self, df, root_dir, transform=None):
        self.pokemons_df = df
        self.root_dir = root_dir
        self.transform = transform
        self.classes = self.pokemons_df["Type1"].unique().tolist()
        self.classes_dict = {cls: id for id, cls in enumerate(self.classes)}

    def __len__(self):
        return len(self.pokemons_df)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = os.path.join(self.root_dir, self.pokemons_df.iloc[idx, 0] + ".png")
        try:
            image = Image.open(img_name).convert('RGB')
        except FileNotFoundError:
            img_name = os.path.join(self.root_dir, self.pokemons_df.iloc[idx, 0] + ".jpg")
            image = Image.open(img_name).convert('RGB')
        cls = self.classes_dict[self.pokemons_df.iloc[idx]["Type1"]]

        if self.transform:
            image = self.transform(image)

        sample = {'image': image, 'class': torch.tensor(cls)}

        return sample

class Net(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.layers = nn.Sequential(
                    nn.Conv2d(3, 6, 3),
                    nn.MaxPool2d(2, 2),
                    nn.BatchNorm2d(6),
                    nn.ReLU(),

                    nn.Conv2d(6, 12, 5),
                    nn.MaxPool2d(2, 2),
                    nn.BatchNorm2d(12),
                    nn.ReLU(),

                    nn.Flatten(),

                    nn.Linear(5808, 128),
                    nn.ReLU(),
                    nn.Dropout(p=0.5),

                    nn.Linear(128, num_classes),
                    )

    def forward(self, x):
        return self.layers(x)

def train_epoch(loader, net, optimizer, criterion):
    for i, data in enumerate(loader):
        # get the inputs; data is a list of [inputs, labels]
        inputs = data["image"]
        clss = data["class"]

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, clss)
        loss.backward()
        optimizer.step()

def run_model(loader, net, criterion):
    epoch_loss = 0
    epoch_acc = 0
    count = 0
    with torch.no_grad():
        for _, data in enumerate(loader):
            inputs = data["image"]
            clss = data["class"]
            count += len(clss)
            outputs = net(inputs)
            loss = criterion(outputs, clss)
            epoch_loss += loss.item()
            predictions = torch.argmax(outputs, 1)
            epoch_acc += np.sum(np.array(predictions) == np.array(clss))
    return epoch_acc / count, epoch_loss / count

def read_pokemon_stats(file_name):
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for row in reader:
            values = [v for v in row["value"].strip("[").strip("]").split(" ") if v != '']
            if row["name"] == "mean":
                pokemons_mean = list(map(float, values))
            elif row["name"] == "std":
                pokemons_std = list(map(float, values))
    return pokemons_mean, pokemons_std

def main(args):
    np.random.seed(args.random_seed)
    torch.random.manual_seed(args.random_seed)

    pokemons_df = pd.read_csv(args.pokemon_csv)

    pokemons_mean, pokemons_std = read_pokemon_stats(args.pokemon_stats_file)
    print("read stats:", pokemons_mean, pokemons_std)

    batch_size = args.batch_size
    transform = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(pokemons_mean, pokemons_std),
                transforms.CenterCrop(100),
            ]
        )
    dataset = PokemonsDataset(pokemons_df, os.path.join(args.dataset), transform)
    loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=0)

    classes = pokemons_df["Type1"].unique().tolist()

    net = Net(len(classes) if args.num_classes == -1 else args.num_classes)

    if args.saved_model:
        net.load_state_dict(torch.load(args.saved_model))
        print("loaded saved model")

    print(net)
    print("model parameters count:", parameters_to_vector(net.parameters()).numel())

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(net.parameters(), lr=args.learning_rate, weight_decay=0.001)

    if args.mode == "training":
        for epoch in range(args.epochs):
            train_epoch(loader, net, optimizer, criterion)
            epoch_acc, epoch_loss = run_model(loader, net, criterion)
            print(f"epoch {epoch+1} finished | train acc: {epoch_acc:.4f}\ttrain loss: {epoch_loss:.4f}")

        print("finished training")

        torch.save(net.state_dict(), args.trained_model)
        print("saved model")

    if args.mode == "inference":
        loss, acc = run_model(loader, net, criterion)
        print(f"accuracy: {acc:.4f}\tloss: {loss:.4f}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # inputs
    parser.add_argument("--pokemon_stats_file", help="file with precomputed pokemons mean and std", type=str, required=True)
    parser.add_argument("--pokemon_csv", help="file with image->class mappings", type=str, required=True)
    parser.add_argument("--dataset", help="dir with images", type=str, required=True)
    parser.add_argument("--saved_model", help="previously saved model to load", type=str, required=False, default="")
    # output
    parser.add_argument("--trained_model", help="trained model output", type=str, required=False, default="")
    # parameters
    parser.add_argument("--mode", help="mode: training/inference", type=str, required=False, default="training")
    parser.add_argument("--epochs", help="number of epochs to train", type=int, required=False, default=10)
    parser.add_argument("--batch_size", help="the batch size", type=int, required=False, default=4)
    parser.add_argument("--learning_rate", help="the learning rate", type=float, required=False, default=1e-3)
    parser.add_argument("--random_seed", help="random seed", type=int, required=False, default=42)
    parser.add_argument("--num_classes", help="number of classes", type=int, required=False, default=-1)
    main(parser.parse_args())
