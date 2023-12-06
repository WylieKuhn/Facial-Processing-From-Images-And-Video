from pyfiglet import Figlet
from video_frame_extractor_v2 import extract_frames
from finder import face_finder

f = Figlet(font='slant')
print(f.renderText('FaceFinder'))

while True:
    print("""
    Select an option:
        extract: Extract every n frames of a video and save them in an output folder you specify
        find: search a folder of frames against a folder of faces and get a csv file of all possible matches
        exit: close the program
    """)
    
    selection = input("Make A Selection: ")
    
    
    if selection.lower() == "extract":
        input_video = input("Enter the input path of the video you wish to extract the frames from: ")
        output_folder_name = input("Enter The name of the folder where you wish to store the saved frames: ")
        frame_skip = int(input("Extract every n-frames (enter a whole number): "))
        extract_frames(input_video, output_folder_name, frame_skip)
    elif selection.lower() == "find":
        frame_folder = input("Enter the input path of the folder of frames you wish to check: ")
        face_folder = input("Enter the input path of the folder of faces you wish search for in the frames: ")
        face_finder(frame_folder, face_folder)
    elif selection.lower() == "exit":
        print("Closing Program")
        break
    else:
        print("Invalid Selection")
    