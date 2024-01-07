import customtkinter
import os
from PIL import Image
import threading
from modules.effort import PrintEffort
from config import config_form



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("One Click Orange")
        self.geometry("800x450")

        

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "images")
        self.iconbitmap(os.path.join(image_path, "favicon.ico"))
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "orange.webp")), size=(26, 26))
        self.logo_main = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo-main.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "icon.webp")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "icon-bw-dark.webp")),
                                                 dark_image=Image.open(os.path.join(image_path, "icon-bw-light.webp")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "icon-bw-dark.webp")),
                                                     dark_image=Image.open(os.path.join(image_path, "icon-bw-light.webp")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Squeeze an option", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_node_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Node",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_node_button_event)
        self.frame_node_button.grid(row=2, column=0, sticky="ew")

        self.frame_config_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Config",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_config_button_event)
        self.frame_config_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_columnconfigure(1, weight=1)

        # create a separate frame for the logo
        self.logo_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.logo_frame.grid(row=0, column=0, columnspan=3)  # span across two columns
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.logo_frame, text="", image=self.logo_main)
        self.home_frame_large_image_label.pack(padx=20, pady=10)  # use pack instead of grid

        # In a separate thread
        self.home_frame_text = customtkinter.CTkTextbox(self.home_frame)
        self.home_frame_text.grid(row=2, column=0, columnspan=3, sticky="nsew")  # Adjust row and column as needed
        threading.Thread(target=PrintEffort, args=(self.home_frame_text,)).start()

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Orange 1", image=self.image_icon_image, compound="top", anchor="center")
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Orange 2", image=self.image_icon_image, compound="top", anchor="center")
        self.home_frame_button_2.grid(row=1, column=1, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="Orange 3", image=self.image_icon_image, compound="top", anchor="center")
        self.home_frame_button_3.grid(row=1, column=2, padx=20, pady=10)

        # create second frame
        self.node_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create config frame
        self.config_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        config_form(self.config_frame)  # call config_form function from config.py


        # select default frame
        self.select_frame_by_name("home")


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_node_button.configure(fg_color=("gray75", "gray25") if name == "frame_node" else "transparent")
        self.frame_config_button.configure(fg_color=("gray75", "gray25") if name == "frame_config" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_node":
            self.node_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.node_frame.grid_forget()
        if name == "frame_config":
            self.config_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.config_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_node_button_event(self):
        self.select_frame_by_name("frame_node")

    def frame_config_button_event(self):
        self.select_frame_by_name("frame_config")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

