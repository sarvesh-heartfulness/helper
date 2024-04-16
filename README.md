# helper

### Create virtual environment

```sh
python3 -m venv venv
```

### Activate virtual environment

```sh
source venv/bin/activate
```

### Install required packages

```sh
pip install -r requirements.txt
```

### Start http server

```sh
uvicorn app:app --reload
```