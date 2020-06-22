# -*- coding: utf-8 -*-
"""Configurations for autoaugmentation test.

- Author: Curt-Park
- Email: jwpark@jmarple.ai
"""

import os

# available for trainer only
config = {
    "SEED": 777,
    "AUG_TRAIN": "autoaugment_train_cifar100",
    "AUG_TEST": "simple_augment_test_cifar100",
    "DATASET": "CIFAR100",
    "MODEL_NAME": "densenet",
    "MODEL_PARAMS": dict(depth=100, num_classes=100, growthRate=12, compressionRate=2),
    "BATCH_SIZE": 32,
    "START_LR": 1e-5,
    "LR": 0.1,
    "MOMENTUM": 0.9,
    "WEIGHT_DECAY": 1e-4,
    "WARMUP_EPOCHS": 10,
    "EPOCHS": 300,
    "N_WORKERS": os.cpu_count(),
}