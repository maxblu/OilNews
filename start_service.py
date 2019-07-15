
import subprocess
import os


def start():
    # subprocess.Popen(['echo','hello'] )

    subprocess.call(['python', 'fix_cfg-file_time.py'])
    subprocess.call(['news-please', '-c', 'config/'])

    ##añadir aqui la parte de esperar para repetir el proceso
    

if __name__ == "__main__":
    start()