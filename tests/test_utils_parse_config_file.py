"""
    Copyright (c) 2022. All rights reserved. NS Coetzee <nicc777@gmail.com>

    This file is licensed under GPLv3 and a copy of the license should be included in the project (look for the file 
    called LICENSE), or alternatively view the license text at 
    https://raw.githubusercontent.com/nicc777/acfop/main/LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
print('sys.path={}'.format(sys.path))

import unittest

from acfop.models.runtime import VariableStateStore
from acfop.utils.cli_arguments import parse_command_line_arguments
from acfop.utils.parse_config_file import *


class TestFunctionUpdateStateStoreFromConfigFile(unittest.TestCase):    # pragma: no cover

    def setUp(self):
        self.overrides = dict()
        self.overrides['config_file'] = 'examples/example_02/example_02.yaml'
        self.cli_args=[
            '--conf', 'examples/example_01/example_01.yaml',
        ]

    def test_call_update_state_store_from_config_file_defaults(self):
        state_store = parse_command_line_arguments(cli_args=self.cli_args)
        result = update_state_store_from_config_file(state_store=state_store)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, VariableStateStore)
        # TODO add tests for the config file parsing... there will be LOTS!!!


if __name__ == '__main__':
    unittest.main()