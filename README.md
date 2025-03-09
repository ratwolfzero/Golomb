
# Golomb Rulers: History and Purpose  

Golomb rulers were invented by **Solomon W. Golomb** in the 1950s. They are sets of marks at integer positions along a ruler such that no two pairs of marks have the same distance. Originally studied in **combinatorial mathematics**, Golomb rulers have practical applications in:  

- **Radio astronomy** (minimizing interference in antenna arrays).  
- **X-ray crystallography** (improving measurement accuracy).  
- **Error correction codes** (helping with unique signal identification).  

## Golomb Ruler-Based Fractal Trees  

In this code, we use a **Golomb ruler to generate fractal-like trees**. The Golomb ruler defines branch placement, creating a structured yet non-uniform growth pattern. By iterating through recursive depth levels, the fractal expands with each branch positioned according to Golomb ruler marks.  

To enhance visualization, colors are assigned based on both **angle and depth**, ensuring clear differentiation even in dense regions. This approach blends **combinatorial mathematics with fractal geometry**, producing unique and intricate branching structures.  

## How This Code Works  

The code **recursively generates a fractal tree-like structure** using a **Golomb ruler** to determine branching points. Here’s how it works:

### 1. User Input  

- The user selects an **N-value** (defining the Golomb ruler) and a recursion **depth**.  
- Example: If `N=5`, the ruler `{0, 1, 4, 9, 11}` determines branch positions.  

### 2. Recursive Fractal Growth  

- A **stack-based iterative method** (instead of recursion) is used to prevent deep recursion issues.  
- The fractal starts at `(0,0)`, growing upwards (`π/2` radians).  
- Each branch spawns two new branches at ±30° (`π/6`).  
- The **Golomb ruler** determines the spacing of these branches.  

### 3. Color Assignment (Depth & Angle Blending)  

- Instead of using depth alone for coloring, it blends **depth and angle** into a **smooth gradient**.
- Formula:  

    colors[line_count] = ((depth / max_depth) + (angle / (2 * np.pi))) % 1.0

- The `'twilight'` colormap ensures a visually appealing distribution.  

### 4. Plotting the Fractal  

- The code uses **Matplotlib** to plot the computed line segments.  
- Dense regions become visually distinct due to the angle-depth-based color mapping.  

## Why Is This Approach Interesting?  

- **Golomb rulers provide a structured but non-uniform branching pattern** → creating a unique fractal.  
- **Color mapping by angle + depth** makes dense areas visually interesting.  
- **Iterative approach using a stack** avoids recursion depth issues in Python.  
