import matplotlib.pyplot as plt
import numpy as np
from numba import njit

# Predefined Golomb rulers for different N
GOLOMB_RULERS = {
    5: [0, 1, 4, 9, 11],
    6: [0, 1, 4, 10, 12, 17],
    7: [0, 1, 4, 10, 18, 23, 25],
    8: [0, 1, 4, 9, 15, 22, 32, 34],
}

@njit
def compute_fractal_lines(start, angle, length, depth, ruler, max_lines, max_depth):
    """
    Compute the line segments for the fractal tree iteratively.
    Returns:
        ax_lines: Array of line segments (x1, y1, x2, y2).
        colors: Array of normalized values for coloring based on angle and depth.
        line_count: Number of valid lines computed.
    """
    stack = [(start[0], start[1], angle, length, depth)]
    
    ax_lines = np.zeros((max_lines, 4), dtype=np.float64)
    colors = np.zeros(max_lines, dtype=np.float64)
    line_count = 0
    
    while stack:
        x, y, angle, length, depth = stack.pop()
        
        if depth == 0:
            continue
        
        for mark in ruler[1:]:  # Skip the first mark (0)
            new_length = length / 1.5  # Scale factor for recursion
            dx = new_length * np.cos(angle)
            dy = new_length * np.sin(angle)
            new_x = x + dx * mark
            new_y = y + dy * mark
            
            # Store the line segment and its color based on angle and depth
            if line_count < max_lines:
                ax_lines[line_count, 0] = x
                ax_lines[line_count, 1] = y
                ax_lines[line_count, 2] = new_x
                ax_lines[line_count, 3] = new_y
                
                # Normalize color based on both depth and angle
                colors[line_count] = ((depth / max_depth) + (angle / (2 * np.pi))) % 1.0
                
                line_count += 1
            
            # Push branches onto the stack
            stack.append((new_x, new_y, angle + np.pi / 6, new_length, depth - 1))
            stack.append((new_x, new_y, angle - np.pi / 6, new_length, depth - 1))
    
    return ax_lines, colors, line_count

def plot_fractal(ax_lines, colors, line_count):
    """
    Plot the fractal using the computed line segments and colors.
    """
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    # Create a colormap
    cmap = plt.get_cmap('twilight')  # Smooth gradient color transitions
    
    # Plot all line segments with computed colors
    for i in range(line_count):
        ax.plot(
            [ax_lines[i, 0], ax_lines[i, 2]],
            [ax_lines[i, 1], ax_lines[i, 3]],
            color=cmap(colors[i]),  # Use angle-depth blended color
            lw=1
        )
    
    plt.show()

def get_user_input():
    """
    Get user input for Golomb ruler and depth.
    Returns:
        ruler: Selected Golomb ruler.
        depth: Selected recursion depth.
    """
    print("Available Golomb rulers:")
    for n, ruler in GOLOMB_RULERS.items():
        print(f"N={n}: {ruler}")
    
    n = int(input("Select N for the Golomb ruler (e.g., 5, 6, 7, 8): "))
    depth = int(input("Select recursion depth (e.g., 3, 4, 5): "))
    
    if n not in GOLOMB_RULERS:
        print("Invalid N selected. Using default N=5.")
        n = 5
    
    ruler = GOLOMB_RULERS[n]
    print(f"Using Golomb ruler for N={n}: {ruler}")
    print(f"Drawing fractal with depth={depth}...")
    
    return ruler, depth

def main():
    """
    Main function to orchestrate the fractal generation and plotting.
    """
    # Get user input
    ruler, depth = get_user_input()
    
    # Preallocate arrays to store line segments and colors
    max_lines = 1000000  # Adjust this based on expected number of lines
    
    # Compute fractal lines
    ax_lines, colors, line_count = compute_fractal_lines(
        (0.0, 0.0), np.pi / 2, 10.0, depth, np.array(ruler), max_lines, depth
    )
    
    # Plot the fractal
    plot_fractal(ax_lines, colors, line_count)

if __name__ == "__main__":
    main()
