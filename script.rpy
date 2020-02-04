# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("[player_name] (Subject 185)",  color="#1b77ee")
define a = Character("{b}Archo2{/b}",  color="#1b77ee")
define c = Character("Crawler",  color="#bff3d6")
define suba = Character("Subject 130", color="#bfe8f3")
define subb = Character("Subject 163", color="#b8a1d6")


# The game starts here.

label start:
    $ player_name = ""
    $ player_name = renpy.input("Please input a username. Please note that this name will e used throughout the entire visual novel:")
    a "Hey"
    "I awoke to the familiar buzzing of the facility."
    "Trying to rid my eyes of the grimy feeling of sleep, I shifted slightly on the hard mattress, my body aching from the intense muscle-test-training I had done the day before."
    "This had been the 5th time they had done the experiments and I was getting awfully tired of it, especially because I would always end up passing out or get stuck with a horrible migrane."
    "I turned my head towards the electro-cuffs, 4 in total, one at the end of each limb."
    a "Welcome back. Subject 185. I hope your rest was well, be prepared for more training today. Initiating wake up protocol."
    "The cuffs reclined into their slots with a small click, allowing me to stretch my sore body."
    m "\"Ugh, time for another exhausting day...\" I muttered under my breath as the monitors swiveled, catching every uttered word."
    "I grab my clothes and head into the provided bathroom, changing into the hoodie I was gifted by the head of Zerithin's secret corporation."
    "After washing my face, I rubbed my wet face onto the sleeve of my oversized hoodie. "
    "Looking into the mirror, I saw a darker-skinned girl with freckles, the color slowly draining out of her face as every day passed with some sort of suffering."
    "But what could she do when she was stuck miles in the middle of nowhere?"
    menu:
                "I stumbled out into the hallway, deciding upon two options I could take."
                
                "Challenge myself to blindly find my way to the cafeteria using my enhanced senses":
                    "I closed my eyes and relied on my sense of hearing and scent to guide me to the cafeteria."
                    "Only when I turned for a corner did I then bump into something - or rather {i}someone.{/i}"
                    # Black sprite shakes and jolts
                    "I look up to see Crawler's smiling face at me."
                    c "\"Oh hey, Subject 186.\""
                    c "\"Good to see that you're out and about. I didn't think anybody was her in the corridors, but it sure seems that the training you've been doing is paying off,\" he winked at me."
                    c "\"Well, meet me back at your room after you've eaten and I'll come fetch you for your Enhanced-Sense-Training.\" He pats my shoulder comfortingly."
                    c "\"I'll try to make your training better to the best of my abilities,\" he mumured gently. \"I know you hate them very much.\""
                    c "\"Well, off to breakfast you go!\" With that, he turned his back and left me alone in the facility hallway, on my way to breakfast."
                "Walk down the hallway as usual":
                    "Choosing not to make a fool of myself, I put my hands in my pocket and made my way through the winding complex."
                    "My steps pattered against the metal floor, the echos rattling inside my brain."
                    "A shiver crawled down my spine, creeping to the tip of my tail as the faint memories of the {i}incident{/i} darted into my conciousness."
                    # *short moment, flashes of red (not neccisarily blood lmao) and hazy vision, shaking screen, jolting*
                    "Trying to ignore the violent moments that continue to scar me to this day, I proceeded down the hall, closing my eyes for a brief moment and taking a deep breath."
                    m "It's alright, just forget about it. It doesn't matter now..."

    "Finally seeing the entrance of the dining hall, I walked into 163 shoving his face with oatmeal and fruit, whilst 130 sat there, facing me as I showed myself."
    # Have Subject 130 come into the left, and then:
    suba "\"Welcome 185. I was expecting you.\""
    suba "\"I could hear your relenting thoughts from down the corridor.\""
    # Have Subject 163 come in from the left heheheh
    subb "\"Morning,\" he greeted, the food in his mouth muffling his voice. I nodded in acknowledgement of his greeting,"
    m "\"Well it's certainly been a bit of a boring morning, but I'm glad you're always here to eavesdrop,\" I teased, chuckling as I saw the expression on 130's face."
    suba "\"Why, you know I can't control it, otherwise I would've stayed out of your thoughts, or would I?\""
    suba "\"It's always {i}fun{/i} to know everything about everyone before I even meet them in real life,\" he muttered, rolling his eyes."
    m "\"Alright alright, I get your point, tis was only a joke,\" I said light-heartedly."
    "Strolling over to the giant heating plate, I grabbed a plate beside the big pot and picked up the ladle, dumping the oatmeal onto my plate."
    "Walking back over to the table, I pulled out a chair and down, starting to eat my meal."
    menu:
                "Munching on some bland mush that people consider suitable for consumption, I try to start a conversation."
                
                "Find that the atmosphere is rather intimidating to say anything":
                    # 130 Neutral, 163 Eating
                    "Trying to find the right moment to say anything, I try to think of something to say, only to make my heart race faster than it usually would. {i}I guess I won't say anything today...{/i}"
                    "Scraping the rest of the oatmeal off my bowl, I placed my plate into the sink."
                    "Taking one last look atthe duo, I walk away, heading towards my room."
                "Try to start a conversation with 130":
                    # 130 Pained
                    "Pushing myself togo talk to 130, I lifted my head, only to see 130's eyes start to flicker in their sockets."
                    m "\"130, you alright?\""
                    suba "\"Yeah, freaking stupid glitchy tech augs.\""
                    m "\"Tech augs? I thought Zerithin already moved on to more natural methods like gene manipulation and specifically developed fluids, instead of tech.\""
                    suba "\"No- Sorry, wrong word. I just like to blame the tech augs, I had to use them once and they sucked like hell. But anyways, the things they've been injecting into me have been making my head hurt and apparently now my eyes won't focus.\""
                    suba "He massaged his temples, wrinkles forming on his forehead. Deciding that I should probably leave 130 in peace, I pick up my bowl and stand up."
                    m "\"I'm going to get going. Crawler told me to get back to my room for training so I better get to that. Bye 130, 173.\""
                    "130 didn't reply, but that's alright."
                    # SUBB (163) eating sprite
                    subb "I waved my farewells to 163 before putting away my dishes and leaving the vicinity."
                "Tease 163 for geting more food after shoving his face full of food":
                    "I observed as 163 got up from his seat to grab yet another bowl of oatmeal."
                    m "\"Are you actually getting another bowl of oatmeal? That's like your third one this morning.\""
                    # shrug sprite
                    subb "He shrugs."
                    m "\"Oh alright then. I'll get going, Got to get to training with Crawler.\""
                    "Standing up, I grabbed my bowl and put it in the sink before saying my farewells."
                "Ask where Subject 124 has been":  # PATH D
                    "Gathering my thoughts, I realized I hadn't seen Subject 124 around the past week."
                    "{i}I wonder where she is...{/i}"
                    m "\"Have any of you seen where 124 has been? I havent seen her for at least a week now.\""
                    # 130 neutral sprite
                    "130 seemed deep in thought."
                    suba "\"I don't think I've heard her usual anxious thoughts around, though my mind's definitely clearer without her.\""
                    m "\"When I find her, I'm definitely telling her that.\""
                    suba "\"You better not.\""
                    m "\"No promises!\" I exclaimed as I dumped my bowl into the sink and left."

    

    scene bg room

    show eileen happy

    "You've created a new Ren'Py game."

    "Once you add a story, pictures, and music, you can release it to the world!"

    return
