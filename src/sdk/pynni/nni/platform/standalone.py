# Copyright (c) Microsoft Corporation. All rights reserved.
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
# OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ==================================================================================================


import logging
import json_tricks

from ..common import init_standalone_logger

__all__ = [
    'get_next_parameter',
    'get_experiment_id',
    'get_trial_id',
    'get_sequence_id',
    'send_metric',
]

init_standalone_logger()
_logger = logging.getLogger('nni')


def get_next_parameter():
    _logger.warning('Requesting parameter without NNI framework, returning empty dict')
    return {
        'parameter_id': None,
        'parameters': {}
    }

def get_experiment_id():
    pass

def get_trial_id():
    pass

def get_sequence_id():
    pass

def send_metric(string):
    metric = json_tricks.loads(string)
    if metric['type'] == 'FINAL':
        _logger.info('Final result: %s', metric['value'])
    elif metric['type'] == 'PERIODICAL':
        _logger.info('Intermediate result: %s  (Index %s)', metric['value'], metric['sequence'])
    else:
        _logger.error('Unexpected metric: %s', string)
