import customtkinter
import random


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Anime Picker")
app.geometry("650x700")


#intro label
intro = customtkinter.CTkLabel(app, 
        text="Welcome to the random anime picker!\n Have you ever struggled to just pick an anime?\n Well, you're in the right place! \n Just list all your overwhelming options and I'll choose for you!", 
        font=("Helvetica", 18)
        )
intro.grid(pady=25)


anime_list = []

#load saved data
def load_data():
    anime_list.clear()
    try:
        with open("anime_list.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                anime_list.append(line.strip())
    
        my_label.configure(text="\n".join(anime_list))

    except FileNotFoundError:
        pass




def submit():
    anime_name = entry.get().strip()

    if anime_name == "":
        return

    anime_list.append(anime_name)

    my_label.configure(text="\n".join(anime_list))

    entry.delete(0, "end")



# label
my_label = customtkinter.CTkLabel(
    app,
    text="",
    font=("Helvetica", 14)
)
my_label.grid(row=6, column=0, pady=30)

load_data()

# entry box
entry = customtkinter.CTkEntry(
    app,
    placeholder_text="Enter Anime" ,
    width=250
)
entry.grid(row=2, column=0, pady=20)

# add_anime_button
add_anime_button = customtkinter.CTkButton(
    app,
    text="Add Anime",
    command=submit
)
add_anime_button.grid(row=3, column=0, pady=10)

app.grid_columnconfigure(0, weight=1)


#random anime picker
def random_anime():
    
    if not anime_list:
        anime_declaration.configure(
            text="Add some anime first!"
        )
        return
    
    rand_anime = random.choice(anime_list)

    anime_declaration.configure(
        text=f"Congrats!\nYou have to watch {rand_anime}.\nEnjoy!"
    )

#Pick anime button and random choice

#I need a button
pick_anime_button = customtkinter.CTkButton(
    app,
    text="Pick an Anime",
    command=random_anime
)
pick_anime_button.grid(row=4, column=0, pady=10)

app.grid_columnconfigure(0, weight=1)
#a way to randomly pick one of the provided options



#A label that declares the user has to watch the randomly picked option
anime_declaration = customtkinter.CTkLabel(app, 
        text="", 
        font=("Helvetica", 18)
        )
anime_declaration.grid(row=7, column=0, pady=50)

#remove anime
def remove_anime():
    anime_name = entry.get().strip()
    print(anime_name)

    if anime_name in anime_list:
        anime_list.remove(anime_name)
    else:
        print("Not found!")
    
    my_label.configure(text="\n".join(anime_list))
    entry.delete(0, "end")


#remove anime button
remove_anime_button = customtkinter.CTkButton(
    app,
    text="Remove Anime",
    command=remove_anime
)
remove_anime_button.grid(row=5, column=0, pady=10)

app.grid_columnconfigure(0, weight=1)


def save_data():
    with open("anime_list.txt", "w") as file:
       file.write("\n".join(anime_list))


#save data button
save_data_button = customtkinter.CTkButton(
    app,
    text="Save Data",
    command=save_data
)
save_data_button.grid(row=8, column=0, pady=10)

app.grid_columnconfigure(0, weight=1)




app.mainloop()