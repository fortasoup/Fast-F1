"""Overlaying speed traces of two laps
======================================

Compare two fastest laps by overlaying their speed traces.
"""


import matplotlib.pyplot as plt

import fastf1.plotting


# Enable Matplotlib patches for plotting timedelta values and load
# FastF1's dark color scheme
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme="fastf1")

# load a session and its telemetry data
session = fastf1.get_session(2021, "Spanish Grand Prix", "Q")
session.load()

fig, ax = plt.subplots()

for i in range(int(input("How many drivers do you want to compare? "))):
    driver_name = input("Enter the driver's abbreviation (e.g., VER, HAM): ")
    lap = session.laps.pick_drivers(driver_name).pick_fastest()
    telemetry = lap.get_car_data().add_distance()
    color = fastf1.plotting.get_team_color(lap["Team"], session=session)

    # Plot the speed trace
    plt.plot(telemetry['Distance'], telemetry['Speed'], color=color, label=driver_name.upper())


ax.set_xlabel("Distance in m")
ax.set_ylabel("Speed in km/h")

ax.legend()
plt.suptitle(f"Fastest Lap Comparison \n "
             f"{session.event['EventName']} {session.event.year} Qualifying")

plt.show()
