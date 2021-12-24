import gin

@gin.configurable
def loss(x=None):
    return (x - 3.0)**2

gin_config_string = """
loss.x = (-1, 0, 2.0, 3.0, 10.0)
"""

if __name__ == '__main__':
    gin.parse_config(gin_config_string)
    loss()
