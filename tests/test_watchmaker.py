# -*- coding: utf-8 -*-
"""Watchmaker main test module."""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)

import os

from watchmaker import Arguments
from watchmaker.cli import LOG_LOCATIONS


def test_log_location_dict():
    """Tests the LOG_LOCATIONS dict."""
    # Test strings that are in the dict.
    location = LOG_LOCATIONS['linux']
    assert location == os.path.sep.join(('', 'var', 'log', 'watchmaker'))
    location = LOG_LOCATIONS['windows']
    assert location == os.path.sep.join((
        os.environ.get('SYSTEMDRIVE', 'C:'), 'Watchmaker', 'Logs'))


def test_default_argument_settings():
    """Tests that initial Arguments class default settings are correct."""
    args = Arguments()
    assert args.config_path is None
    assert args.log_dir is None
    assert not args.no_reboot
    assert args.log_level is None
    assert args.admin_groups is None
    assert args.admin_users is None
    assert args.computer_name is None
    assert args.environment is None
    assert args.salt_states is None
    assert args.s3_source is None
    assert args.ou_path is None
    assert args.extra_arguments == []


def skip_cli_main_entry_point():
    """
    We can skip the test for cli's main.

    Use the comment (# pragma: no cover) so coverage.py will ignore them.
    prepare_logging() is tested in test_logger.py
    exception_hook() is tested in test_logger.py
    Parts of Arguments and Client are tested in this file
    """
    pass
