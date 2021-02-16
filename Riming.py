from vpython import *
#GlowScript 3.0 VPython
win = 500

# Typical values
L = 1 # container is a cube L on a side
gray = color.gray(0.7) # color of edges of container
mass = 4E-3/6E23 # helium mass
Ratom = 0.03 # wildly exaggerated size of helium atom
k = 1.4E-23 # Boltzmann constant
T = 300 # around room temperature
dt = 1E-5
Ndrops = 200

animation = canvas( width=win, height=win, align='left')
animation.range = L
animation.title = 'The riming process'
s = """  Theoretical and averaged speed distributions (meters/sec).
  Initially all atoms have the same speed, but collisions
  change the speeds of the colliding atoms. One of the atoms is
  marked and leaves a trail so you can follow its path."""
animation.caption = s
gray = color.gray(0.7) # color of edges of container
Ratom = 0.003 # wildly exaggerated size of helium atom
       
d = L/2+Ratom
r = 0.005 #box radius
mass= 0.1
boxbottom = curve(color=gray, radius=r)
boxbottom.append([vector(-d,-d,-d), vector(-d,-d,d), vector(d,-d,d), vector(d,-d,-d), vector(-d,-d,-d)])
boxtop = curve(color=gray, radius=r)
boxtop.append([vector(-d,d,-d), vector(-d,d,d), vector(d,d,d), vector(d,d,-d), vector(-d,d,-d)])
vert1 = curve(color=gray, radius=r)
vert2 = curve(color=gray, radius=r)
vert3 = curve(color=gray, radius=r)
vert4 = curve(color=gray, radius=r)
vert1.append([vector(-d,-d,-d), vector(-d,d,-d)])
vert2.append([vector(-d,-d,d), vector(-d,d,d)])
vert3.append([vector(d,-d,d), vector(d,d,d)])
vert4.append([vector(d,-d,-d), vector(d,d,-d)])
ice_length = 0.5/2
ice_width = 0.5/2
ice_height = 0.1/2
ice=ellipsoid(pos=vector(0,0,0),length=ice_length, height=ice_height, width=ice_width, color=color=color.cyan, make_trail=True, retain=10, trail_radius=0.1, opacity=0.2)

Atoms = []
p = [] #momentum 
apos = [] #position
pavg=2 # average kinetic energy p**2/(2mass) = (3/2)kT
    
for i in range(Ndrops): #initialisation
    x = L*random()-L/2
    y = 2*L*random()-L #not divided by two as I want this to be longer in y 
    z = L*random()-L/2
    Atoms.append(sphere(pos=vector(x,y,z), radius=Ratom, color=gray))
    apos.append(vec(x,y,z))
    theta = pi*random()
    phi = 2*pi*random()
#    px = pavg*sin(theta)*cos(phi) these were too random, I need an upward v
#    py = pavg*sin(theta)*sin(phi)
#    pz = pavg*cos(theta)
    px = 0
    py = pavg
    pz = 0
    p.append(vector(px,py,pz))

while True:
    rate(300)
    
    for i in range(Ndrops): 
            Atoms[i].pos = apos[i] = apos[i] + (p[i]/mass)*dt #momentum transfer determines direction, need to use upward g
    
    for i in range(Ndrops): #this accounts for the box edges, I need to account for y only 
        loc = apos[i]
        if abs(loc.y) > L:
            if loc.y < 0: p[i].y = abs(p[i].y) #make positive to bounce off bottom lid (LEAVE FOR NOW)
            else: 
                apos[i].y = -2*d #moves to the bottom, but make random in position. They dissapear at the top, make them dissapear out of view 
                apos[i].x = L*random()-L/2
                apos[i].z = L*random()-L/2
                
        if loc.y < ice.pos.y+ice_length: #rule to make these drops stick to the surface of ellipse 
            if loc.x < ice.pos.x+ice_width :
                if loc.z < ice.pos.y+ice_height:
                    apos[i].y = apos[i].y 
                    apos[i].x = apos[i].x
                    apos[i].z = apos[i].z 
                
        

