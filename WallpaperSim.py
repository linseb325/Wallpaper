from WallpaperGenerator import WallpaperGenerator

# The only job of this class is to begin the simulation and manage user input/logic.
# It creates an instance of WallpaperGenerator each time the simulation is run.

class WallpaperSim:

    __generator = None      # Stores the wallpaper data for the current simulation.

    # Call this to begin the prompts for the wallpaper simulation.
    def begin_simulation(self):
        num_colors = input("\n\nWALLPAPER SIMULATOR: \n\nWould you like 2-color or 3-color wallpaper? [Type the number '2' or '3' and press the return key.] \n-> ")

        # Check user input to make sure the user typed either '2' or '3'. Otherwise, default to 2 colors.
        if (num_colors != "2") and (num_colors != "3"):
            print("\nInvalid input. Defaulting to 2-color wallpaper.")
            num_colors = "2"

        # Get remaining input values from the user.
        corna = input("\nInput for corna... [Type an integer and press the return key.] \n-> ")
        cornb = input("\nInput for cornb... [Type an integer and press the return key.] \n-> ")
        side = input("\nInput for side length... [Type an integer and press the return key.] \n-> ")

        # Make sure the user typed values that we can cast to integers. Otherwise, use default inputs.
        try:
            self.__generator = WallpaperGenerator(int(corna), int(cornb), int(side))
        except:
            print("\nOne of your inputs was invalid! Defaulting to: \ncorna = 0 \ncornb = 0 \nside = 50")
            self.__generator = WallpaperGenerator(0, 0, 50)

        # Generate the wallpaper based on the correct number of colors.
        if (num_colors == "2"):
            self.__generator.generate_two_color_wallpaper()
        else:
            self.__generator.generate_three_color_wallpaper()

        # Ask the user if he/she would like to see the generated wallpaper, and respond accordingly.
        print("\nGenerated " + num_colors + "-colored wallpaper. Want to display it? [Type 'yes' or 'no' and press the return key.]")
        shouldDisplay = input("-> ")
        if shouldDisplay == "yes":
            self.__generator.display_wallpaper()
        else:
            print("\nOK, I won't show you.")

        # Ask the user if he/she would like to make more wallpaper, and respond accordingly.
        shouldRestart = input("\nWant to restart the simulation? [Type 'yes' or 'no' and press the return key.]\n-> ")
        if shouldRestart == "yes":
            self.begin_simulation()
        else:
            print("\nOK. So long!")