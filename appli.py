from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q", "").lower()  # Get search query
    try:
        with open("jobs.json", "r") as f:
            jobs = json.load(f)
    except Exception as e:
        return f"Error loading jobs: {e}"

    # Filter jobs based on search query
    if query:
        jobs = [job for job in jobs if query in job["title"].lower() or query in job["company"].lower()]

    return render_template("jobs-1.html", jobs=jobs, query=query)

if __name__ == "__main__":
    app.run(debug=True)