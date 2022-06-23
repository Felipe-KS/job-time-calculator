Job time calculator
==================

Simple program that calculate how much someone have to earn base on time, period of the day and 
if is in the week or weekend

How to run
-----------------
To run this project you have to have Python and pytest installed in you machine. 

Get into the project paste and run

```
python program.py
```

To run the tests 

```
pytest
```

Architectur
-----------------
1. Python for the development 
2. Usind the library datetime for work whit times
3. pytest for the test part

Approach
-----------------
To beggin I broke the string of input to manage the day and times, after I discover in whit part of 
the day is the time that I'm working whit, after that the program calculat the amount of time in 
each part of the day and calculate how much the worker earn in each part of the day, and to finish 
I sum all the values and show how much have to be payed for all times

Methodology
-----------------
For this project I started with the worst case scenario for inputs to start development, 
after that I went to extreme cases, along with all that I created tests using pytest to 
ensure that what I had already done doesn't give bugs in future developments

