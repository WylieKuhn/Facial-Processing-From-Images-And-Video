# Facial Processing From Images And Video  
  
This is a rough prototype for a program written with the help of ChatGPT.  
  
This program is designed to take video footage of large groups of people and do analysis on it by allowing you to  
- Extract every n-frames of a video file and save them to a folder as standalone images.  
- Extract every n-frames of a video file and save them to a folder as standalone images as well as save any faces detected in those frames in a separate directory with a corosponding frame name. 
- Use the image of a face of a person of interest to search for them in the extracted frames of a video file and return a dataframe with the frames they appear in (this is not exact and there are false positives).

#### Libraries Used
- DeepFace
- OpenCV


