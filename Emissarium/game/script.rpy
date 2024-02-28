# # The script of the game goes in this file.

# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

define w = Character('Woman', color="#c8ffc8")
define m = Character('Man', color="#72bbdd")
define y = Character('You', color = "#9b689d")
define mcb = Character('Young man', color = "#5a70dd")
define mcg = Character('Young lady', color = "#e24be2")
define my = Character("Mayor", color = "#b64e1e" )
define om = Character("Old man", color = "#b64e1e")
define mn_r = Character("The Man", color = "#7f7773")
define muz_man = Character("The Man", color = "#debf59")
define cr = Character("Creepy Man", color = "#75524d")

default sex = 0
default knowledge = 0
default alertness = 0
default mayor_child = "Young lady"
default pronoun_1 = "his"
default pronoun_2 = "he"
default pronoun_3 = "him"
default romantic = 0
default apples = False
default museum = False
default door = False
default city_info = False
default menuset = set()

image bg choose_character = "images/choose_character.jpg"
image bg your_character_m = "images/your_character_m.jpg"
image bg your_character_w = "images/your_character_w.jpg"
image bg enter_yes_no = "images/enter_yes_no.jpg"
image bg enter_yes_no = "images/enter_yes_no.jpg"
image bg cave = "images/cave.jpg"
image bg city_poppy = "images/city_poppy.jpg"
image bg no_cave = "images/no_cave.jpg"
image bg game_over = "images/game_over.jpg"
image bg poppy_f = "images/poppy_f.jpg"
image bg choose_direction = "choose_direction.jpg"
image bg city_r = "images/city_r.jpg"
image bg city_le = "images/city_le.jpg"
image bg city_str = "images/city_str.jpg"
image bg outsk_house = "images/outsk_house.jpg"
image bg choose_city_right = "images/choose_city_right.jpg"
image bg parents_child = "images/parents_child.jpg"
image bg man_eye = "images/man_eye.jpg"
image bg choice_city_left = "images/choice_city_left.jpg"
image bg sales_w = "images/sales_w.jpg"
image bg painter = "images/painter.jpg"
image bg choose_city_food = "images/choose_city_food.jpg"
image bg city_view = "images/city_view.jpg"
image bg choice_food = "images/choice_food.jpg"
image bg tea = "images/tea.jpg"
image bg apple = "images/apple.jpg"
image bg food = "images/food.jpg"
image bg door = "images/door.jpg"
image bg outsk_man = "images/outsk_man.jpg"
image bg outsk_sofa_armchair = "images/outsk_sofa_armchair.jpg"
image bg sofa = "images/sofa.jpg"
image bg arm = "images/arm.jpg"
image bg door_ins = "images/door_ins.jpg"
image bg city_fest = "images/city_fest.jpg"
image bg outsk_house_night = "images/outsk_house_night.jpg"
image bg leave_city = "images/leave_city.jpg"
image bg speak_people = "images/speak_people.jpg"
image bg muz = "images/muz.jpg"
image bg mayor_house = "images/mayor_house.jpg"
image bg girl_dr = "images/girl_dr.jpg"
image bg boy1 = "images/boy1.jpg"
image bg muz_man = "images/muz_man.jpg"
image bg hall = "images/hall.jpg"
image bg stay_examine = "images/stay_examine.jpg"
image bg gb_room = "images/gb_room.jpg"
image bg kidd = "images/kidd.jpg"
image bg choose_art = "images/choose_art.jpg"
image bg renaissance = "images/renaissance.jpg"
image bg art_gogh = "images/art_gogh.jpg"
image bg contemp = "images/contemp.jpg"
image bg mayor = "images/mayor.jpg"
image bg saveKid_sleep = "images/saveKid_sleep.jpg"
image bg desk = "images/desk.jpg"
image bg key = "images/key.jpg"
image bg go_basement = "images/go_basement.jpg"
image bg ruins = "images/ruins.jpg"
image bg sofa_2 = "images/sofa_2.jpg"
image bg fest_walk = "images/fest_walk.jpg"
image bg examine = "images/examine.jpg"
image bg proceed = "images/proceed.jpg"
image bg goutsk_sofa_armchair = "images/goutsk_sofa_armchair.jpg"
image bg cave_noCave = "images/cave_noCave.jpg"
image bg never_north_cave_cave = "images/never_north_cave.jpg"
image bg basement = "images/basement.jpg"
image bg north_cave = "images/north_cave.jpg"


label start:
    scene bg choose_character
    with fade
    call reset_game
    return

label reset_game:

    $ sex = 0
    $ knowledge = 0
    $ alertness = 0
    $ mayor_child = "Young lady"
    $ pronoun_1 = "his"
    $ pronoun_2 = "he"
    $ pronoun_3 = "him"
    $ romantic = 0
    $ apples = False
    $ museum = False
    $ city_info = False
    $ door = False


