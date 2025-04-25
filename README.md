# PyPSA Advanced Model

This repository contains an advanced PyPSA (Python for Power System Analysis) model that demonstrates various features of power system simulation and optimization.

## Features

- Multi-bus power system modeling
- Conventional and renewable generation (Coal, Wind, Solar)
- Energy storage simulation
- Time-series load profiles
- Power flow optimization
- Visualization of results

## Requirements

The project requires Python 3.x and several dependencies listed in `requirements.txt`. To install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the model using:

```bash
python advanced_model.py
```

The script will:
1. Set up a two-bus power system
2. Run optimization using the HiGHS solver
3. Generate plots showing generation mix, load profiles, and line loading
4. Print system statistics

## Model Components

- Two buses (North and South)
- Transmission line connecting the buses
- Conventional coal plant
- Wind farm with variable generation profile
- Solar PV with variable generation profile
- Battery storage system
- Variable loads in both regions 