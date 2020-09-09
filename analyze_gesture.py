from keras.models import load_model
from collections import deque
import pandas as pd
from imutils import paths
import numpy as np
import pickle
from cv2 import cv2
import os
import csv
import sys

########## METHODS ##########
# Calculate the total accuracy
def calculate_total_accuracy(accuracy_list):
	sum = 0
	for i in range(0, len(accuracy_list)):
		sum = sum + accuracy_list[i]

	if sum > 0:
		average = sum/len(accuracy_list)
	else:
		average = sum

	return average

# Calculate the accuracy per video
def calculate_single_accuracy(gesture_label, prediction_list):
	num_correct = 0
	acc_rate = 0
	# Dictionary with the gesture recognized
	dict_gestures = {}

	for i in range(0, len(prediction_list)):
		if prediction_list[i] in dict_gestures:
			dict_gestures[prediction_list[i]] = dict_gestures[prediction_list[i]] + 1
		else:
			dict_gestures[prediction_list[i]] = 1
		if(prediction_list[i] == gesture_label):
			num_correct = num_correct + 1
	# Calculating accuracy
	acc_rate = (num_correct/len(prediction_list))*100
	# Get the gesture label detected 
	values_list = list(dict_gestures.values())
	keys_list = list(dict_gestures.keys())
	max_value = max(values_list)
	gesture_detected = keys_list[values_list.index(max_value)]
	print ("The gesture detected has been: ", gesture_detected)

	return acc_rate

def write_header(filename):
	with open(filename, 'w', newline='') as csvfile:
		fieldnames = ['Name', 'Accuracy']
		# writer = csv.writer(csvfile, delimiter=' ')
		writer = csv.writer(csvfile)
		writer.writerow(fieldnames)    

def append_list_as_row(filename, row):
    # Open file in append mode
    with open(filename,'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row)

########## END METHODS ##########

# Initialize variables
gesture_label = "swipe_left"
# gesture_label = "thumb_up"
path_videos = "Keras/input/"+gesture_label
model_path = "Keras/model/model_Adam_vgg19_mse_100_3g_10vids_lr0001_eps01.model"
label_bin = "Keras/model/label_Adam_vgg19_mse_100_3g_10vids_lr0001_eps01.pickle"
output_path = "Keras/output/sample_predicted.avi"
results_path = "Keras/results/"
filename = "accuracy.csv"
filename_path = results_path + filename
size = 1

# Load the trained model and label binarizer from disk
print("Loading model and label binarizer")
model = load_model(model_path)
lb = pickle.loads(open(label_bin, "rb").read())
# Initialize the image mean for mean subtraction along with the predictions queue
mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
Q = deque(maxlen=size)

# Getting the videos for the evaluation
prediction_list = []
videoPaths = list(paths.list_files(path_videos))
accuracy_list = []
# Writing the header of the csv file
write_header(filename_path)
for i in range(0, len(videoPaths)):
	# Initialize the video stream, pointer to output video file, and frame dimensions
	vs = cv2.VideoCapture(videoPaths[i])
	# writer = None
	(width, height) = (None, None)
	# Loop over frames from the video file stream
	while True:
		# Read the next frame from the file
		(grabbed, frame) = vs.read()
		# If the frame was not grabbed, then we have reached the end of the stream
		if not grabbed:
			break
		# If the frame dimensions are empty, grab them
		if width is None or height is None:
			(height, width) = frame.shape[:2]

		# Clone the output frame, then convert it from BGR to RGB ordering, resize the frame to a fixed 224x224, and then
		# perform mean subtraction
		output = frame.copy()
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		frame = cv2.resize(frame, (224, 224)).astype("float32")
		frame -= mean

		# Make predictions on the frame and then update the predictions queue
		# preds = model.predict(np.expand_dims(frame, axis=0))[0]
		preds = model.predict(np.expand_dims(frame, axis=0))
		Q.append(preds)
		# Perform prediction averaging over the current history of previous predictions
		results = np.array(Q).mean(axis=0)
		j = np.argmax(results)
		label = lb.classes_[j]

		# Draw the activity on the output frame
		text = format(label)
		# Store the prediction
		prediction_list.append(text)
		""" cv2.putText(output, text, (15, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
		# Check if the video writer is None
		if writer is None:
			# Initialize our video writer
			fourcc = cv2.VideoWriter_fourcc(*"MJPG")
			writer = cv2.VideoWriter(output_path, fourcc, 30, (width, height), True)
		# Write the output frame to disk
		writer.write(output)
		# Show the output image
		cv2.imshow("Output", output) """
		key = cv2.waitKey(1) & 0xFF
		# If the `q` key was pressed, break from the loop
		if key == ord("q"):
			break
	# Calculate the accuracy for a single video
	acc_rate = calculate_single_accuracy(gesture_label, prediction_list)
	accuracy_list.append(acc_rate)
	# Write in the csv file
	path_elems = videoPaths[i].split(os.path.sep)[-1]
	name_vid = path_elems.split('.')[0]
	row = [name_vid, acc_rate]
	append_list_as_row(filename_path, row)
	# Release the file pointers
	print("Cleaning up")
	# writer.release()
	vs.release()
# Calculate the total accuracy 
total_acc = calculate_total_accuracy (accuracy_list)
# Add the total accuracy to the file
row_total = ["Total", total_acc]
append_list_as_row(filename_path, row_total)
# Printing the total accuracy
print("Total accuracy:", total_acc)