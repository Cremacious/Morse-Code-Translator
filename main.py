import PySimpleGUI as sg

alphabet = {
    ' ': '/ ',
    'A': 'o- ',
    'B': '-ooo ',
    'C': '-o-o ',
    'D': '-oo ',
    'E': 'o ',
    'F': 'oo-o ',
    'G': '--o ',
    'H': 'oooo ',
    'I': 'oo ',
    'J': 'o--- ',
    'K': '-o- ',
    'L': 'o-oo ',
    'M': '-- ',
    'N': '-o ',
    'O': '--- ',
    'P': 'o--o ',
    'Q': '--o- ',
    'R': '--o- ',
    'S': 'ooo ',
    'T': '- ',
    'U': 'oo- ',
    'V': 'ooo- ',
    'W': 'o--- ',
    'X': '-oo- ',
    'Y': '-o-- ',
    'Z': '--oo '

}

def translator(user_text):
    letters_in_user_text = []
    translated_text = []
    for letter in user_text:
        letters_in_user_text.append(letter.upper())
    for letter in letters_in_user_text:
        new_letter = alphabet[letter]
        translated_text.append(new_letter)
    finished_text = ''.join(str(x) for x in translated_text)
    return finished_text


layout = [
    [sg.Text('Enter text to translate to Morse Code:', size=(40, 1))],
    [sg.InputText('', size=(40, 4), key='-INPUT-')],
    [sg.Text('Text in Morse Code:', size=(40, 1))],
    [sg.InputText('', size=(40, 4), key='-OUTPUT-')],
    [sg.Button('Translate')],
]

# Create the window
window = sg.Window('Morse Code Translator', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'Translate':
        input_text = values['-INPUT-']
        translated_text = translator(input_text)
        window['-OUTPUT-'].update(translated_text)

# Close the window
window.close()
