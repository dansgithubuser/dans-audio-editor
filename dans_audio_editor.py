import json
import os

import numpy
import soundfile

os.chdir(os.path.dirname(os.path.realpath(__file__)))

class Edit:
    def __init__(self, original_file_path=None, edit_file_path=None):
        if original_file_path:
            self.original_file_path = original_file_path
            self.original_data, self.original_sample_rate = soundfile.read(original_file_path)
            self.sections = {}
            self.order = []
        elif edit_file_path:
            self.load(edit_file_path)
        self.render_last_file_path = None

    def to_json(self):
        return json.dumps(
            {
                k: v
                for k, v in self.__dict__.items()
                if k in [
                    'original_file_path',
                    'sections',
                    'order',
                ]
            },
            indent=2,
        )

    def save(self, file_path=None):
        if not file_path: file_path = self.original_file_path+'.edit'
        with open(file_path, 'w') as file:
            file.write(self.to_json())

    def load(self, file_path):
        with open(file_path) as file:
            for k, v in json.loads(file.read()).items():
                setattr(self, k, v)
        self.original_data, self.original_sample_rate = soundfile.read(self.original_file_path)

    def add_section(self, start, end, name):
        self.sections[name] = {'start': start, 'end': end}

    def add_order(self, name, before=None):
        assert name in self.sections
        if not before and before != 0: before = len(self.order)
        self.order.insert(before, name)

    def render(self, file_path):
        assert not os.path.exists(file_path)
        final_data = self.original_data[0:0]
        for section_name in self.order:
            final_data = numpy.concatenate((final_data, self.get_section_data(section_name)))
        soundfile.write(file_path, final_data, self.original_sample_rate)
        self.render_last_file_path = file_path

    def render_delete(self):
        if not self.render_last_file_path: return
        os.remove(self.render_last_file_path)

    def get_section_data(self, name):
        section = self.sections[name]
        to_sample = lambda seconds: int(seconds * self.original_sample_rate)
        return self.original_data[to_sample(section['start']):to_sample(section['end'])]
