from datetime import datetime

with open('note', 'a') as h:
    h.write(datetime.now().strftime("%d.%b %Y %H:%M:%S") + '\n')
