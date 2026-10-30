import pandas as pd
import element_manager as pt   

# Constants
density_water = 1.0 #g/cm3
c = 4.2 # Specific heat capacity of water in kJ/kg/K

df = pd.read_csv("data.csv")

# Calculate heat change in water H = mc(Tf-Ti)/1000
mass_water = df['vol_water']* density_water
temp_diff = df['final_temp_water'] - df['init_temp_water']

H_kJ = (mass_water * c * temp_diff)/1000
print(f"Heat change of water: {H_kJ.iloc[0]}kJ")

# Molar heat of combustion of ethanol (C2H5OH)
# C - 12, H = 1, O = 16
c, h, o = pt.get_atomic_mass('c'), pt.get_atomic_mass('h'), pt.get_atomic_mass('o')
RFM_ethanol = c*2 + h*6 + o

mass_of_ethanol_used = df['fin_mass_ethanol'] - df['init_mass_ethanol']

mh_c = (RFM_ethanol*H_kJ)/mass_of_ethanol_used
print(f"Molar heat of combustion of ethanol: {round(mh_c.iloc[0], 2)}kJmol-1")