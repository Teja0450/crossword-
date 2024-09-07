import tkinter as tk


def solve_crossword():
    global solution_text
    rows = int(rows_entry.get())
    columns = int(columns_entry.get())

    puzzle_grid = []
    for i in range(rows):
        row = ''
        for j in range(columns):
            entry_value = puzzle_entries[(i * columns) + j].get()
            row += entry_value
        puzzle_grid.append(row)

    # The existing code for solving the crossword goes here.
    # ... (unchanged)
    # Instead of printing the solution, we will update the GUI Text widget.

    solution_text.delete(1.0, tk.END)  # Clear any previous solution

    across_words = []
    down_words = []
    a = []
    d = []
    count = 1
    for row in range(rows):
        for col in range(columns):
            cell = puzzle_grid[row][col]
            t = 0
            if cell != '*' and (col == 0 or puzzle_grid[row][col - 1] == '*'):
                word = ''
                for c in range(col, columns):
                    if puzzle_grid[row][c] == '*':
                        break
                    word += puzzle_grid[row][c]
                if len(word) >= 1:
                    across_words.append((count, word))
                t = 1
            u = 0
            if cell != '*' and (row == 0 or puzzle_grid[row - 1][col] == '*'):
                u = 1
                word = ''
                for r in range(row, rows):
                    if puzzle_grid[r][col] == '*':
                        break
                    word += puzzle_grid[r][col]
                if len(word) >= 1:
                    down_words.append((count, word))
            if u == 1 and t == 1:
                a.append(count)
                d.append(count)
            elif u == 1:
                d.append(count)
            elif t == 1:
                a.append(count)
            if (cell != '*' and (u == 1 or t == 1)):
                count += 1

    if across_words:
        solution_text.insert(tk.END, "Across\n", "header")
        for number, word in across_words:
            solution_text.insert(tk.END, f"{number}. {word}\n", "content")

    if down_words:
        solution_text.insert(tk.END, "Down\n", "header")
        for number, word in down_words:
            solution_text.insert(tk.END, f"{number}. {word}\n", "content")

def create_grid():
    rows = int(rows_entry.get())
    columns = int(columns_entry.get())

    for widget in grid_frame.winfo_children():
        widget.grid_forget()

    puzzle_entries.clear()

    for i in range(rows):
        for j in range(columns):
            entry = tk.Entry(grid_frame, width=2)
            entry.grid(row=i, column=j, columnspan=1, rowspan=1, padx=2, pady=2, sticky="nsew")
            entry.grid_propagate(0)
            puzzle_entries.append(entry)

    grid_frame.grid_rowconfigure(0, minsize=45)
    grid_frame.grid_rowconfigure(1, minsize=45)
    for i in range(2, rows):
        grid_frame.grid_rowconfigure(i, minsize=45)
    grid_frame.grid_columnconfigure(0, minsize=45)
    grid_frame.grid_columnconfigure(1, minsize=45)
    for i in range(2, columns):
        grid_frame.grid_columnconfigure(i, minsize=45)


# Create the main window
root = tk.Tk()
root.title("Crossword Solver")
root.geometry('1930x1080')
# Color settings
root.configure(bg="lightgray")
button_bg_color = "blue"
button_fg_color = "white"
button_active_bg_color = "darkblue"
button_active_fg_color = "white"
root['background']='#CBC3E3'


heading=tk.Label(root,text="CROSSWORD PUZZLE",fg="black",font=("times new roman", 50, "bold") ,bg="#CBC3E3")
                 
heading.place(x=300,y=100)

# Input fields for rows and columns
rows_label = tk.Label(root, text="Rows:", bg="lightgray")
rows_label.place(x=500,y=200)
rows_entry = tk.Entry(root)
rows_entry.place(x=540,y=200)

columns_label = tk.Label(root, text="Columns:", bg="lightgray")
columns_label.place(x=670,y=200)
columns_entry = tk.Entry(root)
columns_entry.place(x=730,y=200)

# Button to create the crossword grid
create_grid_button = tk.Button(root, text="Create Grid", command=create_grid, bg=button_bg_color, fg=button_fg_color, activebackground=button_active_bg_color, activeforeground=button_active_fg_color)
create_grid_button.place(x=860,y=197)

# Button to trigger the crossword solver
solve_button = tk.Button(root, text="Solve Crossword", command=solve_crossword, bg=button_bg_color, fg=button_fg_color, activebackground=button_active_bg_color, activeforeground=button_active_fg_color)
solve_button.place(x=935,y=197)

# Frame to hold the crossword grid
grid_frame = tk.Frame(root, bg="lightgray")
grid_frame.place(x=200,y=300)

# List to store the puzzle grid entries
puzzle_entries = []

# Text widget to display the crossword solution
solution_text = tk.Text(root, wrap=tk.WORD, width=40, height=20)
solution_text.place(x=600,y=260)

# Add tag configurations for header and content in the solution_text widget
solution_text.tag_configure("header", font=("Arial", 12, "bold"))
solution_text.tag_configure("content", font=("Arial", 12))

root.mainloop()