# What is the project about?

An app that lets the user provide the coordinates of geometrical shapes like squares and rectangles, their dimensions,
and their colors. The program produces an image file canvas with all
the geometrical shapes drawn in it.

CLI image of the app given below:

![CLI.png](CLI.png)


# How to run the program
1. Either clone this repo or download all these files by going to _Code -> Download ZIP_.
2. Create a PyCharm (or other IDE) project and configure a Python interpreter for the project.
3. Open the terminal and install the required packages by running:
   
   `pip install -r requirements.txt`
3. Run _main.py_ with Python.
4. Enter the input values as asked by the program in the command line interface.

An example of user input values could be this:
```
Enter canvas width: 600
Enter canvas height: 700
Enter canvas color (white or black): black
What do you like to draw? Enter quit to quit. square
Enter x of the square: 20
Enter y of the square: 120
Enter the side length of the square: 200
How much red should the square have? 134
How much green? 100
How much blue? 94
What do you like to draw? Enter quit to quit. rectangle
Enter x of the rectangle: 200
Enter y of the rectangle: 200
Enter the width of the rectangle: 340
Enter the height of the rectangle: 120
How much red should the rectangle have? 40
How much green? 4
How much blue? 130
What do you like to draw? Enter quit to quit. quit
```

5. The expected output is a _canvas.png_ image generated in the root directory.