label character_select:
    scene bg choose_character
    menu:
        "Your character is a traveler passionate about finding special and hidden places from the eyes of the majority. Select a character to progress through the story."
        "Male":
            $ sex = 1
            $ char = mcg
            $ pronoun_1 = "her"
            $ pronoun_2 = "she"
            $ pronoun_3 = pronoun_1
            jump cave
        "Female":
            $ mayor_child = "Young Man"
            $ char = mcb
            jump cave

label cave:
    if sex == 1:
        scene bg your_character_m
    else:
        scene bg your_character_w
    # Add a scene for the lower text
    "It’s a sunny spring morning. You woke up in a good mood and with a lot of energy, because today is the day when you will roam the mountains to find something special."
    # Add a scene for the lower text
    "You have arrived at your destination and started wandering around. After some time, you decided to go higher and finally began to see something unusual. There was a contrasting spot in the snow-white landscape of the mountains, so you went there."
    scene bg enter_yes_no
    menu:
        # Add a scene for the lower text
        "You found a cave, but it doesn't look like a normal one, at its end you could see a light, as if it was passing through another part of the mountain. Enter the cave?"
        "Yes":
            scene bg cave
            "You took the risk, entered the cave, and proceeded to move to the light. Reaching the end of the cave you expected to see the source of the brightness, a hole in the mountain, or maybe someone who settled there and decided to make a bonfire, but you did not foresee e a magnificent view.In front of your eyes has been a city of majestic beauty."
            jump cave_entered
        "No":
            scene bg no_cave
            "You decided to not take the risk. Who knows what might be at the end of this cave, so you thought that is better to proceed to roam the mountain, and maybe you will find something interesting and less dangerously looking."
            "Unfortunately, there was nothing interesting, so you started to go higher and deeper through the mountains. It starts getting late, but you are too stubborn to stop here so you decided to change the approach and take the risk now. You saw a path, it was a dangerous one, because of its narrowness and high position, but you felt like you had no other choice than to pass it, you had to reach the other cliff."
            "You started to pass it and almost got to its end. You take one more step but the rock under your feet breaks and you got down with its debris. In a panic, you tried to grab onto something, in order to save yourself from falling, but your hands helplessly cut through the air…"
            "You fell off the cliff…The mountain’s snow started to get red under your body, its warmth faded away with every drop of your blood…"
            jump try_again_or_give_up

label cave_entered:
    scene bg city_poppy
    "You foresee a magnificent view. In front of your eyes has been a city of majestic beauty."
    "It was surrounded by the mountains with red poppies laid at its feet and above it a blue sky looked down on all this beauty."
    "You couldn't believe your eyes, on the other side of the cave where you came from are snowy mountains and the weather is quite cold, but here is the embodiment of summer."
    call Cave("")

label Cave(previousChoice=""):
    if previousChoice == "":
        menu:
            "Go to the poppy field.":
                scene bg poppy_f
                "You decided to admire the beauty of the red poppies. They were bathing in the light of the sunset. You have seen plenty of poppies in your life, but none of them were so red, redder than the roses in their full bloom, redder than the blood. You wondered if what you have seen was an illusion created by the rays of the sunset or it is their singularity. "
                call Cave("p")
            "Go to the city.":
                jump City
    elif previousChoice == "p":
        "You were mesmerized by these flowers, but it didn’t calm your curiosity about the city."
        jump City

label City:
    "You have entered the city. Apparently, there was something similar to a festival going on. You have seen that the streets and houses are festively decorated with garlands and flowers, also there have been set up multiple stalls with different stuff. People are having fun, dancing and surprisingly riding horses, you rarely see horse riders on the city’s streets in your homeland and in other countries you have visited. "
    scene bg choose_direction
    "You have looked in the face of every passing citizen and on each ones face you have seen a smile, everyone looked so happy that it makes you alarmed. How can a city exist inside a mountain? And how it can be so prosperous? It makes no sense. "
    "In order to explore the city and find more about it choose where to go."
    menu:
        "Right":
            scene bg city_r
            "You decided to turn right."
            jump City_Right
        "Left":
            scene bg city_le
            "You walked on the left road."
            jump City_Left
        "Straight":
            scene bg city_str
            "Going straight ahead, you find a path that leads to the outskirts of the city."
            jump outskirts

label City_Right:
    "Here you see a couple who tries to calm down their crying child, a man with a blank look in his red eyes and a path to the museum (pointed by a signpost)."
   
    menu right_trope:
        set menuset
        "Talk to the parents":
            jump Talk_To_The_Parents
         
        "Talk to the man":
            jump Talk_To_The_Man_R

        "Go to the museum":
            jump Go_To_The_Museum

            
    

            ######### HERE

