## oly-scribe

is a quick and dirty order entry helper for the play by email game Olympia ([http://www.pbm.com/oly/](http://www.pbm.com/oly/ "Olympia PBEM")) and its latest incarnation Olympia G4 ([http://www.shadowlandgames.com/olympia/](http://www.shadowlandgames.com/olympia/ "Olympia G4")). As this program has been frankensteined from some python libs in a super quick manner, dont expect it to be perfect in matters of code and functionality. But it did its job very well.  At last, no more need to memorize these terrible game order codes! 

###Software requirements
It has been developed for the game *Olympia G4* and Python 2.7x, but should be easily adaptable for other flavours of the game like *Olympia: The Age of Gods (TAG)*. 


### Features & ultra quick manual
The program has two main features: 

- entry game orders in *semi-human language* with the help of a **autocompletion** function. Hit *space* to autocomplete a word.
- **transcribe** the entered orders to Olympia order format 
- **copy all** copies the entire text into the buffer memory. In order to selectively copy a part of the orders you need to mark the specific text before pressing the copy button. 

Example: 

    unit 2321 # [2321] John the demonstration Noble
    # This is a comment. John will give Yoshi the Gulper all dragons. 
    # And do some more stuff.
    # This could be a fancy order template (not integrated yet).
    study ciphered_writing_of_areth-pirn
    give Yoshi_the_Gulper dragon 2
    take Yoshi_the_Gulper gold all 
    message "Glory to the Ivory Tower!" 
    give garrison gate_crystal all 
    explore 
    breed centaur centaur 
    move n
    move west 
    claim riding_horse 1
    quarry 5
    collect wood 5

After hitting *transcibe*, these are translated into Olympia order language. You can also cut away comments by using the *Clean Comments* function.

    unit 2321 # [2321] John the demonstration Noble 
    study 844 
    give Yoshi_the_Gulper 286 2 
    take Yoshi_the_Gulper 1 0 
    message "Glory to the Ivory Tower!" 
    give garrison 83 0 
    explore 
    breed 271 271 
    move n 
    move west 
    claim 52 1 
    quarry 5 
    collect 77 5  

It is also possible to transcribe noble names into IDs. However, these must be present in the *olyG3_transcribedata.py* dictionary. **Note:** It is advised to delete the old noble names from the dictionary.

### Issues

- there is a problem with "wood" beeing converted to *77* while being a at the same time. use "COLLECT wood" to avoid this problem.

- the keyword transcription does not stop from transcribing messages, rumours and times articles. 



### Licence 

It is free as that air that we breathe - but check the python licence ([http://docs.python.org/2/license.html](http://docs.python.org/2/license.html "Python license")) to be 100% sure. Hack away! (:
