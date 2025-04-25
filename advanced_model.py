# %% Advanced PyPSA model demonstrating multiple features
import pypsa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create network
network = pypsa.Network()

# Time settings - let's simulate 24 hours
hours = 24
network.set_snapshots(range(hours))

# Add buses
network.add("Bus", "Bus North", v_nom=220.)
network.add("Bus", "Bus South", v_nom=220.)

# Add transmission line between buses
network.add("Line",
           "North-South Line",
           bus0="Bus North",
           bus1="Bus South",
           x=0.1,  # Reactance
           r=0.01,  # Resistance
           s_nom=1000)  # Nominal power in MW

# Add conventional generator in the North
network.add("Generator",
           "Coal Plant",
           bus="Bus North",
           p_nom=1000,  # Nominal power
           marginal_cost=50,  # Cost per MWh
           p_min_pu=0.3)  # Minimum output as fraction of nominal power

# Add wind generator in the North with varying availability
wind_profile = 0.3 + 0.2 * np.sin(np.linspace(0, 2*np.pi, hours))
network.add("Generator",
           "Wind Farm",
           bus="Bus North",
           p_nom=800,  # Nominal power
           marginal_cost=0.1,
           p_max_pu=pd.Series(wind_profile, index=network.snapshots))

# Add solar generator in the South with varying availability
solar_profile = np.maximum(0, np.sin(np.linspace(0, 2*np.pi, hours)))
network.add("Generator",
           "Solar PV",
           bus="Bus South",
           p_nom=500,  # Nominal power
           marginal_cost=0.2,
           p_max_pu=pd.Series(solar_profile, index=network.snapshots))

# Add storage unit in the South
network.add("StorageUnit",
           "Battery Storage",
           bus="Bus South",
           p_nom=200,  # Power capacity in MW
           max_hours=6,  # Energy capacity in MWh = p_nom * max_hours
           efficiency_store=0.95,
           efficiency_dispatch=0.95,
           cyclic_state_of_charge=True)  # Force state of charge to be the same at start and end

# Add loads
# North load: constant 400 MW
network.add("Load",
           "Load North",
           bus="Bus North",
           p_set=400)

# South load: varying between 100 and 600 MW
south_load_profile = 350 + 250 * np.sin(np.linspace(0, 2*np.pi, hours))
network.add("Load",
           "Load South",
           bus="Bus South",
           p_set=pd.Series(south_load_profile, index=network.snapshots))

# Run optimization
network.optimize(solver_name="highs")

# Plot results
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 10))

# Plot generation
generation = pd.DataFrame({
    'Coal': network.generators_t.p['Coal Plant'],
    'Wind': network.generators_t.p['Wind Farm'],
    'Solar': network.generators_t.p['Solar PV'],
    'Battery': network.storage_units_t.p['Battery Storage']
})
generation.plot(ax=ax1, title='Generation Mix')
ax1.set_xlabel('Hour')
ax1.set_ylabel('Power (MW)')
ax1.grid(True)

# Plot loads
loads = pd.DataFrame({
    'North Load': network.loads_t.p['Load North'],
    'South Load': network.loads_t.p['Load South']
})
loads.plot(ax=ax2, title='Load Profiles')
ax2.set_xlabel('Hour')
ax2.set_ylabel('Power (MW)')
ax2.grid(True)

# Plot line loading
line_loading = pd.DataFrame({
    'Line Loading': network.lines_t.p0['North-South Line'] / network.lines.s_nom['North-South Line']
})
line_loading.plot(ax=ax3, title='North-South Line Loading (% of capacity)')
ax3.set_xlabel('Hour')
ax3.set_ylabel('Line Loading (p.u.)')
ax3.grid(True)

plt.tight_layout()
plt.show()

# Print some statistics
print("\nSystem Statistics:")
print("Total Generation Cost:", network.objective)
print("\nEnergy Generated (MWh):")
print("Coal:", network.generators_t.p['Coal Plant'].sum())
print("Wind:", network.generators_t.p['Wind Farm'].sum())
print("Solar:", network.generators_t.p['Solar PV'].sum())
print("Battery:", abs(network.storage_units_t.p['Battery Storage']).sum() / 2)  # Divide by 2 to avoid double counting charge/discharge 
# %%
