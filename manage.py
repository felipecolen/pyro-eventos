#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':

    try:
        import env_vars
        print("""
        ##########################################
        -> -> -> Arquivo env_vars.py encontrado :D
        ##########################################
        """)
    except ImportError:
        print("""
        ########################################################################
        -> -> -> =! Não localizado arquivo env_vars.py 
        
        crie uma cópia do arquivo env_vars.py.sample com o nome env_vars.py
        e ajuste as confs necessárias para uso local
        ou add as variáveis de ambiente
        ########################################################################
        """)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyro_eventos.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