label Talk_To_The_Parents:
    scene bg parents_child
    "You approach the young family."
    show y
    y "Hello, excuse me. Could I ask you some questions?"
    show w
    w "Hi! I see you are not from this parts. I would like to help you, but as you can see we have some troubles calming down this little child. (smiles guiltily)"
    show y
    y "May I know what caused his tears? Maybe I could help..."
    hide y
    "You get interrupted by her husband."
    show m
    m "Don't worry, we will deal with this."
    show w
    w "Yeah, don't worry, is just that we saw \"It\" at the mayor's residence so the child got emotional."
    show m "The man looks at his wife with a disapproving look."
    show y "It?"
    $ alertness += 1
    $ knowledge += 1
    "The woman wants to say something, but closes her mouth quickly."
    show m "Sorry, but we need to go home, the child doesn't calm down. Since you are a newcomer what about greeting the mayor?"
    hide m "They certainly hide something, but you understand that the man will not tell you anything and will not let his wife speak either. So, you have only one choice, to look for the answers from the mayor."
    show y "Where can I find the mayor?"
    show m "See the building at the end of the street? Go right there."
    hide m
    ### HERE MENU
    jump Mayor_House

label Talk_To_The_Man_R:
    scene bg man_eye
    "You approach the man. Coming closer you see that his eyes have a red color and his stare seems blank. You immidiatly got scared, but a few moments later you understand that his gaze is not empty, it holds something, something grievous. His eyes looked drained from crying they were full of sadness...remorse and fear..."
    "The sounds coming from your mouths quivered."
    show y
    y "I am de..ahem..deeply sorry, sir...may I ask you why you're in such a condition? Can I help you? (carefully)"
    "He looked you straight in the eyes and put his hands on your shoulders. You could feel his pain gripping you from the inside."
    show mn_r
    mn_r "I need to go...I can't stay here..How...(sobs)...How could they do this to an innocent soul... (mumbles)"
    "For a moment he came to his senses and looked at you with pity, after patting your shoulders he returned to follow his path...to the north..."
    "You didn't fully realize what was going on, but one thing was clear, you shouldn't disturb this person anymore."
    jump right_trope

label Go_To_The_Museum:
    scene bg muz
    $ museum = True
    "You enter the building and see the owner of the museum."
    menu:
        "Speak with the owner":
            scene bg muz_man
            show y 
            y " Hello, I suppose that I got to the right place to ask questions about this city?"
            show muz_m
            muz_m "Hmmm, it depends on what you want to ask."
            menu:
                "Ask how did the city became so prosperous":
                    show y 
                    y "I would like to know why this city is so prosperous despite being isolated."
                    $ knowledge +=1
                    jump Muz_Owner
                "Ask if the city has some legends":
                    $ knowledge +=2
                    jump Muz_Owner

label Muz_Owner:
    show muz_m
    muz_m "Well, let me tell you the story of founding this city."
    muz_m "It is said from the ancestors that there was a big natural disaster in their village, all their possesings were lost, many of their siblings died and they had nowhere to go. The head of the villagers lost his life and let two of his sons alone. Nobody knew what to do in such situation without a leader, but after some time the younger son of the deceased head took the lead and directed everyone to the mountains. It was said that a spirit lived there so they hoped to get help from it."
    muz_m "They headed to the mountains and found a cave, I suppose you passed through that cave too entering here.(chuckles) There they found a beautiful creature, the spirit. It did not appreciate the intrusion in his habitat and acted agressively, but the young man tryed to persuade it and he did well. The spirit agreed to let them in and showed the beautiful peisage you have seen while entering, but there was a condition. The boy must to sacrifice his life for the sake of the other people if he cares about them so much that he dared to speak to the spirit."
    show y
    y " He died?"
    show muz_m
    muz_m "No, he just agreed and lived for the sake of his people, he was a hero. His older brother bacame the mayor in order to help him and the curent head of the city is his descendant."
    menu:
        "Ask why the younger brother did not become the mayor":
            $ alertness += 1
            show y 
            y "Why the young brother did not become the mayor?"
            "Well, because he had his own duty in order to contribute to the well being of the citizens. You could ask more about it from the mayor directly, he knows more about his family."




label Mayor_House:
    scene bg mayor_house
    "You follow the given directions."
    "Going near the building, in the mayor's garden, you see a silluete. It moves gently a paint brush on a canvas, these moves are full of grace and dedication. You come closer to see the face of the person who awakened your admiration."
    "The face of the silluete started to get clearer and you could see its unexpected beauty. There was a [mayor_child]."
    menu:
        "Talk with the [mayor_child]":
            if sex == 1:
                scene bg girl_dr
            else:
                scene bg boy1
            "Your intense gaze didn't go unnoticed, [pronoun_2] rised [pronoun_1] eyes from the canvas and looked at you inquiringly. You've decided to quickly gather your thoughts and say something."
            
            show y 
            y "Hi...(awkwardly)"
            show char
            char "Greetings. (smiles politely)"
            " You were enchanted by [pronoun_1] smile, it shone brighter than the sun itself, but you came here with the purpose to find more about the city, so you need to pull yourself together."
            jump mayor_child_dialog

