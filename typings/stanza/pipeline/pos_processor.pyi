"""
This type stub file was generated by pyright.
"""

from stanza.pipeline._constants import *
from stanza.pipeline.processor import UDProcessor

"""
Processor for performing part-of-speech tagging
"""
class POSProcessor(UDProcessor):
    PROVIDES_DEFAULT = ...
    REQUIRES_DEFAULT = ...
    def _set_up_model(self, config, use_gpu):
        ...
    
    def process(self, document):
        ...
    

