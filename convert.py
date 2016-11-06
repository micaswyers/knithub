from PIL import Image

image = Image.open('chart.png')
image = image.resize((17*5,14*5))
width, height = image.size
#print "%s x %s" % (width, height)
# Load image data
data = list(image.getdata())
for y in xrange(14):
    for x in xrange(17):
        center_y = y * height/14 + height/14/2
        center_x = x * width/17 + width/17/2
        pos = center_y * width + center_x
        val = data[pos][0] < 128 # If < half-black, count as black. ROBUST.
        print ' X'[val] + ",",
    print

# TODO: Resize image slightly smaller to increase likelihood of hitting the "target"
