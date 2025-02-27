# MATLAB_Simulink_to_Blender_Simulation

This repository contains the code and resources for simulating and animating a dynamic system using **MATLAB Simulink**, **Python**, and **Blender**. It provides a step-by-step guide for users who wish to modify or build upon the project, whether it's adjusting the simulation parameters or tweaking the 3D animation.

## Project Overview

This project simulates a dynamic system where two objects are connected by springs. The system's output response is modeled using **MATLAB Simulink**, with the data exported into an Excel sheet. Python scripting in **Blender** is used to animate the motion of the objects. A custom mathematical model calculates the behavior of the springs in the simulation.

### Key Features

- **MATLAB Simulink** for modeling and system response simulation.
- **Blender** for 3D animation of the objects based on the simulation data.
- Python script to import simulation data and create keyframe animations in Blender.
- Mathematical model for spring behavior, allowing dynamic simulation adjustments.

## Requirements

To run or modify this project, you will need the following:

- **MATLAB** (with Simulink) to edit or run the dynamic system simulation.
- **Blender** (v2.9+) to adjust or create new animations.

## How to Edit/Modify

### 1. **Editing the Simulink Model**

If you want to change the system parameters (e.g., mass, damping, spring constant):
- Open the Simulink model file in MATLAB.
- Modify the block parameters as needed.
- Run the simulation and **export the new data** into an Excel file by saving the output signals.

### 2. **Modifying the Python Script for Animation**

To adjust the animation based on new simulation data:
- **Update the Excel file**: If you've re-run the Simulink model, place the new Excel data in the folder.
- Open the Python script, and ensure the file path to the Excel data is updated.
  - The script reads data from the Excel file and assigns keyframe movements to the objects in Blender.
  - If you’ve changed the number of objects or added new variables, adjust the script logic to reflect the new data structure.


### 4. **Modifying the Blender Animation**

To adjust or add new visual elements to the Blender scene:
- Open the Blender project file.
- You can move, scale, or rotate the objects, add new keyframes, or adjust the camera angles for improved visualization.
- Run the updated Python script in Blender’s scripting panel to apply new animation keyframes based on your modified simulation data.

### 5. **Rendering the Animation**

Once satisfied with your modifications:
- Set your render settings in Blender (resolution, frame rate, etc.).
- Render the animation using Blender's rendering options.


## Troubleshooting & Tips

- **Simulink Issues**: Ensure all blocks and signals are correctly configured in the model before running the simulation.
- **Excel Data Format**: The Python script assumes a specific format for the Excel data (time and position data for the objects). Ensure your data follows this structure or adjust the script accordingly.
- **Blender Animation**: If the animation isn’t updating properly, check that the Python script is running in Blender’s scripting panel and that the objects are properly linked to the keyframe data.

