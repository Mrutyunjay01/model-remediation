# coding=utf-8
# Copyright 2022 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Implementation of Pairwise Cosine Loss."""

from typing import Optional

import tensorflow as tf

from tensorflow_model_remediation.common import types
from tensorflow_model_remediation.counterfactual.losses import base_loss


@tf.keras.utils.register_keras_serializable()
class PairwiseCosineLoss(base_loss.CounterfactualLoss):

  """Pairwise cosine loss between the original and counterfactual.

  Arguments:
    name: Name used for logging and tracking. Defaults to
      `'pairwise_cosine_loss'`.
  """

  # pyformat: enable

  def __init__(self, name: Optional[str] = None):
    """Initialize an instance of Pairwise Cosine Loss."""
    super(PairwiseCosineLoss,
          self).__init__(name=name or "pairwise_cosine_loss")

  def call(self,
           original: types.TensorType,
           counterfactual: types.TensorType,
           sample_weight: Optional[types.TensorType] = None):
    """Computes the pairwise cosine distance loss."""

    cosine = tf.keras.losses.CosineSimilarity()
    return cosine(original, counterfactual, sample_weight=sample_weight)
