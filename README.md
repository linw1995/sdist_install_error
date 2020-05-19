# Source distribution that pip can not install

* pip 20.1
* python 3.8
* poetry 1.0.5

```bash
poetry build
pip install -v ./dist/sdist_install_error-0.1.0.tar.gz 2>&1 | tee install.log
```

# Problem Resolved by [@frostming](https://github.com/frostming)

**poetry build** produces a source distribution built without `build.py` file (it is configured by `pyproject.toml`). When running **pip install**, due to the `build.py` missing it imports `pip/_vendor/pep517/build.py` instead. It caused a lot of unknown error. So **pip install** produced a long and unreadable output.

Add a single line of code to fix this problem.

```toml
[tool.poetry]
# ...
include = ["build.py"]
# ...
```

> See [linw1995/jsonpath#11](https://github.com/linw1995/jsonpath/issues/11) for additional detials.
And thanks for @frostming's help.
