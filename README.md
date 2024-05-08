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
This project features a Brain-Computer Interface (BCI) game that uses neural data to control the movement of a cursor on the screen towards a target. The application utilizes the `PyOPXClientAPI` for handling neural data and `tkinter` for the graphical user interface.

## Installation

1. **Library Dependencies**:
   Before running the game, install the necessary Python libraries using pip:
   ```bash
   pip install tkinter
   ```

2. **Plexon and PyOPXClient SDK**:
   Ensure that Plexon and the PyOPXClient SDK for Python are installed and configured on your system to handle real-time acquisition of neural data. Installation guides and support can be found on the [Plexon website](https://plexon.com/).

3. **Clone Repository**:
   Clone this repository to your local machine using:
   ```bash
   git clone <repository-url>
   ```

## Setup and Running the Game

1. **Start OmniPlex Server**:
   Begin by starting the OmniPlex Server and PlexControl with a valid configuration to ensure that neural data can be processed in real-time.

2. **Navigate to the PyOPXClient Folder**:
   Open a command prompt window, navigate to the folder containing the `PyOPXClient` installation, and then proceed to the directory of the cloned game script.

3. **Run the Game**:
   Execute the game by running:
   ```bash
   python bci_game.py
   ```
   Follow the on-screen prompts to configure the number of neural data groups, specify units for each group, and assign groups for upward and downward movements. The game window will open after these configurations, and you can start playing by clicking the "Start" button.

### Game Controls:
- **Start Button**: Initiates the game session.
- **Reverse Button**: Switches the control groups for upward and downward movements.

### How It Works:
The cursor's movement is controlled by the differences in spike density between the designated neural groups assigned to move the cursor upward and downward. The goal is to align the cursor with a target placed randomly on the screen.

## Features
- **Real-time Neural Data Integration**: Utilizes the PyOPXClientAPI for fetching and processing neural data in real-time.
- **Adaptive Difficulty**: Adjusts cursor movement speed based on calculated average speeds to balance game difficulty.
- **Interactive GUI**: Offers visual feedback for cursor and target positions and includes controls to adjust movement directions.

## Contributing
To contribute to this project:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to your branch.
5. Submit a pull request for review.

## License
This project is licensed to Runda Li, Gonzalas Lab at Vanderbilt University.
