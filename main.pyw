from pytubefix import YouTube
import customtkinter as ctk
import tkinter as tk
import os




def main(): 

    def is_yt_link(link: str):
    #just checking if it start with youtu nothing else lel
        return (link.startswith("https://youtu") or link.startswith("youtu") or link.startswith("https://www.youtu"))
    
    def Download(video: bool, music: bool,link: str) -> (tuple | int):
        youtubeObject = YouTube(link)
        video_name = ""
        audio_name = ""
        if (video):
            youtubeObject_video = youtubeObject.streams.get_highest_resolution()
            try:
                video_name = youtubeObject_video.download()
            except:
                return -1
        if (music):
            youtubeObject_audio = youtubeObject.streams.get_audio_only()
            try:
                audio_name = youtubeObject_audio.download()
            except:
                return -1
        return (video_name, audio_name)

    def transform(name_file: str, name_out: str) -> (None | int):
        new_name = ''
        #getting the file name wihtout the extension
        for letter in name_file:
            if letter == ".": break
            new_name+=letter

        #checking if the user has put the dor or not
        if name_out[0] != ".": name_out = "." + name_out
        new_name += name_out

        if (new_name == name_file): return
        #ffmpeg magic
        os.system(f'ffmpeg -y -i "{name_file}" "{new_name}"')
        os.remove(name_file)
    
    def enable_video_entry():
        if (video_switch.get()): video_entry.configure(state="normal")
        else: video_entry.configure(state="disabled")
    def enable_audio_entry():
            if (audio_switch.get()): audio_entry.configure(state="normal")
            else: audio_entry.configure(state="disabled")
    def download():
        #youtube link check
        if (not(is_yt_link(yt_link_entry.get()))):
            error_link_label.configure(text="link is malformed or wrong")
            return
        error_link_label.configure(text="link is good")

        #downloading check
        r = Download(video_switch.get(),audio_switch.get(), yt_link_entry.get())
        if (r == -1): 
            error_link_label.configure(text="link is malformed or wrong")
            return
        video_name, audio_name = r

        #changing file type check
        if (video_entry.get() != ""):
            transform(video_name, video_entry.get())
        if (audio_entry.get() != ""):
            transform(audio_name, audio_entry.get())
            
    #main window
    root = ctk.CTk()
    root.geometry("300x300")
    root.resizable(False, False)
    root.title("Youtube Downloader")
    
    root.iconbitmap(r'./logo.ico')

    #insert info
    insert_label = ctk.CTkLabel(root, text="Youtube link goes here")
    insert_label.place(anchor=tk.N, relx=0.5, rely= 0.1)
    
    
    #create the label to entry the yt link
    yt_link_entry = ctk.CTkEntry(root, width=250,placeholder_text="youtube link", justify=tk.CENTER)
    yt_link_entry.place(anchor=tk.N, relx=0.5, rely= 0.2)
    
    #error handling entry
    error_link_label = ctk.CTkLabel(root, text="")
    error_link_label.place(anchor=tk.N, relx=0.5, rely= 0.3)

    #video option
    video_switch = ctk.CTkSwitch(root,text="video", onvalue=True, offvalue=False, command=enable_video_entry)
    video_switch.place(anchor=tk.N, relx=0.25, rely= 0.4)
    video_entry = ctk.CTkEntry(root, width=100,placeholder_text="output type",justify=tk.CENTER)
    video_entry.place(anchor=tk.W,relx=0.6, rely= 0.425)
    video_entry.configure(state="disabled")
    
    #audio option
    audio_switch = ctk.CTkSwitch(root,text="audio", onvalue=True, offvalue=False, command=enable_audio_entry)
    audio_switch.place(anchor=tk.N, relx=0.25, rely= 0.5)
    audio_entry = ctk.CTkEntry(root, width=100,placeholder_text="output type",justify=tk.CENTER)
    audio_entry.place(anchor=tk.W,relx=0.6, rely= 0.525)
    audio_entry.configure(state="disabled")

    #download button
    download_button = ctk.CTkButton(root,width=250, text="DOWNLOAD",text_color="red",command=download)
    download_button.place(anchor=tk.S, relx=0.5, rely= 0.8)

    
    label = ctk.CTkLabel(root, text="made by koala | for the community", text_color="yellow")
    label.place(anchor=tk.N, relx=0.5, rely= 0.9)
    
    #main loop
    root.mainloop()

if __name__ == "__main__":
    main()
    
    
    