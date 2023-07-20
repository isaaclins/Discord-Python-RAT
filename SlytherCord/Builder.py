from guietta import _, Gui, Quit

# Define a function for the calculation
def calculate():
    gui.result = float(gui.a) + float(gui.b)

gui = Gui(
    [ "Enter numbers:",  "__a__", "+", "__b__", ["Calculate", calculate] ],
    [    "Result: -->", "__result__",   _,       _,                        _ ],
    [                _,        _,   _,       _,                     Quit ]
)

# Initialize the result variable as empty
gui.result = ""

gui.run()
