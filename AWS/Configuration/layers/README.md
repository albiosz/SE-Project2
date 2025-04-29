# SE-Project2

## Deploying the configuration

In order to create a layer, one has to download all the dependencies from requirements.txt to a directory with the
name ```./python```. **This is very important!**

E.g., in Linux this script can be used:
```
pip install -r requirements.txt \
     --platform manylinux2014_x86_64 \
     --target=./requirements/python \
     --implementation cp \
     --python-version 3.13 \
     --only-binary=:all:
```

Then a ```.zip``` file needs to be created from the entire ```./python``` directory.
```
zip -r <layername>.zip ./python
```

Assuming you already have an AWS account, you need to go to the lambdas/layers and create a new layer. It is very
important for the functionality to be working that the runtime versions exactly coincide. Therefore, carefully choose
the architecture and python runtime, so that they can match up. In this project, I selected ```x86_64``` and
```python3.13```.

In order to make the modules available for the lambda, you need to provide the layer to the lambda. This setting can
be found in the lambda "Code" directly, scrolling to the very bottom. Simply "Add a layer". The modules can then be
used as if donwloaded with ```pip install```.