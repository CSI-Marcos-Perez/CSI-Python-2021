import math
from ExperimentalDATA import ExperimentalDATA

from pathlib import Path
import json
import os

# sniper = "Orsis_T-5000"
# caliber = "7.62x51mm"
# ammunition = "FMJ"
# velocity_ms = 840
# building = "Caribbean Sea View"
# height = 334
# gravity = 9.81

#Convert the variables into the parameters

def ProjectileFunction (experimentalDATA:ExperimentalDATA):
    time_s = math.sqrt((2 * experimentalDATA.height) / experimentalDATA.gravity)

    distance = (experimentalDATA.velocity_ms * time_s)
    # distance = (experimentalDATA[velocity_ms] * time_s)
    print(f"The gun selected for the experiment is {experimentalDATA.sniper}. The caliber of the gun is {experimentalDATA.caliber}")

    print("The ORSIS T-5000 rifle is a sniper rifle that is known for its high-accuracy. This weapon was created thanks to the help of professional shooters. This gun is a hand-reloaded repeater with sliding breech bolt and two front locking lugs. This serves many purposes, as it has specifications that provide high-accuracy long-range shots. An estimate to the each shot's distnace is up to 1500m. The firing and recoil phases, and the gun can swiftly recover the sighting line.")


# #The script parameters have been converted into the single JSON Object
# experimentalDATA = {
#  "sniper": "Orsis_T-5000",
# "caliber": "7.62x51mm",
# "ammunition": "FMJ",
# "velocity_ms": 840,
# "building": "Caribbean Sea View",
# "height": 334,
# "gravity": 9.81

# }


experimentalDATA = ExperimentalDATA("Orsis_t-5000", "FMJ", 840, "Caribbean Sea View", 334, "7.62x51mm", 9.81)


myDATAset = [
ExperimentalDATA("FN GL40", "HE", 76, "Caribbean Sea View", 334, "40x46 mm", 9.81),
ExperimentalDATA("Orsis_t-5000", "FMJ", 840, "Coliseum Towers Residences", 259, "7.62x51mm", 9.81),
ExperimentalDATA("Orsis_t-5000", "FMJ", 840, "Edificio Seaborne Plaza", 256, "7.62x51mm", 9.81),
ExperimentalDATA("P90", "FN", 792, "Ocean Tower", 243, "5.7x28mm", 9.81)
]

for data in myDATAset:
    print("\n-------------------------------------------\n")
    ProjectileFunction(data)

# Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDATAset], outfile)
    # json.dump(myDATAset[0].__dict__, outfile)

# ProjectileFunction(experimentalDATA)

