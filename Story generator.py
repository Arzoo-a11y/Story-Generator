import random
readername=input("WHAT IS YOUR NAME? ")
print("hello  " +readername)
HERO=["Faizaan", "Ben", "Shaquib", "TONY STARK", "Salman Khan"]
HEROINE=["Arzoo", "Shakira", "Munnu","Zara", "Helen", "Aisha"]
OCCUPATION=["teacher", "doctor","engineer", "pilot", "waiter", "terrorist", "business man", "police officer", "actor","singer", "dancer"]
RIVAL=["TAN","CAPTAIN AMERICA","CHHEDI SINGH","THANOS","VOLDEMORT","DUDLEY","KANGANA","FARUQUE","AMIR ASIF"]
PLACES=["UDAIPUR","RAMGARH","muzzafarpur","delhi","mumbai","kalyan","bangalore","chennia","kolkata"]
GOODVALUES=["kind","beautiful","honest","intelligent","extraordinary"]
BADVALUES=["arrogant","dishonest","lier"]
ACTIVITIES=["fishing","swimming","walking","running","dancing","retutning to home","going for his job","just doing daily chores","painting","speaking","listening to music","watching movies ","dreaming"]
random_hero=random.choice(HERO)
random_heroine=random.choice(HEROINE)
random_occupation=random.choice(OCCUPATION)
random_rival=random.choice(RIVAL)
random_places=random.choice(PLACES)
random_goodvalues=random.choice(GOODVALUES)
random_badvalues=random.choice(BADVALUES)
random_activities=random.choice(ACTIVITIES)
story="We keep on meeting with people around us . \nSome become our beloved ones, some are just casual ones whose presence or absence hardly matters,\nwith some we want a safe distance ,we think it will be more beneficial if we keep a distance from them.\nmay be it's out of some negative vibes and etc. let's read the story of "+random_hero+ " who was a "+random_occupation+ " \nand "+random_heroine+" who was a "+random_occupation+" \nabout their friendship and bonding .they met in a road while travelling anf after that they both started to spend time together.they started feeling for each other but there was a hurdle between them and that was "+random_rival+" he was a "+random_badvalues+" who used to like the heroine but was a bad human.the hero was "+random_goodvalues+" once the hero and heroine decided to go to "+random_places+" to hage some good time together. there he was doing  "+random_activities+" there the rival came and shoot the hero then he died."
print("\n\n LET'S BEGIN THE STORY : \n\n" ,story)