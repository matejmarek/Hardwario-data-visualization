using Plots
gr()

temperature = []
let i = 1
  open("hardwario-temp.txt") do temp
      for line in eachline(temp)
          line = replace(line, "\n" => "")
          line = parse(Float64,line)
          push!(temperature, [i, line])
          i = i+1
      end
  end
end

time = [d[1] for d in temperature]
temp = [d[2] for d in temperature]

scatter(time, temp, legend=false, xlabel="Time", ylabel="Temperature")
savefig("temp.png")