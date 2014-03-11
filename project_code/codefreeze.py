#!//usr/bin/python
#Story generation by Nick Montfort
#Story by J.R. Carpenter
#2009-06-24
#Thanks to Ingrid & Pookie
from random import choice
while True:
 s=['There was a knock at the door It was Edwin, dressed in black'
'My god you look like crap today said Emma who was attempting to remove a coffee stain from her chemise'

]
 l=choice(range(5,10))
 while len(s)>l:
  s.remove(choice(s))
 print "\nCODEFREEZE:\n"+'.\n'.join(s)+'.'
 raw_input('To be continued...')
