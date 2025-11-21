import numpy as np
import matplotlib.pyplot as plt
import os

# --- 1. Extracted Data for the Trend Line (Red Dashed Line) ---
# This data represents the approximate relationship between Average Outside Temperature (X) 
# and Average Coefficient of Performance (Y) as seen in the uploaded image.
TREND_LINE_DATA = {
    'temperature_c': np.array([-20, -15, -10, -5, 0, 5, 10]),
    'cop_avg': np.array([1.8, 2.0, 2.2, 2.5, 2.8, 3.3, 3.7])
}

def generate_synthetic_scatter_data(trend_x, trend_y, num_points=1200):
    """
    Generates synthetic scatter data points that cluster around the provided trend line.
    
    The original plot shows increasing scatter/variance as temperature increases, 
    and a noticeable dip in the middle (around -5C to 0C). This function attempts
    to mimic that visual distribution.
    """
    # Create an interpolation function from the trend data
    trend_poly = np.polyfit(trend_x, trend_y, 3) # Use a 3rd degree polynomial fit
    p = np.poly1d(trend_poly)

    # Generate random temperatures within the plot range (-20 to 10)
    # Use a normal distribution centered slightly above the average to mimic the point density
    np.random.seed(42) # for reproducibility
    synthetic_temp = np.random.uniform(trend_x.min(), trend_x.max(), num_points)
    
    # Calculate the expected COP based on the trend line polynomial
    expected_cop = p(synthetic_temp)

    # Calculate the variance for the scatter: variance increases with temperature
    # and has a fixed component (0.2) plus a temp-dependent component.
    variance_factor = 0.2 + 0.1 * ((synthetic_temp + 20) / 30)
    
    # Introduce random noise (the scatter)
    synthetic_cop = expected_cop + np.random.normal(0, variance_factor, num_points)

    # Clip the data to ensure it stays within a reasonable range (e.g., COP >= 0.5)
    synthetic_cop = np.maximum(synthetic_cop, 0.5) 
    
    return synthetic_temp, synthetic_cop, p(synthetic_temp)


def reproduce_plot(trend_data, output_filename='reproduced_cop_plot.png'):
    """
    Encodes the styling, plots the data, and saves the figure as a PNG file.
    """
    
    # Generate the synthetic data for the scatter plot
    scatter_x, scatter_y, fitted_trend_y = generate_synthetic_scatter_data(
        trend_data['temperature_c'], 
        trend_data['cop_avg']
    )
    
    # --- Plotting Setup ---
    plt.figure(figsize=(10, 6))
    
    # 1. Scatter Plot (Blue, translucent points)
    plt.scatter(
        scatter_x, 
        scatter_y, 
        s=15,                 # Marker size
        alpha=0.4,            # Translucency for density effect
        color='#3498db',      # A distinct blue color
        label='Hourly Data Points'
    )
    
    # 2. Trend Line (Red, dashed line)
    # Generate points for a smooth trend line based on the fitted polynomial
    smooth_x = np.linspace(trend_data['temperature_c'].min(), trend_data['temperature_c'].max(), 300)
    
    plt.plot(
        smooth_x, 
        np.poly1d(np.polyfit(trend_data['temperature_c'], trend_data['cop_avg'], 3))(smooth_x),
        linestyle='--', 
        color='#e74c3c', 
        linewidth=2,
        label='Average Trend Line'
    )

    # --- Styling and Labels to Match Original Image ---
    
    # Set labels
    plt.xlabel('Average outside temperature (°C)', fontsize=14, labelpad=15)
    plt.ylabel('Average Coefficient of Performance', fontsize=14, labelpad=15)
    
    # Set limits (slightly beyond the data for context)
    plt.xlim(-20.5, 10.5)
    plt.ylim(0.8, 6.0) 
    
    # Set Ticks for X and Y axes
    plt.xticks(np.arange(-20, 11, 5))
    plt.yticks(np.arange(1, 7, 1))

    # Add grid lines (horizontal only, as in the original)
    plt.grid(axis='y', color='gray', linestyle='-', linewidth=0.5, alpha=0.7)
    
    # Remove the top and right spines (border lines)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Ensure the bottom and left spines are visible and align with the axes
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')

    # Display the plot title
    plt.title('Average Coefficient of Performance vs. Outside Temperature (Simulated)', fontsize=16)
    
    # --- Save the figure to a PNG file ---
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    plt.close() # Close the plot figure after saving to free memory
    
    print(f"\nSuccessfully generated and saved the plot to '{output_filename}'")


# Run the plotting function
if __name__ == "__main__":
    reproduce_plot(TREND_LINE_DATA)
    