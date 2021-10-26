sniper = "Orsis_T-5000"
caliber = "7.62x51mmNATO"
ammunition = "Single (Bolt Action)"
velocity_ms = 600

building = "Caribbean Sea View"
height = 334

gravity = 9.81

import math

time_s = math.sqrt((2 * height) / gravity)

distance = (velocity_ms * time_s)

print("The ORSIS T-5000 rifle is a sniper rifle that is known for its high-accuracy. This weapon was created thanks to the help of professional shooters. This gun is a hand-reloaded repeater with sliding breech bolt and two front locking lugs. This serves many purposes, as it has specifications that provide high-accuracy long-range shots. An estimate to the each shot's distnace is up to 1500m. The firing and recoil phases, and the gun can swiftly recover the sighting line.")