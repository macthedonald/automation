from spotify import StreamSpotify
from apple import StreamApple
from youtube import StreamYoutube
from audiomack import StreamAudiomack
from boom import StreamBoom
import PySimpleGUI as sg
import csv
import os
from localStoragePy import localStoragePy
import machineid
import requests
import json


BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20, 20), (20, 10))
BPAD_LEFT = ((20, 10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10, 20), (10, 20))

SList = ['Apple Music', 'Audiomack',  'Boomplay', 'Spotify', 'Youtube',]

SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'
localstorage = localStoragePy("app.sporty.bot", "json")


def collapse(layout, key):
    return sg.pin(sg.Column(layout, key=key, visible=False))


def run():
    sg.theme('Material2')

    spotify = [
        [sg.Text('Authentication accounts(csv)')],
        [sg.In(), sg.FileBrowse(key='-CSV-')],
    ]
    youtube = [
        [sg.Text('Number of nodes')],
        [sg.Slider(range=(1, 1000), default_value=2,
                   expand_x=True, enable_events=True,
                   orientation='horizontal', key='-NODES-')],
    ]

    """apple = [
        [sg.Text('Authentication accounts(csv)')],
        [sg.In(), sg.FileBrowse(key='-CSVAP-')],
    ]"""

    general = [
        [sg.Listbox(values=SList, size=(30, 5),
                    key='-LIST-', enable_events=True)],
        [sg.Text('Song URL')],
        [sg.Input(key='-URL-')],
        [sg.Text('Stream time(minutes)'), sg.Text('Number of replays')],
        [sg.Slider(range=(1, 100), default_value=2,
                   expand_x=True, enable_events=True,
                   orientation='horizontal', key='-MINUTES-'), sg.Slider(range=(1, 5000), default_value=4,
                                                                         expand_x=True, enable_events=True,
                                                                         orientation='horizontal', key='-REPEAT-')],
    ]

    options = [
        [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SPOT-', text_color='green'),
         sg.T('Spotify/Apple Music', enable_events=True, text_color='green', k='-OPEN SPOT-TEXT')],
        [collapse(spotify, '-SPOT-')],
        [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN TUBE-', text_color='red'),
         sg.T('Youtube/Boomplay/Audiomack', enable_events=True, text_color='red', k='-OPEN TUBE-TEXT')],
        [collapse(youtube, '-TUBE-')],
        # [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN APPLE-', text_color='red'),
        # sg.T('Apple Music', enable_events=True, text_color='red', k='-OPEN APPLE-TEXT')],
        # [collapse(apple, '-APPLE-')]
    ]

    layout = [
        [sg.Output(size=(100, 10), text_color='blue',
                   background_color='Black')],
        [sg.Column(general, size=(400, 220),  pad=BPAD_LEFT_INSIDE,
                   )],
        [sg.Column(options, size=(400, 200), pad=BPAD_LEFT_INSIDE)],
        [sg.Button('Stream',  k='-STREAM-'), sg.Button('Info',  k='-INFO-'), sg.Button('Exit', k='-EXIT-')]]

    window = sg.Window('StreamBooster(v2)                                             © crea8tek inc',
                       border_depth=0,
                       grab_anywhere=True,
                       icon='logo.ico').Layout(layout)

    select_spot, select_tube, select_apple, select_boom, select_audiomack = False, False, False, False, False

    while True:  # Event Loop
        event, values = window.read()

        url = values['-URL-']
        minutes = values['-MINUTES-']
        repeat = values['-REPEAT-']

        # toggle spotify buttton
        if event.startswith('-LIST-') and values['-LIST-'][0] == "Spotify":

            if select_apple:
                select_apple = not select_apple
                window['-OPEN SPOT-'].update(
                    SYMBOL_DOWN if select_apple else '')
                window['-OPEN SPOT-TEXT'].update(
                    'Apple Open' if select_apple else '')
                window['-SPOT-'].update(visible=select_apple)

            select_spot = not select_spot
            window['-OPEN SPOT-'].update(
                SYMBOL_DOWN if select_spot else '')
            window['-OPEN SPOT-TEXT'].update(
                'Spotify Open' if select_spot else '')
            window['-SPOT-'].update(visible=select_spot)

            if select_tube:
                select_tube = not select_tube
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_tube else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Youtube Open' if select_tube else '')
                window['-TUBE-'].update(visible=select_tube)

            if select_boom:
                select_boom = not select_boom
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_boom else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Boomplay Open' if select_boom else '')
                window['-TUBE-'].update(visible=select_boom)

            if select_audiomack:
                select_audiomack = not select_audiomack
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_audiomack else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Audiomack Open' if select_audiomack else '')
                window['-TUBE-'].update(visible=select_audiomack)

        # toggle youtube button
        elif event.startswith('-LIST-') and values['-LIST-'][0] == "Youtube":

            if select_boom:
                select_boom = not select_boom
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_boom else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Boomplay Open' if select_boom else '')
                window['-TUBE-'].update(visible=select_boom)

            select_tube = not select_tube
            window['-OPEN TUBE-'].update(
                SYMBOL_DOWN if select_tube else '')
            window['-OPEN TUBE-TEXT'].update(
                'Youtube Open' if select_tube else '')
            window['-TUBE-'].update(visible=select_tube)

            if select_spot:
                select_spot = not select_spot
                window['-OPEN SPOT-'].update(
                    SYMBOL_DOWN if select_spot else '')
                window['-OPEN SPOT-TEXT'].update(
                    'Spotify Open' if select_spot else '')
                window['-SPOT-'].update(visible=select_spot)

            if select_apple:
                select_apple = not select_apple
                window['-OPEN SPOT-'].update(
                    SYMBOL_DOWN if select_apple else '')
                window['-OPEN SPOT-TEXT'].update(
                    'Apple Open' if select_apple else '')
                window['-SPOT-'].update(visible=select_apple)

            if select_audiomack:
                select_audiomack = not select_audiomack
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_audiomack else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Audiomack Open' if select_audiomack else '')
                window['-TUBE-'].update(visible=select_audiomack)

        # toggle audiomack
        elif event.startswith('-LIST-') and values['-LIST-'][0] == 'Audiomack':

            if select_tube:
                select_tube = not select_tube
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_tube else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Youtube Open' if select_tube else '')
                window['-TUBE-'].update(visible=select_tube)

            if select_boom:
                select_boom = not select_boom
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_boom else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Boomplay Open' if select_boom else '')
                window['-TUBE-'].update(visible=select_boom)

            select_audiomack = not select_audiomack
            window['-OPEN TUBE-'].update(
                SYMBOL_DOWN if select_audiomack else '')
            window['-OPEN TUBE-TEXT'].update(
                'Audiomack Open' if select_audiomack else '')
            window['-TUBE-'].update(visible=select_audiomack)

            if select_spot:
                select_spot = not select_spot
                window['-OPEN SPOT-'].update(
                    SYMBOL_DOWN if select_spot else '')
                window['-OPEN SPOT-TEXT'].update(
                    'Spotify Open' if select_spot else '')
                window['-SPOT-'].update(visible=select_spot)

            if select_apple:
                select_apple = not select_apple
                window['-OPEN SPOT-'].update(
                    SYMBOL_DOWN if select_apple else '')
                window['-OPEN SPOT-TEXT'].update(
                    'Apple Open' if select_apple else '')
                window['-SPOT-'].update(visible=select_apple)

         # toggle boom
        elif event.startswith('-LIST-') and values['-LIST-'][0] == 'Boomplay':

            if select_tube:
                select_tube = not select_tube
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_tube else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Youtube Open' if select_tube else '')
                window['-TUBE-'].update(visible=select_tube)

            if select_audiomack:
                select_audiomack = not select_audiomack
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_audiomack else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Audiomack Open' if select_audiomack else '')
                window['-TUBE-'].update(visible=select_audiomack)

            select_boom = not select_boom
            window['-OPEN TUBE-'].update(
                SYMBOL_DOWN if select_boom else '')
            window['-OPEN TUBE-TEXT'].update(
                'Boomplay Open' if select_boom else '')
            window['-TUBE-'].update(visible=select_boom)

            if select_spot:
                select_spot = not select_spot
                window['-OPEN SPOT-'].update(
                    SYMBOL_DOWN if select_spot else '')
                window['-OPEN SPOT-TEXT'].update(
                    'Spotify Open' if select_spot else '')
                window['-SPOT-'].update(visible=select_spot)

            if select_apple:
                select_apple = not select_apple
                window['-OPEN SPOT-'].update(
                    SYMBOL_DOWN if select_apple else '')
                window['-OPEN SPOT-TEXT'].update(
                    'Apple Open' if select_apple else '')
                window['-SPOT-'].update(visible=select_apple)

        # toggle Apple button
        elif event.startswith('-LIST-') and values['-LIST-'][0] == "Apple Music":

            if select_spot:
                select_spot = not select_spot
                window['-OPEN SPOT-'].update(
                    SYMBOL_DOWN if select_spot else '')
                window['-OPEN SPOT-TEXT'].update(
                    'Spotify Open' if select_spot else '')
                window['-SPOT-'].update(visible=select_spot)

            select_apple = not select_apple
            window['-OPEN SPOT-'].update(
                SYMBOL_DOWN if select_apple else '')
            window['-OPEN SPOT-TEXT'].update(
                'Apple Open' if select_apple else '')
            window['-SPOT-'].update(visible=select_apple)

            if select_tube:
                select_tube = not select_tube
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_tube else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Youtube Open' if select_tube else '')
                window['-TUBE-'].update(visible=select_tube)

            if select_boom:
                select_boom = not select_boom
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_boom else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Boomp Open' if select_boom else '')
                window['-TUBE-'].update(visible=select_boom)

            if select_audiomack:
                select_audiomack = not select_audiomack
                window['-OPEN TUBE-'].update(
                    SYMBOL_DOWN if select_audiomack else '')
                window['-OPEN TUBE-TEXT'].update(
                    'Audiomack Open' if select_audiomack else '')
                window['-TUBE-'].update(visible=select_audiomack)

        # stream spotify
        if event.startswith('-STREAM-') and select_spot:

            fname = values['-CSV-']
            if not fname or not url or not repeat or not minutes:
                print("Please input all values")
                # sg.popup("Cancel", "Please enter all values")
                # raise SystemExit("Cancelling: some values missing")
            elif os.stat(fname).st_size == 0:
                print("Authentication accounts file is empty")
                raise SystemExit("Cancelling: empty file supplied")
            else:
                # open the file in read mode
                filename = open(fname, 'r')
                # creating dictreader object
                file = csv.DictReader(filename)
                for col in file:
                    t = StreamSpotify(
                        url, col['email'], col['password'], int(repeat), int(minutes))
                    t.start_thread(window)

                print('Initializing Spotify, please do not close window..\n')

             # stream youtube
        elif event.startswith('-STREAM-') and (select_tube or select_boom or select_audiomack):
            node = int(values['-NODES-'])
            if not node or not url or not minutes or not repeat:
                print("Please input all values")
            else:
                for i in range(node):
                    if select_tube:
                        t = StreamYoutube(url, int(minutes), int(repeat))
                    elif select_boom:
                        t = StreamBoom(url, int(minutes), int(repeat))
                    else:
                        t = StreamAudiomack(url, int(minutes), int(repeat))
                    t.start_thread(window)

                print('Initializing stream, please do not close window..\n')

           # stream apple music
        elif event.startswith('-STREAM-') and select_apple:

            fname = values['-CSV-']
            if not fname or not url or not repeat or not minutes:
                print("Please input all values")
                # sg.popup("Cancel", "Please enter all values")
                # raise SystemExit("Cancelling: some values missing")
            elif os.stat(fname).st_size == 0:
                print("Authentication accounts file is empty")
                raise SystemExit("Cancelling: empty file supplied")
            else:
                # open the file in read mode
                filename = open(fname, 'r')
                # creating dictreader object
                file = csv.DictReader(filename)
                for col in file:
                    t = StreamApple(
                        url, col['email'], col['password'], int(repeat), int(minutes))
                    t.start_thread(window)

                print('Initializing, please do not close window..\n')

        elif event == sg.WIN_CLOSED or event.startswith('-EXIT-'):
            break
        elif event.startswith('-STREAM DONE-'):
            print('Streaming completed')
            raise SystemExit(
                "Stream Completed...Made with ❤️ by crea8tek🎶")
        elif event.startswith('-INFO-'):
            print(event, values)

    window.close()


