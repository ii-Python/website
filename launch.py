# Copyright 2022 iiPython

# Modules
from flask import Flask, abort, render_template, send_from_directory

# Initialization
app = Flask(
    "iiPython",
    template_folder = "src/templates"
)

# Routes
@app.route("/~/<path:path>")
def get_relative_file(path: str) -> None:
    return send_from_directory("src/static", path, conditional = True)

@app.route("/")
@app.route("/<path:path>")
def get_template(path: str = "index") -> None:
    if path == "base":
        return abort(400)

    return render_template(f"{path}.html"), 200

# Launch
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True)
