import tkinter as tk
from tkinter import ttk
import ttkthemes
from generator import GeneratorTab
from version_control import VersionControlTab
from editor import EditorTab
from terminal import TerminalTab
from file_explorer import FileExplorerTab

class HolyToolsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HolyTools - Made by 𝕾𝖍𝖆𝖓𝖌𝖗𝖎-𝕷𝖆")
        self.root.geometry("1000x700")
        self.root.configure(bg="#1a1a1a")
        self.style = ttkthemes.ThemedStyle(self.root)
        self.style.set_theme("equilux")
        header = tk.Frame(self.root, bg="#2d2d2d", height=60)
        header.pack(fill="x")
        tk.Label(header, text="HolyTools", font=("Helvetica", 24, "bold"), fg="#00d4ff", bg="#2d2d2d").pack(side="left", padx=15)
        tk.Label(header, text="by 𝕾𝖍𝖆𝖓𝖌𝖗𝖎-𝕷𝖆", font=("Helvetica", 14), fg="#aaaaaa", bg="#2d2d2d").pack(side="right", padx=15)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=15, padx=15, fill="both", expand=True)
        self.generator_tab = GeneratorTab(self.notebook)
        self.vc_tab = VersionControlTab(self.notebook)
        self.editor_tab = EditorTab(self.notebook)
        self.terminal_tab = TerminalTab(self.notebook)
        self.explorer_tab = FileExplorerTab(self.notebook)
        self.notebook.add(self.generator_tab.frame, text="Generator")
        self.notebook.add(self.vc_tab.frame, text="Version Control")
        self.notebook.add(self.editor_tab.frame, text="Editor")
        self.notebook.add(self.terminal_tab.frame, text="Terminal")
        self.notebook.add(self.explorer_tab.frame, text="File Explorer")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HolyToolsApp(root)
    root.mainloop()
