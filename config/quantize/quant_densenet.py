# -*- coding: utf-8 -*-
"""Configurations for quantization for simplenet.

- Author: Curt-Park
- Email: jwpark@jmarple.ai
"""

from config.train import densenet_small

config = densenet_small.config
config.update(
    {
        "MODEL_NAME": "quant_densenet",
        "LR_SCHEDULER_PARAMS": dict(warmup_epochs=0, start_lr=1e-4),
        "LR": 1e-4,
        "EPOCHS": 5,
    }
)
