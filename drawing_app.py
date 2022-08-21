import tkinter as tk
import tkinter.ttk as ttk

class FreeHandDrawing(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Free Hand Drawing Tool")
        self._xold = None
        self._yold = None
        self.canvas = None
        self.color = "Black"
        self.thickness = 1
        self.tag = ["tag", "0"]
        self._create_widgets()

    def _create_widgets(self):
        topframe = tk.Frame(self)
        topframe.grid(row=0, column=0, pady=10)

        self.col_select = tk.StringVar()
        colorList = ttk.Combobox(topframe, textvariable=self.col_select,
                                 values=["Black", "Green", "Brown", "Red", "Yellow"],
                                 state="readonly", width=10)

        colorList.current(0)
        self.option_add("*TComboBox*ListBox.selectBackground", "skyblue")
        colorList.bind("<<ComboboxSelected>>", self._change_color)
        colorList.grid(row=0, column=0, padx=5)

        self.t_select = tk.StringVar()
        tList = ttk.Combobox(topframe, textvariable=self.t_select, values=[1, 2, 3, 4, 5, 6, 7],
                             state="readonly", width=3)

        tList.current(0)
        tList.bind("<<ComboboxSelected>>", self._change_thicknewss)
        tList.grid(row=0, column=1, padx=5)

        tk.Button(topframe, text="Undo", bg="blue", fg="white",
                  activebackground="blue4", activeforeground="white",
                  command=self._undo).grid(row=0, column=2, padx=5)

        tk.Button(topframe, text="Clear", bg="brown", fg="white",
                  activebackground="brown4", activeforeground="white",
                  command=self._clear).grid(row=0, column=3, padx=5)

        self.canvas = tk.Canvas(self, width=500, height=500, bg="white")
        self.canvas.grid(row=1, column=0, padx=10, pady=(0, 10))
        self.canvas.bind("<ButtonRelease-1>", self._on_release)
        self.canvas.bind("<B1-Motion>", self._on_movement)

    









FreeHandDrawing().mainloop()