if __name__ == "__main__":
    def activate_license(license_key):
        machine_fingerprint = machineid.hashed_id('SportyBot')
        validation = requests.post(
            "https://api.keygen.sh/v1/accounts/2701475b-6d41-485c-99d1-a5da404b44dd/licenses/actions/validate-key",
            headers={
                "Content-Type": "application/vnd.api+json",
                "Accept": "application/vnd.api+json"
            },
            data=json.dumps({
                "meta": {
                    "scope": {"fingerprint": machine_fingerprint},
                    "key": license_key
                }
            })
        ).json()

        if "errors" in validation:
            errs = validation["errors"]

            return False, "license validation failed: {}".format(
                map(lambda e: "{} - {}".format(e["title"],
                    e["detail"]).lower(), errs)
            )

        # If the license is valid for the current machine, that means it has
        # already been activated. We can return early.
        if validation["meta"]["valid"]:
            return True, "license has already been activated on this machine"

        # Otherwise, we need to determine why the current license is not valid,
        # because in our case it may be invalid because another machine has
        # already been activated, or it may be invalid because it doesn't
        # have any activated machines associated with it yet and in that case
        # we'll need to activate one.
        validation_code = validation["meta"]["code"]
        activation_is_required = validation_code == 'FINGERPRINT_SCOPE_MISMATCH' or \
            validation_code == 'NO_MACHINES' or \
            validation_code == 'NO_MACHINE'

        if not activation_is_required:
            return False, "license {}".format(validation["meta"]["detail"])

        # If we've gotten this far, then our license has not been activated yet,
        # so we should go ahead and activate the current machine.
        activation = requests.post(
            "https://api.keygen.sh/v1/accounts/2701475b-6d41-485c-99d1-a5da404b44dd/machines",
            headers={
                "Authorization": "License {}".format(license_key),
                "Content-Type": "application/vnd.api+json",
                "Accept": "application/vnd.api+json"
            },
            data=json.dumps({
                "data": {
                    "type": "machines",
                    "attributes": {
                        "fingerprint": machine_fingerprint
                    },
                    "relationships": {
                        "license": {
                            "data": {"type": "licenses", "id": validation["data"]["id"]}
                        }
                    }
                }
            })
        ).json()

        # If we get back an error, our activation failed.
        if "errors" in activation:
            errs = activation["errors"]

            return False, "license activation failed: {}".format(
                ','.join(
                    map(lambda e: "{} - {}".format(e["title"], e["detail"]).lower(), errs))
            )

        return True, "license activated"

    # Run from the command line:
    #   python main.py some_license_key

    if not localstorage.getItem('activated_key'):
        sg.theme('DarkGrey14')   # Add a touch of color
        layout = [[sg.Text('Enter Activation Key: '), sg.Text(size=(15, 1), key='-OUTPUT-')],
                  [sg.Input(key='-IN-')],
                  [sg.Button('Activate'), sg.Button('Cancel')]]

        window = sg.Window('Activation', icon='logo.ico').Layout(layout)

        while True:  # Event Loop
            event, values = window.read()
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Activate':
                key = values['-IN-']
                status, msg = activate_license(key)
                window['-OUTPUT-'].update(msg)
                if status == True:
                    localstorage.setItem('activated_key', True)
                    window.close()
                    run()

    else:
        run()
    # print(status, msg)
