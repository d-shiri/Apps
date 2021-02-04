#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:57:15 2021

@author: dariyoushsh
"""
import os
import json
from time import sleep
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from main_helper import navigation
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDDatePicker, MDThemePicker
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget
from kivymd.uix.snackbar import Snackbar
from kivy.base import EventLoop
import sys

os.environ['KIVY_VIDEO'] = 'ffpyplayer'  # for android
#os.environ['KIVY_VIDEO'] = 'ffmpeg'     # for ios
#Window.size = (300, 500)

class Content(BoxLayout):
    pass


class WalkApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.primary_palette = 'Red'        
        screen = Builder.load_string(navigation)

        return screen
    
    
    def radio_check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'
            
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
        
    def show_datepicker(self):
        datepicker = MDDatePicker(callback=self.got_the_date)
        datepicker.open()

    def got_the_date(self, the_date):
        self.the_date = the_date


    def show_confirmation_dialog(self):
        if not self.dialog:
            cancel = MDFlatButton(text="CANCEL", text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog)
            accept =  MDFlatButton(text="ACCEPT", text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog)
            self.result = accept
            self.dialog = MDDialog(
                title="Reset all data?",
                text="This action will delete all of your data.",
                size_hint = (0.7, 1),
                #auto_dismiss = False,
                buttons=[cancel, accept])
            self.dialog.set_normal_height()
        self.dialog.open()
        
    def get_goal(self):
        goal = self.root.ids.set_goal.text
        goal_json = {"goal":[{"goal": goal}]}
        self.write_json(goal_json, 'goal.json')
        sleep(0.5)
        self.load()
        
    def show_snackbar(self, text):
        Snackbar(text=text).show()
        
    def show_popup(self, title, message):
        ok_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title=title, text=message,
                         size_hint=(0.7, 1), buttons=[ok_button])
        self.dialog.open()
            
    def get_new_record(self, file='data.json'):
        if self.root.ids.set_new_record.text == '':
            self.show_popup('Try again!', 'New Record Can Not Be Empty!')
            return
        new_data = {
              "new_record": self.root.ids.set_new_record.text,
              "the_date"  : str(self.the_date),
              "location"  : self.root.ids.set_location.text
              }
        if os.path.exists(file) == True:
            with open (file) as json_file:
                data = json.load(json_file)
                temp = data['NewRecord']
                temp.append(new_data)
                self.write_json(data, 'data.json')
        self.root.ids.set_new_record.text = ''
        self.root.ids.set_location.text   = ''
        self.show_snackbar("New Input Saved.")
        sleep(0.5)
        self.load()
        
    def write_json(self, data, file='data.json'):
        with open (file, 'w') as f:
            json.dump(data, f, indent=4)

    def reset_data(self):
        if os.path.exists('data.json'):
            os.remove('data.json')
            self.show_snackbar('Everything deleted!')
            self.load()
        else:
            self.show_snackbar('Something went wrong!')
            
    def play_video(self):
        source = 'data/video.mp4'
        return source
        
    def on_start(self):
        self.load()
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        
    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            #if self.current_screen.name == 'history'
            self.root.ids.screen_manager.current = 'Home'
            return True 
   
    def close_dialog(self, obj):
        if obj.text == 'CANCEL':
            self.dialog.dismiss()
        elif obj.text == 'ACCEPT':
            self.dialog.dismiss()
            sleep(0.5)
            self.reset_data()
        else:
            pass
        
    def load(self):
        first_data = {"NewRecord":[ 
                    {"new_record": 0, "the_date": "",
                      "location": ""}]}
        try:
            if os.path.exists('data.json') == False:
                self.write_json(first_data, 'data.json')
            with open ('goal.json') as json_file:
                goal_data = json.load(json_file)
                goal = goal_data['goal'][0]['goal']
                self.root.ids.set_goal.text = goal

            with open ('data.json') as json_file:
                data = json.load(json_file)
                self.store = data['NewRecord']
                new = []
                if self.store[0]['new_record'] != '':
                    for item in self.store:
                        new.append(float(item['new_record']))
                    self.root.ids.completed.text = '[b]Completed: [/b]' + str(sum(new))
                    self.root.ids.remaining.text = '[b]Remaining: [/b]' + str(float(goal) - sum(new))
                    self.root.ids.max.text = '[b]Max:  [/b]' + str(max(new))
                    mx = new.index(max(new))
                    max_date = self.store[mx]['the_date']
                    max_loc  = self.store[mx]['location']
                    self.root.ids.max.secondary_text = 'Date: ' + str(max_date)
                    self.root.ids.max.tertiary_text = 'Location: ' + str(max_loc)
                    new.pop(0)
                    self.root.ids.min.text = '[b]Min:  [/b]' + str(min(new))
                    mn = new.index(min(new))+1
                    min_date = self.store[mn]['the_date']
                    min_loc  = self.store[mn]['location']
                    self.root.ids.min.tertiary_text = 'Location: ' + str(min_loc)
                    self.root.ids.min.secondary_text = 'Date: ' + str(min_date)
                    if sum(new) >= float(goal):
                        self.show_snackbar('Congratulations, goal accomplished :)')
            
        except:
            pass
 
    def history(self):
        self.root.ids.screen_manager.current = 'screen_5'
        # clear the previous lists from the screen
        self.root.ids.hist_id.clear_widgets()
        with open ('data.json') as json_file:
                data = json.load(json_file)
                data = data['NewRecord']
        if len(data) > 1:
            data.pop(0)
        icon = 'data/history_2.png'
        for item in data:
            first  = 'Distance: ' + str(item['new_record'])
            second = 'Date: ' + str(item['the_date']) 
            third  = 'Location: ' + str(item['location'])
            items = ThreeLineIconListItem(text=first, secondary_text=second, 
                                          tertiary_text=third)
            items.add_widget(IconLeftWidget(icon=icon))
            self.root.ids.hist_id.add_widget(items)


            
    def back(self):
        self.root.ids.screen_manager.current = 'Home'
           
if __name__ == '__main__':
    WalkApp().run()






