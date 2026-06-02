import customtkinter
import random

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Anime Picker")
app.geometry("650x700")

# scroll frame (main container)
scroll_frame = customtkinter.CTkScrollableFrame(app, width=600, height=650)
scroll_frame.pack(fill="both", expand=True)
scroll_frame.grid_columnconfigure(0, weight=1)

# ---------------- INTRO ----------------
intro = customtkinter.CTkLabel(
    scroll_frame,
    text=(
        "Welcome to the Anime Picker!\n\n"
        "Struggling to decide what to watch?\n"
        "Add your anime list and let the app choose for you!"
    ),
    font=("Helvetica", 14),
    justify="center"
)
intro.grid(row=0, column=0, pady=(20, 10))

anime_list = []

# ---------------- LOAD DATA ----------------
def load_data():
    anime_list.clear()
    try:
        with open("anime_list.txt", "r") as file:
            for line in file:
                anime_list.append(line.strip())

        my_label.configure(text="\n".join(anime_list))

    except FileNotFoundError:
        pass


# ---------------- ADD ANIME ----------------
def submit():
    anime_name = entry.get().strip()

    if anime_name == "":
        return

    anime_list.append(anime_name)
    my_label.configure(text="\n".join(anime_list))
    entry.delete(0, "end")


# ---------------- DISPLAY LIST ----------------
my_label = customtkinter.CTkLabel(
    scroll_frame,
    text="",
    font=("Helvetica", 14),
    justify="center"
)
my_label.grid(row=3, column=0, pady=20)

load_data()

# ---------------- ENTRY ----------------
entry = customtkinter.CTkEntry(
    scroll_frame,
    placeholder_text="Enter Anime",
    width=250
)
entry.grid(row=1, column=0, pady=10)

# ---------------- ADD BUTTON ----------------
add_anime_button = customtkinter.CTkButton(
    scroll_frame,
    text="Add Anime",
    command=submit
)
add_anime_button.grid(row=2, column=0, pady=5)

# ---------------- RANDOM PICK ----------------
def random_anime():
    if not anime_list:
        anime_declaration.configure(text="Add some anime first!")
        return

    pick = random.choice(anime_list)

    anime_declaration.configure(
        text=f"You should watch:\n{pick}"
    )


pick_anime_button = customtkinter.CTkButton(
    scroll_frame,
    text="Pick Anime",
    command=random_anime
)
pick_anime_button.grid(row=4, column=0, pady=5)

# ---------------- RESULT LABEL ----------------
anime_declaration = customtkinter.CTkLabel(
    scroll_frame,
    text="",
    font=("Helvetica", 18),
    justify="center"
)
anime_declaration.grid(row=5, column=0, pady=20)

# ---------------- REMOVE ----------------
def remove_anime():
    anime_name = entry.get().strip()

    if anime_name in anime_list:
        anime_list.remove(anime_name)

    my_label.configure(text="\n".join(anime_list))
    entry.delete(0, "end")


remove_anime_button = customtkinter.CTkButton(
    scroll_frame,
    text="Remove Anime",
    command=remove_anime
)
remove_anime_button.grid(row=6, column=0, pady=5)

# ---------------- SAVE ----------------
def save_data():
    with open("anime_list.txt", "w") as file:
        file.write("\n".join(anime_list))


save_data_button = customtkinter.CTkButton(
    scroll_frame,
    text="Save Data",
    command=save_data
)
save_data_button.grid(row=7, column=0, pady=(5, 20))

# ---------------- RUN ----------------
app.mainloop()