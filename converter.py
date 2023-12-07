import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'),  # value
        sg.Spin(['km ke mile', 'kg ke lbs', 'detik ke menit'], key='-UNITS-'),
        sg.Button('Konversi', key='-CONVERT-')  # event
    ],
    [sg.Text('Output', key='-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    # event = sesuatu yang memicu, seperti klik tombol
    # value = adalah nilai dari suatu element, seperti inputan
    event, values = window.read()

    # jika event nya close window, hentikan program
    if event == sg.WIN_CLOSED:
        break

    # jika event nya sama dengan -CONVERT-
    if event == '-CONVERT-':
        input_value = values['-INPUT-']  # nama dari inputan adalah -INPUT-
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km ke mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km adalah {output} miles'
                    window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Anda harus memasukkan angka')

window.close()
