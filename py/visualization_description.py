#Makes html page and png graf visualiyation of data in hardwario-temp.txt
import plotly.express as px

# Read temperature data from the file
temperature = []
i = 1

with open("C:\Users\machm\OneDrive\Dokumenty\Hardwario") as temp:
    for line in temp:
        line = line.strip()
        temperature.append(float(line))
        i += 1

# Create a scatter plot using plotly
fig = px.scatter(x=list(range(1, i)), y=temperature, title="Temperature Plot")
fig.update_layout(xaxis_title="Time", yaxis_title="Temperature")
fig.show()

# Save the scatter plot as an HTML file in the current directory
fig.write_html("temperature_plot.html", include_plotlyjs="cdn")

# Save the scatter plot as an image (PNG format) in the current directory
fig.write_image("temperature_plot.png")