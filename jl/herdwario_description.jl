# Import the Plots package for creating visualizations
using Plots

# Set the plotting backend to GR
gr()

# Initialize an empty array to store temperature data
temperature = []

# Define a local scope to read and process temperature data from the file
let i = 1
    # Open the "hardwario-temp.txt" file and process its content line by line
    open("hardwario-temp.txt") do temp
        for line in eachline(temp)
            # Remove the newline character from the line
            line = replace(line, "\n" => "")
            # Parse the line as a floating-point number
            line = parse(Float64, line)
            # Append the index 'i' and parsed temperature 'line' to the 'temperature' array
            push!(temperature, [i, line])
            # Increment the index for the next iteration
            i = i + 1
        end
    end
end

# Create an array 'time' containing the indices from the 'temperature' array
time = [d[1] for d in temperature]

# Create an array 'temp' containing the temperature values from the 'temperature' array
temp = [d[2] for d in temperature]

# Create a scatter plot of time versus temperature
scatter(time, temp, legend=false, xlabel="Time", ylabel="Temperature")

# Save the scatter plot as a PNG image named "temp.png"
savefig("temp.png")
