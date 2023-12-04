from deepface import DeepFace

objs = DeepFace.analyze(img_path = r"Images\test.jpg", 
        actions = ['age', 'gender', 'race', 'emotion']
)