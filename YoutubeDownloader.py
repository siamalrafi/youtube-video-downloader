import time
from pytube import YouTube
import os
import imps.__init__ as fancy_console

os.system("cls")


def download_video(genre):
    """Function that allows you to download videos from YouTube"""
    fancy_console.mp3_console() if genre == "mp4" else fancy_console.mp4_console()
    link = input("Video URL :\n >>")

    try:
        download_object = YouTube(link)
        print("\n\n _____Downloading process has been started!!")

        # If the genre is mp4, then download object will be prepared as an MP4 file, otherwise it will gonna take as MP3
        download_video = download_object.streams.get_highest_resolution(
        ) if genre == "mp4" else download_object.streams.filter(only_audio=True).first()
        print("\n ___Downloading started...")

        # Making a directory to prettify every downloads with a good structure
        if not os.path.exists(os.path.join(os.getcwd(), "downloads")):
            os.mkdir(os.getcwd() + "\downloads")
            os.mkdir(os.getcwd() + "\downloads\mp3")
            os.mkdir(os.getcwd() + "\downloads\mp4")

        save_path = "downloads\mp3" if genre == "mp3" else "downloads\mp4"
        out = download_video.download(os.path.join(os.getcwd(), save_path))
        base = os.path.splitext(out)
        os.rename(
            out, base[0] + ".mp3") if genre == "mp3" else os.rename(out, base[0] + ".mp4")
        print(f"__ => The file was downloaded! ^-^")
        time.sleep(3)

    except Exception as e:
        os.system("cls")
        fancy_console.error_console()
        print("- The Link you've provided was wrong, please check it again!")
        homepage()


def homepage():
    fancy_console.homeprint_console()
    print("Choose your Operation : \n 1. Download MP4 from Youtube \n 2. Download MP3 from Youtube \n")
    operation_target = input(f">> ")

    if operation_target == "1":
        download_video("mp4")
    elif operation_target == "2":
        download_video("mp3")
    else:
        os.system("cls")
        fancy_console.error_console()
        print("- Put a option between 1 and 2")
        homepage()


homepage()
