
## How was this repo inited?

Install `dotdrop`:

```sh
pipx install dotdrop
```

Configure `dotdrop`:

```sh
dotdrop gencfg > config.yaml
```

Add files:

```sh
dotdrop import ~/.gitconfig
```

Install `protoprimer`:

```sh
git fetch https://github.com/uvsmtid/protoprimer.git
git show FETCH_HEAD:cmd/proto_code/proto_kernel.py > proto_kernel.py
```



