# CursorControlPlexon
A cursor control system using firing rate, based on Plexon

## Class: FiringRateCalculator

### Initialization

The class is initialized with an optional `time_slot_duration` parameter (default is 1000 milliseconds). This parameter determines the duration of the time slot for which the firing rates are calculated.

```python
calculator = FiringRateCalculator(time_slot_duration=1000)
```

### Method: connect
This method connects to the OmniPlex Server. If the connection is successful, it prints the source of the keyboard events.

```python
calculator.connect()
```

Method: calculate_firing_rates
This method is a generator that continuously calculates and yields the firing rates of units. The firing rates are calculated for each time slot and are returned as a dictionary where the keys are the units and the values are the firing rates.

```python
for firing_rates in calculator.calculate_firing_rates():
    print(firing_rates)
```

Usage
To use this class in your larger program, you can import it and create an instance of it. Then, you can call the connect method to connect to the OmniPlex Server and the calculate_firing_rates method to get the real-time firing rates.

```python
from firing_rate_class import FiringRateCalculator

calculator = FiringRateCalculator()
calculator.connect()
for firing_rates in calculator.calculate_firing_rates():
    # Use firing_rates to control the cursor
    ...
```

This will continuously calculate and yield firing rates until you stop the loop.

# Brain Computer Interface Game

## Description
This project features a Brain-Computer Interface (BCI) game that uses neural data to control the movement of a cursor on the screen towards a target. The application is written in Python and utilizes the `PyOPXClientAPI` for handling neural data and `tkinter` for the graphical user interface.

## Installation

1. **Library Dependencies**:
   Before running the game, you must install the necessary Python libraries. You can install them using pip:
   ```bash
   pip install pyopxclient tkinter
   ```

2. **Plexon Installation**:
   Ensure that Plexon is installed and running on your system to handle the real-time acquisition of neural data. Visit the [Plexon website](https://plexon.com/) for installation guides and support.

3. **Clone Repository**:
   Clone this repository to your local machine using:
   ```bash
   git clone <repository-url>
   ```

## Usage

To start the game, navigate to the directory containing the script and run:
```bash
python bci_game.py
```
Upon launching, the game will prompt for configuration settings such as the number of neural data groups, specific units per group, and groups assigned to control upward and downward movements. After these initial setups, the game window will open, and you can start the game by clicking the "Start" button.

### Game Controls:
- **Start Button**: Begins the game session.
- **Reverse Button**: Reverses the control groups for up and down movements.

### How It Works:
The game calculates cursor movement based on the spike density differences between the designated neural data groups for upward and downward movements. The cursor moves towards a randomly placed target on the screen, and the objective is to align the cursor with the target.

## Features
- **Real-time Neural Data Processing**: Integrates with PyOPXClientAPI to fetch and process neural data in real-time.
- **Dynamic Difficulty Adjustment**: The speed of the cursor's movement adjusts based on the average speed calculated from recent movements, providing a balanced difficulty level.
- **GUI Feedback**: Provides visual feedback on cursor and target positions, as well as controls to reverse movement directions.

## Contributing
Contributors are welcome to propose enhancements or fix bugs. To contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License
This project is licensed to Runda Li, Gonzalas Lab at Vanderbilt University.
