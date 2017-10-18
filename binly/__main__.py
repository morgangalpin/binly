#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program entry point"""

from __future__ import print_function

import argparse
import errno
import logging
import os
import sys

import binly.metadata as metadata

from binly.api.api_controller_class import ApiController
from binly.platform.platform_controller import PlatformController

DATA_DIR = '/mnt/ramdisk/data'
CAMERA1_IMAGE_DIR = os.path.join(DATA_DIR, 'camera1', 'image')
CAMERA_IMAGE_FORMAT = '%d.jpg'
CAMERA1_MAX_IMAGE_AGE_SECONDS = 60


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
    arg_parser.add_argument(
        '-f', '--fake',
        action='store_true',
        dest='fake')

    args = arg_parser.parse_args(args=argv[1:])

    if not args.fake:
        mkdir_p(CAMERA1_IMAGE_DIR)
    api_controller = ApiController(
        camera1_image_dir=CAMERA1_IMAGE_DIR,
        camera_image_format=CAMERA_IMAGE_FORMAT,
        camera1_image_max_age_seconds=CAMERA1_MAX_IMAGE_AGE_SECONDS)
    platform_controller = PlatformController(
        fake=args.fake,
        camera1_image_dir=CAMERA1_IMAGE_DIR,
        camera_image_format=CAMERA_IMAGE_FORMAT,
        camera1_image_max_age_seconds=CAMERA1_MAX_IMAGE_AGE_SECONDS)
    start_resources = os.environ.get('WERKZEUG_RUN_MAIN') or not args.debug
    if start_resources:
        logging_level = logging.WARNING if args.debug else logging.DEBUG
        logging.basicConfig(level=logging_level)
        logging.info('startup: pid %d is the active werkzeug' % os.getpid())
        logging.info('debug = %s' % args.debug)

        print(epilog)

        # Create the controllers and link the communication of the matching
        # resources.
        platform_controller.add_subscriber_to_resource_publisher(
            'camera', api_controller.get_resource_subscriber('camera'), 'feed')
        platform_controller.add_subscriber_to_resource_publisher(
            'gps', api_controller.get_resource_subscriber('gps'), 'feed')
        platform_controller.add_resource_subscriber_to_publisher(
            'steering', api_controller.get_resource_publisher('steering'),
            'update')
        platform_controller.add_resource_subscriber_to_publisher(
            'throttle', api_controller.get_resource_publisher('throttle'),
            'update')
        platform_controller.add_resource_subscriber_to_publisher(
            'gripper', api_controller.get_resource_publisher('gripper'),
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


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


if __name__ == '__main__':
    entry_point()
