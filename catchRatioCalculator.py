#actual calculator for probabilities
#first, we include some variables to hold some ratios depending on the ball used, status of the pokemon, etc...

status={"asleep":2.5, "frozen":2.5, "no status":1}

balls={"super ball":1.5, "ultra ball":2, "net ball":3, "quick ball":5, "dive ball":3.5, "repeat ball":3, "dusk ball": 3.5}
#Remaining balls have ratio 1 or need additional calculous

o_power={1:1.5, 2:2, 3:2.5}

critPokeMod = {0:0.5, 1:1, 2:1.5, 3:2}  #<30 will be 0 /// >600 will be 2.5



