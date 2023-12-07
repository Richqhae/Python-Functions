#Quaye Richard
# 14 October 2023
#Testing and fixing functions


from pytest import approx
import pytest 

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016

PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless
SUPPLY_VELOCITY = 1.65  # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018  # (unitless)
HOUSEHOLD_VELOCITY = 1.75  # (meters / second)

# Function to calculate water column height
def qr_water_column_height(tower_height, tank_height):
    return tower_height + tank_height

# Function to calculate pressure gain from water height
def qr_pressure_gain_from_water_height(water_height):
    return WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * water_height / 1000  # Convert to kPa

# Function to calculate pressure loss from a pipe
def qr_pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    k = 0.2
    return (k * WATER_DENSITY * velocity ** 2 * length) / (2 * diameter * friction_factor * 1000)  # Convert to kPa

# Function to calculate pressure loss from fittings
def qr_pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    rho = WATER_DENSITY
    v = fluid_velocity
    n = quantity_fittings
    return (-0.04 * rho * v ** 2 * n) / 2000

# Function to calculate Reynolds number
def qr_reynolds_number(hydraulic_diameter, fluid_velocity):
    rho = WATER_DENSITY
    d = hydraulic_diameter
    v = fluid_velocity
    mu = WATER_DYNAMIC_VISCOSITY
    return (rho * d * v) / mu

# Function to calculate pressure loss from a pipe reduction
def qr_pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    D = larger_diameter
    d = smaller_diameter
    v = fluid_velocity
    k = 0.1 + (50 / reynolds_number) ** 4 - 1
    return (-k * WATER_DENSITY * v ** 2) / 2000

# Main function
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = qr_water_column_height(tower_height, tank_height)
    pressure = qr_pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = qr_reynolds_number(diameter, velocity)
    loss = qr_pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = qr_pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = qr_pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = qr_pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()
