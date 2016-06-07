# pipelines.py

"""Simple coroutine based data pipeline package inspired by David Beazley."""

# Coroutine decorator lifted directly from:
# http://www.dabeaz.com/coroutines/coroutine.py 
def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

@coroutine
def match(p, matcher=lambda p,x: p in x, target):
    """Filter values that do not contain the pattern."""
    while True:
        value = (yield)
        if matcher(p, value):
            target.send(value)

@coroutine
def apply(func, target):
    """Apply a function to each value."""
    while True:
        value = (yield)
        target.send(func(value))

@coroutine
def broadcast(targets):
"""Fan out a value to a set of targets."""
    while True:
        value = (yield)
        for target in targets:
            target.send(value)

def process(data, pipeline):
    """Send data into the pipeline."""
    for datum in data:
        pipeline.send(datum)
