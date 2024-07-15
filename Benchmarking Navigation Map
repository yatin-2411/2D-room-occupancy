import time

def benchmark_navigation_map_creation(stitch_images_function, create_occupancy_grid_function, image_paths):
    start_time = time.time()
    
    # Create the stitched image
    stitched_image = stitch_images_function(image_paths)
    if stitched_image is None:
        return None, None
    
    # Create the occupancy grid
    create_occupancy_grid_function(stitched_image)
    
    end_time = time.time()
    latency = end_time - start_time
    
    # Dummy ground truth map for benchmarking purposes
    ground_truth_map = np.zeros_like(stitched_image[:, :, 0])
    
    # Load the created occupancy grid
    created_occupancy_grid = cv2.imread('occupancy_grid.pgm', cv2.IMREAD_GRAYSCALE) // 255
    
    # Calculate the error between the created map and the ground truth
    error = np.mean(np.abs(created_occupancy_grid - ground_truth_map))
    
    return latency, error

latency, error = benchmark_navigation_map_creation(stitch_images, create_occupancy_grid, image_paths)
print(f"Navigation map creation latency: {latency:.2f} seconds")
print(f"Navigation map accuracy/error: {error:.4f}")
