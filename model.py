#%%
import pypsa
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
 
#%%
network = pypsa.Network()
 
# Add one bus
network.add("Bus", "Bus 0", v_nom=220.)
 
# Add one generator
network.add("Generator", "Gen 0",
            bus="Bus 0",
            p_set=100,
            control="PQ",
            marginal_cost=1)
 
# Add one load
network.add("Load", "Load 0",
            bus="Bus 0",
            p_set=100)
 
#%%
# Run optimization
network.optimize()
# %%
