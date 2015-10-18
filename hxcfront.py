from glob import glob
import os

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


def list_images(instance):
    print ''
    print instance.text
    ret = glob(os.path.join(os.path.expanduser('~'), 'disks', '*.dsk'))
    print ret


def mount_disk(instance, foo):
    pass


class FileSelector(GridLayout):
    def __init__(self, **kwargs):
        kwargs['padding'] = [50]
        super(FileSelector, self).__init__(**kwargs)
        self.cols = 2
        self.a_button = Button(text="A:", font_size=72)
        self.a_button.bind(on_press=list_images)
        self.add_widget(self.a_button)

        self.a_label = Label(text="No disk selected", font_size=36)
        self.add_widget(self.a_label)
        self.a_button.disk_label = self.a_label

        self.b_button = Button(text="B:", font_size=72)
        self.b_button.bind(on_press=list_images)
        self.add_widget(self.b_button)

        self.b_label = Label(text="No disk selected", font_size=36)
        self.add_widget(self.b_label)
        self.b_button.disk_label = self.b_label


class HxcFront(App):
    def build(self):
        return FileSelector() 


if __name__ == '__main__':
    HxcFront().run()
