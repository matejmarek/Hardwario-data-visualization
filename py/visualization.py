#Makes html page and png graf visualiyation of data in hardwario-temp.txt

import plotly.express as px

temperature = []
i = 1

with open("hardwario-temp.txt") as temp:
    for line in temp:
        line = line.strip()
        temperature.append(float(line))
        i += 1

fig = px.scatter(x=list(range(1, i)), y=temperature, title="Temperature Plot")
fig.update_layout(xaxis_title="Time", yaxis_title="Temperature")
fig.show()
fig.write_html("temperature_plot.html", include_plotlyjs="cdn")
fig.write_image("temperature_plot.png")