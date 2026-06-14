from __future__ import annotations

import logging

from metaprimer.pre_commit import (
    Bootstrapper_state_pre_commit_configured,
)
from protoprimer.primer_kernel import (
    ContextBuilder,
    EntryFunc,
    run_process,
)

logger = logging.getLogger()


def custom_main():
    env_ctx = (
        ContextBuilder()
        #
        .entry_func(EntryFunc.func_boot_env)
        #
        .forced_final_state(Bootstrapper_state_pre_commit_configured._state_name())
        #
        .build_context()
    )
    env_ctx.register_factory(
        Bootstrapper_state_pre_commit_configured._state_name(),
        Bootstrapper_state_pre_commit_configured,
        replace_existing=True,
    )
    run_process(env_ctx)


if __name__ == "__main__":
    custom_main()
