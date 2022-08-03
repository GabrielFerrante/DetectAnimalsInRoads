from tabnanny import check
from unittest import result
from cv2 import normalize
from matplotlib.pyplot import annotate, text
from torch import det, unsqueeze
from torchvision import transforms
from utils import *
from PIL import Image, ImageDraw, ImageFont

import argparse
import cv2
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input', required=True, help='path to input image'

)
parser.add_argument(
    '-t', '--threshold', default=0.45, type=float, help='minimum confidence score to consider a prediction'
)
args = vars(parser.parse_args())


#set the computation device

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


#load model checkpoint
checkpoint = 'checkpoints/checkpoint_ssd300.pth.tar'
checkpoint = torch.load(checkpoint)
start_epoch = checkpoint['epoch']+1
print("\n Loaded checkpoint from epoch %d. \n" % start_epoch)

model = checkpoint['model']
model = model.to(device)
model.eval()

#Transforms

resize = transforms.Resize((300, 300))
to_tensor = transforms.ToTensor()
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                std = [0.229, 0.224, 0.225])



"""
The detect()
function accepts 4 required parameters.

    The first one is the original image on which the object detection will happen.
    Then we have the min_score
    below which all the detections will be ignored.
    max_overlap
    is used to indicate whether a bounding box with a lower score will be dropped using NMS (Non-Max Suppression) or not. This case will only arise if two boxes are overlapping.
    Then we have the top_k
    parameter which defines the number of predictions that we will consider out of all the predictions.
    Finally, we have the suppress
    parameter that suppresses the classes that we do not want in an image. By default, it is None
    .

Starting from line 46, first, we apply all the image transforms. Then we move the image to the computation device. At line 52, we propagate the image through the model and get the predicted locations and predicted scores. Now, we need to keep in mind that the SSD object detector returns 8732 predicted locations by default. Out of those we have to choose our top predictions.

Line 55 calls the detect_objects()
function of model
. This returns us the proper detected boxes, the labels, and the corresponding scores. All of this happen in accordance to the minimum threshold score, the maximum overlap, and the top predictions that we want.

Lines 62 to 64 convert the normalized bounding box coordinates into the dimensions corresponding to the dimensions of the original input. This is important for proper visualization.

Then line 67 gets all the class names by mapping the output labels to rev_label_map
in the utils
script. If no objects are detected, then we just return the original image at line 72.

From line 75 to 77, we set up all the drawing and font settings. Lines 80 to 83 suppresses the specific classes if suppress
parameter is not empty and the class names are provided.

In the remaining of the code, we draw the bounding boxes around the objects and put the class label text on top of each detection. Finally, we return the image with all the detections at line 101.

That is all we need for the detection function. 

"""


def detect(original_image, min_score, max_overleap, top_k, suppress=None):
    """
    Detect objects in an image with a trained SSD300, and visualize the results.
    :param original_image: image, a PIL Image
    :param min_score: minimum threshold for a detected box to be considered a match for a certain class
    :param max_overlap: maximum overlap two boxes can have so that the one with the lower score is not suppressed via Non-Maximum Suppression (NMS)
    :param top_k: if there are a lot of resulting detection across all classes, keep only the top 'k'
    :param suppress: classes that you know for sure cannot be in the image or you do not want in the image, a list
    :return: annotated image, a PIL Image
    """
    #Transform
    image = normalize(to_tensor(resize(original_image)))

    #move to default device
    image = image.to(device)

    #foward prop.

    predicted_locs = predicted_scores = model(image.unsqueeze(0))

    #Detect objects in SSD output
    det_boxes, det_labels, det_scores = model.detect_objects(
        predicted_locs, predicted_scores, min_score = min_score, 
        max_overlap = max_overleap, top_k = top_k 
    )                    

    #move detections to the CPU
    det_boxes = det_boxes[0].to('cpu')

    #transforms to original image dimensions
    original_dims = torch.FloatTensor(
        [original_image.width, original_image.height, original_image.width, original_image.height]
    ).unsqueeze(0)
    det_boxes = det_boxes * original_dims

    #decode class integer labels
    det_labels = [rev_label_map[l] for l in det_labels[0].to('cpu').tolist()]

    #if no objects found, to detected labels will be set to ['0.'], i.e. ['background'] in SSD300.detect_objects() in model.py

    if det_labels == ['background']:
        #Just return original image
        return original_image

    #Annotate
    annotated_image = original_image
    draw = ImageDraw.Draw(annotated_image)
    font = ImageFont.truetype("./calibril.ttf", 15)

    #Suppress specific classes, if needed
    for i in range(det_boxes.size(0)):
        if suppress is not None:
            if det_labels[i] in suppress:
                continue
        
        #boxes
        box_location = det_boxes[i].tolist()
        draw.rectangle(xy=box_location, outline=label_color_map[det_labels[i]])
        draw.rectangle(xy=[l + 1 for l in box_location], outline=label_color_map[det_labels[i]])

        #text

        text_size = font.getsize(det_labels[i].upper())
        text_location = [box_location[0]+2., box_location[1] - text_size[1]]
        textbox_location = [box_location[0], box_location[1] - text_size[1], box_location[0] + text_size[0]+4., box_location[1]]

        draw.rectangle(xy=textbox_location, fill=label_color_map[det_labels[i]])
        draw.text(xy=text_location, text=det_labels[i].upper(), fill='white', font=font)
    del draw

    return annotated_image


if __name__ == '__main__':
    img_path = args['input']
    
    #read as PIL image
    original_image = Image.open(img_path, mode='r')
    #conver to RGB color format
    original_image = original_image.convert('RGB')
    #get the output as PIL Image
    pil_image_out = detect(original_image, min_score=args['threshold'], max_overleap=0.5, top_k=200)

    #conver to NumPy array format
    result_np = np.array(pil_image_out, dtype=np.uint8)

    #convert from RGB to BGR format for OPenCV visualizations
    result_np = cv2.cvtColor(result_np, cv2.COLOR_RGB2BGR)

    #show the image with detected objects on screen 
    cv2.imgshow('Result', result_np)
    cv2.waitKey(0)

    #save the image to disk
    save_name = args['input'].split('/')[-1]
    cv2.imwrite(f'outputs/{save_name}', result_np)
    