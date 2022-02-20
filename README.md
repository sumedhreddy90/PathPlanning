# PathPlanning


## Usage
```python
git clone --recursive https://github.com/sumedhreddy90/PathPlanning.git
python puzzleSolver.py
Enter the Initial State:
1 4 7 
5 0 8
2 3 6
```
## Output
```python
Enter the Initial State:
1 4 7 
5 0 8
2 3 6
Initial State [[1, 4, 7], [5, 0, 8], [2, 3, 6]]
Solvable
8 Puzzle Solved!!! Please run plot_path.py script
generating output files
```
## Usage: Plot Planned Path
```python
python plot_path.py
```
## Planned start -> goal Output
Start Node
-------------
| 4 | 1 | 3 | 
-------------
| 7 | 2 | 5 | 
-------------
| 0 | 8 | 6 | 
-------------


Step  1
-------------
| 4 | 1 | 3 | 
-------------
| 7 | 2 | 5 | 
-------------
| 8 | 0 | 6 | 
-------------


Step  2
-------------
| 4 | 1 | 3 | 
-------------
| 0 | 2 | 5 | 
-------------
| 7 | 8 | 6 | 
-------------


Step  3
-------------
| 0 | 1 | 3 | 
-------------
| 4 | 2 | 5 | 
-------------
| 7 | 8 | 6 | 
-------------


Step  4
-------------
| 1 | 0 | 3 | 
-------------
| 4 | 2 | 5 | 
-------------
| 7 | 8 | 6 | 
-------------


Step  5
-------------
| 1 | 2 | 3 | 
-------------
| 4 | 0 | 5 | 
-------------
| 7 | 8 | 6 | 
-------------


Step  6
-------------
| 1 | 2 | 3 | 
-------------
| 4 | 5 | 0 | 
-------------
| 7 | 8 | 6 | 
-------------


Achieved Goal Node
-------------
| 1 | 2 | 3 | 
-------------
| 4 | 5 | 6 | 
-------------
| 7 | 8 | 0 | 
-------------

## Procedure to run the code

1. Initially run the python file puzzleSolver.py
2. Enter the initial values as shown below 
        
 ```python
 Enter the Initial State:
                1 4 7 
                5 0 8
                2 3 6
   ```
3. Then the code checks for solvability condition. If the given input is solvable then the goal state is planned. else program prints a message as "Not solvable"
4. Finally output files are generated
5. To view the paths planned please run plot_path.py
