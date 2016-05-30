# -*- coding: utf-8 -*-
from django import forms

class PicForm(forms.Form):
    picform = forms.FileField(
            label = 'Select a file',
            help_text = 'max 10 MegaBytes'
    )


class RadioForm(object):
    def __init__(self, list_traits):
        self.list_traits = list_traits
        self.htmlframe = ''

    def gen_html(self,action = ''):
        
        master_frame = """
        {content}
        <script>
            var PropChar = {{
            {js_chunk}

            }};
            $.post('{action}',myData) 
        </script>
        """

        js_frame = "{text}: $('#{text}').val(),"

        frame = "{feature} <input type = 'radio' value = 'True' name = '{feature}'><input type = 'radio' value = 'False' name= '{feature}'><br/>"

        return_list = []
        js_list = []
        for entry in self.list_traits:
            return_list.append(frame.format(feature = entry))
            js_list.append(js_frame.format(text = entry))

        return_list = ''.join(return_list)
        js_frame = ''.join(js_frame)

        self.htmlframe = master_frame.format(action = action,content = return_list, js_chunk = js_frame)

        return self.htmlframe

    #def for_db(json_obj):
       #for entry in self.list_traits
     


test_list = (
"foo",
"bar",
"baz",
"al",
"jazeera",
)

properties_list = (
"low_deposit",
"new_renovated_bath",
"balcony",
"big_windows",
"furnished",
"air_conditioning",
"spacious_living_area",
"elevator",
"new_building",
"big_closet",
"parking",
"pets_allowed",
"newly_renovated_building",
"near_subway_transit",
)


def radio_mach():
    return RadioForm(properties_list)