label mayor_child_dialog:
        menu ask_city: ########HERE MAYOR's CHILD 
            set menuset

            "Give [pronoun_3] an apple" if apples:
                show y 
                y "Here...an apple. (awkwardly)"
                $ romantic += 1
                show char
                char "Very nice of you, thanks."

            "Ask [pronoun_3] about the city.":
                show y
                y "Sorry for intrerupting you. I am new here so I would like to know more about the city and its people. Could you help me?"
                show char
                char "Sure, but instead just answering you questions what about going on a walk? This way I could not only tell you about the city but also show it to you."
                
                menu: 
                    "Agree":                
                        $ romantic += 2
                        show y
                        y " It would be perfect, thank you!"
                        show char
                        char "It's my pleasure. Just let me pack all this stuff (points at [pronoun_1] art tools)."
                        show y
                        y "Yes,sure. Let me help you."
                        "You help [pronoun_3] pack [pronoun_1] things and then go for a walk."
                        scene bg fest_walk
                        "You once again see the streets you walked on not long time ago, the festively decorated houses, people having fun."
                        "On the walk [pronoun_2] points at different places on the street and starts to tell you about people living there."
                        show char
                        char "The museum you see there (points to another part of the street) is one of the first buildings in this city... "
                        char "This flower boutique was built long before my grandfather was born. There are different types of flowers, but my favorite are sunflowers (smiles)... "
                        char "See the woman who sells food? (points)."
                        show y
                        y "*nod*"
                        show char
                        char "She's the biggest gossip girl in our city. If she sees you doing something then all people from here will know about it. I wonder she does it. (laughs slightly)"
                        show y
                        y "What are you celebrating today?"
                        show char
                        char "Celebrating?"
                        show y
                        y "Yes, I see that all the houses are decorated, people are dancing on the streets, there is a fair and things like this."
                        show char
                        char "It's a day like every other one(looks at you surprised) Is it different from where you came from?"
                        show y
                        y "Well, yes, in my homeland we decorate houses only on special ocasions and it’s the same with dancing."
                        show char 
                        char "Then...What are you doing? (curious)"
                        show y
                        y "Well,usually we just take care of our business struggling to earn money."
                        show char 
                        char "Oh...okay. (confused)"
                        "After a few moments [pronoun_2] continued to speak about the people of this city, who does what and where he/she lives."
                        jump Find_More_Mayor_Child


                    "Refuse":
                        show y
                        y "Sorry, but I don't really have time for this. "
                        show char
                        char " Oh...okay...I understand. (dissapointed)"
                        jump ask_city

            "Ask where you can find the mayor":
                show y
                y " Sorry for distracting you. Could you tell me where can I find the mayor? I need to ask him some questions."
                show char
                char "As far as I know, he must be in the residence."

                menu:
                    "Request a meeting with the mayor.":
                        show y 
                        y "Could you help me meet him?"
                        show char
                        char "Yes, follow me. I will try to bring my father to you as soon as possible."
                        "You should have guessed that [pronoun_2] is the mayor's child, [pronoun_2] invites you inside the building and explains that [pronoun_2] needs to go on the 3rd floor to call the mayor."
                        scene bg hall
                        "The interior of the mayor's residence is beautiful both outside and inside. The floor is covered with expensive decorative tiles, the stairs are carved from mahogany, and the chairs in the hall are upholstered in high quality fabric. You wonder where he got all these materials from in such an isolated place. "
                        "[mayor_child] doesn't come for a long time."

                        menu:
                            "Take a look around":
                                scene bg stay_examine
                                menu:
                                    "Stay here":
                                        scene bg hall
                                        "The Mayor's child comes down the stairs with [pronoun_1] father."
                                        menu:
                                            "Greet the Mayor":
                                                scene bg mayor
                                                show y 
                                                y "Good evening, Mr.Mayor."
                                                show my 
                                                my "Greetings, newcomer, my child told me about you, but I would like if you could share some information with me. For example, who are you? How did you get here?"
                                                menu:
                                                    "Tell him who you are and how you got here":
                                                        show y
                                                        y "I am a traveler, I spend time exploring the world and finding unique places like your city. Honestly, this is the most wonderful place I have ever seen in my entire life. As for how I got to this city, it was through a cave in the mountains. It is located in the south."
                                                        show my
                                                        my "That's...interesting. (smirks)"
                                                        " For a second, a strange spark of malevolence flickered in the mayor's eyes, but it disappeared in the blink of an eye. Maybe you are overthinking and it seemed that way to you."
                                                        my "As you can see, our city is an isolated place, so we would appreciate it if it stays that way. It's incredible how you got here and I'm sure you've come a long way to this place, but it means a lot to us. My people grow up in comfortable conditions for generations and will not be able to withstand the cruelty of the outside world. (serious)"
                                                        show y 
                                                        y "Yes, I understand."
                                                        show my
                                                        my "Very good, so as a token of appreciation, I would like to ask if you want to stay in this city or return to your homeland. But if you choose to stay, you cannot go beyond the mountains, and if you leave, you should guarantee that you will never return. "
                                                        " Mayor's words caught you off guard, but you need to make a choice."
                                                        jump Make_Choice

                                                



                                    # "Examine the first floor":


                                    # "Go back to the central hall":


