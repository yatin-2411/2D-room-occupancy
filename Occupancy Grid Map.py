def create_occupancy_grid(stitched_image, resolution=0.05):
    gray_image = cv2.cvtColor(stitched_image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Create occupancy grid with 1 for obstacles and 0 for free space
    occupancy_grid = (binary_image // 255).astype(np.uint8)
    
    # Save the occupancy grid as a PGM file
    pgm_image = Image.fromarray(occupancy_grid * 255)
    pgm_image.save('occupancy_grid.pgm')
    
    # Save the YAML file for map metadata
    map_metadata = f"image: occupancy_grid.pgm\nresolution: {resolution}\norigin: [0.0, 0.0, 0.0]\nnegate: 0\noccupied_thresh: 0.65\nfree_thresh: 0.196"
    with open('occupancy_grid.yaml', 'w') as f:
        f.write(map_metadata)

create_occupancy_grid(stitched_image)
