model = {
    "Room1": None,
    "Room2": None
}


def temperature_agent(room, reading):
    model[room] = reading

    if reading == "Cold":
        return "Turn Heater ON"

    elif reading == "Hot":
        return "Turn Heater OFF"

    elif model["Room1"] == "Normal" and model["Room2"] == "Normal":
        return "All Rooms Comfortable - Idle"

    else:
        return "Move to Other Room to Check"


percept_sequence = [
    ("Room1", "Cold"),
    ("Room1", "Normal"),
    ("Room2", "Hot"),
    ("Room2", "Normal")
]

print("Room\tReading\tAction\t\t\tModel")

for room, reading in percept_sequence:
    action = temperature_agent(room, reading)
    print(room, "\t", reading, "\t", action, "\t", model)