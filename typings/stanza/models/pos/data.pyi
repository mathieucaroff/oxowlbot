"""
This type stub file was generated by pyright.
"""

import logging
from stanza.models.common.doc import *
from typing import Any, Optional

logger = logging.getLogger('stanza')
class DataLoader:
    def __init__(self, doc, batch_size, args, pretrain, vocab: Optional[Any] = ..., evaluation: bool = ..., sort_during_eval: bool = ...):
        self.batch_size = ...
        self.args = ...
        self.eval = ...
        self.shuffled = ...
        self.sort_during_eval = ...
        self.doc = ...
        self.pretrain_vocab = ...
        self.num_examples = ...
        self.data = ...
    
    def init_vocab(self, data):
        ...
    
    def preprocess(self, data, vocab, pretrain_vocab, args):
        ...
    
    def __len__(self):
        ...
    
    def __getitem__(self, key):
        """ Get a batch with index. """
        ...
    
    def __iter__(self):
        ...
    
    def load_doc(self, doc):
        ...
    
    def resolve_none(self, data):
        ...
    
    def reshuffle(self):
        self.data = ...
    
    def chunk_batches(self, data):
        ...
    


