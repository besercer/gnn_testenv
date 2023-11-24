import datetime
import os

class PatricksLog:
    def __init__(self):
        self.current_time = datetime.datetime.now()
        self.output_folder_name = 'experiments'
        self.model_folder_name = self.current_time.strftime('%Y_%m_%d__%H_%M_%S')
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
        file.write(msg + '\n')
        file.close()

    def write_kv_to_file(self, key, value):
        file = open(self.info_file, 'a+')
        file.write(str(key) + ': ' + str(value) + '\n')
        file.close()

    def write_div_to_file(self):
        file = open(self.info_file, 'a+')
        file.write('----------' + '\n')
        file.close()
        
