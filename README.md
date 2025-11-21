# heat_pump_thermo
Models and snippets for calculating stuff about COP, SPF etc.
Read https://en.wikipedia.org/wiki/Coefficient_of_performance

Whatever the refrigerant or mechanisms, you can't do better than 
the theoretical maximum COP as it is limited by the thermodynamics.

Practical heat pumps typically achieve 40% to 60% of their theoretical maximum (Carnot) 
coefficient of performance (COP), due to part-load running, friction, motor and pump 
efficiency, and thermodynamic irreversibility losses.
If the refrigerant boiling point curve with respect to pressure is a poor match for the 
inlet and outlet temperatures, then the percentage efficiency achieved for the theoretical 
maximum COP will be worse.

From Wikipedia:  
"increasing the size of pipes... would help to reduce noise and the energy consumption of pumps... by decreasing the speed of the fluid, which in turn lowers the Reynolds number and hence the turbulence (and noise) and the head loss. The heat pump itself can be improved by increasing the size of the internal heat exchangers, which in turn increases the efficiency (and the cost) relative to the power of the compressor, and also by reducing the system's internal temperature gap over the compressor. Obviously, this latter measure makes some heat pumps unsuitable to produce high temperatures, which means that a separate machine is needed for producing, e.g., hot tap water."
<img width="1000" height="600" alt="carnot_cop_plot" src="https://github.com/user-attachments/assets/3dffae5f-c88d-4418-b834-36ae63d1e9b4" />



# Carnot COP Summary
Target T_hot: 35°C (308.15 K) and 65°C (338.15 K)

COP Values at Extreme Cold (-35°C):  
Ambient Temp (-35°C): COP @ 35°C = 4.40  
Ambient Temp (-35°C): COP @ 65°C = 3.38

COP Values at Moderate Cold (0°C):  
Ambient Temp (0°C): COP @ 35°C = 8.80  
Ambient Temp (0°C): COP @ 65°C = 5.20

COP Values at Max Ambient (15°C):  
Ambient Temp (15°C): COP @ 35°C = 15.41  
Ambient Temp (15°C): COP @ 65°C = 6.76
