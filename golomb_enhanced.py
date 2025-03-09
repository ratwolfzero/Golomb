import matplotlib.pyplot as plt
import numpy as np
from numba import njit

# Predefined Golomb rulers
GOLOMB_RULERS = {
    5: [0, 1, 4, 9, 11],
    6: [0, 1, 4, 10, 12, 17],
    7: [0, 1, 4, 10, 18, 23, 25],
    8: [0, 1, 4, 9, 15, 22, 32, 34],
}

@njit
def compute_fractal_lines(start, angle, length, depth, ruler, max_lines, max_depth):
    stack = [(start[0], start[1], angle, length, depth)]
    ax_lines = np.zeros((max_lines, 4), dtype=np.float64)
    colors = np.zeros(max_lines, dtype=np.float64)
    line_count = 0
    
    while stack:
        x, y, angle, length, depth = stack.pop()
        if depth == 0:
            continue
        
        for mark in ruler[1:]:
            scale_factor = 1.2 + (mark % 2) * 0.3  # Irregular scaling
            new_length = length / scale_factor
            new_angle = angle + ((mark % 3) - 1) * (np.pi / 6)  # Diverse angles
            dx = new_length * np.cos(new_angle)
            dy = new_length * np.sin(new_angle)
            new_x = x + dx * mark
            new_y = y + dy * mark
            
            if line_count < max_lines:
                ax_lines[line_count, 0] = x
                ax_lines[line_count, 1] = y
                ax_lines[line_count, 2] = new_x
                ax_lines[line_count, 3] = new_y
                colors[line_count] = ((depth / max_depth) + (new_angle / (2 * np.pi)) + (mark / max(ruler))) % 1.0
                line_count += 1
            
            stack.append((new_x, new_y, new_angle + np.pi / 6, new_length, depth - 1))
            stack.append((new_x, new_y, new_angle - np.pi / 6, new_length, depth - 1))
    
    return ax_lines, colors, line_count


def plot_fractal(ax_lines, colors, line_count):
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')  # Dark background
    ax.set_aspect('equal')
    ax.axis('off')
    cmap = plt.get_cmap('twilight')
    
    for i in range(line_count):
        ax.plot(
            [ax_lines[i, 0], ax_lines[i, 2]],
            [ax_lines[i, 1], ax_lines[i, 3]],
            color=cmap(colors[i]),
            lw=1.2, alpha=0.7  # Glowing effect
        )
    
    plt.show()


def get_user_input():
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
    ruler, depth = get_user_input()
    max_lines = 1000000  
    ax_lines, colors, line_count = compute_fractal_lines(
        (0.0, 0.0), np.pi / 2, 10.0, depth, np.array(ruler), max_lines, depth
    )
    plot_fractal(ax_lines, colors, line_count)


if __name__ == "__main__":
    main()
