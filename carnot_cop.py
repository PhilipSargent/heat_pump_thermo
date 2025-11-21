import numpy as np
import matplotlib.pyplot as plt

def celsius_to_kelvin(temp_celsius):
    """Converts temperature from Celsius to Kelvin."""
    return temp_celsius + 273.15

def carnot_cop_heating(T_hot_K, T_cold_K):
    """
    Calculates the theoretical maximum Coefficient of Performance (COP) 
    for a heating system (Carnot Cycle).

    COP = T_hot / (T_hot - T_cold)

    Args:
        T_hot_K (float): Absolute temperature of the hot reservoir (e.g., heating water).
        T_cold_K (float or np.ndarray): Absolute temperature of the cold reservoir 
                                        (e.g., ambient air).

    Returns:
        float or np.ndarray: The theoretical maximum COP.
    """
    # Calculate the temperature difference
    delta_T = T_hot_K - T_cold_K
    
    # Calculate the base COP
    cop = T_hot_K / delta_T

    # Use np.where to replace invalid results (where T_hot <= T_cold) with NaN
    return np.where(delta_T <= 0, np.nan, cop)


# --- Define Parameters ---

# 1. Ambient Temperature Range (Cold Reservoir, T_cold)
# From -35°C to +15°C
T_ambient_C = np.linspace(-35, 15, 100) # 100 points for a smooth curve
T_ambient_K = celsius_to_kelvin(T_ambient_C)

# 2. Target Heating Temperatures (Hot Reservoir, T_hot)
T_target_1_C = 35  # For floor heating or fan coils (lower temperature)
T_target_2_C = 65  # For domestic hot water (DHW) or standard radiators (higher temperature)

T_target_1_K = celsius_to_kelvin(T_target_1_C)
T_target_2_K = celsius_to_kelvin(T_target_2_C)

# --- Calculate COP Values ---

# Carnot COP for 35°C target
cop_35C = carnot_cop_heating(T_target_1_K, T_ambient_K)

# Carnot COP for 65°C target
cop_65C = carnot_cop_heating(T_target_2_K, T_ambient_K)

# --- Plotting ---

plt.figure(figsize=(10, 6))

# Plot the 35°C target curve
plt.plot(T_ambient_C, cop_35C, label=f'Target Heating Temp: {T_target_1_C}°C', 
         color='green', linewidth=2)

# Plot the 65°C target curve
plt.plot(T_ambient_C, cop_65C, label=f'Target Heating Temp: {T_target_2_C}°C', 
         color='red', linewidth=2)

# --- Annotations and Styling ---

plt.title('Theoretical Maximum COP (Carnot Efficiency) vs. Ambient Temperature')
plt.xlabel('Ambient Temperature (Source, °C)')
plt.ylabel('Coefficient of Performance (COP)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Hot Reservoir Temperature ($T_{hot}$)')

# Add vertical line for a typical cold-climate operation limit
plt.axvline(-20, color='gray', linestyle=':', label='Typical Cold-Climate Operation Limit (-20°C)')

# Annotate key points
# Find the COP at 0°C for both curves
zero_c_index = np.argmin(np.abs(T_ambient_C - 0)) 

cop35_at_0 = cop_35C[zero_c_index]
if not np.isnan(cop35_at_0):
    plt.plot(0, cop35_at_0, 'go')
    plt.annotate(f'COP $\\approx$ {cop35_at_0:.1f} at 0°C', (2, cop35_at_0 - 0.5), color='green')

cop65_at_0 = cop_65C[zero_c_index]
if not np.isnan(cop65_at_0):
    plt.plot(0, cop65_at_0, 'ro')
    plt.annotate(f'COP $\\approx$ {cop65_at_0:.1f} at 0°C', (2, cop65_at_0 + 0.5), color='red')

# Set y-axis limits to focus on the relevant range
plt.ylim(1.0, 9.0)
plt.xlim(T_ambient_C.min(), T_ambient_C.max())

# Add a text box explaining the relationship
plt.text(T_ambient_C.min() + 5, 8.5, 
         'Key Takeaway: COP drops as the temperature difference\n($T_{hot} - T_{cold}$) increases.', 
         fontsize=10, bbox=dict(facecolor='white', alpha=0.7, boxstyle="round,pad=0.5"))

# Save the plot to a PNG file instead of showing it interactively
plt.savefig('carnot_cop_plot.png')

# --- Print Summary Data ---
print("\n--- Carnot COP Summary ---")
print(f"Target T_hot: {T_target_1_C}°C ({T_target_1_K:.2f} K) and {T_target_2_C}°C ({T_target_2_K:.2f} K)")

def print_cop_at_temp(T_cold_C, T_hot_C, T_hot_K):
    T_cold_K = celsius_to_kelvin(T_cold_C)
    cop = carnot_cop_heating(T_hot_K, T_cold_K)
    
    # FIX: Check if the result is a NumPy array and extract the scalar value 
    # using .item(), which works for 0D arrays.
    if isinstance(cop, np.ndarray):
        cop = cop.item() # Use .item() to safely extract the scalar value
    
    # Check for NaN before printing
    if np.isnan(cop):
        print(f"Ambient Temp ({T_cold_C}°C): COP @ {T_hot_C}°C = Invalid (T_hot <= T_cold)")
    else:
        print(f"Ambient Temp ({T_cold_C}°C): COP @ {T_hot_C}°C = {cop:.2f}")

print("\nCOP Values at Extreme Cold (-35°C):")
print_cop_at_temp(-35, T_target_1_C, T_target_1_K)
print_cop_at_temp(-35, T_target_2_C, T_target_2_K)

print("\nCOP Values at Moderate Cold (0°C):")
print_cop_at_temp(0, T_target_1_C, T_target_1_K)
print_cop_at_temp(0, T_target_2_C, T_target_2_K)

print("\nCOP Values at Max Ambient (15°C):")
print_cop_at_temp(15, T_target_1_C, T_target_1_K)
print_cop_at_temp(15, T_target_2_C, T_target_2_K)