# First Setup

Install Python. (How?)

Install virtualenv:

```
pip install virtualenv
```

Create a virtual enviroment (a sandbox) for the project. From the project
directory:

```
virtualenv venv
```

This will create a directory containing the packages, etc. To start using the
virtual enviroment we need to source it. (What happens on windows?)

```
source venv/bin/activate
```

See how it adds `(venv)` to our prompt?

We should also tell git to ignore the `venv` directory, so we don't
accidentally push the dependency files to github. Our project relies on them,
but they are not part of the project, so we don't want them in the git
repository.

```
echo venv > .gitignore
```

Now we can install Flask from within our virtual enviroment.

```
pip install flask
```

We can save our currently install dependacies to a file like this:

```
pip freeze requirements.txt
```

This allows us to get back the exact same set of dependacies again at a later
date by running this:

```
pip install -r requirements.txt
```

Marvellous. We're ready to start building stuff.
