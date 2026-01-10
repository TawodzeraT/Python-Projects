# Program Name: SnowMan Turtle Graphics
# Author: Tavonga Tawodzera
# Date: December 2, 2025
# Description: This program draws a snowman using turtle graphics based on
#              user-specified dimensions for hat, head, body sections, and arms.

import turtle

class SnowMan:
    """A class to draw a snowman using turtle graphics."""
    
    def __init__(self, hatCrownLength, hatBrimLength, hatBrimWidth, 
                 headRadius, midSectionRadius, baseRadius, armsLength):
        """Initialize the SnowMan with specified dimensions."""
        self.hatCrownLength = hatCrownLength
        self.hatBrimLength = hatBrimLength
        self.hatBrimWidth = hatBrimWidth
        self.headRadius = headRadius
        self.midSectionRadius = midSectionRadius
        self.baseRadius = baseRadius
        self.armsLength = armsLength
        
        # Setup turtle
        self.t = turtle.Turtle()
        self.t.speed(3)
        
    def drawHat(self):
        """Draw the snowman's hat with a square crown and rectangular brim."""
        # Calculate proper spacing from head
        hatYPosition = self.baseRadius + self.midSectionRadius * 2 + self.headRadius * 2
        
        # Position turtle at top of head to start hat
        self.t.penup()
        self.t.goto(-self.hatBrimLength / 2, hatYPosition)
        self.t.pendown()
        
        # Draw hat brim (rectangle) with color
        self.t.setheading(0)
        self.t.color("black")
        self.t.fillcolor("black")
        self.t.begin_fill()
        for i in range(2):
            self.t.forward(self.hatBrimLength)
            self.t.left(90)
            self.t.forward(self.hatBrimWidth)
            self.t.left(90)
        self.t.end_fill()
        
        # Draw hat crown (square) with color
        self.t.penup()
        self.t.goto(-self.hatCrownLength / 2, hatYPosition + self.hatBrimWidth)
        self.t.pendown()
        
        self.t.fillcolor("black")
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(self.hatCrownLength)
            self.t.left(90)
        self.t.end_fill()
    
    def drawHead(self):
        """Draw the snowman's head with eyes and mouth."""
        # Calculate proper position - head sits on top of mid-section
        headYPosition = self.baseRadius + self.midSectionRadius * 2
        
        # Draw head circle
        self.t.penup()
        self.t.goto(0, headYPosition)
        self.t.setheading(0)
        self.t.pendown()
        self.t.circle(self.headRadius)
        
        # Draw left eye (simple dot)
        self.t.penup()
        self.t.goto(-self.headRadius / 3, headYPosition + self.headRadius * 0.6)
        self.t.pendown()
        self.t.dot(6)
        
        # Draw right eye (simple dot)
        self.t.penup()
        self.t.goto(self.headRadius / 3, headYPosition + self.headRadius * 0.6)
        self.t.pendown()
        self.t.dot(6)
        
        # Draw simple smile (curved line made of small dots)
        smileY = headYPosition + self.headRadius * 0.2
        smilePositions = [-self.headRadius / 4, -self.headRadius / 8, 
                         0, self.headRadius / 8, self.headRadius / 4]
        for i in range(len(smilePositions)):
            self.t.penup()
            offset = abs(smilePositions[i]) * 0.2
            self.t.goto(smilePositions[i], smileY - offset)
            self.t.pendown()
            self.t.dot(3)
    
    def drawMidSection(self):
        """Draw the middle section of the snowman."""
        # Mid-section sits on top of base
        midYPosition = self.baseRadius
        
        self.t.penup()
        self.t.goto(0, midYPosition)
        self.t.setheading(0)
        self.t.pendown()
        self.t.circle(self.midSectionRadius)
    
    def drawBase(self):
        """Draw the base (bottom) section of the snowman."""
        self.t.penup()
        # Position base at the bottom
        yPosition = -self.baseRadius
        self.t.goto(0, yPosition)
        self.t.setheading(0)
        self.t.pendown()
        self.t.circle(self.baseRadius)
    
    def drawArms(self):
        """Draw the snowman's arms."""
        # Arms should be at the middle of the mid-section
        midYPosition = self.baseRadius
        armY = midYPosition + self.midSectionRadius
        
        # Draw left arm (simple line angled upward)
        self.t.penup()
        self.t.goto(-self.midSectionRadius * 0.7, armY)
        self.t.setheading(135)  # Angle upward-left
        self.t.pendown()
        self.t.forward(self.armsLength * 0.8)
        
        # One small branch on left arm
        self.t.backward(self.armsLength * 0.3)
        self.t.right(45)
        self.t.forward(self.armsLength * 0.2)
        
        # Draw right arm (simple line angled upward)
        self.t.penup()
        self.t.goto(self.midSectionRadius * 0.7, armY)
        self.t.setheading(45)  # Angle upward-right
        self.t.pendown()
        self.t.forward(self.armsLength * 0.8)
        
        # One small branch on right arm
        self.t.backward(self.armsLength * 0.3)
        self.t.left(45)
        self.t.forward(self.armsLength * 0.2)
        
        # Hide turtle
        self.t.hideturtle()


def main():
    """Main function to get user input and draw the snowman."""
    print("Welcome to the SnowMan Drawing Program!")
    print("Please enter the following dimensions:")
    print()
    
    # Get user input for all dimensions
    hatCrownLength = float(input("Enter hat crown length: "))
    hatBrimLength = float(input("Enter hat brim length: "))
    hatBrimWidth = float(input("Enter hat brim width: "))
    headRadius = float(input("Enter head radius: "))
    midSectionRadius = float(input("Enter mid-section radius: "))
    baseRadius = float(input("Enter base radius: "))
    armsLength = float(input("Enter arms length: "))
    
    # Create SnowMan object
    snowman = SnowMan(hatCrownLength, hatBrimLength, hatBrimWidth,
                      headRadius, midSectionRadius, baseRadius, armsLength)
    
    # Draw the snowman in correct order
    snowman.drawBase()
    snowman.drawMidSection()
    snowman.drawHead()
    snowman.drawHat()
    snowman.drawArms()
    
    print("\nSnowman drawing complete!")
    print("Click on the graphics window to close.")
    
    # Keep window open
    turtle.done()


# Call main function
main()
