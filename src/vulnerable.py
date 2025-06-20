'''
# src/vulnerable.py
import subprocess

def danger():
    subprocess.call("ls -l", shell=True)
'''
