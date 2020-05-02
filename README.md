# Source distribution that pip can not install

* pip 20.1
* python 3.8
* poetry 1.0.5

```bash
poetry build
pip install -v ./dist/sdist_install_error-0.1.0.tar.gz 2>&1 | tee install.log
```
