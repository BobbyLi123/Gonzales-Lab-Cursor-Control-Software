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
