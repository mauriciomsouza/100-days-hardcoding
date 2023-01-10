import cv2
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    name = request.args.get('name')
    return jsonify({'message': 'Hello, {}!'.format(name)})

@app.route('/api/identify', methods=['POST'])
def identify():
    # Save the image file to a temporary file
    image_file = request.files['image']

    temp_file = '/tmp/temp.jpg'
    image_file.save(temp_file)
    # Load the image from the temporary file
    image = cv2.imread(temp_file)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds of the red color range in the HSV color space
    lower_red = (0, 50, 50)
    upper_red = (10, 255, 255)

    # Create a mask that filters out all pixels that are not within the red color range
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find the contours in the mask
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        # Check if the contour has four sides and if the area of the contour is within a certain range
        if len(contour) == 4 and cv2.contourArea(contour) > 100 and cv2.contourArea(contour) < 1000:
            # The contour is a red square
            return jsonify({'result': 'yes'})

    # No red square was found
    return jsonify({'result': 'no'})

if __name__ == '__main__':
    app.run()