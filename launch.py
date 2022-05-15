# Copyright 2022 iiPython

# Modules
import json
from flask import Flask, abort, render_template, send_from_directory

# Initialization
app = Flask(
    "iiPython",
    template_folder = "src/templates"
)
try:
    app._config = json.loads(open("config.json", "r").read())

except Exception:
    exit("You need to setup a config.json file.")

# Routes
@app.route("/~/<path:path>")
def get_relative_file(path: str) -> None:
    return send_from_directory("src/static", path, conditional = True)

@app.route("/")
@app.route("/<path:path>")
def get_template(path: str = "index") -> None:
    try:
        if path == "base":
            return abort(400)

        return render_template(f"{path}.html", app = app), 200

    except Exception:
        return abort(404)

# Launch
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True)
