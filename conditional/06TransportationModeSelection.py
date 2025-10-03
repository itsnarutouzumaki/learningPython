distance = int(input("Enter the distance to be traveled (in km): "))

modeOfTransport = ""
if distance < 3:
  modeOfTransport = "walking"
elif distance <= 15:
  modeOfTransport = "Bike"
else:
  modeOfTransport = "Car"
print(f"For a distance of {distance} km, you should consider {modeOfTransport}.")