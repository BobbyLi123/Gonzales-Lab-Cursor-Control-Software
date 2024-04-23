from pyopxclient import PyOPXClientAPI, OPX_ERROR_NOERROR

class FiringRateCalculator:
    def __init__(self, time_slot_duration=1000):
        self.client = PyOPXClientAPI()
        self.time_slot_duration = time_slot_duration
        self.unit_timestamps = {}

    def connect(self):
        self.client.connect()
        if not self.client.connected:
            print ("Client isn't connected, exiting.\n")
            print ("Error code: {}\n".format(self.client.last_result))
            exit()

        print ("Connected to OmniPlex Server\n")

        global_parameters = self.client.get_global_parameters()
        for source_id in global_parameters.source_ids:
            source_name, _, _, _ = self.client.get_source_info(source_id)
            if source_name == 'KBD':
                keyboard_event_source = source_id
                print ("Keyboard event source is {}".format(keyboard_event_source))

    def calculate_firing_rates(self):
        while True:
            self.client.opx_wait(self.time_slot_duration)
            new_data = self.client.get_new_data(timestamps_only=True)
            for i in range(new_data.num_timestamps):
                unit = new_data.unit[i]
                if unit not in self.unit_timestamps:
                    self.unit_timestamps[unit] = []
                self.unit_timestamps[unit].append(new_data.timestamp[i])

            firing_rates = {}
            for unit, timestamps in self.unit_timestamps.items():
                duration = self.time_slot_duration / 1000.0
                spiking_rate = len(timestamps) / duration
                firing_rates[unit] = spiking_rate

            self.unit_timestamps = {}
            yield firing_rates

if __name__ == '__main__':
    calculator = FiringRateCalculator()
    calculator.connect()
    for firing_rates in calculator.calculate_firing_rates():
        print(firing_rates)