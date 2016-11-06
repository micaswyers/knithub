from PIL import Image
import csv
import sys

def convert_chart(img_file, width, height):
    image = Image.open(img_file)
    image = image.resize((17*5,14*5))
    width, height = image.size
    #print "%s x %s" % (width, height)
    # Load image data
    data = list(image.getdata())
    with open('converted_chart.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for y in xrange(14):
            row = []
            for x in xrange(17):
                center_y = y * height/14 + height/14/2
                center_x = x * width/17 + width/17/2
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
