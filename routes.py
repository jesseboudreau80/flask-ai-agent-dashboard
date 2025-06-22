from flask import Blueprint, render_template, jsonify
import csv

main = Blueprint("main", __name__)

# View Routes
@main.route("/lp-tasks")
def lp_tasks():
    return render_template("lp_tasks.html")

@main.route("/mkt-tasks")
def mkt_tasks():
    return render_template("mkt_tasks.html")

@main.route("/fac-tasks")
def fac_tasks():
    return render_template("fac_tasks.html")

# Data Endpoints
@main.route("/lp-tasks-data")
def lp_tasks_data():
    with open("static/data/L&P_Inbox.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = list(reader)
    return jsonify(tasks)

@main.route("/mkt-tasks-data")
def mkt_tasks_data():
    with open("static/data/Marketing_Tasks.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = list(reader)
    return jsonify(tasks)

@main.route("/fac-tasks-data")
def fac_tasks_data():
    with open("static/data/Facilities_Tasks.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = list(reader)
    return jsonify(tasks)
