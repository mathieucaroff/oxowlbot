"""
This type stub file was generated by pyright.
"""

import logging
from stanza.pipeline._constants import *
from stanza.pipeline.tokenize_processor import TokenizeProcessor
from stanza.pipeline.mwt_processor import MWTProcessor
from stanza.pipeline.pos_processor import POSProcessor
from stanza.pipeline.lemma_processor import LemmaProcessor
from stanza.pipeline.depparse_processor import DepparseProcessor
from stanza.pipeline.ner_processor import NERProcessor
from typing import Any, Optional

"""
Pipeline that runs tokenize,mwt,pos,lemma,depparse
"""
logger = logging.getLogger('stanza')
NAME_TO_PROCESSOR_CLASS = { TOKENIZE: TokenizeProcessor,MWT: MWTProcessor,POS: POSProcessor,LEMMA: LemmaProcessor,DEPPARSE: DepparseProcessor,NER: NERProcessor }
PROCESSOR_SETTINGS = { TOKENIZE: ['batch_size', 'pretokenized', 'no_ssplit'],MWT: ['batch_size', 'dict_only', 'ensemble_dict'],POS: ['batch_size'],LEMMA: ['batch_size', 'beam_size', 'dict_only', 'ensemble_dict', 'use_identity'],DEPPARSE: ['batch_size', 'pretagged'],NER: ['batch_size'] }
class PipelineRequirementsException(Exception):
    """
    Exception indicating one or more requirements failures while attempting to build a pipeline.
    Contains a ProcessorRequirementsException list.
    """
    def __init__(self, processor_req_fails):
        ...
    
    @property
    def processor_req_fails(self):
        ...
    
    def build_message(self):
        self.message = ...
    
    def __str__(self):
        ...
    


class Pipeline:
    def __init__(self, lang=..., dir=..., package=..., processors=..., logging_level=..., verbose: Optional[Any] = ..., use_gpu: bool = ..., **kwargs):
        self.load_list = ...
        self.load_list = ...
        self.load_list = ...
        self.config = ...
        self.processors = ...
        self.use_gpu = ...
    
    def update_kwargs(self, kwargs, processor_list):
        ...
    
    def filter_config(self, prefix, config_dict):
        ...
    
    @property
    def loaded_processors(self):
        """
        Return all currently loaded processors in execution order.
        :return: list of Processor instances
        """
        ...
    
    def process(self, doc):
        ...
    
    def __call__(self, doc):
        ...
    


