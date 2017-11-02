# Generates a matrix of characters based on three arguments. Capable of both 2 and 3-color wallpaper.

class WallpaperGenerator:

    __corna = None
    __cornb = None
    __side = None           # The side argument is an upper bound on (i * self.__side / 10) and (j * self.__side / 10)
                            # in the wallpaper generation methods below.
    __matrixToDisplay = []  # A list of lists which represents rows and columns of wallpaper pixels

    # When we initialize an instance of this class, we pass in and store the 3 arguments from the user.
    def __init__(self, corna, cornb, side):
        self.__corna = corna
        self.__cornb = cornb
        self.__side = side

    # Creates a matrix of X's and whitespace characters and stores it in the matrix instance variable.
    def generate_two_color_wallpaper(self):
        self.clear_wallpaper()
        for i in range(1, 11):
            self.__matrixToDisplay.append([])   # Because we need a new row for each i
            for j in range(1, 11):
                x = self.__corna + (i * self.__side / 10)
                y = self.__cornb + (j * self.__side / 10)
                c = int(x**2 + y**2)
                if (c % 2 == 0):
                    # Put a 'X' into the matrix at this pixel position.
                    self.__matrixToDisplay[i - 1].append("X")
                else:
                    # Put a ' ' into the matrix at this pixel position.
                    self.__matrixToDisplay[i - 1].append(" ")

    # Creates a matrix of X's, Y's, and whitespace characters and stores it in the matrix instance variable.
    def generate_three_color_wallpaper(self):
        self.clear_wallpaper()
        for i in range(1, 11):
            self.__matrixToDisplay.append([])   # Because we need a new row for each i
            for j in range(1, 11):
                x = self.__corna + (i * self.__side / 10)
                y = self.__cornb + (j * self.__side / 10)
                c = int(x**2 + y**2)
                if (c % 3 == 0):
                    # Put a 'Y' into the matrix at this pixel position.
                    self.__matrixToDisplay[i - 1].append("Y")
                elif (c % 2 == 0):
                    # Put a 'X' into the matrix at this pixel position.
                    self.__matrixToDisplay[i - 1].append("X")
                else:
                    # Put a ' ' into the matrix at this pixel position.
                    self.__matrixToDisplay[i - 1].append(" ")

    # Displays the rows and columns of the wallpaper matrix in the console.
    def display_wallpaper(self):
        print("\nWALLPAPER:\n")
        for aList in self.__matrixToDisplay:
            stringToPrint = ""
            # Build up a string containing the characters of the current row, then print it on the console.
            for pixel in aList:
                stringToPrint = stringToPrint + pixel
                if len(stringToPrint) == 10:            # Meeting this condition means we've reached the last character in the current row.
                    print(stringToPrint)

    # Resets the wallpaper matrix to an empty list containing no wallpaper data.
    def clear_wallpaper(self):
        self.__matrixToDisplay = []




