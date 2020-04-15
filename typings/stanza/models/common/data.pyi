"""
This type stub file was generated by pyright.
"""

"""
Utility functions for data transformations.
"""
def map_to_ids(tokens, vocab):
    ...

def get_long_tensor(tokens_list, batch_size, pad_id=...):
    """ Convert (list of )+ tokens to a padded LongTensor. """
    ...

def get_float_tensor(features_list, batch_size):
    ...

def sort_all(batch, lens):
    """ Sort all fields by descending order of lens, and return the original indices. """
    ...
