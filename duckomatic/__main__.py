#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program entry point"""

from __future__ import print_function

import argparse
import logging
import os
import sys

import duckomatic.metadata as metadata

from duckomatic.api.api_controller_class import ApiController
from duckomatic.platform.platform_controller import PlatformController


def main(argv):
    """Program entry point.

    :param argv: command-line arguments
    :type argv: :class:`list`
    """
    author_strings = []
    for name, email in zip(metadata.authors, metadata.emails):
        author_strings.append('Author: {0} <{1}>'.format(name, email))

    epilog = '''
{project} {version}

{authors}
URL: <{url}>
'''.format(
        project=metadata.project,
        version=metadata.version,
        authors='\n'.join(author_strings),
        url=metadata.url)

    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=metadata.description,
        epilog=epilog)
    arg_parser.add_argument(
        '-V', '--version',
        action='version',
        version='{0} {1}'.format(metadata.project, metadata.version))
    arg_parser.add_argument(
        '-d', '--debug',
        action='store_true',
        dest='debug')

    args = arg_parser.parse_args(args=argv[1:])

    api_controller = ApiController()
    platform_controller = PlatformController()
    start_resources = os.environ.get('WERKZEUG_RUN_MAIN') or not args.debug
    if start_resources:
        logging.basicConfig(level=logging.DEBUG)
        logging.info('startup: pid %d is the active werkzeug' % os.getpid())

        print(epilog)

        # Create the controllers and link the communication of the matching
        # resources.
        platform_controller.add_subscriber_to_resource_publisher(
            'camera', api_controller.get_resource_subscriber('camera'), 'feed')
        platform_controller.add_subscriber_to_resource_publisher(
            'gps', api_controller.get_resource_subscriber('gps'), 'feed')
        platform_controller.add_resource_subscriber_to_publisher(
            'rudder', api_controller.get_resource_publisher('rudder'),
            'update')
        platform_controller.add_resource_subscriber_to_publisher(
            'throttle', api_controller.get_resource_publisher('throttle'),
            'update')

        platform_controller.socketio = api_controller._socketio
        platform_controller.start()
    else:
        logging.info('startup: pid %d is the werkzeug reloader' %
                     os.getpid())

        # Workaround for the werkzeug reloader removing the current directory
        # from the path. It's nasty, but it works! Inspired by:
        # https://github.com/mitsuhiko/flask/issues/1246
        os.environ['PYTHONPATH'] = os.getcwd()

    api_controller.start(start_resources, debug=args.debug)
    api_controller.stop()
    platform_controller.stop()

    return 0


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()
