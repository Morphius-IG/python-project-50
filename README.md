### Hexlet tests and linter status:
[![Actions Status](https://github.com/Morphius-IG/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Morphius-IG/python-project-50/actions)
[![Python CI](https://github.com/Morphius-IG/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Morphius-IG/python-project-50/actions/workflows/pyci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Morphius-IG_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Morphius-IG_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Morphius-IG_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Morphius-IG_python-project-50)

### Description

This project show you a diiference between two files (JSON, YML) in three different output formats

### Setup

```bash
make install
```

### Usage
| Command                                                                | Description                           |
|------------------------------------------------------------------------|---------------------------------------|
| gendiff -f[--format] stylish file1.json file2.yml                      | "Show difference in pytest-like mode" |
| gendiff -f[--format] plain file1.json file2.yml                        | "Show difference in text mode"        |
| gendiff -f[--format] json file1.json file2.yml                         | "Show difference in JSON format"      |
```bash
gendiff -f stylish file1.json file2.yml
gendiff --format plain file1.yml file2.json
gendiff --format json file1.yml file2.yml
```

### Run tests

```bash
make test
```
### Run linter(ruff)

```bash
make lint
```
1. stylish (pytest-like mode)
<a href="https://asciinema.org/a/UUc37fgOHiGdhrfXSNwQlncqW" target="_blank"><img src="https://asciinema.org/a/UUc37fgOHiGdhrfXSNwQlncqW.svg" /></a>
2. plain (text mode)
<a href="https://asciinema.org/a/qWl9BI10tpgmJUV3TyO94nyx3" target="_blank"><img src="https://asciinema.org/a/qWl9BI10tpgmJUV3TyO94nyx3.svg" /></a>
3. json (JSON format)
<a href="https://asciinema.org/a/CTzE6KH5NThTEjS8xSxBGoMdO" target="_blank"><img src="https://asciinema.org/a/CTzE6KH5NThTEjS8xSxBGoMdO.svg" /></a>
