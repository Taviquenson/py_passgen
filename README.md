# py_passgen
A Python password generator for the terminal (Command Line Interface).

By default it generates a 12 characters long password that may contain uppercase, lowercase, numbers and symbols. However, ambiguous characters like O, 0, I, l, 1 aren't included.

The password can be customized as indicated in usage.

## Usage
passgen.py [-h] [-l] [-u] [-d] [-s] [opt_pass_len]

*positional arguments:*
  opt_pass_len     Optionally indicates password length

*options:*
  -h, --help       show this help message and exit
  -l, --lowercase  Use lowercase.
  -u, --uppercase  Use uppercase
  -d, --digits     Use digits
  -s, --symbols    Use symbols

## Examples
```
$ python3 passgen.py
@QJ^hpBJ!GdY
```

```
$ python3 passgen.py -u  
UZRSUPLHWFYB
```

```
$ python3 passgen.py -ul
SwzvFeBQGDqA
```

```
$ python3 passgen.py 20
Yzzb&phydPuSk$vmSTa9
```

```
$ python3 passgen.py -d 8
56443422
```
