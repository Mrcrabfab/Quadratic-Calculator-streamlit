import streamlit as st
import math
import matplotlib.pyplot as mat

st.title("Quadratic Calculator", text_alignment = "center")
state = 0

col1, col2, col3 = st.columns(3)

# Get a, b and c
a = col1.number_input("a", placeholder = "...", value = None)
b = col2.number_input("b", placeholder = "...", value = None)
c = col3.number_input("c", placeholder = "...", value = None)

container_1 = st.container(border = False, width = "content")
container_2 = st.container(border = False, width = "content")

if a == 0:

    container_1.write("a cannot be zero.")
disc = 0
if a != None and b != None and c != None and a != 0:
    disc = (b*b) - (4*a*c)


# Display discriminant value
col2.metric("Discriminant", f"{disc:g}")

# check for distinct roots when a, b and c are inputed
if disc > 0 and a != None and b != None and c != None and a != 0:
    st.markdown(":green[Two distinct roots exist]")
    x1 = (-b - math.sqrt(disc))/(2*a)
    x2 = (-b + math.sqrt(disc))/(2*a)
    st.write(f"X1 = {x1}")
    st.write(f"X2 = {x2}")

# check for no real roots when a, b and c are inputed
elif disc < 0 and a != None and b != None and c != None and a != 0:
    st.markdown(":red[No real roots.]")

# check for double root when a, b and c are inputed
elif disc == 0 and a != None and b != None and c != None and a != 0:
    x1= (-b)/(2*a)
    x2 = (-b)/(2*a)
    st.markdown(":green[Double root]")
    st.write(f"X1 = X2 = {x1}")


# Represent the parabola
if  disc >= 0 and a is not None and b is not None and c is not None and a != 0:
    # Use a modern built-in style sheet
    mat.style.use("seaborn-v0_8-darkgrid")

    # Center the X-axis grid dynamically on the vertex of the parabola
    vertex_x = -b / (2 * a)
    
    # Generate 100 smooth points around the vertex
    import numpy as np
    x_values = np.linspace(vertex_x - 20, vertex_x + 20, 200)
    y_values = (a * (x_values**2)) + (b * x_values) + c

    fig, ax = mat.subplots(figsize=(10, 5))
    
    # Plot the curve with a thick, vibrant color
    ax.plot(x_values, y_values, color="#1E88E5", linewidth=2.5, label=f"y = {a:g}x² + {b:g}x + {c:g}")
    
    # Highlight the vertex point aswell as the roots
    vertex_y = (a * (vertex_x**2)) + (b * vertex_x) + c
    ax.scatter(vertex_x, vertex_y, color="#D81B60", s=100, zorder=5, label=f"Vertex ({vertex_x:.2f}, {vertex_y:.2f})")
    ax.scatter(x1, 0, color="#E6DCDC", s=100, zorder=5, label=f"Root1 ({x1:.2f}, 0)")
    ax.scatter(x2, 0, color="#000000", s=100, zorder=5, label=f"Root2 ({x2:.2f}, 0)")

    # Clean up axis lines and labels
    ax.axvline(0, color="gray", linewidth=1, linestyle="--")
    ax.axhline(0, color="gray", linewidth=1, linestyle="--")
    ax.set_xlabel("X Axis", fontsize=12)
    ax.set_ylabel("Y Axis", fontsize=12)
    ax.set_title("Parabola Graph Visualization", fontsize=14, fontweight="bold")
    ax.legend(frameon=True, facecolor="white")
    
    st.pyplot(fig)
    state = 1

if state == 1:
    selected = st.feedback("stars")
        






