
# Center and radius of pie chart
cx, cy, r = 100, 320, 75

# Background circle

value = 25 # amount of pie slice
total = 100 # amount of total

# Calculate the angle in degrees
angle = int(25*360/100)

# Start list of polygon points
p = [(cx, cy)]

# Get points on arc
for n in range(0,angle):
    x = cx + round(r*math.cos(n*math.pi/180), 0)
    y = cy+ round(r*math.sin(n*math.pi/180), 0)
    p.append((x, y))
p.append((cx, cy))

# draw base circle
pygame.draw.circle(screen, (17, 153, 255), (cx, cy), r)

# draw pie slice
if len(p) > 2:
    pygame.draw.polygon(screen, (0, 0, 0), p)
