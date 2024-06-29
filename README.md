
# Heuristics-Algorithm-Graph

Heuristics-Algorithm-Graph is a Python project designed to generate visual representations of process mining data. The project utilizes heuristic algorithms along with the PM4Py library to create insightful PNG graph images from process data.

## Technologies Used

- **Python**: The core programming language.
- **PM4Py**: A process mining library, used for its robust data processing and mining capabilities.
- **Matplotlib**: Utilized for generating and plotting the graphs.
- **Pandas**: For reading and manipulating CSV data effectively.
- **NumPy**: Employed for handling numerical operations.

## Installation

To get started, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/EgliTafa/Heuristics-Algorythm-Graph.git
   cd Heuristics-Algorythm-Graph
   ```

2. Set up a Python virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```bash
   pip install pm4py matplotlib pandas numpy
   ```

## Usage

To run the project and generate graphs from your process data, execute the main script by specifying the CSV input file:
   ```bash
   python heuristic_algorithm_for_bpmn.py --input case_activities.csv
   ```
This command processes the data in 'case_activities.csv' to generate a graph, which visualizes the process flow using heuristic algorithms. The output is a PNG image that represents these data-driven insights effectively.

## Output
The output of this project is a PNG file that provides a visual graph representation of the processed data, aiding in the analysis of workflow processes and decision-making points.
