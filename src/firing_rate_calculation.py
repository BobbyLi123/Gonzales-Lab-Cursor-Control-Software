from pyopxclient import PyOPXClientAPI, OPX_ERROR_NOERROR
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import time
from datetime import datetime

SPIKE_TYPE = 1

def run():
    # Initialize the API class
    client = PyOPXClientAPI()

    # Connect to OmniPlex Server, check for success
    client.connect()
    if not client.connected:
        print ("Client isn't connected, exiting.\n")
        print ("Error code: {}\n".format(client.last_result))
        exit()

    print ("Connected to OmniPlex Server\n")

    num_groups = int(input("Enter the number of groups: "))
    groups = {}
    for i in range(num_groups):
        units = input("Enter the units for group {}, separated by commas: ".format(i+1)).split(',')
        units = [int(unit) for unit in units]
        groups[i+1] = units

    group_timestamps = {group: [] for group in range(1, num_groups+1)}
    group_spike_densities = {group: [] for group in range(1, num_groups+1)}
    group_channels = {group: set() for group in range(1, num_groups+1)}

    global_parameters = client.get_global_parameters()
    for source_id in global_parameters.source_ids:
        source_name, _, _, _ = client.get_source_info(source_id)
        if source_name == 'KBD':
            keyboard_event_source = source_id
            print ("Keyboard event source is {}".format(keyboard_event_source))

    # Include all spike sources
    source_ids = client.get_global_parameters().source_ids

    # Define the time slot duration in milliseconds
    time_slot_duration = 1000

    try:
        while True:
            # Wait for new data for the duration of the time slot
            # client.opx_wait(time_slot_duration)
            # Get a new batch of client data
            time.sleep(time_slot_duration/1000.0)
            
            new_data = client.get_new_data(timestamps_only=True)
            
            # Iterate over the new data
            for i in range(new_data.num_timestamps):
                unit = new_data.unit[i]
                for group, units in groups.items():
                    if unit in units:
                        # Add the timestamp to the list for this group
                        group_timestamps[group].append(new_data.timestamp[i])
                        group_channels[group].add(new_data.channel[i])
            
            # Compute and print the spike density for each group
            for group, timestamps in group_timestamps.items():
                # Compute the duration of the time slot in seconds
                duration = time_slot_duration / 1000.0
                # Compute the number of channels for this group
                num_channels = max(len(group_channels[group]), 1)
                # Compute the spike density
                spike_density = len(timestamps) / (num_channels * duration)
                # print("number of group_channels: ", num_channels)
                print ("Spike density for group {}: {} Hz".format(group, spike_density))

                group_spike_densities[group].append(spike_density)

            # Clear the timestamps for the next time slot
            group_timestamps = {group: [] for group in range(1, num_groups+1)}
            # group_channels = {group: set() for group in range(1, num_groups+1)}

    except KeyboardInterrupt:
        print ("\nExiting...")

if __name__ == '__main__':
    run()