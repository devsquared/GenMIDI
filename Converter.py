import py_midicsv as midicsv
import os
import datetime

# Given a pathFrom and pathTo, this class provides
class converter():
    def __init__(self):
        pass

    def midi_to_csv(self, midi_path):
        file = os.fsencode(midi_path)
        filename = os.fsdecode(file)
        if filename.endswith(".mid") or filename.endswith(".midi"):
            csv = midicsv.midi_to_csv(filename)
            # lets write all of these to a new directory
            return csv

    def all_midi_in_path_to_csv(self, midi_folder_path, destination_path):
        now = datetime.datetime.now()

        # Create the new folder
        try:
            os.mkdir(destination_path)
        except OSError:
            print("Creation of the directory %s failed" % destination_path)
        else:
            print("Successfully created the directory %s " % destination_path)

        # Here iterate through folder and use midi_to_csv on each
        directory = os.fsencode(midi_folder_path)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".mid") or filename.endswith(".midi"):
                new_csv = midicsv.midi_to_csv(filename)
                current_timestamp = now.strftime("%Y-%m-%d %H:%M")
                save_name = destination_path + "/" + "weewee_%d.csv" % current_timestamp
                new_file_name = os.path.join(os.path.expanduser('~'), 'Documents', save_name)
                f = open(new_file_name, "x")
                f.write(new_csv)

                continue
            else:
                continue
