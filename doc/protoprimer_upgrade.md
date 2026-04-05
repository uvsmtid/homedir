
To upgrade `protoprimer` to the latest version, check these lines in `pyproject.toml`:

```
"protoprimer @ git+https://github.com/uvsmtid/protoprimer.git@26028d51440067b6f13233c3bdd97e5e81791da4#egg=protoprimer&subdirectory=src/protoprimer",
"neoprimer @ git+https://github.com/uvsmtid/protoprimer.git@26028d51440067b6f13233c3bdd97e5e81791da4#egg=neoprimer&subdirectory=src/neoprimer",
```

Update commit id to the latest from `main`:
https://github.com/uvsmtid/protoprimer/

Remove `constraints.txt` file (because it would point to the old commit id):

```sh
rm lconf/constraints.txt
```

Run:

```sh
./prime
```

It may fail as `protoprimer` has not moved beyond version `1.0.0` yet.
