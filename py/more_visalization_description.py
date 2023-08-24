#Makes html page and png graf visualizations of data in output hardwario folder
import plotly.express as px
import os

# Defines a function to capitalize the first letter and remove the extension
def process_filename(filename):
    parts = filename.split(".")  # Split the filename into parts using the dot as a separator
    if len(parts) > 1:
        parts.pop()  # Remove the last part (the extension)
    filename_without_extension = ".".join(parts)  # Join the remaining parts back together
    filename_capitalized = filename_without_extension.capitalize()  # Capitalize the first letter
    return filename_capitalized

# Defines the main function to create visualizations and save files
def create_visualization(source_folder, output_folder):
    list_child = os.listdir(source_folder)  # Get a list of files in the source folder

    for child in list_child:
        list_values = []
        i = 1
        with open(os.path.join(source_folder, child)) as temp:
            for line in temp:
                line = line.strip()
                list_values.append(float(line))
                i += 1

        # Create a folder with the same name as the processed filename
        pf_child = process_filename(child)  # Process the filename
        folder_path = os.path.join(output_folder, pf_child)
        os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

        # Create a scatter plot using Plotly Express
        fig = px.scatter(x=list(range(1, i)), y=list_values, title=f"{pf_child} Plot")
        fig.update_layout(xaxis_title="Time", yaxis_title=pf_child)
        fig.show()

        # Creating a Python list of dictionaries for tabulated data
        data_table = [{'Time': i, 'Values': value} for i, value in enumerate(list_values, start=1)]
        # Saving the Python data as a variable
        python_data_path = os.path.join(folder_path, f"{pf_child}_data.py")
        with open(python_data_path, "w") as python_data_file:
            python_data_file.write(f"data = {data_table}")

        # Save the scatter plot as an HTML file within the folder
        html_path = os.path.join(folder_path, f"{pf_child}_plot.html")
        fig.write_html(html_path, include_plotlyjs="cdn")

        # Save the scatter plot as an image (PNG format) within the folder
        image_path = os.path.join(folder_path, f"{pf_child}_plot.png")
        fig.write_image(image_path)

# Entry point of the program
if __name__ == '__main__':
    source_folder = "C:/Users/machm/OneDrive/Dokumenty/Hardwario" #replace this with your own folders
    output_folder = "C:/Users/machm/julia-vizualizace-dat-main/how_python_outputs_looks_like" #aswell

    create_visualization(source_folder, output_folder)  # Call the function to create visualizations
    print("Done successfully!")