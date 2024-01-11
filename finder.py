from deepface import DeepFace
import os
import pandas as pd 

def face_finder(check_directory, face_directory):

    master_results_dataframe = pd.DataFrame(columns=["identity", "source_x", "source_y", "source_w", "source_h", "VGG-Face_cosine"])
    image_count = 0
    num_files_in_directory = 0

    for filename in os.listdir(check_directory):
        num_files_in_directory += 1

    for filename in os.listdir(check_directory):
        file_path = os.path.join(check_directory, filename)
        
        try:   
            img = DeepFace.extract_faces(file_path, detector_backend="retinaface", enforce_detection=False)
            
            if img is not None:
                
                dfs = DeepFace.find(img_path = file_path, db_path = face_directory, enforce_detection=False, detector_backend = "retinaface")
                
                for df in dfs:
                    df["master_frame"] = file_path
                    dfs_dataframe = pd.DataFrame(df)
                    master_results_dataframe = pd.concat([master_results_dataframe, dfs_dataframe], ignore_index=True)
            else:
                print("File Not Found")
                
        except Exception as e:
            print(f"Error processing image {file_path}: {str(e)}")
        
        image_count += 1
        
        print(f"Processed image {image_count} of {num_files_in_directory}, {round((image_count/num_files_in_directory)*100,2)}% finished")
            
    csv_filename = "output_results.csv"
    master_results_dataframe.to_csv(csv_filename, index=False)

#db = "faces"
#search_folder = "output_frames"
#face_finder(search_folder, db)