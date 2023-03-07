import cv2
import os
from tqdm import tqdm
# Open the video file
NUM_OF_EPS = 9

directory = 'fullImages/TheGoodPlace'
os.chdir(directory)

for ep in tqdm(range(1, 51)):
    video = cv2.VideoCapture(f"../../vids/TheGoodPlace/ep{ep}.mkv")

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Set the frame extraction interval
    interval = 1

    # Loop over the frames
    for i in range(0, total_frames, int(interval * video.get(cv2.CAP_PROP_FPS))):
        # Set the video position to the desired frame
        video.set(cv2.CAP_PROP_POS_FRAMES, i)

        # Read the frame from the video
        ret, frame = video.read()

        # Save the frame as an image
        if frame is not None and frame.size:
            cv2.imwrite(f"ep{ep}frame{i}.jpg", frame)
    # Release the video capture
    video.release()


