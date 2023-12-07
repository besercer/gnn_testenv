import datetime
import time
import os
import torch

class PatricksLog:
    def __init__(self, name_extend = ''):
        self.current_time = datetime.datetime.now()
        self.start_time = time.time()
        self.checkpoint_time = 0.
        self.name_extend = name_extend
        self.output_folder_name = 'experiments'
        self.model_folder_name = self.current_time.strftime('%Y_%m_%d__%H_%M_%S') + self.name_extend
        self.path = self.output_folder_name + '/' + self.model_folder_name
        self.info_file = self.path + '/' + 'info.txt'
        
        self.create_folder(self.model_folder_name, self.output_folder_name) # create folder like: 2023_11_20__23_12_26
        self.write_kv_to_file('Experiment date', self.model_folder_name)
        

    def create_folder(self, model_folder_name = 'my_folder', output_folder_name = 'experiments'):
        if not os.path.exists(output_folder_name):
            os.mkdir(output_folder_name)
        if not os.path.exists(output_folder_name + '/' + model_folder_name):
            os.mkdir(output_folder_name + '/' + model_folder_name)

    def write_to_file(self, msg):
        file = open(self.info_file, 'a+')
        file.write(str(msg) + '\n')
        file.close()

    def write_kv_to_file(self, key, value):
        file = open(self.info_file, 'a+')
        file.write(str(key) + ': ' + str(value) + '\n')
        file.close()

    def write_div_to_file(self):
        file = open(self.info_file, 'a+')
        file.write('----------' + '\n')
        file.close()

    def save_model(self, name, model):
        torch.save(model, self.path + '/' + name)

    def save_time_since_start(self):
        time_temp = time.time() - self.start_time

        hours, rem = divmod(time_temp, 3600)
        minutes, seconds = divmod(rem, 60)
        seconds, milliseconds = divmod(seconds, 1)
        milliseconds, microseconds = divmod(milliseconds * 1000, 1000)
        microseconds, nanoseconds = divmod(microseconds * 1000, 1000)
        print_string = f"Gesamtzeit seit beginn: {int(hours)} Stunden, {int(minutes)} Minute, {int(seconds)} Sekunden, {milliseconds} Millisekunden, {microseconds} Mikrosekunden, {nanoseconds} Nanosekunden"
        print(print_string)
        self.write_to_file(print_string)

        if self.checkpoint_time != 0:
            short_time = time.time() - self.checkpoint_time
            hours, rem = divmod(short_time, 3600)
            minutes, seconds = divmod(rem, 60)
            seconds, milliseconds = divmod(seconds, 1)
            milliseconds, microseconds = divmod(milliseconds * 1000, 1000)
            microseconds, nanoseconds = divmod(microseconds * 1000, 1000)
            print_string = f"Zeit seit letztem Check: {int(hours)} Stunden, {int(minutes)} Minute, {int(seconds)} Sekunden, {milliseconds} Millisekunden, {microseconds} Mikrosekunden, {nanoseconds} Nanosekunden"
            print(print_string)
            self.write_to_file(print_string)
            
        self.checkpoint_time = time.time()

    def get_total_model_size(self):
        totel_size = 0
        folder_path = self.output_folder_name + '/' + self.model_folder_name

        for filename in os.listdir(folder_path):
            if filename.startswith("model_"):
                filepath = os.path.join(folder_path, filename)
                totel_size += os.path.getsize(filepath)
        
        totel_model_size_in_kb = totel_size / 1024
        totel_model_size_in_mb = totel_model_size_in_kb / 1024
        totel_model_size_in_gb = totel_model_size_in_mb / 1024

        print_string = f"Gesamtgröße alle Model-Dateien: {totel_size} Bytes, {totel_model_size_in_kb:.2f} KB, {totel_model_size_in_mb:.2f} MB, {totel_model_size_in_gb:.2f} GB"
        print(print_string)
        self.write_to_file(print_string)

        
    


