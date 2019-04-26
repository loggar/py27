# python virtualenv

## install virtualenv

```
C:\_dev\python\Python37-32\Scripts
λ pip install virtualenv
```

```
λ virtualenv --version
16.0.0
```

### make virtualenv for an workspace with different python version from system environment

```
virtualenv --python=C:\_dev\python\Python27\python.exe .venv
```

### activate virtual env for the workspace

```
# Windows cmd
λ .venv\Scripts\activate

# Windows powershell
$ .venv\Scripts\Activate.ps1

(.venv) PS C:\Users\webnl\Documents\_workspace\loggar-py2> which python
/c/Users/webnl/Documents/_workspace/loggar-py2/.venv/Scripts/python


# MacOS
$ . ./venv/activate
```

### install packages

```
(.venv) λ pip list

(.venv) λ pip install jupyter
```

or, with requirements file:

`requirements.txt`

```
pytest
pylint
autopep8
future
```

```
(.venv) λ pip install -r requirements.txt

(.venv) λ pip list
```

### deactivate

```
(.venv) λ deactivate
```
