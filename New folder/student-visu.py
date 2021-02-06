import csv
import pandas as pd
import plotly.graph_objects as go

fd = pd.read_csv("data.csv")
studentdf = fd.loc[fd["student_id"]== "TRL_zet"]
print(studentdf.groupby("level") ["attempt"].mean())

figure = go.Figure(go.Bar(
    x = studentdf.groupby("level") ["attempt"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = "h"
    ))

figure.show()
