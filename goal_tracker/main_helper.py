#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 21:58:32 2021

@author: dariyoushsh
"""

navigation = '''
#:import Snackbar kivymd.uix.snackbar.Snackbar
#:import md_icons kivymd.icon_definitions.md_icons
Screen:
    NavigationLayout:
        ScreenManager:
            id: screen_manager
            Screen:
                name: 'Home'
                ScrollView:
                    MDList:
                        id: main_id
                        OneLineAvatarListItem:
                        OneLineAvatarListItem:
                            markup: True
                            text: '[b]Goal: {}[/b]'.format(root.ids.set_goal.text)
                            ImageLeftWidget:
                                source: 'data/goal.png'
                        OneLineAvatarListItem:
                            id: completed
                            markup: True
                            text: '[b]Completed:[/b] '
                            ImageLeftWidget:
                                source: 'data/completed.png'
                        OneLineAvatarListItem:
                            id: remaining
                            markup: True
                            text: '[b]Remaining:[/b]'
                            ImageLeftWidget:
                                source: 'data/couple.png'
                        ThreeLineIconListItem:
                            id: max
                            markup: True
                            text: '[b]Max:[/b]'
                            secondary_text: 'Date: '
                            tertiary_text: 'Location'
                            ImageLeftWidget:
                                source: 'data/max.png'
                        ThreeLineIconListItem:
                            id: min
                            markup: True
                            text: '[b]Min:[/b]'
                            secondary_text: 'Date: '
                            tertiary_text: 'Location'
                            ImageLeftWidget:
                                source: 'data/min.png'
          

                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar: 
                        title: 'Home'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
                        right_action_items: [['theme-light-dark', lambda x: app.show_theme_picker()],\
                        ['history', lambda x: app.history()]]
                        elevation: 10
                    Widget: 
                MDFloatingActionButton:
                    icon: 'plus'
                    md_bg_color: app.theme_cls.primary_color
                    elevation_normal: 12
                    pos_hint:{'center_x':0.85, 'center_y':0.1}
                    on_release: 
                        screen_manager.current = "screen_3"
            Screen:
                name: "screen_2"
                BoxLayout:
                    #spacing: '8dp'
                    #padding: '8dp'
                    spacing: dp(100)
                    orientation: 'vertical'
                    MDToolbar: 
                        title: 'Goal'
                        left_action_items: [['keyboard-backspace', lambda x: app.back()]]
                        elevation: 10
                    Widget: 
                
                MDTextField:
                    id: set_goal
                    hint_text: 'Enter your goal'
                    mode: "rectangle"
                    #max_text_length: 3
                    color_mode: 'accent'
                    #helper_text: 'Enter your ultimate goal'
                    helper_text_mode: 'on_focus'
                    #icon_right: 'walk'
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint:{'center_x':0.5, 'center_y':0.5}
                    size_hint_x: None
                    width: 600
                MDRaisedButton:
                    text: "Save"
                    on_release: 
                        app.get_goal()
                        Snackbar(text="Goal Saved:)").show()
                    pos_hint: {"center_x": .5, "center_y": .37}
                #MDRectangleFlatButton:
                    #text: 'Submit' 
                    #pos_hint: {'center_x':0.5, 'center_y':0.37}
                    #on_release:
                        #app.get_goal()
            Screen:
                name: 'screen_3'
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: 1, 1
                    spacing: dp(10)
                    #padding: dp(10)
                    MDToolbar: 
                        title: 'New Input'
                        left_action_items: [['keyboard-backspace', lambda x: app.back()]]
                        elevation: 10
                    Widget: 
                #ScrollView:
                    #size_hint: (0.65, 0.50)
                    #pos_hint: {'center_x': .60, 'y': -0.2}
                    #halign: 'center'
                    #MDList:

                MDRaisedButton:
                    id: set_the_date
                    text: "Choose the date"
                    on_release: 
                        app.show_datepicker()
                    pos_hint: {"center_x": .5, "center_y": .70}                        
                MDTextField:
                    id: set_new_record
                    required: True
                    hint_text: 'Add a new record: '
                    #helper_text: 'How much did you walk today?'
                    helper_text_mode: 'on_error'
                    icon_right: 'walk'
                    #icon_right_color: app.theme_cls.primary_color
                    pos_hint:{'center_x':0.5, 'center_y':0.60}
                    size_hint_x: None
                    width: 750
                    #size_hint_y: None  
                MDTextField:
                    id: set_location
                    hint_text: 'Enter a location'
                    helper_text: 'Where did you walk today?'
                    helper_text_mode: 'on_focus'
                    icon_right: 'location-enter'
                    #icon_right_color: app.theme_cls.primary_color
                    pos_hint:{'center_x':0.5, 'center_y':0.50}
                    size_hint_x: None
                    width: 750
# =============================================================================
#                 MDTextField:
#                     id: set_comment
#                     multiline: True
#                     hint_text: 'Enter a comment'
#                     helper_text: 'You can add a comment here.'
#                     helper_text_mode: 'on_focus'
#                     #icon_right: 'comment'
#                     #icon_right_color: app.theme_cls.primary_color
#                     pos_hint:{'center_x':0.5, 'center_y':0.40}
#                     size_hint_x: None
#                     width: 750
# =============================================================================
                MDRaisedButton:
                    text: "Save"
                    on_release: 
                        app.get_new_record()
                    pos_hint: {"center_x": .5, "center_y": .25}
            Screen:
                name: 'screen_4'
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: 1, 1
                    spacing: dp(10)
                    MDToolbar: 
                        title: 'About'
                        left_action_items: [['keyboard-backspace', lambda x: app.back()]]
                        elevation: 10
                    Widget: 
            
                Video:
                    id: vid
                    source: app.play_video()
                MDRoundFlatButton:
                    text: "Tap to Start"
                    pos_hint: {"center_x": .5, "center_y": .2}
                    on_release:
                        root.ids.vid.state = 'play'
                        
                        #source = app.play_video()
                        #vid.state = 'play'
                        #setattr(vid, 'source', app.play_video())
                        #setattr(vid, 'state', 'play')
                Label:
                    text: f"[color=#000000][font=Roboto]Coded by Dariyoush Shiri:) [/font][/font][/color]"
                    pos_hint: {"center_x": .5, "center_y": .1}
                    markup: True
                    font_size: 30

 
            Screen:
                name: 'screen_5'
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: 1, 1
                    MDToolbar: 
                        id: toolbar5
                        title: 'History'
                        left_action_items: [['keyboard-backspace', lambda x: app.back()]]
                        elevation: 10
                    Widget: 
                ScrollView:
                    pos_hint: {'top': 1.0 - toolbar5.height / self.parent.height}
                    MDList:
                        id: hist_id

                
        MDNavigationDrawer:
            id: nav_drawer
            type: 'standard'

            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
            
                Image:
                    size_hint: None, None
                    size: "150dp", "150dp"
                    source: 'data/an2.png'
                MDLabel:
                    text: 'Hello :)'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    text: 'First set a goal and then add your new records via the + sign.'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                ScrollView:
                    
                    MDList:
# =============================================================================
#                         OneLineIconListItem:
#                             text: 'Night mode'
#                             IconLeftWidget
#                                 icon: 'theme-light-dark'
#                             MDSwitch:
#                                 pos_hint: {'center_x': .9, 'center_y': 0.5}
#                                 on_active: app.radio_check(*args)
# =============================================================================
                        OneLineIconListItem:
                            on_release: 
                                nav_drawer.set_state("close")
                                screen_manager.current = "screen_2"  
                            text: 'Set a goal'
                            IconLeftWidget:
                                icon: 'umbrella'
                        OneLineIconListItem:
                            on_release: 
                                nav_drawer.set_state("close")
                                app.show_confirmation_dialog()
                            text: 'Delete data'
                            IconLeftWidget:
                                icon: 'delete'
                        OneLineIconListItem:
                            on_release:
                                nav_drawer.set_state("close")
                                screen_manager.current = "screen_4"
                            text: 'about'
                            IconLeftWidget:
                                icon: 'nature-people'
                                
                        OneLineIconListItem:
                            on_release: app.stop()
                            text: 'Exit'
                            IconLeftWidget:
                                icon: 'exit-to-app'

'''