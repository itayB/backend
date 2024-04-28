# A FastAPI Server with a packaged React Application

The story: [Packaging Your TypeScript Client into a Python Backend](https://medium.com/towards-data-science/packaging-your-typescript-client-into-a-python-backend-b087e50c5c1a).

A simple demo server for demonsrating how to use a packaged [frontend application](https://github.com/itayB/vite-project).

## Getting Started

### Installation

You can install this server and run it with:

```shell
python3 -m venv venv             # create virtual environment
. venv/bin/activate              # activate the vitrual environment
pip install -r requirements.txt  # install dependencies
python -m backend                # run the server
```

### Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update/add tests.

On your first contribution, please install `pre-commit`:

```bash
pre-commit install --install-hooks -t pre-commit -t commit-msg
```
