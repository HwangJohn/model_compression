# -*- coding: utf-8 -*-
"""Configurations for training densenet_small.

- Author: Curt-Park
- Email: jwpark@jmarple.ai
"""

import os

config = {
    "SEED": 777,
    "AUG_TRAIN": "randaugment_train_cifar100",
    "AUG_TRAIN_PARAMS": dict(n_select=2, level=None),
    "CUTMIX": dict(beta=1, prob=0.5),
    "AUG_TEST": "simple_augment_test_cifar100",
    "DATASET": "CIFAR100",
    "MODEL_NAME": "densenet",
    "MODEL_PARAMS": dict(
        num_classes=100,
        inplanes=24,
        block_configs=(32, 32, 32),
        growthRate=12,
        compressionRate=2,
    ),
    "CRITERION": "CrossEntropy",
    "CRITERION_PARAMS": dict(num_classes=100),
    "LR_SCHEDULER": "WarmupCosineLR",
    "LR_SCHEDULER_PARAMS": dict(warmup_epochs=5, start_lr=1e-3),
    "BATCH_SIZE": 64,
    "LR": 0.1,
    "MOMENTUM": 0.9,
    "WEIGHT_DECAY": 1e-4,
    "EPOCHS": 300,
    "N_WORKERS": os.cpu_count(),
}