label Find_More_Mayor_Child:
    menu: 
        "Find out more about the [mayor_child]":
            $ romantic += 1
            "[mayor_child] told you a lot about other people, but you started to get curious about [pronoun_1] personality. So you try to find more about [pronoun_3]."
            show y
            y "You told me pretty much about other people, but I would like to know about you too."
            show char
            char " I'm really not an interesting person, especially compared to you, you must have seen a lot beyond the mountains, while I have lived all my life between them."
            
            jump Romantic_Choice

label Romantic_Choice:
    menu:
        "Tell to the [mayor_child] that [pronoun_2] is an interesting person.":
            show y
            y "It's not true. You seem very interesting to me."
            $ romantic += 2
            show char
            char "Thank you...I understand that you are not from here and probably don't have a place to stay overnight, so, if you want you could stay here. I will provide you with a place to sleep."
            menu:
                "Refuse politly":
                    $ romantic -= 2
                    show y
                    y "Thank you for the offer, but I will decline. I came here to ask the mayor some questions."
                    show char
                    char "Okay, If you need my help let me know, I am always here here."
                    jump ask_city

                "Refuse in a rude way":
                    $ romantic -= 3
                    show y
                    y "No thanks, I don't sleep in the houses of strangers and I advice you to do the same."
                    show char 
                    char "Oh, okay... (embarassed)"
                    jump ask_city
                
                "Agree":
                    $ romantic += 1
                    "[mayor_child] brings you into the mayor's house."
                    scene bg hall         
                    show y
                    y "Are you related to the mayor in some way?" 
                    show char 
                    char "Yes, he is my dad."        

                    "You walk up the stairs and go to the door of [pronoun_1] room."
                    jump Enter_Mayor_Child_Room
                

        "Tell to the [mayor_child] that [pronoun_2] is right.":
            $ romantic -= 4
            jump ask_city


label Enter_Mayor_Child_Room:
    menu:
        "Enter room":
            scene bg gb_room
            "The room is very spacious and holds a lot of light. You see paintings filling the room and one of them caught your attention."
            
            scene bg kidd
            show y 
            y "In this painting you see a small child in a dark and small room, he stands with his back to you, but you could fell that if he turns , you would see his eyes full of tears."
            
            menu:
                "Tell that [pronoun_2] has great painting skills":
                    jump Painting_Skills
                    ######## ADD HERE
                
                "Ask about the painting":
                    show y 
                    y "It is an interesting work, where did you get the inspiration to paint this?"
                    show char 
                    char "It's nothing special, I just painted what I felt about a...child who could not live as happily as the other ones from here."
                    $ knowledge += 3
                    
                    if museum:
                        menu:
                            "Ask if it's related to the story of the city":
                                show y 
                                y "Is it related to the story if this city?"
                                show char
                                char "Yes, you are right. This child is the \"saviour\" of this city, the descendant of the hero from the story and a relative of mine. In reality he is a scapegoat, the name of our city \"Emissarium\" tells directly about its roots."
                                show y 
                                y "Where is he now?"
                                show char
                                char "He is in the basement...All his life he was treatened miserably, because some dumb spirit said that the sacrifice must suffer lonlyness and all kind of mistreats in order to keep the prosperity of this city at least one soul shows mercy to him, then the city will turn into ruins...So everybody knows about him but don't dare to help him someway. There are people who could not stand the fact that they live off someone else's suffering and leave the city ..."
                                
                                if door:
                                    menu:
                                        "Ask more about the people who leave the city":
                                            show y
                                            y "They left because they saw how poor the child is treated?"
                                            show char
                                            char "Yes, I also wanted to leave the city because i have seen it.."
                                            menu:
                                                "Tell that you saw someone leaving the city":
                                                    show y 
                                                    y "I saw a couple leaving the city when I stayed at the outskirts."
                                                    show char
                                                    char "No-one leaves this city, my father won't allow this city to be discovered. (smiles bitter)"
                                                    menu:
                                                        "Ask where these people go.":
                                                            show y 
                                                            y "Then where they are going to?"
                                                            show char
                                                            char "...The mayor kills all the people who want to leave and make them fertilizers for the poppy field, his beloved garden...He is a mad man who killed my mother, his own wife...and everyone knows about it but never say anything, they always stay silent about such things..."
                                                            "You are in deep shook from [pronoun_1] words."
                                                            show char 
                                                            char " You know...her remains are somewhere in the field, she just wanted to leave and did nothing wrong...(sobs) But she couldn't, even after her death she still here..."

                                                            menu:
                                                                "Help [pronoun_3] leave": ####
                                                                    $ romantic += 1
                                                                    menu: 
                                                                        "Tell that [pronoun_1] has great painting skills":
                                                                            jump Painting_Skills
                                    

                    ######## ADD HERE IF NOT MUSEUM
                      

