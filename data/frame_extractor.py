import numpy as np
import os
import cv2
import mediapipe as mp
from mp_keypoints import extract_keypoints, mediapipe_detection

mp_holistic = mp.solutions.holistic

# Khởi tạo danh sách để lưu sequences và labels
sequences, labels = [], []
no_sequence = 50  # Số frame tối đa cho mỗi sequence

with open("data/words.txt", "r") as file:
    actions = [line.strip() for line in file]

label_map = {label: num for num, label in enumerate(actions)}
print("Actions:", actions)
print("Label map:", label_map)

def transform(path, gloss):
    window = []
    cap = cv2.VideoCapture(path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Processing {path} - Frame count: {frame_count}")
    if frame_count == 0:
        cap.release()
        return False
    step = max(1, frame_count // no_sequence)  # Chọn frame cách bước đều nhau
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        for frame_number in range(0, frame_count, step):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame = cap.read()
            if not ret:
                break
            image, results = mediapipe_detection(frame, holistic)
            keypoints = extract_keypoints(results)
            window.append(keypoints)
            if len(window) >= no_sequence:
                break
        cap.release()
        cv2.destroyAllWindows()
    while len(window) < no_sequence:
        window.append(extract_keypoints(results))
    sequences.append(window)
    return True

videos_folder = "data/videos"

# Xử lý từng video trong folder
for video_file in os.listdir(videos_folder):
    if video_file.endswith(".mp4"):
        action = os.path.splitext(video_file)[0]
        if action in actions:
            video_path = os.path.join(videos_folder, video_file)
            if transform(video_path, action):
                labels.append(label_map[action])
        else:
            print(f"Warning: Action '{action}' not found in words.txt, skipping.")

sequences_path = "data/sequences.npy"
np.save(sequences_path, np.array(sequences))

actions_path = "data/actions.npy"
np.save(actions_path, np.array(actions))

labels_path = "data/labels.npy"
np.save(labels_path, np.array(labels))

try:
    sequences_array = np.array(sequences)
    print("Shape of sequences array:", sequences_array.shape)
except Exception as e:
    print(f"Error creating numpy array: {e}")