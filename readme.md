
# `homdir`

A repo with `$HOME` dir user files (dotfiles and such):
*   privately used but publicly shared for copying-and-pasting
*   not supposed to contain secret (keys, passwords, etc.)

## Usage

Bootstrap the repo via [protoprimer][protoprimer_repo]:

```sh
./prime
```

Install [homedir][homedir_link] files via [dotbot][dotbot_repo]:

```sh
./cmd/install_homedir
```

See [install_homedir.conf.yaml][install_homedir_conf] for details.

---

[protoprimer_repo]: https://github.com/uvsmtid/protoprimer
[dotbot_repo]: https://github.com/anishathalye/dotbot

[homedir_link]: homedir
[install_homedir_conf]: gconf/install_homedir.conf.yaml
