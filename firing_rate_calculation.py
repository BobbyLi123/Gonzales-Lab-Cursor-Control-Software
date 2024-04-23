from pyopxclient import PyOPXClientAPI, OPX_ERROR_NOERROR

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

    global_parameters = client.get_global_parameters()
    for source_id in global_parameters.source_ids:
        source_name, _, _, _ = client.get_source_info(source_id)
        if source_name == 'KBD':
            keyboard_event_source = source_id
            print ("Keyboard event source is {}".format(keyboard_event_source))

    # Include all spike sources
    source_ids = client.get_global_parameters().source_ids

    # Initialize a dictionary to store the timestamps for each unit
    unit_timestamps = {}

    # Define the time slot duration in milliseconds
    time_slot_duration = 1000

    try:
        while True:
            # Wait for new data for the duration of the time slot
            client.opx_wait(time_slot_duration)
            
            # Get a new batch of client data
            new_data = client.get_new_data(timestamps_only=True)
            
            # Iterate over the new data
            for i in range(new_data.num_timestamps):
                # If the data is a spike
                # print(new_data.source_num_or_type[i])
                # if new_data.source_num_or_type[i] == 6:
                    # If the unit is not in the dictionary, add it
                unit = new_data.unit[i]
                if unit not in unit_timestamps:
                    unit_timestamps[unit] = []
                    # Add the timestamp to the list for this unit
                unit_timestamps[unit].append(new_data.timestamp[i])
                    # print ("Source: {}\tChannel: {}\tUnit: {}\tTS: {}".format(new_data.source_num_or_type[i], new_data.channel[i], new_data.unit[i], new_data.timestamp[i]))
            
            # Compute and print the spiking rate for each unit
            for unit, timestamps in unit_timestamps.items():
                # Compute the duration of the time slot in seconds
                duration = time_slot_duration / 1000.0
                # Compute the spiking rate
                spiking_rate = len(timestamps) / duration
                print ("Spiking rate for unit {}: {} spikes/sec".format(unit, spiking_rate))

            # Clear the timestamps for the next time slot
            unit_timestamps = {}

            if client.last_result != OPX_ERROR_NOERROR:
                print ("Error code: {}\n".format(client.last_result))
                break
    except KeyboardInterrupt:
        print ("\nExiting...")


if __name__ == '__main__':
    run()