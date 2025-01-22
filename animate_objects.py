import bpy
import csv

# Paths to your data files (adjust the file paths accordingly)
file_path_1 = r'F:\apps\Blender\projects\system dynamics\ball1.csv'
file_path_2 = r'F:\apps\Blender\projects\system dynamics\ball2.csv'

# Create lists to hold time and position data
time_data_1 = []
pos_data_1 = []

time_data_2 = []
pos_data_2 = []

# Function to read the CSV file data
def read_csv_data(file_path, time_list, pos_list):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if needed
        for row in reader:
            time_list.append(float(row[0]))  # Time data
            pos_list.append(float(row[1]))   # Position (or response data)

# Read data for both objects
read_csv_data(file_path_1, time_data_1, pos_data_1)
read_csv_data(file_path_2, time_data_2, pos_data_2)

# Selecting the objects
obj_1 = bpy.data.objects['obj_1']  
obj_2 = bpy.data.objects['obj_2']  

# adding some constants
obj_1.location.x = -5
obj_2.location.x = 5
obj_1.location.z = 5
obj_2.location.z = 5
objfs =obj_1.location.x
objss =obj_2.location.x

# Apply keyframes based on the transfer function data
for i in range(len(time_data_1)):
    # Set keyframes for Object 1 (X-axis movement based on pos_data_1)
    obj_1.location.x = objfs + pos_data_1[i]
    obj_1.keyframe_insert(data_path="location", frame=10*time_data_1[i])

for i in range(len(time_data_2)):
    # Set keyframes for Object 2 (X-axis movement based on pos_data_2)
    obj_2.location.x = objss + pos_data_2[i]
    obj_2.keyframe_insert(data_path="location", frame=10*time_data_2[i])

print("done")
