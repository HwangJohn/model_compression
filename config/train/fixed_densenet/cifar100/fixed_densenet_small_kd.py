# -*- coding: utf-8 -*-
"""Configurations for knowledge distillation with densenet.

- Author: Junghoon Kim
- Email: jhkim@jmarple.ai
"""

from config.train.fixed_densenet.cifar100 import fixed_densenet_small

config = fixed_densenet_small.config
config_override = {
    "CRITERION": "HintonKLD",
    "CRITERION_PARAMS": dict(
        T=4.0,
        alpha=0.9,
        teacher_model_name="densenet",
        teacher_model_params=dict(
            depth=190, growthRate=40, compressionRate=2, num_classes=100
        ),
        crossentropy_params=dict(num_classes=100),
    ),
    "LR_SCHEDULER": "WarmupCosineLR",
    "LR_SCHEDULER_PARAMS": dict(warmup_epochs=3, start_lr=1e-4),
    "BATCH_SIZE": 32,
    "LR": 0.1,
    "MOMENTUM": 0.9,
    "WEIGHT_DECAY": 1e-4,
    "EPOCHS": 5,
}
config.update(config_override)
