# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2022 Intel Corporation
# SPDX-License-Identifier: BSD-3-Clause

# pylint: disable=C0415,E0401,R0914

"""
Run benchmarks for Intelligent Indexing.
"""

import argparse
import logging
import os
import pathlib
import time

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

from utils.preprocessing import (
    clean_headline,
    clean_link,
    clean_short_description,
    tokenize
)
from memory_profiler import profile


def main(flags):
    """Setup model for inference and perform benchmarking

    Args:
        flags: benchmarking flags
    """
    if flags.logfile == "":
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(filename=flags.logfile, level=logging.DEBUG)
    logger = logging.getLogger()

    if flags.intel:
        logging.debug("Loading intel libraries...")

        import modin.pandas as pd
        from sklearnex.svm import SVC
        import ray
        ray.init()

    else:
        logging.debug("Loading stock libraries...")

        import pandas as pd
        from sklearn.svm import SVC
    
    @profile
    def get_data(path_to_csv: str) -> pd.DataFrame:
        """Read in and clean data

        Args:
            path_to_csv (str): processed data
        """
        data = pd.read_csv(path_to_csv)[
            ['category', 'headline', 'short_description', 'link']
        ]
        data = data.dropna(subset=['headline', 'short_description', 'link'])

        data.link = data.link.apply(clean_link)
        data.short_description = data.short_description \
            .apply(clean_short_description)
        data.headline = data.headline.apply(clean_headline)

        data['text'] = data.link + " " + data.short_description \
            + " " + data.headline
        data['tokens'] = data.text.apply(tokenize)
        return data

    # Read and clean training and testing data
    logger.info("Preprocessing Data...")
    start = time.time()

    if not os.path.exists("../data/huffpost/train_all.csv"):
        logger.error(
            "Train data file ../data/huffpost/train_all.csv not found")
        return

    if not os.path.exists("../data/huffpost/test.csv"):
        logger.error("Test data file ../data/huffpost/test.csv not found")
        return

    
    
    train = get_data("../data/huffpost/train_all.csv")
    test = get_data("../data/huffpost/test.csv")
    
    preprocessing_time = time.time()
    logger.info(
        "=======> Preprocessing Time : %.3f secs",
        preprocessing_time - start
    )

    if not flags.preprocessing_only:

        # Build TFIDF features and train the model
        logger.debug("Training & Evaluating Model...")
        
        @profile
        def train_data(train,test):
            vectorizer = TfidfVectorizer(
            min_df=50,
            lowercase=False,
            tokenizer=lambda x: x)
                                            
            svc = SVC()
            svc.fit(vectorizer.fit_transform(train.tokens), train.category)
            training_time = time.time()
            y_pred = svc.predict(vectorizer.transform(test.tokens))
            return svc, training_time, y_pred
        
        
        svc, training_time, y_pred = train_data(train,test)

        prediction_time = time.time()

        if flags.save_model_dir:

            path = pathlib.Path(flags.save_model_dir)
            path.mkdir(parents=True, exist_ok=True)

            with open(path / "model.pkl", 'wb') as outfile:
                joblib.dump(svc, outfile)

        logger.info(
            "=======> Test Accuracy : %.2f",
            accuracy_score(y_pred, test.category)
        )
        logger.info(
            "=======> Training Time : %.3f secs",
            training_time - preprocessing_time
        )
        logger.info(
            "=======> Inference Time : %.3f secs",
            prediction_time - training_time
        )
        logger.info(
            "=======> Total time : %.3f secs",
            prediction_time - start
        )

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-l',
                        '--logfile',
                        type=str,
                        default="",
                        help="log file to output benchmarking results to")

    parser.add_argument('-i',
                        '--intel',
                        default=False,
                        action="store_true",
                        help="use intel accelerated technologies where available"
                        )

    parser.add_argument('-p',
                        '--preprocessing_only',
                        default=False,
                        action="store_true",
                        help='only perform preprocessing step')

    parser.add_argument('-s',
                        '--save_model_dir',
                        default=None,
                        type=str,
                        required=False,
                        help="directory to save model to"
                        )

    main(parser.parse_args())