
def specialize(f, *args, **kwargs):
    """This function wraps some arguments for another function."""
    def specialized(*rest_args, **rest_kwargs):
        return f(*args, *rest_args, **kwargs, **rest_kwargs)
    return specialized
