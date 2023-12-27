import serial
import time
import PySimpleGUI as sg

porta_serial = serial.Serial('COM3', 9600)

def tela_inicial():
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
            [sg.Text("Ligar LED's", font=('Arial 16'))],
            [sg.Button('LED 1', size=(7,3), key='1'), sg.Button('LED 2', size=(7,3), key='2'), sg.Button('LED 3', size=(7,3), key='3')],
            [sg.Button('LED 4', size=(7,3), key='4'), sg.Button('LED 5', size=(7,3), key='5')]
        ]

    janela = sg.Window('Produtos', layout, element_justification='c')

    ledUm = 0
    ledDois = 0
    ledTres = 0
    ledQuatro = 0
    ledCinco = 0

    def ligar_led(led):
        comando = str(led)
        porta_serial.write(comando.encode())
        time.sleep(0.1)

    def desligar_led(led):
        comando = str(led)
        porta_serial.write(comando.encode())
        time.sleep(0.1)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED: 
            break
        elif eventos == '1':
            if ledUm == 0:
                print('ligando led um...')
                ledUm = 1
                ligar_led(eventos)
            else:
                print('desligando led um...')
                ledUm = 0
                desligar_led(6)
        
        elif eventos == '2':
            if ledDois == 0:
                print('ligando led dois...')
                ledDois = 1
                ligar_led(eventos)
            else:
                print('desligando led tres...')
                ledDois = 0
                desligar_led(7)

        elif eventos == '3':
            if ledTres == 0:
                print('ligando led tres...')
                ledTres = 1
                ligar_led(eventos)
            else:
                print('desligando led tres...')
                ledTres = 0
                desligar_led(8)
            
        elif eventos == '4':
            if ledQuatro == 0:
                print('ligando led quatro...')
                ledQuatro = 1
                ligar_led(eventos)
            else:
                print('desligando led quatro...')
                ledQuatro = 0
                desligar_led(9)
        
        elif eventos == '5':
            if ledCinco == 0:
                print('ligando led cinco...')
                ledCinco = 1
                ligar_led(eventos)
            else:
                print('desligando led cinco...')
                ledCinco = 0
                desligar_led(0)
            

tela_inicial()