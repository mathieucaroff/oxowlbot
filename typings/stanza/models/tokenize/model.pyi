"""
This type stub file was generated by pyright.
"""

import torch.nn as nn

class Tokenizer(nn.Module):
    def __init__(self, args, nchars, emb_dim, hidden_dim, N_CLASSES=..., dropout=...):
        self.args = ...
        self.embeddings = ...
        self.rnn = ...
        self.tok_clf = ...
        self.sent_clf = ...
        self.mwt_clf = ...
        self.dropout = ...
        self.toknoise = ...
    
    def forward(self, x, feats):
        ...
    


