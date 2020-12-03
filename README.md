<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mkcache.svg?maxAge=3600)](https://pypi.org/project/mkcache/)
[![](https://img.shields.io/npm/v/mkcache.svg?maxAge=3600)](https://www.npmjs.com/package/mkcache)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mkcache/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mkcache/actions)

### Installation
```bash
$ [sudo] pip install mkcache
```

```bash
$ [sudo] npm i -g mkcache
```

#### How it works
```
$XDG_CACHE_HOME/mkcache/<hash>
```

#### Config
```bash
export MKCACHE=path/to/cache # ~/.cache/mkcache by default
```

#### Examples
example 1. run script only once:
```bash
path="$(mkcache script "$@")"
! [ -e "$path" ] && { script "$@" || exit; touch "$path"; }
```

example 2. speed up macOS tts with mkcache:
```bash
path="$(mkcache "$@")"
! [ -e "$path" ] && /usr/bin/say "$@" -o "$path"
afplay "$path"
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
