import subprocess

subprocess.run(
    "rm -rf .DS_Store app.py model.py pipe.pkl mapper.pkl model.h5 model.pkl requirements.txt runtime.txt Procfile",
shell=True)
