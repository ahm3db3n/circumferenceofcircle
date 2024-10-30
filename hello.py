from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def circle_calculator():
    results = None
    if request.method == "POST":
        diameter = float(request.form.get("diameter", 0))
        radius = diameter / 2
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        results = {
            "diameter": diameter,
            "area": round(area, 2),
            "circumference": round(circumference, 2)
        }
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
