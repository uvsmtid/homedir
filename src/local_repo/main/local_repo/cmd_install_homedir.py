# !/usr/bin/env python3
import os
import sys

import dotbot


def install_homedir(
    ref_root_dir_abs_path: str,
):

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

    print(sys.argv)

    dotbot.cli.main()
