import argparse
import numpy as np
import pandas as pd

from joblib import dump
from sklearn import datasets, svm, tree, preprocessing, metrics
import sklearn.ensemble as ske


def main(args):
    df = pd.read_csv(args.train_set, delimiter=args.delimiter)
    df = df.dropna()
    if args.classifier == "DecisionTreeClassifier":
        classifier = tree.DecisionTreeClassifier(
            max_depth=args.max_depth, random_state=args.random_seed)
    elif args.classifier == "GradientBoostingClassifier":
        classifier = ske.GradientBoostingClassifier(
            n_estimators=args.n_estimators, random_state=args.random_seed)
    else:
        raise ValueError(f"Unknown classifier: '{args.classifier}'")

    train_X = df[[x for x in list(df.columns.values) if x != args.y_column]]
    train_y = df[args.y_column]

    classifier.fit(train_X, train_y)

    dump(classifier, args.trained_model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Train sklearn model")
    parser.add_argument("train_set", type=str, help="train set csv")
    parser.add_argument("trained_model", type=str, help="trained model file")
    parser.add_argument("-y", "--y_column", type=str,
                        required=True, help="class column")
    parser.add_argument("-c", "--classifier", type=str,
                        choices=["DecisionTreeClassifier",
                                 "GradientBoostingClassifier"],
                        required=True, help="classifier")
    parser.add_argument("--max_depth", required=False, type=int)
    parser.add_argument("--n_estimators", required=False, type=int)
    parser.add_argument("--random_seed", required=False, type=int)
    parser.add_argument("-d", "--delimiter", type=str,
                        default=",", help="column delimiter (default: ',')")
    args = parser.parse_args()
    main(args)
