"""
This type stub file was generated by pyright.
"""

import torch
import torch.nn as nn

class PairwiseBilinear(nn.Module):
    ''' A bilinear module that deals with broadcasting for efficient memory usage.
    Input: tensors of sizes (N x L1 x D1) and (N x L2 x D2)
    Output: tensor of size (N x L1 x L2 x O)'''
    def __init__(self, input1_size, input2_size, output_size, bias: bool = ...):
        self.input1_size = ...
        self.input2_size = ...
        self.output_size = ...
        self.weight = ...
        self.bias = ...
    
    def forward(self, input1, input2):
        ...
    


class BiaffineScorer(nn.Module):
    def __init__(self, input1_size, input2_size, output_size):
        self.W_bilin = ...
    
    def forward(self, input1, input2):
        ...
    


class PairwiseBiaffineScorer(nn.Module):
    def __init__(self, input1_size, input2_size, output_size):
        self.W_bilin = ...
    
    def forward(self, input1, input2):
        ...
    


class DeepBiaffineScorer(nn.Module):
    def __init__(self, input1_size, input2_size, hidden_size, output_size, hidden_func=..., dropout=..., pairwise: bool = ...):
        self.W1 = ...
        self.W2 = ...
        self.hidden_func = ...
        self.dropout = ...
    
    def forward(self, input1, input2):
        ...
    


if __name__ == "__main__":
    x1 = torch.randn(3, 4)
    x2 = torch.randn(3, 5)
    scorer = DeepBiaffineScorer(4, 5, 6, 7)