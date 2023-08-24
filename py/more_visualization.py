#Makes html page and png graf visualizations of data in output hardwario folder
import plotly.express as px
import os

def process_filename(filename):
    parts = filename.split(".")
    if len(parts) > 1:
        parts.pop()
    filename_without_extension = ".".join(parts)
    filename_capitalized = filename_without_extension.capitalize()
    return filename_capitalized

def create_visualization(source_folder, output_folder):
    list_child = os.listdir(source_folder)

    for child in list_child:
        list_values = []
        i = 1
        with open(os.path.join(source_folder, child)) as temp:
            for line in temp:
                line = line.strip()
                list_values.append(float(line))
                i += 1

        pf_child = process_filename(child)
        folder_path = os.path.join(output_folder, pf_child)
        os.makedirs(folder_path, exist_ok=True)
        
        fig = px.scatter(x=list(range(1, i)), y=list_values, title=f"{pf_child} Plot")
        fig.update_layout(xaxis_title="Time", yaxis_title=pf_child)
        fig.show()

        data_table = [{'Time': i, 'Values': value} for i, value in enumerate(list_values, start=1)]
        python_data_path = os.path.join(folder_path, f"{pf_child}_data.py")
        with open(python_data_path, "w") as python_data_file:
            python_data_file.write(f"data = {data_table}")

        html_path = os.path.join(folder_path, f"{pf_child}_plot.html")
        fig.write_html(html_path, include_plotlyjs="cdn")

        image_path = os.path.join(folder_path, f"{pf_child}_plot.png")
        fig.write_image(image_path)

    print("Done successfully!")

if __name__ == '__main__':
    source_folder = "C:/Users/machm/OneDrive/Dokumenty/Hardwario" #replace this with your own folders
    output_folder = "C:/Users/machm/julia-vizualizace-dat-main/how_python_outputs_looks_like" #aswell

create_visualization(source_folder, output_folder)