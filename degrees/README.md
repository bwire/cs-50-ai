# CS50 AI - Degrees of Separation

🎬 **Finding the shortest path between actors in Hollywood**

This project implements a solution to find the degrees of separation between any two actors using breadth-first search (BFS) algorithm, inspired by the "Six Degrees of Kevin Bacon" game.

## 📋 Project Overview

Based on the [CS50 AI Project 0: Degrees](https://cs50.harvard.edu/ai/projects/0/degrees/), this program determines how many "degrees of separation" apart two actors are by finding the shortest path through movies they've starred in together.

### Example Output
```
$ python degrees.py small
Loading data...
Data loaded.
Name: Robin Wright
Name: Tom Hanks
1 degrees of separation.
1: Robin Wright and Tom Hanks starred in Forrest Gump
```

## 🚀 Key Implementation Details

### 1. `shortest_path(source, target)` Function
- **Algorithm**: Breadth-First Search (BFS) using `QueueFrontier`
- **Optimization**: Early goal detection - checks for target when adding nodes to frontier
- **Path Reconstruction**: Custom `unwind_node_back()` function to trace the shortest path
- **Edge Cases**: Handles same person (returns empty list) and disconnected actors (returns None)

### 2. Enhanced `neighbors_for_person(person_id, frontier)` Function
- **Optimization**: Prevents duplicate states in frontier using `frontier.contains_state()`
- **Efficiency**: Only adds new (movie_id, person_id) pairs not already in the search frontier
- **Memory Management**: Reduces redundant nodes and improves search performance

### 3. Additional Helper Functions
- **`unwind_node_back(node)`**: Reconstructs the path from target back to source
- **Visited Set**: Prevents revisiting the same person during search
- **State Management**: Tracks (movie_id, person_id) pairs for path reconstruction

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   CSV Data      │    │   Data Loading   │    │   BFS Search    │
│   (people,      │───▶│   (load_data)    │───▶│   (shortest_    │
│    movies,      │    │                  │    │    path)        │
│    stars)       │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                                                         ▼
                                                ┌─────────────────┐
                                                │  Path Output    │
                                                │  (degrees of    │
                                                │   separation)   │
                                                └─────────────────┘
```

## 📊 Data Structure

- **`names`**: Maps actor names to person IDs
- **`people`**: Maps person IDs to actor details and their movies
- **`movies`**: Maps movie IDs to movie details and their stars
- **`stars`**: Establishes relationships between people and movies

## 🎯 Algorithm Efficiency

- **Time Complexity**: O(V + E) where V is vertices (actors) and E is edges (movie connections)
- **Space Complexity**: O(V) for visited set and frontier
- **Optimizations**:
  - Early goal detection
  - Duplicate state prevention
  - Visited set to avoid cycles

## 🧪 Testing

The solution works with both datasets:
- **Small dataset**: For testing and development
- **Large dataset**: Full IMDb data for comprehensive testing

```bash
# Test with small dataset
python degrees.py small

# Test with large dataset  
python degrees.py large
```

## 📚 Course Information

This project is part of [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/projects/0/degrees/) from Harvard University.

**Project Requirements**:
- Implement `shortest_path()` function using BFS
- Return shortest path as list of (movie_id, person_id) tuples
- Handle cases with no path (return None)
- Optimize for efficiency and correctness

## 🏆 Features

✅ **Breadth-First Search Implementation**  
✅ **Early Goal Detection**  
✅ **Duplicate State Prevention**  
✅ **Path Reconstruction**  
✅ **Edge Case Handling**  
✅ **Memory Optimization**  

---

*Built with Python 3.12 | CS50 AI Project 0*
