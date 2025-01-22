# MATLAB_Simulink_to_Blender_Simulation

This repository contains the code and resources for a project that simulates a dynamic system and animates it using MATLAB Simulink, Python, and Blender. The project involves plotting the system's response, exporting data, and using it to create an animated 3D simulation in Blender.

## Project Overview

In this project, the system's output response is modeled in **MATLAB Simulink**, and the resulting data for two objects in the system is extracted as an Excel sheet. Python scripting is used in **Blender** to animate the motion of the objects using keyframes. A custom mathematical model was developed to calculate the behavior of the springs connecting the objects, as no direct data for their stretch or position was available.

### Key Features

- **MATLAB Simulink** for modeling and system response plotting.
- **Excel** export of object motion data.
- **Python** scripting for animating objects in **Blender**.
- Mathematical model to calculate spring stretch and position.
- Integration of diverse tools for 3D animation of a physical simulation.

## Requirements

To run this project, you'll need the following software installed:

- **MATLAB** (with Simulink)
- **Blender** (v4.1+)
- **Python** (v3.8+)

## simulation material

1. **Simulink Simulation**:  
   - Open the Simulink model (`system_simulation.slx`) in MATLAB.
   - Run the simulation and export the output response as an Excel file.
   
2. **Blender Animation**:  
   - Open the Blender file (`simulation.blend`).
   - add the Python script (`animate_objects.py`) to import the Excel data and create keyframe animations.

3. **Mathematical Model**:  
   - The Python script also computes the spring's stretch and position using a mathematical model defined in `spring_model.py`.

## Project Structure

- `/MATLAB/`: Contains the Simulink model and any related MATLAB files.
- `/Blender/`: Contains the Blender scene file and Python scripts for animation.
- `/Data/`: Example Excel data from the Simulink simulation.

## Acknowledgments

Special thanks to **Dr. Ahmed Zaki** for his guidance in the "System Dynamics and Control Components" course, and for featuring this work in the course material.


