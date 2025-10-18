
# `homdir`

A repo with `$HOME` dir user files (dotfiles and such).

They are privately used but publicly shared to reuse snippets.

They are not supposed to contain secret (keys, passwords, etc.).

## init

Bootstrap the repo:

```
./prime
```

Install `dotdrop`:

```sh
pipx install dotdrop
```

Add files:

```sh
dotdrop import ~/.gitconfig
```
