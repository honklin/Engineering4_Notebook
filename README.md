# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Raspberry_Pi_Assignment_Template

### Launchpad 1

This assignment counts down from 10 to 0.

### Code

[Launch 1 Code](https://github.com/honklin/Engineering4_Notebook/blob/main/raspberry-pi/Launch1.py)

### Evidence 

![GIF](images/launch1.gif)

### Reflection

This assignment was pretty simple, but I did figure out that the syntax for 'for' statements is for var in range (limit inclusive, other limit exclusive, interval). I also figured out how to run the PICOs in the repl using Ctrl+D and Ctrl+S on the code.py file. The code.py file needs to be opened from the CircuitPy folder once the device is connected, not from a code.py file in the documents folder.

&nbsp;

### Launchpad 2

This assignment blinks a green LED every second as it counts down from 10 seconds, then turns the red LED on for liftoff.

### Code

[Launch 2 Code](https://github.com/honklin/Engineering4_Notebook/blob/main/raspberry-pi/Launch2.py)

### Evidence 

![GIF](images/launch2.gif)

### Wiring

![Image](images/launch2wiring.jpg)
Launch 2 wiring

### Reflection

The only problems I had with this assignment was the wiring. I needed to check that my LEDs were working because the red one didn't turn on and was causing problems by turning the green LED on instead. Then, after I replaced the red LED, I discovered that the green LED wasn't turning on so I had to replace that as well.

&nbsp;

### Launchpad 3

This assignment uses a button to start the liftoff countdown from 10 with LEDs.

### Code

[Launch 3 Code](https://github.com/honklin/Engineering4_Notebook/blob/main/raspberry-pi/Launch3.py)

### Evidence 

![GIF](images/launch3.gif)

### Wiring

![Image](images/launch3wiring.jpg)
Launch 3 Wiring

### Reflection

I added a pull down on the button in my code, but that means that I don't need a resistor on the button as well because the pull down declaration restricts the power it gives from the pin. I also ran into a problem where my button was always evaluating True even though I hadn't pressed it, but I realized that I had forgotten the button wires need to be on opposite sides and rails.

&nbsp;

### Launchpad 4

This assignment rotates a servo after the liftoff countdown ends.

### Code

[Launch 4 Code](https://github.com/honklin/Engineering4_Notebook/blob/main/raspberry-pi/Launch4.py)

### Evidence 

![GIF](images/launch4.gif)

### Wiring

![Image](images/launch4wiring.jpg)
Launch 3 Wiring

### Reflection

I had some trouble getting my servo to turn even though my code was correct and I couldn't find any problems with my wiring. Then, I realized that I had accidentally wired my servo to ground through a resistor so the servo wasn't rotating. 

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Link](http://www.google.com)

### Test Image
![Image](images/engineeringimg.png)

### Test GIF
![GIF](images/engineeringgif.gif)
