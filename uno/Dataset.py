import uno.Draw_Playing_Display as Draw_Playing_Display
import uno.Draw_Start_Display as Draw_Start_Display
import uno.Draw_Stop_Display as Draw_Stop_Display

def change_size(idx):    
    for item in Draw_Playing_Display.Text_list:
        item.change_size(idx)
    for item in Draw_Start_Display.Text_list:
        item.change_size(idx)
    for item in Draw_Start_Display.Button_list:
        item.change_size(idx)
    for item in Draw_Stop_Display.Text_list:
        item.change_size(idx)
    for item in Draw_Stop_Display.Button_list:
        item.change_size(idx)
    
    