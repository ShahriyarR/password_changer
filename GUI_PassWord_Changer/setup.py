from distutils.core import setup
import py2exe

opts={"py2exe" : {"dll_excludes": ["OCI.dll",], "includes" : ["decimal", ]}}
setup(console=['change_password.py'],options=opts)