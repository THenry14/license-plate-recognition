import numpy as np
import os
import sys
import tensorflow as tf
import re
from collections import defaultdict
from PIL import Image
import pytesseract
import cv2

# used to clear plate
t_pattern = re.compile('[^a-zA-Z0-9]+')

def clearprint(text, pattern=t_pattern):
  """
  Method clears text recognised by tesseract from any non alphanumerical characters
  
  Parameters:

    :param: text (str): input text to be cleared

  Returns:

    :return: (str): cleared text
  """
  plate = pattern.sub('', text)
  try:
    if plate[2].isdigit():
      plate = plate[:2] + ' ' + plate[2:]
    else:
      plate = plate[:3] + ' ' + plate[3:]
  except IndexError:
    pass
  finally:
    return plate.upper()

cap = cv2.VideoCapture(0)

# object detection imports
sys.path.append("..")
from utils import label_map_util
from utils import visualization_utils as vis_util

# model import
MODEL_NAME = 'tablice_graph'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
PATH_TO_LABELS = os.path.join('gen_data/training', 'object-detection.pbtxt')
NUM_CLASSES = 1

# load a (frozen) Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')


# load label map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# detection
with detection_graph.as_default():
  with tf.Session(graph=detection_graph) as sess:
    while True:
      ret, image_np = cap.read()
      image_np_expanded = np.expand_dims(image_np, axis=0)
      image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
      boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
      scores = detection_graph.get_tensor_by_name('detection_scores:0')
      classes = detection_graph.get_tensor_by_name('detection_classes:0')
      num_detections = detection_graph.get_tensor_by_name('num_detections:0')

      (boxes, scores, classes, num_detections) = sess.run(
          [boxes, scores, classes, num_detections],
          feed_dict={image_tensor: image_np_expanded})

      try:
        # for tesseract
        ymin = boxes[0,0,0]
        xmin = boxes[0,0,1]
        ymax = boxes[0,0,2]
        xmax = boxes[0,0,3]

        (im_width, im_height) = (640, 480) #(cap.get(3), cap.get(4))
        (xminn, xmaxx, yminn, ymaxx) = (xmin * im_width, xmax * im_width, ymin * im_height, ymax * im_height)
        cropped_image = tf.image.crop_to_bounding_box(image_np, int(yminn), int(xminn),int(ymaxx - yminn), int(xmaxx - xminn))
        img_data = sess.run(cropped_image)

        text = pytesseract.image_to_string(img_data,lang=None)
      except ValueError:
        pass

      vis_util.visualize_boxes_and_labels_on_image_array(
          image_np,
          np.squeeze(boxes),
          np.squeeze(classes).astype(np.int32),
          np.squeeze(scores),
          category_index,
          use_normalized_coordinates=True,
          line_thickness=8)

      try:
          cv2.putText(image_np, clearprint(text), (int((xminn + xmaxx)/2), int(yminn - 20)), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,127), thickness=1)
          #print(text)
      except UnicodeError: # hackhackhackhack
          pass
      cv2.imshow('Rozpoznajmy tablice', cv2.resize(image_np, (800,600)))
      if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

