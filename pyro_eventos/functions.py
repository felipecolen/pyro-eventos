import os


def get_env_var(name_env):
    return os.environ.get(name_env, '')
