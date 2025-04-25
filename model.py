#%%
import pypsa
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
#%%
network = pypsa.Network()

# Set time index for optimization
hours = 24  # Let's simulate one day
network.set_snapshots(range(hours))
 
# Add one bus
network.add("Bus", "Bus 0", v_nom=220.)
 
# Add one generator
network.add("Generator", "Gen 0",
            bus="Bus 0",
            p_nom=100,  # Nominal power capacity in MW
            marginal_cost=1)  # Cost per MWh
 
# Add one load with time-varying demand
load_profile = 80 + 20 * np.sin(np.linspace(0, 2*np.pi, hours))  # Varying between 60 and 100 MW
network.add("Load", "Load 0",
            bus="Bus 0",
            p_set=pd.Series(load_profile, index=network.snapshots))
 
#%%
# Run optimization
network.optimize(solver_name="highs")

# Plot results
fig, ax = plt.subplots(figsize=(10, 6))
pd.DataFrame({
    'Generation': network.generators_t.p['Gen 0'],
    'Load': network.loads_t.p['Load 0']
}).plot(ax=ax)
ax.set_xlabel('Hour')
ax.set_ylabel('Power (MW)')
ax.grid(True)
plt.title('Generation and Load Profile')
plt.show()

# Print optimization results
print("\nOptimization Results:")
print(f"Total Generation: {network.generators_t.p['Gen 0'].sum():.2f} MWh")
print(f"Total Load: {network.loads_t.p['Load 0'].sum():.2f} MWh")
print(f"Total System Cost: {network.objective:.2f}")
# %%
