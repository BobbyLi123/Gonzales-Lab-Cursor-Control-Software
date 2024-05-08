# Brain Computer Interface Toolkit

## Description
This Brain Computer Interface (BCI) Toolkit provides tools to interface with neural data through the OmniPlex Server using the PyOPXClientAPI. It includes two primary applications: a game that uses neural data to control cursor movement and a utility for calculating firing rates of neural groups.

## Installation

1. **Library Dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install tkinter matplotlib numpy
   ```

2. **Plexon and PyOPXClient SDK**:
   Ensure Plexon and the PyOPXClient SDK for Python are installed and properly configured on your system for real-time neural data acquisition. For installation guides and support, visit the [Plexon website](https://plexon.com/).

3. **Clone Repository**:
   Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```

## Setup and Running the Components

### Game (`game.py`)
#### Running the Game
- **Start OmniPlex Server**: Ensure that the OmniPlex Server and PlexControl are running with a valid configuration.
- **Launch the Game**: Navigate to the project directory in a command prompt or terminal and execute:
  ```bash
  python game.py
  ```
  Follow the on-screen prompts to configure neural data groups and control settings. The game interface will appear subsequently.

#### Game Controls and Mechanics
- **Start Button**: Click to begin the game. The cursor will appear and start moving based on the neural data input.
- **Reverse Button**: Click to swap the neural groups controlling upward and downward movements. This allows dynamic control adjustments during gameplay.
- **Cursor Movement**: Controlled by the difference in spike densities between two designated neural groups. The cursor moves toward a target displayed on the screen.

#### How It Works
The game calculates cursor movement using spike density differences from two neural groups specified for upward and downward movements. The spike density is computed by averaging the number of spikes over a 10-second window, normalized by the number of channels, providing a smoothed representation of neural activity influencing the cursor’s motion.

### Firing Rate Calculation (`firing_rate_calculation.py`)
#### Usage
- **Ensure OmniPlex Server Connectivity**: Check that the OmniPlex Server is connected, as this script interfaces directly with it.
- **Execute the Script**: Run the script by executing:
  ```bash
  python firing_rate_calculation.py
  ```
  Enter the number of groups and their units when prompted. The script will continuously compute and display firing rates.

#### Spiking Rate Calculation
The firing rate for each group is calculated by dividing the total number of spikes by the product of the number of channels and the duration of the measurement window. This rate is expressed in Hertz (Hz) and provides insights into the neural activity of each group.

## Features
- **Real-time Neural Data Processing**: Both components use PyOPXClientAPI for real-time data fetching and processing.
- **Interactive GUI in Game**: Provides a user-friendly interface where the cursor is controlled through neural signals.
- **Dynamic Data Analysis**: The firing rate calculator processes and displays neural firing rates, aiding in scientific studies and demonstrations.

## Contributing
Contributors are encouraged to submit improvements or bug fixes through the following process:
1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your modifications.
4. Push to your branch.
5. Create a pull request for review.

## License
This project is licensed to Runda Li, Gonzalas Lab at Vanderbilt University.

---

For detailed information on installation, setup, and operation, refer to the project documentation or raise an issue on the GitHub repository. Explore neural data with this comprehensive BCI Toolkit!
