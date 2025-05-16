# Ford-Fulkerson Algorithm Visualization with Manim

This project visualizes the **Ford-Fulkerson algorithm** using [Manim](https://www.manim.community/), a mathematical animation engine. 
The animation demonstrates step-by-step how the algorithm finds the maximum flow in a flow network.

## 🎥 Video
[![Watch the video](https://i.imgur.com/fMRlPC8.png)](https://www.youtube.com/watch?v=yrL2SJI37b0)



## 📌 What It Does

- Animates the Ford-Fulkerson algorithm on a simple directed graph.
- Shows augmenting paths and bottlenecks in each step.
- Updates flow values dynamically on each edge.
- Includes an introductory explanation of how the algorithm works.

## 🎥 Features

- Clear visual layout of graph nodes and edges.
- White-colored labels and explanations for dark theme compatibility.
- Text explanations under each step for educational clarity.

## 🧠 Algorithm Overview

The Ford-Fulkerson algorithm finds the **maximum flow** from a **source** to a **sink** by:
1. Repeatedly finding augmenting paths with available capacity.
2. Sending flow along these paths.
3. Terminating when no more such paths exist.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Manim CE (Community Edition)

Install Manim with pip:

```bash
pip install manim
```
## 🎬 Render the Animation

To render the animation at low quality locally using Manim, run:

```bash
manim -pql ford_fulkerson.py FordFulkersonStepByStep
```

To render the animation at high quality locally using Manim, run:

```bash
manim -pqh ford_fulkerson.py FordFulkersonStepByStep
```
