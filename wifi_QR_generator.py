from PIL import Image, ImageDraw, ImageFont
import wifi_qrcode_generator
from tkinter import ttk
import tkinter as tk
from os.path import dirname as os_dirname
from os.path import join as os_join

class WifiQrGenerator():
    def __init__(self) -> None:       
        self.wifi_name = None
        self.password = None
        self.root = tk.Tk()
        self.qr_code = None
        self.text_var = tk.StringVar()
        self.ssid_var = tk.StringVar()
        self.pass_var = tk.StringVar()

    
    def creating_gui(self):
        self.root.title('Wifi QR Generator')
        self.root.geometry('400x350')
        self.root.resizable(False, False)
        photo_path = os_join(os_dirname(__file__), 'wifi.png')
        photo = tk.PhotoImage(file=photo_path)
        self.root.iconphoto(False, photo)
        
        #creating labels
        text_label = ttk.Label(self.root, text='Connect to: ', font='Arial', width=300)
        ssid_label = ttk.Label(self.root, text='Wifi name: ', font='Arial', width=300)
        pass_label = ttk.Label(self.root, text='Password: ', font='Arial', width=300)

        #creating entrys
        text_entry = ttk.Entry(text_label, textvariable=self.text_var, font='Arial')
        ssid_entry = ttk.Entry(ssid_label, textvariable=self.ssid_var, font='Arial')
        pass_entry = ttk.Entry(pass_label, textvariable=self.pass_var, font='Arial', show='*')

        #creating the button
        btn = ttk.Button(self.root, text='Submit', command=self.submit)

        #place the widges in the main window
        text_label.place(x=5, y=70, anchor='nw')
        ssid_label.place(x=5, y=130, anchor='nw')
        pass_label.place(x=5, y=190, anchor='nw')

        #place the entry widges
        text_entry.place(x=140)
        ssid_entry.place(x=140)
        pass_entry.place(x=140)

        #place the button
        btn.place(x= 200, y=300, anchor='center', width=200, height=50)

        self.root.mainloop()

    def submit(self):
        #generating qr code
        wifiName = self.ssid_var.get()
        passwd = self.pass_var.get()    

        self.qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
            ssid=wifiName, 
            hidden=False, 
            authentication_type='WPA', 
            password=passwd
        )

        self.save()    

    def save(self, *args, **kwargs):
        # self.qr_code.print_ascii()
        text = f'Connect to {self.text_var.get()}'
        qr = self.qr_code.make_image()
        img = Image.new('RGB', (400,450), 'white')
        draw = ImageDraw.Draw(img)
        font_path = os_join(os_dirname(__file__), 'SourceCodePro-Regular.ttf')
        font = ImageFont.truetype(font_path, 20)
        draw.text((20, 50), text=text, fill='black', font=font, anchor='ls')
        img.paste(qr, (1, 60))
        img.show()

        #reset the inputs
        self.text_var.set('')
        self.ssid_var.set('')
        self.pass_var.set('')
        

if __name__ == '__main__':
    wifi_gen = WifiQrGenerator()
    wifi_gen.creating_gui()