import PySimpleGUI as sg


# This is a simple Tasks List (or To_Do List) python aplication that I made in my ToDo_List of #100daysofcode

tarefas = []  # Starting a list that will receive user´s tasks

sg.theme('Reddit')  # Setting up the application theme
sg.popup('\t Hello! \n This is my 1st application for the #100dayscode', 'Have fun!')

# Building the window layout. For a layout building with the PySimpleGUI module is necessary to knows that the window
# is mapped in rows and columns

layout = [
    [sg.Text('Lista de Tarefas')],
    [sg.InputText('Adicione uma tarefa', key='todo_item'), sg.Button(button_text='Adicionar', key="add_save")],
    [sg.Listbox(values=tarefas, size=(30, 10), key="items"), sg.Button('Apagar'), sg.Button('Editar')],
]

janela = sg.Window('Lista de Tarefas', layout)  # Here is the window building through the assignment variable
while True:  # Event Loop
    eventos, valores = janela.Read()
    if eventos == "add_save":
        tarefas.append(valores['todo_item'])
        janela.FindElement('items').Update(values=tarefas)
        # janela.FindElement('items').Update(sg.Checkbox(size=(1,1)))
        janela.FindElement('add_save').Update("Adicionar")
    elif eventos == "Apagar":
        tarefas.remove(valores["items"][0])
        janela.FindElement('items').Update(values=tarefas)
    elif eventos == "Editar":
        edit_val = valores["items"][0]
        tarefas.remove(valores["items"][0])
        janela.FindElement('items').Update(values=tarefas)
        janela.FindElement('todo_item').Update(value=edit_val)
        janela.FindElement('add_save').Update("Salvar")
    elif eventos == None:
        break

janela.Close() #closing the window

#Thank you!
