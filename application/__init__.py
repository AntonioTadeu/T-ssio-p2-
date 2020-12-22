from flask import Flask
import os 

app = Flask(_name_, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))
