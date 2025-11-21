# heat_pump_thermo
Models and snippets for calculating stuff about COP, SPF etc.

Whatever the refrigerant or mechanisms, you can't do better than 
the theoretical maximum COP as it is limited by the thermodynamics.

Practical heat pumps typically achieve 40% to 60% of their theoretical maximum (Carnot) 
coefficient of performance (COP), due to part-load running, friction, motor and pump 
efficiency, and thermodynamic irreversibility losses.

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
