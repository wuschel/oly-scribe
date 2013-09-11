## oly-scribe

is a quick and dirty order entry helper for the play by email game Olympia ([http://www.pbm.com/oly/](http://www.pbm.com/oly/ "Olympa PBEM")). 

###Software requirements
It has been developed for the game *Olympia G3* and Python 2.7x, but should be easily adaptable for other flavours of the game like *Olympia: The Age of Gods (TAG)*  

###Features
The program has two main features: 

- entry game orders in *semi-human language* with the help of a **autocompletion** function
- **transcribe** the entered orders to Olympia order format 

Example: 

    # [2321] John the demonstration Noble
    # This is a comment
	study ciphered_writing_of_areth-pirn
    give Yoshi_the_Gulper dragon 2
    breed centaur centaur 
    move n

After hitting *transcibe*, these are translated into Olympia order language. You can also cut away comments by using the *Clean Comments* function.

    # [2321] John the demonstration Noble
    study 844  
    give 6406 286 2  
    breed 271 271   
    move n  

It is also possible to transcribe noble names into IDs. However, these must be present in the *olyG3_transcribedata.py* dictionary.

###Licence 

As this program has been frankensteined from some python libs in a super quick manner, dont expect it to be perfect in matters of code and functionality. But it did its job very well. 

It is free as that air that we breathe - but check the python licence ([http://docs.python.org/2/license.html](http://docs.python.org/2/license.html "Python license")) to be 100% sure. Hack away! (: