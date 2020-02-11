# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("[player_name]",  color="#1b77ee")
define a = Character("{b}Archo2{/b}",  color="#1b77ee")
define s = Character("{b}Security Bot{/b}",  color="#1b77ee")
define c = Character("Crawler",  color="#bff3d6")
define suba = Character("Subject 130", color="#bfe8f3")
define subb = Character("Subject 163", color="#b8a1d6")
define q = Character("Qar", color="#FF7070")
define y = Character("???", color="#FF7070")
default pathd = False


# The game starts here.

label start:
    $ player_name = ""
    play music "Tune_Leaps.mp3"
    $ player_name = renpy.input("Please input a username. Please note that this name will be used throughout the entire visual novel:") 
    q "As this is a small sample, this was made under the span of two weeks, which is clearly not ideal to make a quality product."
    
    
    
    q "Because of that, a donation of at least $500000000000000000 is {i}{b}{u}REQUIRED{/i}{/b}{/u} to view the content shown to you know. Failure to comply with the tax will put you in federal prison. (-Jason, the programmer of this visual novel.)"
    q "Ehem, aside from the point, because of the time constraint put upon us, the product you see below may not be the best quality it could be."
    q "Thank you for understanding, now let us introduce you to the characters."
    q "You will be placed in the shoes of a character named Dorine Finch, known as Subject 185. but as this should be a customizable experience, you can enter the name of what you want to go by in this simulation."
    q "For example here, let's see an example slide."
    m "\"Hey, this is what the template looks like :D\""
    q "As you can see, your inputted name is set to the upper hand corner, and although you won't be called by the name of whatever you inputted, you might see some sneak peaks later if you choose to support me and my friends on our universe-building journey."
    q "Let us carry on now."
    q "You are set in the yaer 2122. Only 19 years before, mankind seeked to create a specialized kind of \"human\" that had access to powers the average human could not possess."
    q "The secret organization that created these \"humans\" goes by the name of Zerithin. They classify this project as 2103: Avrin, 2103 being the year these so called avrins were created."
    q "Now that you have some background info on our story universe, let's jump right into the actual product."
    # heheh flashy uwu

    a "System booting: Subject 185. Status: Awakening."
    "I awoke to the familiar buzzing of the facility."
    "Trying to ignore the faint buzzing, I shifted as much as I could on the hard mattress, my body aching from the intense muscle-test training I had done the day before."
    "This had been the 5th time they had done the experiments and I was getting TIRED of it, especially because I would always end up passing out or get stuck with a horrible migrane."
    "Unable to sleep because of my light-sleeper issues, I groaned and resigned by turning my head towards the electro-cuffs, 4 in total, one at the end of each limb."
    "A few quiet moments pass and I hear the monotone, lifeless voice that signaled that the Archo2 had figured out that I was awake."
    a "Welcome back, Subject 185. I hope your rest was well, be prepared for more training today. Initiating wake up protocol."
    "The cuffs reclined into their slots with a small click, allowing me to stretch my sore body."
    m "\"Ugh, time for another exhausting day..\" I hissed under my breath as the monitors swiveled, catching every uttered word."
    "I grab my clothes and head into the provided bathroom, changing into the hoodie I got from the head of Zerithin's secret corporation."
    "After washing my face, I rubbed my dripping face into the sleeve of my oversized hoodie."
    "Looking into the mirror, I saw a disheartened individual, the color slowly draining out of their face as every day passed with suffering."
    "But what could they do when they were stuck miles in the middle of nowhere?"
    "Shaking my head, I ventured towards the door of my room."
    menu:
                "Taking a hold of my doorknob, I opened the door and stumbled out into the hallway, deciding upon two choices I could take."
                
                "Challenge myself to blindly find my way to the cafeteria using my enhanced senses":
                    "I closed my eyes and relied on my sense of hearing and scent to guide me to the cafeteria."
                    "Only when I turned a corner did I bump into something- or rather {i}someone.{/i}"
                    # Black sprite shakes and jolts
                    "I wrinkled my nose and looked up to see Crawler's annoyingly radiant smiling face at me."
                    c "\"Oh hey, Subject 86!\""
                    c "\"Good to see that you're out and about. I didn't think anybody was here in the corridors, seemed all too quiet, but it sure seems that the training you've been doing is paying off,\" he winked at me."
                    m "I looked away, giving a small shrug."
                    c "\"Well, meet me back at your room after you've eaten and I'll come fetch you for your training.\" He patted my shoulder comfortingly."
                    c "\"I'm currently trying to adjust your training system.\" he mumured gently. \"I know how much you hate the way the boss does things around here.\""
                    c "\"Well, off to breakfast you go!\" With that, he turned his back and left me alone in the facility hallway, on my way to breakfast."
                "Walk down the hallway as usual":
                    "Choosing not to make a fool of myself again, I put my hands in my pocket and made my way through the winding complex, now in a slightly more irritated-stance."
                    "My steps pattered against the metal floor, the echos rattling inside my brain like those rubbery bouncy balls that people played with all the way in the '19s."
                    "A shiver crawled down my spine, creeping to the tip of my tail as the faint memories of the {i}incident{/i} darted into my conciousness."
                    # *short moment, flashes of red (not neccisarily blood lmao) and hazy vision, shaking screen, jolting*
                    "Feeling my body tremble, I forced myself to push away the violent moments, knowing it was better to leave untouched."
                    "Dragging myself down the hall, I closed my eyes for a brief moment and took a deep breath for every thought that harmed my mind."
                    m "\"It's alright, just forget about it. It doesn't matter now..\""      
                    
    play music "doneee.mp3"
    "Finally seeing the entrance of the dining hall, I walked in to 163 shoving his face with weird green mush, whilst 130 sat there, facing me as I showed myself."
    # Have Subject 130 come into the left, and then:
    suba "\"Welcome 185. I was expecting you.\""
    suba "\"I could hear your relenting thoughts from down the corridor.\""
    # Have Subject 163 come in from the left heheheh
    subb "\"Morning,\" he greeted, the food in his mouth muffling his voice. I nodded to make sure he knew I heard his greeting,"
    m "\"Well it's certainly been a bit of a boring morning, but I'm glad you're always here to eavesdrop,\" I teased, smiling as I saw the expression on 130's face."
    suba "\"Why, you know I can't control it, otherwise I would've stayed out of your thoughts, or would I?\""
    suba "\"It's always {i}fun{/i} to know everything about everyone before I even meet them in real life,\" he muttered, rolling his eyes."
    m "\"Alright alright, I get your point, can't take a joke can you?\" I commented light-heartedly."
    "Strolling over to the giant heating plate, I grabbed a plate beside the big pot and picked up the ladle, dumping a giant blob of oatmeal onto my bowl."
    "Walking back over to the table, I pulled out a chair and sat down, starting to eat my meal."
    menu:
                "Munching on some bland mush that people consider suitable for consumption, I tried to start a conversation."
                
                "Find that there's nothing on my mind at the moment":
                    # 130 Neutral, 163 Eating
                    "Finding that I didn't have anything else to say to 130 or 163, I continued eating in silence."
                    "Finishing up, I scraped the rest of the oatmeal off my bowl and into my mouth, placing my dish into the sink."
                    "Taking one last look at the duo, I walk away, heading towards my room."
                "Try to start a conversation with 130":
                    # 130 Pained
                    "Pushing myself togo talk to 130, I lifted my head, only to see 130's eyes start flickering in their sockets."
                    m "\"130, you alright?\""
                    suba "\"Yeah, freaking stupid, glitchy tech augs.\""
                    m "\"Tech augs? I thought Zerithin already moved on to more natural methods like gene manipulation and specifically developed fluids, instead of tech.\""
                    suba "\"No- Sorry, wrong word. I just like to blame the tech augs, I had to use them once and they sucked like hell. But anyways, the things they've been injecting into me have been making my head hurt and apparently now my eyes won't focus.\""
                    suba "He massaged his temples, wrinkles forming on his forehead. Deciding that I should probably leave 130 in peace, I pick up my bowl and stand up."
                    m "\"I'm going to get going. Crawler told me to get back to my room for training so I better get to that. Gonna be horrible, but oh well I guess. Bye 130, 163.\""
                    "130 didn't reply, but sucks for him, he's now on my {i}rude{/i} list.."
                    # SUBB (163) eating sprite
                    subb "I waved my farewells to 163 before putting away my dish and leaving the vicinity."
                "Tease 163 for geting more food after shoving his face full of food":
                    "I observed as 163 got up from his seat to grab yet another bowl of oatmeal."
                    m "\"Are you actually getting another bowl of oatmeal? That's like your third one this morning.\""
                    # shrug sprite
                    subb "He shrugs."
                    m "\"Oh alright then. I'll get going, Got to get to training with Crawler.\""
                    "Standing up, I grabbed my bowl and put it in the sink before saying my farewells."
                "Ask where Subject 124 has been":  # PATH D
                    $pathd = True
                    "Gathering my thoughts, I realized I hadn't seen Subject 124 around the past week."
                    "{i}I wonder where she is..{/i}"
                    m "\"Have y'all seen where 124 has been? I havent seen her for at least a week now.\""
                    # 130 neutral sprite
                    "130 seemed deep in thought."
                    suba "\"I don't think I've heard her usual anxious thoughts around, though my mind's definitely clearer without her.\""
                    m "I scoff."
                    m "\"When I find her, I'm definitely telling her that.\""
                    suba "\"You better not.\""
                    m "\"No promises!\" I exclaimed as I dumped my bowl into the sink and left."
    "Walking into the hallway, I'm approached by a security bot."
    "It stood tall above me, turning its head down to scan me."
    s "\"Halt. Starting a scan.\""
    # Blank Slide
    s "\"Scanning... Subject identified. Subject 185. Encounter noted. You may resume activity.\""
    "Taking my leave, I listen yet again to the pitter patter of my footsteps."
    menu:
                "Passing through the same hallway I did about 10 minutes ago, I realize a door was left open where it wasn't before."
                
                "Check it out":
                    "Scanning the perimeters of my door, I peered my head into the area, only to find a big room with a staircase that went on past my vision."
                    "Familiarizing myself with the area, I remembered trespassing into a place like this before."
                    "Memories of trying to escape the suffocating facility of Zerithin whirred in my mind, being monitored all-day and all-night after my escape attempt."
                    "Nobody was stopping me now."
                    "Taking one last peek into the hallway to ensure no one was looking, I entered while gazing up at the tall stairway."
                    "I started the climb by running up the first initial steps."
                    "Halfway up the maybe, 10th flight of stairs, I remembered the security cameras."
                    m "\"Oh frick..\" I slapped my face, disappointed that I didn't realize sooner."
                    m "\"Well, too late now, isn't it?\" I muttered, rolling my eyes. \"Just another reason for me to get to the top of these stairs ASAP.\""
                    "Running a couple more flights, I saw that I only had a few more levels to go."
                    "Hastening my pace, I was nearing the top when my side started to hurt, a faint throbbing in my head."
                    m "\"You've got to be kidding me..\" I grimaced as I clutched my side."
                    "Pushing myself to get to the top, I accidentally tripped and stumbled upon the hard-edge stone stairs."
                    # Sceren shakes
                    m "\"Ugh-\""
                    "Rubbing the arm that fell against the edge, I pursed my lips, pushing against the wall to prop my body upright."
                    "Taking a deep breath in, I limped up the rest of the way, the pain in my head worsening with every movement."
                    "Putting step upon step, slight anticipation drove through my body as I was met with a trapdoor."
                    "The only time I had ever seen a trapdoor was when Crawler lowered himself down into the supervisor room so that he could monitor me from a bottom-up perspective."
                    "But even then, I had never used one before."
                    "Slowly, I approached it and yanked on the handle weakly."
                    "Nothing."
                    a "\"Activity sensed. Please enter the passcode to unlock the door.\""
                    "Knowing an easier method, I transformed into Finch."
                    "Feeling my head grow in size and my body shift into one of a winged beast, my head raced as it usually did when I transformed."
                    m "\"Time to see what I can do..\" I screeched in animal language."
                    "Ramming the door with as much force as I could muster, I could feel the metal dent slightly as my head made contact with it."
                    "Lowering myself to see the progress I made, my vision started to cloud, focusing and unfocusing inconsistently."
                    "{i}Can I even make it..?{/i}"
                    "Not ready to give up yet, I rammed the door again, continuing the process until the alarms were set off, blaring in my ears."
                    a "\"Warning! Breach detected! Warning!"
                    "A slight panic started to sieze my chest, only adding to the haze of my senses."
                    "{i}I can't get caught! Security is going to start coming after me soon!{/i}"
                    "Pounding against the metal trapdoor, I could feel the metal start to give in."
                    "Starting to hear the shouts from the bottom of the stairs, I broke through the door, scrambling desperately through the hole in the metal, catching a whiff of the crisp breeze."
                    "The familiar scenary of grass filled my vision, trees lining the distance."
                    "A safe feeling washed over me before I snapped back to reality."
                    m "\"Hide hide hide... But there's only grass-\""
                    "My eyes flittered around to find a potential hiding spot, but the only place that would be reasonable was to get over to the forest or jump off a cliff and hope for the best."
                    "Such great options to be met with."
                    menu:
                                "Thinking about how I was weakened by my symptoms and about the time that was ticking away, I started to enter a state of panic."
                                
                                "Get to the trees as fast as possible":
                                    "Deciding that my best option was to get to the trees, I sprinted. Or at least I tried to."
                                    "Adrenaline trudged through my veins, making me rush when my body was already weak, causing me to stumble."
                                    "I knew that I was gonna fall, my muscles would give up on me soon and I would lay there like dead prey, waiting to be picked off by the crows."
                                    # Blank screen
                                    "The trees were only a couple yards away now, but I couldn't even feel my limbs anymore."
                                    "{i}Keep going, almost there, don't fail on me!{/i}"
                                    "The next thing I knew, I face-planted into the ground."
                                    "I flailed, trying to get back up, but I had no control over my arms and legs anymore."
                                    "I sat there, defeated."
                                    "Closing my eyes, I let my consciousness go and faded away into the darkness, knowing the next time I would wake up would be met with severe consequences."
                                    q "Sample ends."
                                    jump credits
                                    # END SECTOR
                                "Jump off the nearby cliff and glide to safety" if pathd:
                                    "Deciding that the best option would be to jump off the cliff and try to glide my way down, I scurried over towards the cliff."
                                    "Halting yards from the actual edge is an extra precaution due to my current physical state, I stretched my wings and help them up shakily."
                                    "The wind swept through and under my wings, shaking the membranes between my fingers."
                                    "It seemed strong enough to support me on the way down."
                                    "Starting to hear the yells of the Zerithin agents, I scurried over to the edge, wings spread."
                                    "Taking a leap of faith, I jumped off the edge and plummeted for a couple seconds until the wind caught my wings and I soared."
                                    "I aimed myself towards the little margin of land wrapping the cliff bottom."
                                    "Right then and there, my side burst into an excruiciating pain."
                                    "Before I could stop myself from faling, my body crashed into the land below, thudding into the cold rock."
                                    "Clecnching my jaws together, I cursed in my mind."
                                    "Just lying there for a moment to catch my breath, I stared at the slow-moving clouds."
                                    "How peaceful it would be to just not hurt for 10 minutes."
                                    "Sitting up, I transformed back into my humanoid form."
                                    "Rubbing my arm, as it was the side of the most force, I braced my future self for severe bruising."
                                    "Looking around, my eyes found a cave not too far from where I sat."
                                    "Its gaping mouth revealed an inky blackness that within that, a small trail of glowing lights appeared."
                                    "Curious as to how lights could randomly just apear in a small line like that, I stood up slowly, feeling for any increasing pain as I got up from the ground."
                                    "After checking myself for any signs of a fracture or a broken bone, I gave a small cheer."
                                    m "\"Crawler did mention strong bones at some point, I guess this is where it applies.\""
                                    "My smile faded quickly as I approached the cave, my gaze fixated on the tiny lights."
                                    "Looking closer, they were suprisingly small rounded pebbles that I assumed were laid out."
                                    "They shined brightly against the half-wet stone, illuminating the dark cave space."
                                    "Not even a moment passes before I feel a hand cover my face."
                                    y "\"Shhhhh, I mean no harm. Just, don't make any niose. Let's go further into the cave, we can talk there.\""
                                    "I couldn't place who's voice this was, but I knew it was from somewhere."
                                    "Trusting the person, I allowed them to drag me futher into the unknown."
                                    q "Sample ends."
                                    jump credits
                                    
                "Know that the head of Zerithin would be outraged if they found out":
                    "Remembering the monitors in the halway, I realized that if the head of Zerithin caught me, they would be downright-angry."
                    "Oh, and I mean,   A  N  G  R  Y  ,"
                    "I had attacked a  former worker during an attempt to escape the facility and I had been put on probation for at least a month."
                    "I could still hear the head's voice in my head, even though that was like, a couple months ago."
                    "Shaking my head, I shut the door with a flick of my tail and headed on my way towards my room."
                    "Striding inside, I found Crawler by my bed looking intently on his tablet."
                    "Clearing my throat, Crawler looked up, almost dropping his tablet when he saw me."
                    c "\"Oh! Subject 185! \""  
                    c "\"I would've expected you to take longer, but I guess my assumptions were wrong.\""
                    "I lowered my eyebrows in exasperation."
                    m "\"I Don't know why I've been able to tolerate you for so longm but get a move on will you?\""
                    c "\"Ouch, well that hurt. Alright then if you want me to 'get a move on.'\""
                    c "\"Anyways, we're {i}not{/i} doing another muscle-test training today, instead we'll be doing an instinctual predatory-sense test.\""
                    c "\"We have to make sure your Hybrid vitals are all up and healthy.\""
                    c "\"Otherwise, it might call for some brain-implant refining.\""
                    "With a few more taps on his tablet, he guided me towards the training room, all set for my training session."
                    q "Sample ends."
                    jump credits

    return
