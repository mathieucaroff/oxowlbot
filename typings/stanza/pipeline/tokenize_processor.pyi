"""
This type stub file was generated by pyright.
"""

import logging
from stanza.pipeline._constants import *
from stanza.pipeline.processor import UDProcessor

"""
Processor for performing tokenization
"""
logger = logging.getLogger('stanza')
class TokenizeProcessor(UDProcessor):
    PROVIDES_DEFAULT = ...
    REQUIRES_DEFAULT = ...
    MAX_SEQ_LENGTH_DEFAULT = ...
    def _set_up_model(self, config, use_gpu):
        ...
    
    def process_pre_tokenized_text(self, input_src):
        """
        Pretokenized text can be provided in 2 manners:

        1.) str, tokenized by whitespace, sentence split by newline
        2.) list of token lists, each token list represents a sentence

        generate dictionary data structure
        """
        ...
    
    def process(self, document):
        ...
    

