"""
This type stub file was generated by pyright.
"""

import logging
from typing import Any, Optional

"""
A trainer class to handle training and testing of models.
"""
logger = logging.getLogger('stanza')
def unpack_batch(batch, use_cuda):
    """ Unpack a batch from the data loader. """
    ...

class Trainer(object):
    """ A trainer for training models. """
    def __init__(self, args: Optional[Any] = ..., vocab: Optional[Any] = ..., emb_matrix: Optional[Any] = ..., model_file: Optional[Any] = ..., use_cuda: bool = ...):
        self.use_cuda = ...
    
    def update(self, batch, eval: bool = ...):
        ...
    
    def predict(self, batch, beam_size=...):
        ...
    
    def postprocess(self, words, preds, edits: Optional[Any] = ...):
        """ Postprocess, mainly for handing edits. """
        ...
    
    def update_lr(self, new_lr):
        ...
    
    def train_dict(self, triples):
        """ Train a dict lemmatizer given training (word, pos, lemma) triples. """
        ...
    
    def predict_dict(self, pairs):
        """ Predict a list of lemmas using the dict model given (word, pos) pairs. """
        ...
    
    def skip_seq2seq(self, pairs):
        """ Determine if we can skip the seq2seq module when ensembling with the frequency lexicon. """
        ...
    
    def ensemble(self, pairs, other_preds):
        """ Ensemble the dict with statistical model predictions. """
        ...
    
    def save(self, filename):
        ...
    
    def load(self, filename, use_cuda: bool = ...):
        self.args = ...
        self.vocab = ...
    


