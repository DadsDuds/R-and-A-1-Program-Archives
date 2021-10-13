# I am considering creating a GUI for this program
# will probably do that at some point...

import numpy as np
import math as m

# place your z,y,x degrees here
z_alpha = np.radians(10)
y_beta = np.radians(20)
x_gamma = np.radians(30)

print("yaw =", np.round(np.degrees(z_alpha), decimals = 2))
print("pitch =", np.round(np.degrees(y_beta), decimals = 2))
print("roll =", np.round(np.degrees(x_gamma), decimals = 2))
print("")

yawMatr = np.matrix([
                    [m.cos(z_alpha), -m.sin(z_alpha), 0],
                    [m.sin(z_alpha), m.cos(z_alpha), 0],
                    [0, 0, 1]
])

pitchMatr = np.matrix([
                    [m.cos(y_beta), 0, m.sin(y_beta)],
                    [0, 1, 0],
                    [-m.sin(y_beta), 0, m.cos(y_beta)]
])

rollMatr = np.matrix([
                    [1, 0, 0],
                    [0, m.cos(x_gamma), -m.sin(x_gamma)],
                    [0, m.sin(x_gamma), m.cos(x_gamma)]
])

R = yawMatr * pitchMatr * rollMatr

print(np.round(R, decimals = 4))
print("")