# this script will work for 125% zoom, full screen

from email import message
import pyautogui as pt
from time import sleep
import pyperclip

# wait sec before chekcing another user
checking_delay = 6

#co-ordinate for last mesage
last_mgs_x = 84
last_mgs_y = 70

#co-ordinate for last mesage from smiley icon
last_mgs_icon_x=100
last_mgs_icon_y=80

# find copy corodinate
copy_x = 15
copy_y = -150


#delay when starting the program
sleep(1)



position1 = pt.locateOnScreen("smiley_paperclip.png",confidence=.6)
x = position1[0]
y = position1[1]



def check_new_messages():


  # pt.moveTo(x + x_factor, y - y_factor, duration=.5)

  while True:
    #continously check for green dot
    try:
      position = pt.locateOnScreen("green_circle.png",confidence=.6)

      if position is not None:
        pt.moveTo(position)
        pt.moveRel(-100,0)
        pt.click()
        sleep(1)

    except(Exception):
      print("Exception")

    #chedck if theres new mesage by checking last message
    if pt.pixelMatchesColor(int(x+last_mgs_x), int(y-last_mgs_y),(32,44,51),tolerance=10):
      
      message = get_message()
      print("new messages : "+message)

      # get and process message
      processed_response = process_response(message)

      # send message
      send_message(processed_response)
    else:
      print("No new messages")

    sleep(checking_delay)



# Get message
def get_message():
  # global x,y

  # position = pt.locateOnScreen("smiley_paperclip.png",confidence=.6)
  # x = position[0]
  # y = position[1]

  pt.moveTo(x,y,duration=.2)

  #move over latest text
  pt.moveTo(x+last_mgs_icon_x,y-last_mgs_icon_y,duration=.2)

  # copy latest text 
  pt.tripleClick()
  pt.rightClick()
  pt.moveRel(copy_x,copy_y,duration=.2)
  pt.click()

  return pyperclip.paste()



def process_response(message):
  # message = str(message).lower()

  if "math" in str(message).lower():
    result = ""

    try:
      result = eval(message[5:])
    except(Exception):
      print("eval Exception")

    return str(result)
  else:
    return "only math is supported"




#post medsage
def send_message(message):
  global x,y

  # position = pt.locateOnScreen("smiley_paperclip.png",confidence=.6)
  # x = position[0]
  # y = position[1]

  #place pointer on input
  pt.moveTo(x+200,y+20,duration=.2)
  pt.doubleClick()
  pt.typewrite(message, interval = .01)

  #send
  pt.typewrite("\n",interval=.01)



check_new_messages()

