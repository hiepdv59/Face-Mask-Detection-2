from detect_mask_image import mask_image
from detect_mask_webcam import mask_video

from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd

def handleImageButton():
    filename = fd.askopenfilename(
        filetypes=(
            ('image files', '*.jpg'),
            ('All files', '*.*')
        )
    )
    mask_image(right_frame, filename)

def handleVideoButton():
    filename = fd.askopenfilename()
    mask_video(right_frame, filename)

def handleMaskWebCamButton():
    mask_video(right_frame, 0)

if __name__ == '__main__':

    background = '#FFCC66'
    bgButton = '#f8f8f8'
    activeBgBtn = '#e6e6e6'
    colorButton = '#000000'

    #Create window
    window = tk.Tk()
    window.title('NHÓM 10 THỰC TẬP CHUYÊN NGÀNH ')

    window_width = 800
    window_height = 400
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    window.configure(bg = background)

    #Left frame
    left_frame = Frame(window, bg = background,
                        width = window_width/4, height = window_height,
                        padx = 20, pady = 5
                )
    left_frame.grid(column = 0, row = 0)
    #Right frame
    global right_frame
    right_frame = Frame(window, bg = '#f8f8f8',
                        width = 500, height = window_height,
                        padx = 20, pady= 20
                )
    right_frame.grid(column = 1, row = 0)
    print(screen_height, window_height)
    #Label
    label = Label(left_frame, text = 'Chọn chức năng: ',
                    justify= CENTER, 
                    font = ("Times New Roman", 20, 'bold'),
                    fg = 'white', bg = background,
                    pady = 25
                    )
    label.grid(column = 0, row = 0)
    #Detect mask image button 
    btnMaskImg = Button(left_frame, text = "Nhận diện qua ảnh", 
                    command = handleImageButton,
                    font = ("Times New Roman", 12, 'bold'),
                    height = 2, width = 25,
                    bg = bgButton, fg = colorButton,
                    activebackground = activeBgBtn
                )
    btnMaskImg.grid(column = 0, row = 1)
    
    #Detect mask video button
    btnMaskVideo = Button(left_frame, text = "Nhận diện qua video",
                    command = handleVideoButton,
                    font = ("Times New Roman", 12, 'bold'),
                    height = 2, width = 25,
                    bg = bgButton, fg = colorButton,
                    activebackground = activeBgBtn
                )
    btnMaskVideo.grid(column = 0, row = 3)

    #Detect mask webcam button 
    btnMaskWebcam = Button(left_frame, text = "Nhận diện qua webcam", 
                    command = handleMaskWebCamButton,
                    font = ("Times New Roman", 12, 'bold'),
                    height = 2, width = 25,
                    bg = bgButton, fg = colorButton,
                    activebackground = activeBgBtn
                )
    btnMaskWebcam.grid(column = 0, row = 5)
    
    #Label no text
    Label(left_frame, height = 2, bg = background).grid(column = 0, row = 2)
    Label(left_frame, height = 2, bg = background).grid(column = 0, row = 4)    
    window.mainloop()
