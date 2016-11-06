from PIL import Image
import csv
import sys

def convert_chart(img_file, input_width, input_height):
    image = Image.open(img_file)
    image = image.resize((input_width*5, input_height*5))
    width, height = image.size
    # Load image data
    data = list(image.getdata())
    with open('converted_chart.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for y in xrange(input_height):
            row = []
            for x in xrange(input_width):
                center_y = y * height/input_height + height/input_height/2
                center_x = x * width/input_width + width/input_width/2
                pos = center_y * width + center_x
                val = data[pos][0] < 128 # If < half-black, count as black
                stitch = ' V'[val]
                row.append(stitch)
            writer.writerow(row)

if __name__ == "__main__":
    img = input("Image filename? (Put in quotes)  ")
    width = input("Chart width (in sts)? ")
    height = input("Chart height (in sts)? ")
    convert_chart(img, width, height)
