"""
This type stub file was generated by pyright.
"""

import torch
import torch.nn as nn
from typing import Any, Optional

class HLSTMCell(nn.modules.rnn.RNNCellBase):
    """
    A Highway LSTM Cell as proposed in Zhang et al. (2018) Highway Long Short-Term Memory RNNs for 
    Distant Speech Recognition.
    """
    def __init__(self, input_size, hidden_size, bias: bool = ...):
        self.input_size = ...
        self.hidden_size = ...
        self.Wi = ...
        self.Wf = ...
        self.Wo = ...
        self.Wg = ...
        self.gate = ...
    
    def forward(self, input, c_l_minus_one: Optional[Any] = ..., hx: Optional[Any] = ...):
        ...
    


class HighwayLSTM(nn.Module):
    """
    A Highway LSTM network, as used in the original Tensorflow version of the Dozat parser. Note that this
    is independent from the HLSTMCell above.
    """
    def __init__(self, input_size, hidden_size, num_layers=..., bias: bool = ..., batch_first: bool = ..., dropout=..., bidirectional: bool = ..., rec_dropout=..., highway_func: Optional[Any] = ..., pad: bool = ...):
        self.input_size = ...
        self.hidden_size = ...
        self.num_layers = ...
        self.bias = ...
        self.batch_first = ...
        self.dropout = ...
        self.dropout_state = ...
        self.bidirectional = ...
        self.num_directions = ...
        self.highway_func = ...
        self.pad = ...
        self.lstm = ...
        self.highway = ...
        self.gate = ...
        self.drop = ...
    
    def forward(self, input, seqlens, hx: Optional[Any] = ...):
        ...
    


if __name__ == "__main__":
    T = 10
    bidir = True
    num_dir = 2 if bidir else 1
    rnn = HighwayLSTM(10, 20, num_layers=2, bidirectional=True)
    input = torch.randn(T, 3, 10)
    hx = torch.randn(2 * num_dir, 3, 20)
    cx = torch.randn(2 * num_dir, 3, 20)
    output = rnn(input, (hx, cx))