label Painting_Skills:
    show y 
    y "Wow... you have great painting skills."
    $ romantic += 1
    show char 
    char "Thank you...But, I am sure that you have seen a lot of great art creations in your homeland. (hides [pronoun_1] pain under a smile)"
    "You decide to distract her and tell [pronoun_3] about the art that can be seen outside of the mountains."
    scene bg choose_art
    show y
    y "I see that you are interested in the art outside of this city. Well, let me tell you about..."
    menu:
        "Tell [pronoun_3] about the Renaissance painters.":
            scene bg renaissance
            show y 
            y "...The Renaissance painters."

            "You started to tell [pronoun_3] about the Renaissance painters and sculptures: Sandro Botticelli, Donattelo, Leonardo da Vinci, Michelangelo and Raphael. You took out your phone to show [pronoun_3] some pictures of their works and you noticed that there is no signal. It was expected. Fortunately you had some photos of their artworks from your journeys so you could show them."
            "You see that [pronoun_2] listened to you very attentlively and persorbed all the information you gave to [pronoun_3]."
    
       
        "Tell [pronoun_3] about Vincent van Gogh":
            scene bg art_gogh
            show y 
            y "...the Vincent van Gogh's art."
            "You started to tell [pronoun_3] about the Van Goth's artworks, his style and about his life. You took out your phone to show [pronoun_3] some pictures of his works and you noticed that there is no signal. It was expected. Fortunately, you had some photos of his artworks from your journeys so you could show them."
            "You see that [pronoun_2] listened to you very attentlively and persorbed all the information you gave to [pronoun_3]."
        
        "Tell [pronoun_3] about abstract art":
            scene bg contemp
            show y 
            y "...the absract art."
            "You started to tell [pronoun_3] about the abstract art, that the world can be painted not only as we see it but also how we feel it. You took out your phone to show [pronoun_3] some pictures of the artworks of that kind and you noticed that there is no signal. It was expected. Fortunately, you had some photos of abstract art that ypu have seen in your journeys so you could show them."
            "You see that [pronoun_2] listened to you very attentlively and persorbed all the information you gave to [pronoun_3]."

    "After you are done talking, [pronoun_2] looks at you with a sad expression. "
    show y
    y "What happened?"
    show char
    char "I want to leave this city, it fells like I am inside of a cage. Would it be possible to leave it with you?"
    "You see in [pronoun_1] eyes an imploring glance."
    menu:
        "Ask why [pronoun_2] thinks so":
            show y
            y "Why do you think of this city as a \"cage\", it is safe and beautiful, the outside world is full of danger, wars and different problems."
            
            "A bitter smile appeared on [pronoun_1] face, [pronoun_2] turns [pronoun_1] back at you and pulls the top of [pronoun_1] clothes. You see scars all over [pronoun_1] back."
            "It shooked you."

            menu:
                "Ask where [pronoun_2] got these scars from.":
                    show y
                    y "God, where do you got these scars from?"
                    show char 
                    char "Well, this city is not as perfect as you might think. To be honest, the people here are not as nice as they seem, and the mayor is one of the rottenest of them all.  He beat my mother when she was still alive, and now he beats me..."
                    jump Mayor_Child_Choice

label Mayor_Child_Choice:
    menu:
        "Help [pronoun_3] to leave":
            show y
            y "Yes, I will help you."
            "The mayor's child looks at you with a grateful gaze."
        
        "Tell that the outside world is crueler":
            $ romantic -= 6
            show y 
            y "The outside world is crueler that you might think and it's better to live here. As about the scars, if you don't want to get beaten what about moving to another house?"
            "Your words make [pronoun_3] shudder, [pronoun_2] pulls [pronoun_1] top back and turns your face to you."
            menu:
                "Ask why didn't he just let [pronoun_3] leave.":
                    show char 
                    char "No-one can leave this city...The mayor kills all the people who want to leave and make them fertilizers for the poppy field, his beloved garden...The mayor is a mad man who killed my mother, his own wife everyone knows about it but never say anything, they always stay silent about such things!" 
                    "You are in deep shook from [pronoun_1] words."
                    show char 
                    char "You know...her remains are somewhere in the field, she just wanted to leave and did nothing wrong...(sobs) But she couldn't, even after her death she still here... "
                    "The things turned out very and very bad, you want to leave this city as soon as possible."
                    menu:
                        "Tell [pronoun_3] that you need to leave.":
                            show y 
                            y "I need to leave..."
                            "[mayor_child] wanted to say something but you left quickly [pronoun_1] room in order to save your life."

                            "You got down the stairs, but bumped into someone and fell."
                            "Here was a man."

                            scene bg mayor
                            "He looks at you with disgrace.You noticed two huge men behind him."
                            show cr
                            cr "Mayor, what should we do with this rat?"
                            
                            "The Mayor's gaze is full of venom. "

                            show my 
                            my "I don't think I have seen you before...Take him to the basement. "
                            
                            "The men took you by the shoulders to the basement."

                                                           
                            menu:
                                "Stand up":
                                    jump Basement_Death

                                "Stand still":
                                    jump Basement_Death   


label Basement_Death:
    menu:
    "Oppose":
        "You try to resist, but you are too weak compared to them. "
        scene bg go_basement
        "They locked you in an isolated room in the basement and started releasing some kind of gas into the room. After a while, you began to choke, your lungs were on fire and your mind was going blank...You left this place... taking a one-way ticket out of city, but its price was your life"
        
        "THE END"
        jump try_again_or_give_up





            


