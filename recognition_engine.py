import sys
import face_recognition
import os
import cv2
import pickle
import time


KNOWN_FACES_DIR = "D:/Dev/Python/PyQT/AM/images"#"known"
UNKNOWN_FACES_DIR = "unknown"
TOLERANCE = 0.4
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"
MODEL_NAME = "DEBUG_MODEL"
EXTENSION = ".skull"
REVISION = 0.0
TRAIN_MODEL = False

def test():
    print(KNOWN_FACES_DIR)

def recognize(retrain_model=False):
    global REVISION
    global sub
    if retrain_model:
        print("loading known faces")
        REVISION += 1.0

        known_faces = []
        known_names = []

        for name in os.listdir(KNOWN_FACES_DIR):
            for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
                image = face_recognition.load_image_file(
                    f"{KNOWN_FACES_DIR}/{name}/{filename}")
                encoding = face_recognition.face_encodings(image)[0]
                print(f"Learning {name}")
                known_faces.append(encoding)
                known_names.append(name)
        print("Processing known faces")

        data = {"encoding": known_faces, "names": known_names}
        print("Saving revised model!")
        f = open(MODEL_NAME + str(REVISION) + EXTENSION, "wb")
        f.write(pickle.dumps(data))
        f.close()

    if not retrain_model:
        data = pickle.loads(
            open(MODEL_NAME + str(REVISION) + EXTENSION, "rb").read())
        known_faces = data["encoding"]
        known_names = data["names"]
        students_present = []

    for filename in os.listdir(UNKNOWN_FACES_DIR):
        print(filename)
        image = face_recognition.load_image_file(
            f"{UNKNOWN_FACES_DIR}/{filename}")
        print("Done Loading")
        locations = face_recognition.face_locations(image, model=MODEL)
        print("Done searching")
        encodings = face_recognition.face_encodings(image, locations)
        print("Done encoding")
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        print(f"Done processing {filename}")
        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(
                known_faces, face_encoding, TOLERANCE)
            match = None
            if True in results:
                match = known_names[results.index(True)]
                if not retrain_model:
                    students_present.append(match)
                print(f"Match found: {match}")
                # enrolldb.update_attendance(f"{match}")
                # subjectatt.ins_att(sub,match)
                # tymdateatt.ins_stu(match)
                continue
                top_left = (face_location[3], face_location[0])
                bot_right = (face_location[1], face_location[2])

                color = [0, 255, 0]

                cv2.rectangle(image, top_left, bot_right,
                              color, FRAME_THICKNESS)

                top_left = (face_location[3], face_location[2])
                bot_right = (face_location[1], face_location[2] + 22)
                cv2.rectangle(image, top_left, bot_right, color, cv2.FILLED)
                cv2.putText(image, match, (face_location[3]+10, face_location[2]+15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), FONT_THICKNESS)
        #cv2.namedWindow(filename, cv2.WINDOW_KEEPRATIO)
        #cv2.imshow(filename, image)
        #cv2.waitKey(0)
        #cv2.destroyWindow(filename)

        if not retrain_model:
            return students_present


if __name__ == "__main__":
    try:
        if sys.argv[1] == "-train":
            TRAIN_MODEL = True
    except IndexError as i:
        print("Reusing the saved model!")

    recognize(TRAIN_MODEL)
