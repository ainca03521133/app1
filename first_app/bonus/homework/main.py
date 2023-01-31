import PySimpleGUI as sg
import feet_inches_func as finc

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")
label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")
button = sg.Button("Convert")
output = sg.Text("",key = "output")

window = sg.Window("Conventor",
                    layout =[[label1,input1],
                    [label2, input2],
                    [button, output]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = finc(feet, inches)
    window["output"].update(values=f"{result}m", text_color ="white")


window.close()

