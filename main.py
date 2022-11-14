#### Commented out stuff is original example script

import pyinotify
import asyncio

def handle_read_callback(notifier):
    """
    Prompt for git commit
    TODO: add 15 minute interval
    TODO: add ability to force save at interval
    TODO: add ability to force commit at interval
    # Just stop receiving IO read events after the first
    # iteration (unrealistic example).
    """
    # print('handle_read callback')
    # notifier.loop.stop()

    

wm = pyinotify.WatchManager()
loop = asyncio.get_event_loop()
notifier = pyinotify.AsyncioNotifier(wm, loop, callback=handle_read_callback)

# https://stackoverflow.com/questions/3876348/using-pyinotify-to-watch-for-file-creation-but-waiting-for-it-to-be-completely
# https://seb.dbzteam.org/pyinotify/pyinotify.WatchManager-class.html
wm.add_watch("/home/sage/expression", pyinotify.IN_CLOSE_WRITE)  #potential custom processing function, proc_fun=MyProcessEvent())

#wm.add_watch('/tmp', pyinotify.ALL_EVENTS)
loop.run_forever()

notifier.stop()