label Make_Choice:
    menu:
        "Stay": 
            show y
            y "I would like to stay in this city."
            show my 
            my " This is a wise choice, welcome to our family of citizens. Also, don't worry about where to stay, there is another man who came to the city from the outside world, he has been living for more than 40 years on the northern outskirts. I'm sure he would be happy to take you in. (politely)"
            "He looks at his child looking for support."
            show char
            char "Yeah, he is indeed a very nice man and the north outskirts are a beautiful place to stay."
            " You think about their offer and, having decided to stay, see no reason to change your mind."
            menu:
                "Agree":
                    "Thank you very much, I will do so."
                    jump Agree_Stay

        "Leave":
            show y 
            y "I would like to leave."
            show my
            my "Well, that's sad, but I understand that you are bounded to your roots. At least you could stay here overnight and leave tommorow."
            menu:
                "Agree":
                    "Thank you very much, I will do so."
                    jump Agree_Leave


label Agree_Leave:
    if (alertness >= 6) and (door == True):
        "You woke, tied up in a dark place, you supposed that it is the north cave. You see the old man from the outskirts and the mayor. "
        "The Mayor sees that you've come to your senses."
        show my 
        my " Did you really think you could stick your nose where it doesn't belong and leave this city? No one is allowed to leave, and they will not leave. The ones who are not grateful for the great gifts of this city will face a miserable end, but don't worry, your death will not be in vain (grins). (menacingly)"
        "You look at him perplexed. The fear took you in its claws and you don't understand what is going on."
        my "I hope you have seen my beautiful garden? "
        "You don't understand what he means."
        my "Yes, you did. So, your countribution to the city will be simple, like every other traitor you will lie under the poppy field and your remains will contribute to the city's beauty. (contemptuously) "
        "Things have become really scary, you are in a panic and try to think of a way out."
        menu:
            "Ask the old man for help":
                "The man comes closer to you."
                show om
                om " I told you to not look into things you must not know, but you didn't listen to me. It's such a pity that an another soul will suffer for this place, but i guess this is the price we need to pay for the better life of the majority. (sorrowful)"
                menu:
                    "Ask for mercy":
                        show y 
                        y "I will not tell anybody about this city and will never come back, just let me go. Please... (begging)"
                        show my 
                        "The Mayor laughs."
                        my "Yes, you won't tell a single soul about this city and you'll never come back, because the dead don't talk and don't return. "
                        jump Ending_Knife
                    
                    "Threaten them":
                        show y
                        y "You will pay for this! People from the outside will search for me! (desperate)"
                        "The mayor laughs."
                        show my 
                        my "We've already sealed off the cave you came from, in fact we should have done it a long time ago to prevent intruders like you from finding this place, but better late than never."
                        jump Ending_Knife
    else:
        jump What_Is_Happening

label What_Is_Happening:
    "You woke up in a dark place by being slapped on the face. You see the mayor and  some brutal men behind him."
    menu:
        "What is happening?":
            show my
            my "Did you really think that you could leave this place? We are not so naive to let someone spill our secrets outside the walls."
            "The Mayor addresses to his guys."
            my " Let's welcome our dear guest with some aromatherapy, I heard it's good for relaxation. (mockingly)"
            "The men took you by the shoulders."
            jump Men_Kill


label Men_Kill:
    menu:
        "Oppose":
            "You try to resist, but you are too weak compared to them."
            scene bg basement
            "They locked you in an isolated room in the basement and started releasing some kind of gas into the room. After a while, you began to choke, your lungs were on fire and your mind was going blank...You left this place... taking a one-way ticket out of city, but its price was your life. "

            "THE END"
            jump try_again_or_give_up

