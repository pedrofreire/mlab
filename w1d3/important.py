import gin

@gin.configurable
def loss(x):
    return (x - 3.0)**2
