import tqdm
import subprocess as sp
import sys
from tkinter import Tk


root = Tk()
# root window title and dimension
root.title("Intalling libraries By Pampa")
# Set geometry(widthxheight)
root.geometry('600x600')

def install_packages(*librearies):

    """
        Install libraries ad-hoc without bash or console. 
        *test* No productive.
        libraries is a list of string
        you have to install tqdm before
    """
    #Test without libraries
    if librearies:
        required.append(librearies)
    else:
       required = ['pandas_gbq', 'google-cloud-bigquery', 'polars', 'tqdm', 'db-dtypes', 'pandas', 'python-dotenv', 'implicit', 'logging'] 

    try:
        

        #required = ['pandas_gbq', 'google-cloud-bigquery', 'polars', 'tqdm', 'db-dtypes', 'pandas', 'python-dotenv', 'implicit', 'logging']
        missing = []

        for package in required:
            try:
                __import__(package)
            except ImportError:
                missing.append(package)

        if missing:
            print(f"Installing missing packages: {missing}")
            for package in tqdm(missing):
                sp.check_call([sys.executable, '-m', 'pip', 'install', package], shell=True)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    set = True
    libraries = []
    while set:
        try:
            print("Para instalar librerias escriba el nombre de la libreria a instalar\nSi desea terminar escriba exit")
            library = input("Que Libreria desea instalar?: ".center(70))
            libraries.append(library.lower())
        except Exception as e:
            print(f"{e}")

        install_packages()
