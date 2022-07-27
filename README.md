# iiPythonx/website
A simple website for people that like minimalism; powered by simple code that gets the job done.

## Features
+ Profile links for Github, Discord, Steam, and Email
+ Light/dark mode
+ Automatically changing tagline
+ Full customizability through config.json

## Installation
1. Clone the repository via git (or download the ZIP from Github directly)
```sh
git clone https://github.com/iiPythonx/website
cd website
```
2. Install the Python requirements
```sh
python3 -m pip install -r reqs.txt
```
3. Edit config.json to your liking
4. Launch the site in development mode
```
python3 launch.py
```

## Deployment
Since this website is built around Flask, you can use any uWSGI server to deploy it if the Flask dev server isn't your favorite.  
For example, to launch the site via gunicorn:
```
python3 -m gunicorn -b 0.0.0.0:8080 -w 8 launch:app
```
