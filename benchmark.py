import time
import numpy as np

def benchmark_map_creation(create_map_function, ground_truth_map):
    start_time = time.time()
    composite_map = create_map_function()
    end_time = time.time()
    latency = end_time - start_time
    error = np.mean(np.abs(composite_map - ground_truth_map))
    return latency, error

def create_dummy_map():
    return np.zeros((512, 512))

def get_ground_truth_map():
    return np.zeros((512, 512))

latency, error = benchmark_map_creation(create_dummy_map, get_ground_truth_map())
print(f"Map creation latency: {latency:.2f} seconds")
print(f"Map accuracy/error: {error:.4f}")