label Agree_Stay:
    if knowledge >= 6:
        "The Mayor sends someone to bring the old man and together you go to his house."
        scene bg outsk_house_night
        "The man asks if you want to sleep on the sofa or on the armchair until he gets a bed for you."
        scene bg goutsk_sofa_armchair
        menu:
            "Sleep on the sofa":
                scene bg sofa #####
            "Sleep in the armchair":
                scene bg arm #####
    else:
        "You got escorted by the mayor's child to the guest room and [pronoun_2] wishes you good night. You felt tired from walking all the way, so you fell asleep as soon as your head hit the pillow."
        "Next day, the [mayor_child] accompanied you to the outskirts where you saw a nice house near the mountains. "
        scene bg outsk_man
        "The old man was beaming with happiness, he was very glad to take you in and confessed that he felt very lonely for the past decades because only an outsider could understand his feeling, but until that moment he was the only one. "
        "It's been a few weeks and you've been enjoying them wholeheartedly. Here every day is a holiday, people are always friendly, you don’t have to worry about making money, because there is no monetary system, as if you are in a fairy tale. You miss your friends from the outside but you don't want to go back to the difficulties that you encountered before."
        "There is one thing that makes you think, a strange thing. Sometimes people come to the old man, and he goes with these people to the northern cave to help them leave the city. You don't understand why anyone would want to leave this place, here nobody needs to worry about making a living, there are no wars, any significant conflicts, hunger and pain, it's like a piece of heaven on earth. But sometimes you wonder how the northern cave looks like, is it the same like the southern one or looks different?"
        
        menu:
            "Ask the old man about the cave":
                "You approach the old man."
                show y
                y "Where does the northern cave lead? Is it the same as the one through that I came here?"
                show om 
                om "It leads to the outside world as the one you came through."
                show y 
                y "Could you lead me there?"
                show om 
                om "You made a promise to the mayor that you would not leave the city, therefore, in order not to lose his trust, I advise you not to delve into this issue either. Live here happily, as before, in these few weeks. (sorrowful)"
                "You were surprised that this simple question would cause such reaction."
                scene bg cave_noCave
                menu:
                    "Never Go to the cave":
                        scene bg never_north_cave
                        "You decided to follow the old man's advice. He lived here for a long time and knows better that will be good for you, also you really don't want to loose the mayor's trust."
                        scene bg city_le
                        "Your life in this city goes on, you have adapted well to this environment, people have begun to sympathize with you and often invite you to parties or ask you for help. You feel like a real citizen of this city, as if there was no life before it. "
                        "Sometimes you missed your old days when you traveled around the world, but what if you did all this journey just to get here? What if this place is your destiny?"
                        "It seems so."

                        # INSERT LATER AN IMAGE

                        "The End."
                        jump try_again_or_give_up

                    "Take a look at the cave when the man falls asleep.":
                        scene bg north_cave
                        "It's midnight, the man came back after accompanying some people to the northern cave and shortly falls asleep in his room."
                        "You took the lantern that the old man left on the table and headed towards the cave. You started to delve into it. It didn't seem special at all compared to the one that you entered before. Well, it didn't until you started hearing screams, you wanted to turn around and leave this place immediately, but you were knocked down by a blow to the head. "
                        ##### INSERT IMAGE
                        "You woke, tied up in a dark place, you supposed that it is the north cave. You see the old man from the outskirts and the mayor. "
                        "The Mayor sees that you've come to your senses."
                        show my 
                        my "Did you really think you could stick your nose where it doesn't belong and leave this city? No one is allowed to leave, and they will not leave. The ones who are not grateful for the great gifts of this city will face a miserable end, but don't worry, your death will not be in vain (grins). (menacingly)"
                        "You look at him perplexed. The fear took you in its claws and you don't understand what is going on."
                        my "I hope you have seen my beautiful garden?"
                        " You don't understand what he means."
                        my "Yes, you did. So, your countribution to the city will be simple, like every other traitor you will lie under the poppy field and your remains will contribute to the city's beauty. (contemptuously)"
                        "Things have become really scary, you are in a panic and try to think of a way out."
                        menu:
                            "Ask the old man for help":
                                "The man comes closer to you."
                                show om
                                om " I told you to not look into things you must not know, but you didn't listen to me. It's such a pity that an another soul will suffer for this place, but i guess this is the price we need to pay for the better life of the majority. (sorrowful)"
                                menu:
                                    "Ask for mercy":
                                        show y 
                                        y "I will not tell anybody about this city and will never come back, just let me go. Please... (begging)"
                                        show my 
                                        "The Mayor laughs."
                                        my "Yes, you won't tell a single soul about this city and you'll never come back, because the dead don't talk and don't return. "
                                        jump Ending_Knife
                                   
                                    "Threaten them":
                                        show y
                                        y "You will pay for this! People from the outside will search for me! (desperate)"
                                        "The mayor laughs."
                                        show my 
                                        my "We've already sealed off the cave you came from, in fact we should have done it a long time ago to prevent intruders like you from finding this place, but better late than never."
                                        jump Ending_Knife

    label Ending_Knife:
        # INSERT IMAGE 
        "The mayor pulls a knife from his belt and stabs you several times in the chest. You feel your soul being torn to pieces with every blow. Your blood colors the floor red, it was the same as the color of the poppy field that you saw entering the city ... It becomes very cold, life leaves your body with every breath to the last one."
        # INSERT IMAGE 
        "THE END"
        jump try_again_or_give_up















label City_Left(dialogue=""):
    if dialogue == "":
        "Here you see a woman who sells different types of food and a painter with a sad expression on his face."
        # Assuming interactions or choices would be placed here
    return

label outskirts:
    "After some time you find a house near the mountains."
    if not mountain_house_visited:
        jump old_man_visited
    else:
        "This path leads to the old man's house. He won't tell me anything else anymore."
        menu:
            "Go back":
                jump City

label old_man_visited:
    "You've already visited the old man. It seems he has nothing more to tell you."
    $ mountain_house_visited = True
    jump City

label try_again_or_give_up:
    scene bg game_over
    "This is the end of your journey..."
    menu:
        "Try Again":
            jump character_select
        "Give Up":
            scene bg game_over
            return
