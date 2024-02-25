
<p align="center">
 <img width="100px" src="https://i.imgur.com/O1T3CrC.png" align="center" alt="Logo" />


<h2 align="center">Scratchie</h2>
<p align="center">Scratchie is an amazing library for when converting from scratch to python. It has similar syntax to scratch in order to help kids to convert to text-based programming quickly.</p>


## Quick Start 🏁

1 Press ```Windows Key + R``` and type in "```cmd```". After doing so, copy and paste this into the terminal, then hit enter.

```
python -m site --user-site
```

2 Now copy the output given.

3 Now run ```cd <paste in the output>```

4 Run the command below and press enter. 
(Make sure you have [Git](https://git-scm.com/downloads) installed!)
```
git clone https://github.com/WorkingAtGoogle/scratchie.git
```

Also run this if you want the text-to-speech features.
```
pip install pyttsx3
```
Done! you're ready to go. Scroll down to start!

(I'm sorry it was kind of hard to install. PyPI is so confusing and just didn't work)

P.S Sorry mac users.



## Documentation 📜

This is all the features for Scratchie explained.


## Importing and Setup
```python
from scratchie import scratchie

s = scratchie.scratchie()
```
This imports the library so you can use it. This is needed to make the project work. This also creates a shortcut to make the other steps easier to do.

## say("")

```python
s.say("<message>")
```

This says the text in the brackets in the console.
To print anything than plain text, take away the quotation marks. (This is also the same for everything else)

## ask("")
```python
<variable> = s.ask("<message>")
```
This asks the user for an input and saves it to a variable

## pick_random()
```pyhon
<variable> = s.pick_random(<number1>, <number2>)
```
This picks a random number from the range you put in and saves it to a variable.

## join()
```python
<variable> = s.join("<string1>", "<string2>")
```
This joins 2 strings (variables can be joined too!) together and saves it to a variable.

## contains()
```python
if s.contains("<string>", "<chars>"):
    s.say("Yay!")
```
This finds wether or not <string> has <chars> in it. If so, it says "Yay!"

## wait()
```python
wait(<seconds>)
```
This pauses the script and waits for the chosen amount of time.

## lengthof()
```python
s.say(lengthof("<string>"))
```
This says the amount of characters the chosen string has.

## letterof()
```python
s.say(letterof(<number>, "<string>"))
```
This says the <number>th letter in the chosen string.

## speak()     [SPECIAL]
```python
speak("<string>")
```
This is a special feature not included in scratch, but it uses text to speech and says the string out loud through your speakers or headphones.

## open() [SPECIAL]
```python
open("<website adress>")
```
This is a special feature not included in scratch, but it opens the website in a new tab in your default browser.

## More Features Coming! 
## Acknowledgements

 - [readme.so (helped me make this readme)](https://readme.so)
 - [CodeKids (The whole reason I made this)](https://codekids.com.au)


