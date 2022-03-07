#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This code was generated from Pelican, only minor CI-related modifications were done.

For more information, please read the official documentation:
    https://docs.getpelican.com/en/stable/index.html.
"""
import os
import shutil
import sys

from invoke import task
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

CONFIG = {
    # Local path configuration (can be absolute or relative to tasks.py)
    "deploy_path": "output",
    # Port for `serve`
    "port": 8000,
}


@task
def clean(c):  # pylint: disable=unused-argument
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def build(c):
    """Build local version of site"""
    c.run("pelican -s pelicanconf.py")


@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run("pelican -d -s pelicanconf.py")


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run("pelican -r -s pelicanconf.py")


@task
def serve(c):  # pylint: disable=unused-argument
    """Serve site at http://localhost:8000/"""

    class AddressReuseTCPServer(RootedHTTPServer):  # pylint: disable=missing-class-docstring
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"], ("", CONFIG["port"]), ComplexHTTPRequestHandler
    )

    sys.stderr.write(f"Serving on port {CONFIG['port']} ...\n")
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    c.run("pelican -s publishconf.py")


@task
def publish(c):
    """Publish to production via rsync"""
    c.run("pelican -s publishconf.py")
    # pylint: disable=consider-using-f-string
    c.run(
        'rsync --delete --exclude ".DS_Store" -pthrvz -c '
        "{} {production}:{dest_path}".format(CONFIG["deploy_path"].rstrip("/") + "/", **CONFIG)
    )
