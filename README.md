# PyPSA Power System Models

This repository contains PyPSA (Python for Power System Analysis) models that demonstrate various features of power system simulation and optimization, from basic to advanced implementations.

## Models

### Basic Model (`model.py`)
A simple single-bus power system model that demonstrates:
- Basic PyPSA optimization setup
- Time-series load variation (24-hour period)
- Single generator and load interaction
- Visualization of generation vs. load profiles
- Basic optimization results reporting

### Advanced Model (`advanced_model.py`)
A more complex multi-bus power system that demonstrates:
- Multi-bus power system modeling
- Conventional and renewable generation (Coal, Wind, Solar)
- Energy storage simulation
- Time-series load profiles
- Power flow optimization
- Advanced visualization of results

## Requirements

The project requires Python 3.x and several dependencies listed in `requirements.txt`. To install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the basic model:
```bash
python model.py
```
This will simulate a 24-hour period with a single generator responding to a sinusoidal load profile.

Run the advanced model:
```bash
python advanced_model.py
```
This will:
1. Set up a two-bus power system
2. Run optimization using the HiGHS solver
3. Generate plots showing generation mix, load profiles, and line loading
4. Print system statistics

## Model Components

### Basic Model Components
- Single bus system
- One generator with optimizable dispatch
- Time-varying load profile
- Basic visualization

### Advanced Model Components
- Two buses (North and South)
- Transmission line connecting the buses
- Conventional coal plant
- Wind farm with variable generation profile
- Solar PV with variable generation profile
- Battery storage system
- Variable loads in both regions 