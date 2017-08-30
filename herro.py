# This program says hello and greets a person by name
#
# Carlitos chavez-knotts
# August 24, 2017


#print("Put noun?")
#noun = input()
#print("Put a place?")
#place = input()
#print("What's a thing you like")
#thing = input()
#print("
#print( noun + " went to " + place + " to get some " + thing + ".")

running = True

while running:
      print("Tell me something about your day so far")
      something = input()

      if something == "goodbye":
          running = False
      elif "bad" or "I know" in something:
          print ("Awww I feel bad is there a way I can help?")

