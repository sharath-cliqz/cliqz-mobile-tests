from fastapi import FastAPI
import sqlite3
from starlette.responses import JSONResponse

api = FastAPI()


@api.get("/")
def root():
    result = []
    conn = sqlite3.connect("vpn.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM status")
    data = cur.fetchall()
    for country in data:
        result.append({'Country': country[0], 'Status': country[1], 'Time_Last_Passed': country[2]})
    conn.close()
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=result, headers=headers)


@api.get("/history/{country}")
def history(country: str):
    result = []
    conn = sqlite3.connect("vpn.db")
    cur = conn.cursor()
    if country == "all":
        cur.execute("SELECT * FROM history".format(country))
    else:
        cur.execute("SELECT * FROM history WHERE country = '{}'".format(country))
    data = cur.fetchall()
    for country in data:
        result.append({'Country': country[2], 'Status': country[3], 'Time': country[1]})
    conn.close()
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=data, headers=headers)


@api.get("/performance/{country}")
def performance(country: str):
    result = []
    conn = sqlite3.connect("vpn.db")
    cur = conn.cursor()
    if country == "all":
        cur.execute("SELECT * FROM performance".format(country))
    else:
        cur.execute("SELECT * FROM performance WHERE country = '{}'".format(country))
    data = cur.fetchall()
    for country in data:
        result.append({'Country': country[2], 'Status': country[3], 'Time': country[1]})
    conn.close()
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=data, headers=headers)