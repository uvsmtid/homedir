# !/usr/bin/env python3
import os
import sys

import dotbot

import logging

from protoprimer.primer_kernel import (
    ColorFormatter,
    PythonExecutableFilter,
)

logger = logging.getLogger()


# TODO: reuse protoprimer.primer_kernel.configure_stderr_logger:
def configure_stderr_logger(
    stderr_log_level: int,
) -> logging.Handler:

    # Log everything (the filters are supposed to be set on output handlers instead):
    logger.setLevel(logging.NOTSET)

    stderr_handler: logging.Handler = logging.StreamHandler(sys.stderr)
    stderr_handler.addFilter(PythonExecutableFilter())

    stderr_formatter = ColorFormatter()

    stderr_handler.setLevel(stderr_log_level)
    stderr_handler.setFormatter(stderr_formatter)

    logger.addHandler(stderr_handler)

    return stderr_handler


def install_homedir(
    ref_root_dir_abs_path: str,
):

    configure_stderr_logger(logging.INFO)

    homedir_abs_path = os.path.join(
        ref_root_dir_abs_path,
        "homedir",
    )

    config_abs_path = os.path.join(
        ref_root_dir_abs_path,
        "gconf",
        "install_homedir.conf.yaml",
    )

    sys.argv.extend(
        [
            "--base-directory",
            homedir_abs_path,
            "--config-file",
            config_abs_path,
            "--exit-on-failure",
        ]
    )

    logger.info(f"sys.argv: {sys.argv}")

    dotbot.cli.main()
