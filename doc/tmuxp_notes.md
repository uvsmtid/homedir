
To load the session, use:

```sh
./venv/bin/tmuxp load "${session_name}"
```

The initial configuration was captured by:

```sh
for tmux_session in $( tmux list-sessions -F "#{session_name}" )
do
    echo "INFO: freezing tmux session: ${tmux_session}" 1>&2
    ./venv/bin/tmuxp freeze --force --quiet --yes "${tmux_session}"
done
```
