# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
$ import os

define g = Character("Prof  Lema", color="#000000")
define r = Character("Rizzsa", color="#FF7F50")
define j = Character("Jisa", color="#ffe155")
define t = Character("Telia", color="#DFFF00")
define c = Character("Christopher", color="#80CBC4")

define slightleft = Position(xalign=0.25, yalign=1.0)
define slightright = Position(xalign=0.75, yalign=1.0)

init:
    $ define.move_transitions('slide', 0.5, subpixel=True)

transform offRight:
    linear 10.0 xalign 20.0
 
image telia_blink:
    "telia"
    1
    "telia eclosed"
    0.15
    repeat

image telia_blink2:
    "telia"
    0.15
    "telia speak"
    1
    "telia eclosed"
    0.15
    repeat

image christopher_blink:
    "christopher"
    1
    "christopher eclosed"
    0.15
    repeat

image rizzsa_blink:
    "rizzsa"
    1
    "rizzsa eclosed"
    0.15
    repeat

image rizzsa_speak:
    "rizzsa"
    0.15
    "rizzsa speak"
    0.1
    "rizzsa"
    0.2
    "rizsa speak"
    0.1
    repeat

image jisa_blink:
    "jisa"
    1
    "jisa eclosed"
    0.15
    repeat

image jisa_speak:
    "jisa"
    0.2
    "jisa concerned speak"
    0.15
    "jisa"
    0.25
    "jisa concerned speak"
    0.2
    repeat

image prof_blink:
    xalign 0.5
    yalign 0.6
    zoom 2.5
    "prof"
    1.5
    "prof eclosed"
    0.15
    repeat

image prof_blink2:
    "prof provoke"
    1.5
    "prof eclosed2"
    0.15
    repeat

image mov_line = Movie(size=(1920, 1080), play= "images/Bg/line art animation 720.webm", loop=-1)
image mov_shape = Movie(size=(1920, 1080), play= "images/Bg/shapes1.webm", loop=-1)
image mov_kindsline = Movie(size=(1920, 1080), play= "images/Bg/kinds of line.webm", loop=-1)
image mov_classshape = Movie(size=(1920, 1080), play= "images/Bg/classification of shapes.webm", loop=-1)
image mov_orgshape = Movie(size=(1920, 1080), play= "images/Bg/organic shape.webm", loop=-1)
image mov_form1 = Movie(size=(1920, 1080), play= "images/Bg/form1.webm", loop=-1)
image mov_space = Movie(size=(1920, 1080), play= "images/Bg/space.webm", loop=-1)
image mov_space2 = Movie(size=(1920, 1080), play= "images/Bg/space2.webm", loop=-1)
image mov_color = Movie(size=(1920, 1080), play= "images/Bg/color.webm", loop=-1)
image mov_colorharmony = Movie(size=(1920, 1080), play= "images/Bg/color harmony.webm", loop=-1)
image mov_colorwheel = Movie(size=(1920, 1080), play= "images/Bg/color wheel.webm", loop=-1)
image mov_colorscheme = Movie(size=(1920, 1080), play= "images/Bg/color scheme.webm", loop=-1)
image mov_psycolors = Movie(size=(1920, 1080), play= "images/Bg/psy colors.webm", loop=-1)
image mov_value = Movie(size=(1920, 1080), play= "images/Bg/value.webm", loop=-1)
image mov_texture = Movie(size=(1920, 1080), play= "images/Bg/texture.webm", loop=-1)
image mov_principles = Movie(size=(1920, 1080), play= "images/Bg/principles of art and design.webm", loop=-1)
image mov_artcritic = Movie(size=(1920, 1080), play= "images/Bg/art critic.webm", loop=-1)


define mypos = Position(xalign=0.5, yalign=-0.01)

# The game starts here.

label start:

    stop music
    scene black
    
    # The phrase in the brackets is the text that the game will display to prompt 
    # the player to enter the name they've chosen.

    $ player_name = renpy.input("Input your name")

    $ player_name = player_name.strip()
    # The .strip() instruction removes any extra spaces the player 
    # may have typed by accident.

    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
    if player_name == "":
        $ player_name="LeBron James"
    # Now the other characters in the game can greet the player.
    player_name "!!!"
    play sound "audio/sfx/school bell.mp3" volume 0.5
    scene bg classroom
    play music "audio/bgm/school ambience.mp3" volume 0.5
    with fade
    player_name "What a crazy dream, I thought that monster was going to eat me"
    show prof_blink with dissolve
    g "Class dismmised, and here are the results of your midterm exam"
    hide prof_blink with dissolve
    player_name "Finally the class is over, this subject is exhausting"
    menu:
        "Check the results":
            show f test paper at center:
                zoom 0.8
                yalign 0.2
            play sound "<from 3 to 4>audio/sfx/paper.mp3"
            "{size=60}{color=#f00}F{/color}{/size}"
            hide f test paper with dissolve
    player_name "OH NO!!! HOW CAN I BE THIS SUPID. I'm going to fail"
    show prof_blink2 at center:
        xalign 0.5
        yalign 0.6
        zoom 2.5
    g "You should have studied harder, %(player_name)s"
    g "That's it for you if fail again in the next exam, you'll lose your scholarship"
    g "Maybe art is not just for everyone"
    g "At this rate you need a miracle to pass my class"
    hide prof_blink2 with dissolve
    player_name "I-I c-c-can't let that happen, I need to find a way to pass this class"
    stop music fadeout 2.0
    jump quadrangle

label quadrangle:

    scene bg quadrangle
    with fade
    play music "audio/bgm/Midsummer Cat.mp3" fadein 1.0 volume 0.25
    player_name "Am I really going to fail?"
    player_name "If only there's a miracle that could help me pass this class"
    play sound "<from 0.25>audio/sfx/wind.mp3" volume 1.0
    with hpunch
    menu:
        "Pick up the poster":
            show club poster:
                yalign 3.0
            play sound "<from 1 to 1.75>audio/sfx/paper.mp3"
            show club poster at center with moveouttop:
                yalign 0.25
                zoom 0.3
    player_name "What's this? Fine Arts & Creative Knowledge Club???"
    player_name "Art club huh... This university has an ART CLUB!!! that's news to me"
    player_name "Maybe this is a sign, I should give it a try"
    player_name "I'll do anything to pass this class"
    hide club poser with dissolve
    stop music fadeout 2.0
    menu:
        "Go to the art club":
           jump art_corridor

label art_corridor:
    scene bg art corridor
    with fade
    play music "audio/bgm/school ambience.mp3" volume 0.25 fadein 1.0
    player_name "Is this the art club? It surely doesn't look like one"
    show jisa at center:
        xalign 0.5
        yalign -0.01
    play sound "audio/sfx/FootStep.mp3" volume 0.6
    show jisa worried at right with moveoutright:
        yalign -0.01
    "..."
    play sound "audio/sfx/FootStep.mp3" volume 0.8
    show jisa determined at left with slide:
        yalign -0.01
    ".................."
    play sound "<from 1.0 to 3.0>audio/sfx/FootStep.mp3" volume 1.0
    show jisa curious at center with moveinleft:
        yalign -0.01
    "!!!"
    play sound "audio/sfx/Respond.mp3"
    show jisa speak at center:
        xalign 0.5
        yalign -0.01
        ease 0.5 zoom 2
    j "Hey there, are you interested to join the art club? {size=-10}I knew those posters would work{/size}"
    stop music
    menu:
        "Do I want to join the art club?"
        "Yes, I am here to join the art club":
            # show at right with moveoutright
            show jisa happy
            play sound "audio/sfx/Twinkle.mp3"
            j "YAYYYYY!!! I knew it, Follow me"
            play sound "audio/sfx/Run.mp3"
            show jisa happy at offRight with ease
            "..."
            jump art_club
        "Hell no, I'd rather die than join your stupid club":
            show jisa sad
            j "Y-You don't have to be that mean"
            show jisa cry
            ""
            jump death_ending

label art_club:

    scene bg art club:
        zoom 2
    with fade
    play music "audio/bgm/Midsummer Cat.mp3" fadein 1.0 volume 0.25
    show jisa_blink:
        xalign 0.5
        yalign -0.01
        zoom 2
    j "Hello I'm Jisa"
    j "What is your name?"
    menu:
        "My name is %(player_name)s":
            player_name "My name is %(player_name)s"
        "My name is LeBron James":
            player_name "My name is LeBron James"
            j "I saw your ID you know"
    j "Nice meeting you, %(player_name)s"
    j "Welcome Fine Arts & Creative Knowledge Club"
    j "Or the F.A.C.K. Club for short"
    j "I'm the secretary of this club"
    hide jisa_blink with dissolve
    play sound "audio/sfx/Respond.mp3"
    show rizzsa_blink at center:
        xalign 0.5
        yalign 0.25
        zoom 1.2
    r "Hey, is this the new recruit?"
    j "This is Rizzsa, our club president"
    hide rizzsa_blink with dissolve
    play sound "audio/sfx/Twinkle.mp3"
    show telia_blink at center with dissolve:
        xalign 0.5
        yalign 0.01
        zoom 1.5
    t "Hello there, it's nice having new face around"
    j "And this is Telia, our club Vice president"
    hide telia_blink with dissolve
    play sound "audio/sfx/Respond.mp3"
    show christopher_blink at center with dissolve:
        yalign 0.3
        zoom 1
    c "Yo!"
    j "And this is Christopher, our club... uhhh... {size=-10}I don't know what he does{/size}"
    hide christopher_blink with dissolve
    show rizzsa with dissolve:
        xalign 0.25
        yalign 1.0
        zoom 1.0
    show telia with dissolve:
        xalign 0.01
        yalign -1.0
        zoom 0.9
    show jisa with dissolve:
        xalign 0.95
        yalign 2.0
        zoom 0.9
    show christopher with dissolve:
        xalign 0.75
        yalign 0.5
        zoom 0.9
    r "We are the members of the F.A.C.K. Club"
    hide telia with dissolve
    hide jisa with dissolve
    hide christopher with dissolve
    show rizzsa eclosed at center with moveoutright:
        ease 0.5
    hide rizzsa eclosed
    show rizzsa_blink
    r "It's a surprise that we are still relevant in this university"
    r "Just to give you a hint, our club doesn't receive that much of a budget"
    r "But we are still able to make it work, and make an impact on the university"
    r "So tell me %(player_name)s, why do you want to join the F.A.C.K club?"
    hide rizzsa_blink with dissolve
    menu:
        "Answer the honestly":
            player_name "I am desperate to pass my art class, and I think joining this club will help me"
            player_name "I don't want to lose my scholarship"
            player_name "I want to have a good future, and reach my dreams"
            player_name "I will do anything to prove my worth to this club"
        "Answer sarcastically":
            player_name "I'm just here for the free food and a sleeping quarter"
            player_name "It's nothing serious"
            show rizzsa annoyed
            r "I like your sense of humor, but we don't have any food"
            r "If you're just here to make fun of our club, I don't think I can accept you"
            r "Our club was made to create, appreciate, and learn more about all types of art"
            r "Now..."
            show rizzsa speak
            r "{size=80}Begone{/size} and never come back again"
            jump death_ending
    show rizzsa eclosed
    r "I appreciate your honesty, our club is full of people who are capable in helping you learn anything about arts"
    show rizzsa
    r "But first, I want to know if you are truly enthusiatic and interested in arts"
    hide rizzsa with dissolve
    menu:
        "Yes":
            player_name "Yes, I am willing to learn more about art so that I could appreciate it"
        "No":
            player_name "You know what I change my mind"
            player_name "This club sucks, and you are all super cringe"
            player_name "See you losers"
            jump death_ending
    show rizzsa smile
    r "That's all I need to know"
    show rizzsa
    r "Come in lets start learning"
    hide rizzsa with dissolve
    stop music fadeout 1.0
    jump lessons
    
label lessons:
    scene bg art club 2
    with fade
    play music "audio/bgm/OST 50. Hue.mp3" fadein 1.0 volume 0.25
    show rizzsa_blink
    r "Now, what do you want to learn?"
    hide rizzsa_blink with dissolve
    menu:
        "I want to learn about..."
        "The Elements of Visual Arts":
            player_name "I can't get The Elements of Visual Arts into my mind"
            show rizzsa_blink
            r "I see this one is a bit complicated, what specific concept about this you have troubles undestanding"
            hide rizzsa_blink with dissolve
            menu:
                "Elements of Visual Arts: Line":
                    player_name "I want to learn about Lines"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_line
                "Functions of Line":
                    player_name"I want to learn about the Functions of Line"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_functions_line
                "Kinds of Lines":
                    player_name "I want to learn about the Kinds of Lines"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_kinds_line
                "Elements of Visual Arts: Shape":
                    player_name "I want to learn about Shapes"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_shape
                "Classification of Shapes":
                    player_name "I want to learn about the Classification of Shapes"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_classification_shapes
                "Form":
                    player_name "I want to learn about Form"
                    show telia_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 1.5                        
                    t "I know that one, let me help you"
                    jump lesson_form
                "Space":
                    player_name "I want to learn about Space"
                    show telia_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 1.5  
                    t "I know that one, let me help you"
                    jump lesson_space
                "Color":
                    player_name "I want to learn about Color"
                    show telia_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 1.5  
                    t "I know that one, let me help you"
                    jump lesson_color
                "Color Harmony":
                    player_name "I want to learn about Color Harmony"
                    show telia_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 1.5  
                    t "I know that one, let me help you"
                    jump lesson_color_harmony
                "Color Scheme":
                    player_name "I want to learn about Color Scheme"
                    show rizzsa_blink with dissolve
                    r "I guess its my turn to teach you, come with me"
                    hide rizzsa_blink with dissolve
                    jump lesson_color_scheme
                "Psychology of Colors":
                    player_name "I want to learn about the Psychology of Colors"
                    show rizzsa_blink with dissolve
                    r "I guess its my turn to teach you, come with me"
                    hide rizzsa_blink with dissolve
                    jump lesson_psychology_colors
                "Value":
                    player_name "I want to learn about the Value"
                    show rizzsa_blink with dissolve
                    r "I guess its my turn to teach you, come with me"
                    hide rizzsa_blink with dissolve
                    jump value
                "Texture":
                    player_name "I want to learn about the Texture"
                    show rizzsa_blink with dissolve
                    r "I guess its my turn to teach you, come with me"
                    hide rizzsa_blink with dissolve
                    jump lesson_texture
                "Elements of Visual Arts: Line":
                    player_name "I want to learn about Lines"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_line
                "Functions of Line":
                    player_name"I want to learn about the Functions of Line"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_functions_line
        "Kinds of Lines":
            player_name "I want to learn about the Kinds of Lines"
            show jisa_blink with dissolve:
                xalign 0.5
                yalign -0.01
                zoom 2
            j "Hey, I can help you with that one"
            jump lesson_kinds_line
        "Principles of Principles of Art and Design":
            player_name "I want to know more about Principles of Art and Design"
            show rizzsa with dissolve
            r "I see, I think Christopher can help you with that one"
            hide rizzsa
            show christopher sweat:
                    yalign 0.3
                    xalign 0.5
            c "Me???"
            show christopher wink
            c "Ok fine... follow me I'll teach you everything about it"
            jump principles_of_art
        "Artistic Criticism":
            player_name "I am having a hard time understanding Artistic Criticism"
            show rizzsa smile
            r "Ohh... That one would be easy for Christopher"
            hide rizzsa
            show christopher wink at center:
                yalign 0.3
            c "Sure, I kinda like this topic"
            show christopher smile
            c "Follow me, lets criticize some art"
            jump art_criticism

label lessons_2:

    scene bg art club 2
    with fade
    play music "audio/bgm/OST 50. Hue.mp3" fadein 1.0 volume 0.25
    show rizzsa_blink
    r "Anything else you wanna learn?"
    hide rizzsa_blink with dissolve
    menu:
        "I want to learn about..."
        "The Elements of Visual Arts":
            player_name "I can't get The Elements of Visual Arts into my mind"
            show rizzsa_blink with dissolve
            r "I see this one is a bit complicated, what specific concept about this you have troubles undestanding"
            hide rizzsa_blink with dissolve
            menu:
                "Elements of Visual Arts: Line":
                    player_name "I want to learn about Lines"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_line
                "Functions of Line":
                    player_name"I want to learn about the Functions of Line"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_functions_line
                "Kinds of Lines":
                    player_name "I want to learn about the Kinds of Lines"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_kinds_line
                "Elements of Visual Arts: Shape":
                    player_name "I want to learn about Shapes"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_shape
                "Classification of Shapes":
                    player_name "I want to learn about the Classification of Shapes"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_classification_shapes
                "Form":
                    player_name "I want to learn about Form"
                    show telia_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 1.5                    
                    t "I know that one, let me help you"
                    jump lesson_form
                "Space":
                    player_name "I want to learn about Space"
                    show telia_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 1.5  
                    t "I know that one, let me help you"
                    jump lesson_space
                "Color":
                    player_name "I want to learn about Color"
                    show telia_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 1.5  
                    t "I know that one, let me help you"
                    jump lesson_color
                "Color Harmony":
                    player_name "I want to learn about Color Harmony"
                    show telia_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 1.5  
                    t "I know that one, let me help you"
                    jump lesson_color_harmony
                "Color Scheme":
                    player_name "I want to learn about Color Scheme"
                    show rizzsa_blink with dissolve
                    r "I guess its my turn to teach you, come with me"
                    hide rizzsa_blink with dissolve
                    jump lesson_color_scheme
                "Psychology of Colors":
                    player_name "I want to learn about the Psychology of Colors"
                    show rizzsa_blink with dissolve
                    r "I guess its my turn to teach you, come with me"
                    hide rizzsa_blink with dissolve
                    jump lesson_psychology_colors
                "Value":
                    player_name "I want to learn about the Value"
                    show rizzsa_blink with dissolve
                    r "I guess its my turn to teach you, come with me"
                    hide rizzsa_blink with dissolve
                    jump value
                "Texture":
                    player_name "I want to learn about the Texture"
                    show rizzsa_blink with dissolve
                    r "I guess its my turn to teach you, come with me"
                    hide rizzsa_blink with dissolve
                    jump lesson_texture
                "Elements of Visual Arts: Line":
                    player_name "I want to learn about Lines"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_line
                "Functions of Line":
                    player_name"I want to learn about the Functions of Line"
                    show jisa_blink with dissolve:
                        xalign 0.5
                        yalign -0.01
                        zoom 2
                    j "Hey, I can help you with that one"
                    jump lesson_functions_line
        "Kinds of Lines":
            player_name "I want to learn about the Kinds of Lines"
            show jisa_blink with dissolve:
                xalign 0.5
                yalign -0.01
                zoom 2
            j "Hey, I can help you with that one"
            jump lesson_kinds_line
        "Principles of Principles of Art and Design":
            player_name "I want to know more about Principles of Art and Design"
            show rizzsa with dissolve
            r "I see, I think Christopher can help you with that one"
            hide rizzsa
            show christopher sweat:
                    yalign 0.3
                    xalign 0.5
            c "Me???"
            show christopher wink
            c "Ok fine... follow me I'll teach you everything about it"
            hide christopher wink
            jump principles_of_art
        "Artistic Criticism":
            player_name "I am having a hard time understanding Artistic Criticism"
            show rizzsa smile
            r "Ohh... That one would be easy for Christopher"
            hide rizzsa
            show christopher wink at center:
                yalign 0.3
            c "Sure, I kinda like this topic"
            show christopher smile
            c "Follow me, lets criticize some art"
            jump art_criticism
        "I think I'm ready":
            stop music
            player_name "I think I'm ready"
            player_name "I'm grateful for all of your help"
            player_name "I feel like I can ace my art appreciation exam now, no matter how hard it is"
            show rizzsa smile with dissolve
            play sound "audio/sfx/Respond.mp3"
            r "I see I'll wish you luck on your exam then"
            hide rizzsa
            show telia smile with dissolve:
                xalign 0.5
                yalign -0.01
                zoom 1.5
            play sound "audio/sfx/Twinkle.mp3"          
            t "Me too, Good luck on you exam"
            hide telia
            show jisa determined with dissolve:
                xalign 0.5
                yalign -0.01
                zoom 2
            play sound "audio/sfx/Twinkle.mp3"
            j "Good luck, and Give it your best %(player_name)s"
            hide jisa
            show christopher smile at center with dissolve:
                yalign 0.3
            play sound "audio/sfx/Respond.mp3"
            c "Good luck I guess, at least don't forget what I taught you"
            hide christopher
            jump ending

label lesson_line:
    stop music
    scene bg line with fade
    show jisa with dissolve:
        xalign 0.5
        yalign -0.01
        zoom 2
    j "Hello"
    show jisa eclosed at mypos
    j "This lesson is about..."
    show jisa concerned speak at mypos
    j "Elements of Visual Arts: Line"
    show jisa at left with moveoutleft:
        yalign 0.01
    j "Ahem"
    hide jisa with dissolve
    show mov_line at center with dissolve
    show jisa speak at left with dissolve:
        yalign -0.25
        zoom 1.2
    voice line
    j "Line is the strongest and most important and influential."

    voice sustain
    j "Without line, there can be no shape. Without shape, there can be no form. Without form, there can be no texture and there can be no pattern."
    
    voice sustain 
    j "Line can be considered as the oldest, simplest, and universal element for creating visual arts."

    show jisa at mypos with moveoutright
    j "I hope this brief explanation helps you"
    
    stop voice
    jump lessons_2

label lesson_functions_line:
    stop music
    scene bg line2 with fade:
        zoom 1.2
    show jisa with dissolve:
        xalign 0.5
        yalign -0.01
        zoom 2
    j "Hello"
    show jisa eclosed at mypos
    j "This lesson is about..."
    show jisa concerned speak at mypos
    j "Functions of Line"
    show jisa at left with moveoutleft:
        yalign 0.01
    j "Ahem"
    hide jisa with dissolve
    show jisa speak at left with dissolve:
        yalign -0.25
        zoom 1.2
    play sound ("<from 1>audio/voice/functions of line.mp3")
    j "There are several functions of line. It includes"
    voice sustain
    show outline with moveinbottom:
        zoom 0.8
        xalign 0.5
        yalign 0.25
        ease 0.25
    j "{size=40}{b} Outline and Form {/b}{/size}"
    voice sustain
    show movement with moveinleft:
        zoom 1.5
        xalign 0.5
        yalign 0.25
        ease 0.25
    j "{size=40}{b} Movement and Emphasis {/b}{/size}"
    voice sustain
    show patterns with moveintop:
        zoom 1.5
        xalign 0.5
        yalign 0.25
        ease 0.25
    j "{size=40}{b} Pattern and Texture {/b}{/size}"
    voice sustain
    show shading with moveinright:
        zoom 2
        xalign 0.5
        yalign 0.25
        ease 0.25    
    j "{size=40}{b} Shading and Modeling {/b}{/size}"
    hide outline with dissolve
    hide movement with dissolve
    hide patterns with dissolve
    hide shading with dissolve
    stop sound
    show jisa at mypos with moveoutright
    j "I hope this brief explanation helps you"
    
    jump lessons_2

label lesson_kinds_line:
    stop music
    scene bg line with fade
    show jisa with dissolve:
        xalign 0.5
        yalign -0.01
        zoom 2
    j "Hello"
    show jisa eclosed at mypos
    j "This lesson is about..."
    show jisa concerned speak at mypos
    j "Kinds of Line"
    show jisa at left with moveoutleft:
        yalign 0.01
    j "Ahem"
    hide jisa
    show jisa speak at left with dissolve:
        yalign -0.25
        zoom 1.2
    play sound ("audio/voice/kinds of line.mp3")
    j "Lines are categorized into five. We have vertical, horizontal, diagonal, curved and jagged lines."
    hide jisa
    play sound ("audio/voice/horizontal lines.mp3")
    show mov_kindsline with dissolve
    show jisa speak at left with dissolve:
        yalign -0.25
        zoom 1.2
    j "{b}Horizontal Line{/b} - is basically associated with rest and repose. It suggests serenity and quietness, relaxation and reflection, as well as stability and inaction. Landscape often impart a feeling of tranquility because of the supremacy of horizontal line."
    play sound ("audio/voice/vertical lines.mp3")
    j "{b}Vertical Lines{/b} - depict power and strength, stability, simplicity, poise or stature, and dynamism.  It also motivates certain emotions or even sentiments, a deeper sense of adoration and praise."
    play sound ("audio/voice/diagonal lines.mp3")
    j "{b}Diagonal Lines{/b} - are lines of action and movement. It also suggests impulse, will power, aspiration, passion, and emotion. Almost all artworks that suggest actions, are assumed to have diagonal lines."
    play sound ("audio/voice/curved lines.mp3")
    j "{b}Curved Lines{/b} - are considered as \"line of grace, and line of beauty\". It is associated with smooth movements like a graceful dance or a simple smile. It implies softness, and flexibility."
    play sound ("audio/voice/jagged lines.mp3")
    j "{b}Jagged Lines{/b} - are associated with pointed and sharp objects that signify difficulty and discomfort. They also show violence, torture, confusion, and conflict."
    
    stop sound
    show jisa at mypos with moveoutright
    j "I hope this brief explanation helps you"
    
    jump lessons_2

label lesson_shape:
    stop music
    scene bg shapes1 with fade
    show jisa with dissolve:
        xalign 0.5
        yalign -0.01
        zoom 2
    j "Hello"
    show jisa eclosed at mypos
    j "This lesson is about..."
    show jisa concerned speak at mypos
    j "Elements of Visual Arts: Shape"
    show jisa at left with moveoutleft:
        yalign 0.01
    j "Ahem"
    hide jisa with dissolve
    show mov_shape with dissolve
    show jisa speak at left with dissolve:
        yalign -0.25
        zoom 1.2
    
    play sound ("audio/voice/shape.mp3")
    j "Shape is an enclosed area or surface."

    voice sustain
    j "It can be easily identified because when a line crosses itself or intersects with other lines, it creates a shape."
    
    voice sustain 
    j "Shape is the principal element of identification. Shape is responsible in creating the subject in art even representational or abstract art."

    voice sustain
    j "Shape is responsible in creating the subject in art even representational or abstract art."

    voice sustain
    j "Shape can be two-dimensional and can be three-dimensional."

    stop sound
    show jisa at mypos with moveoutright
    j "I hope this brief explanation helps you"
    
    stop voice
    jump lessons_2  

label lesson_classification_shapes:
    stop music
    scene bg shapes2 with fade:
        zoom 0.75
    show jisa with dissolve:
        xalign 0.5
        yalign -0.01
        zoom 2
    j "Hello"
    show jisa eclosed at mypos
    j "This lesson is about..."
    show jisa concerned speak at mypos
    j "Classification of shapes"
    show jisa at left with moveoutleft:
        yalign 0.01
    j "Ahem"
    hide jisa with dissolve
    show mov_classshape
    show jisa speak at left with dissolve:
        yalign -0.25
        zoom 1.2
    play sound ("audio/voice/classification of shapes.mp3")
    j "There are two classifications of shape: geometric and organic shape."
    voice sustain
    j "{b}Geometric Shape{/b} origin came from mathematical perspective. It includes Circles, Squares, rectangles and triangles. We see them in architecture and manufactured items. Geometric shape can be Rectilinear or Curvilinear."
    hide jisa speak
    show mov_orgshape
    show jisa speak at left with dissolve:
        yalign -0.25
        zoom 1.2
    voice sustain 
    j "{b}Organic or Biomorphic Shape{/b} we see them in nature and with characteristics that are free-flowing, informal and irregular. These shapes are derived from any living organisms. Trees, flowers, birds, fishes and even sea shells are organic shapes."

    stop sound
    show jisa at mypos with moveoutright
    j "I hope this brief explanation helps you"
    
    stop voice
    jump lessons_2     

label lesson_form:
    stop music
    scene bg form with fade
    show telia smile with dissolve:
        xalign 0.5
        yalign -0.01
        zoom 1.5
    t "Mmm… Morning…"
    show telia eclosed at mypos
    t "I'll teach you about..."
    show telia speak at mypos
    t "Form"
    show telia at left with moveoutleft:
        yalign 0.01
    t "ahem..."
    hide telia with dissolve
    show mov_form1 with dissolve
    show telia speak at left with dissolve:
        xalign -0.05
        yalign -0.25
        zoom 1.1
    play sound ("<from 3>audio/voice/form.mp3")
    t "Form is the structure and shape of an object, giving it a recognizable design."

    voice sustain
    t "In visual arts, form includes size, height, width, and volume, creating a sense of weight."
    show mona lisa with moveinbottom:
        xalign 0.5
        yalign 0.4
        zoom 2
    voice sustain 
    t "In two-dimensional art like painting, form is shown using perspective, shading, and modeling."
    show david with moveintop:
        xalign 0.5
        yalign 0.4
        zoom 0.6
    voice sustain
    t "In three-dimensional art, like sculpture and architecture, form is physically present."
    hide mona lisa
    hide david
    stop sound
    show telia smile at mypos with moveinright
    t "Well... I hope your learned something, see you again"
    
    stop voice
    jump lessons_2

label lesson_space:
    stop music
    scene bg space with fade:
        zoom 0.75
    show telia smile with dissolve:
        xalign 0.5
        yalign -0.01
        zoom 1.5
    t "Mmm… Morning…"
    show telia eclosed at mypos
    t "I'll teach you about..."
    show telia speak at mypos
    t "Space"
    show telia at left with moveoutleft:
        yalign 0.01
    t "ahem..."
    hide telia with dissolve
    show mov_space2 with dissolve
    show telia speak at left with dissolve:
        xalign -0.05
        yalign -0.25
        zoom 1.1
    play sound "<from 1>audio/voice/space.mp3"
    t "Space refers to the area within, around, or between objects in an artwork."

    show telia eclosed
    voice sustain
    t "It creates depth and distance, divided into foreground, middle ground, and background."
    
    show telia speak
    voice sustain 
    t "Positive space is filled with objects or colors, while negative space is the empty area."
    show telia eclosed
    voice sustain
    t "Both work together to create balance and visual interest."

    stop sound
    show telia smile at mypos with moveinright
    t "Well... I hope your learned something, see you again"
    
    stop voice
    jump lessons_2

label lesson_color:
    stop music
    scene bg color with fade:
        zoom 0.8
    show telia smile with dissolve:
        xalign 0.5
        yalign -0.01
        zoom 1.5
    t "Mmm… Morning…"
    show telia eclosed at mypos
    t "I'll teach you about..."
    show telia speak at mypos
    t "Color"
    show telia at left with moveoutleft:
        yalign 0.01
    t "ahem..."
    hide telia with dissolve
    show mov_color with dissolve
    show telia speak at left with dissolve:
        xalign -0.05
        yalign -0.25
        zoom 1.1
    play sound "<from 1.5>audio/voice/colors.mp3"
    t "Color is one of the most expressive elements of art, produced by light reflecting off objects. It has three properties"
    show telia eclosed
    voice sustain
    t "{b}Hue{/b} The name of the color (e.g, red, blue)"
    show telia speak
    voice sustain 
    t "{b}Value{/b} The lightness or darkness of a hue."

    voice sustain
    t "{b}Intensity{/b} The brightness or dullness of a color."
    show telia eclosed
    voice sustain
    t "Colors are classified into primary (red, blue, yellow), secondary (green, orange, violet), and intermediate (red-orange, blue-green)."
    voice sustain
    show telia speak
    t "Warm colors (red, yellow, orange) evoke energy and seem to advance, while cool colors (blue, green, violet) suggest calmness and appear to recede."

    stop sound
    show telia smile at mypos with moveinright
    t "Well... I hope your learned something, see you again"

    jump lessons_2

label lesson_color_harmony:
    stop music
    scene bg color harmony with fade:
        zoom 0.8
    show telia smile with dissolve:
        xalign 0.5
        yalign -0.01
        zoom 1.5
    t "Mmm… Morning…"
    show telia eclosed at mypos
    t "I'll teach you about..."
    show telia speak at mypos
    t "Color Harmony"
    show telia at left with moveoutleft:
        yalign 0.01
    t "ahem..."
    hide telia with dissolve
    show mov_colorharmony with dissolve
    show telia speak at left with dissolve:
        xalign -0.05
        yalign -0.25
        zoom 1.1 
    play sound "<from 2>audio/voice/color harmony.mp3"
    t "When it comes to Color Harmony it is the pleasing arrangement of colors, creating balance and visual appeal."
    voice sustain
    t "Different color schemes, like complementary or analogous, help achieve this harmony."
    stop sound
    show telia smile at mypos with moveinright
    t "Well... I hope your learned something, see you again"

    jump lessons_2

label lesson_color_scheme:
    stop music
    scene bg color scheme with fade
    show rizzsa_blink
    r "Greetings"
    r "Today I'll teach you everything you need to know about..."
    hide rizzsa_blink
    show rizzsa speak
    r "Color Scheme"
    show rizzsa
    r "ahem, excuse me"
    hide rizzsa speak with dissolve
    show mov_colorwheel with dissolve
    play sound "audio/voice/r voice/When you look.mp3"
    r """
    When you look at a color wheel different formulas can be formed
    
    The Color Scheme has 6 formulas namely
    
    {b}Complementary, Analogous, Triadic, Split-Complementary, Rectangle or Tetradic, and Square Color Scheme{/b}

    To understand them more, let us discuss them one by one.
    """
    show mov_colorscheme with dissolve
    play sound "audio/voice/r voice/Complementary.mp3"
    r "First is, Complementary Color Scheme these colors are opposite each other on the color wheel. High contrast of these colors creates a vibrant look especially when used at full saturation"
    
    play sound "audio/voice/r voice/Split-Comple.mp3"
    r "Split-Complementary Color Scheme is the variation of the complementary color scheme. It uses base color and  two adjacent colors to its complement. It has a strong visual contrast but has less tension. This is also a good choice for beginners."

    play sound "audio/voice/r voice/Triadic.mp3"
    r "Triadic Color Scheme uses colors that are evenly spaced around the color wheel, quite vibrant even with pale and unsaturated hues One color dominates and uses the two others for accent."

    play sound "audio/voice/r voice/Rectangle.mp3"
    r "Rectangle or Tetradic Color Scheme uses four colors arranged into two complementary pairs. The rich color scheme offers plenty of possibilities for variation. It works best when you let one color be dominant."

    play sound "audio/voice/r voice/Analogous.mp3"
    r "Analogous Color Scheme uses colors that are next to each other on the color wheel. Match well and create serene and comfortable designs. Commonly found in nature and are harmonious and pleasing to the eye."

    play sound "audio/voice/r voice/Square.mp3"
    r "Square Color Scheme this is similar to the rectangle but with all four colors spaced evenly around the color circle. It also works best if you let one color be dominant."

    stop sound
    show rizzsa smile at center with dissolve
    r "I hope your learn something new today"
    show rizzsa
    r "You can comeback anytime if you still don't get it, or have any questions"
    hide rizsa with dissolve
    jump lessons_2

label lesson_psychology_colors:
    stop music   
    scene bg psy colors with fade
    show rizzsa_blink
    r "Greetings"
    r "Today I'll teach you everything you need to know about..."
    hide rizzsa_blink
    show rizzsa speak
    r "Psychology of Colors"
    show rizzsa
    r "ahem, excuse me"
    hide rizzsa speak with dissolve
    show mov_psycolors with dissolve
    play sound "audio/voice/r voice/Psychology of Colors.mp3"
    r """
    Psychology of Colors

    Colors are known to have varied psychological and emotional connotations.
    Every culture has their own meaning of color and symbolism

    The Philippines has distinct symbolism of colors in diverse cultural groups
    
    Christianity has its own meaning of colors

    Artists in the philippines have strong influence from western world regarding symbolism and meanings of colors
    """
    play sound "audio/voice/r voice/Colors half.mp3"
    show rizzsa speak
    r "Here are the different meanings of every color."
    hide rizzsa speak with dissolve
    show black pallete with pixellate:
        xalign 0.5
        yalign 0.5
    r "Black is Death, despair, mourning, darkness, sorrow."
    show blue palette with pixellate:
        xalign 0.5
        yalign 0.5
        zoom 3
    r "Blue is Infinity, Freedom, Calmness, Masculinity."
    show brown palette with pixellate:
        xalign 0.5
        yalign 0.5
        zoom 2
    r "Brown is Earth, Humidity, Spiritual death, renunciation of the world."
    show green palette with pixellate:
        xalign 0.5
        yalign 0.5
        zoom 2.5
    r "Green is Nature, Freshness, Hope, Money, Life, Good health, envy."
    show orange palette with pixellate:
        xalign 0.5
        yalign 0.5
    r "Orange is Sweetness, energy, cheerfulness, food."
    show pink palette with pixellate:
        xalign 0.5
        yalign 0.5
    play sound "audio/voice/r voice/Other half.mp3"
    r "Pink is Love and femininity."
    show red palette with pixellate:
        xalign 0.5
        yalign 0.5
        zoom 2
    r "Red is Bravery, Passion, War, Warm, Martyrdom."
    show violet palette with pixellate:
        xalign 0.5
        yalign 0.5
        zoom 0.6
    r "Violet is Royalty, Dull, Power."
    show white palette with pixellate:
        xalign 0.5
        yalign 0.5
        zoom 0.8
    r "White is Purity, Clarity, Virginity, Peace, Surrender, Simplicity, Goodness, Mourning."
    show yellow palette with pixellate:
        xalign 0.5
        yalign 0.5
    r "Yellow is Joyful, Vibrant, Happiness, Sunshine."

    stop sound
    show rizzsa smile at center with dissolve
    r "I hope your learn something new today"
    show rizzsa
    r "You can comeback anytime if you still don't get it, or have any questions"
    hide rizsa with dissolve

    jump lessons_2

label value:
    stop music
    scene bg value with fade
    show rizzsa_blink
    r "Greetings"
    r "Today I'll teach you everything you need to know about..."
    hide rizzsa_blink
    show rizzsa speak
    r "Value"
    show rizzsa
    show mov_value with dissolve
    play sound "audio/voice/r voice/VALUES.mp3"
    hide rizzsa
    r """
    Value it can suggest emotional and dramatic impressions by using lightness and darkness in
    a composition
    
    Value refers to Chiaroscuro meaning lightness and darkness from the Italian word ‘chiaro’ for clear, and oscoro for dark
    
    Value is created by a certain source of light that strikes or shines on an object creating highlights and shadows
    
    It also creates depth within the picture by making an object look three dimensional with highlights and cast shadows
    
    Value also refers to the intelligent usage of tint, shades, and tones.
    """
    play sound "audio/voice/r voice/Tint, Shade, Tones.mp3"
    r """
    To understand more, let us define what tint, shades, and tones are

    Tint is the effect when a color is made lighter by adding white

    Shade is the effect when black is added, the result shows a darker version

    Tones if gray is added, it results to different tones
    """
    stop sound
    show rizzsa smile at center with dissolve
    r "I hope your learn something new today"
    show rizzsa
    r "You can comeback anytime if you still don't get it, or have any questions"
    hide rizsa with dissolve

    jump lessons_2

label lesson_texture:
    stop music
    scene bg texture with fade
    show rizzsa_blink
    r "Greetings"
    r "Today I'll teach you everything you need to know about..."
    hide rizzsa_blink
    show rizzsa speak
    r "Texture"
    show rizzsa
    show mov_texture with dissolve
    play sound "audio/voice/r voice/Texture-1.mp3"
    hide rizzsa
    r """
    Texture is found in all visual arts
    
    Element that deals primarily with the sense of touch or the tactile sensation or stimuli
    
    How the surface in a certain composition feels
    
    Texture may be described as smooth, hard, soft, wet, dry, rough, slippery, etc

    There are two different kinds of texture: Actual Texture and Implied or Simulated Texture
    """

    play sound "audio/voice/r voice/Actual Texture.mp3"

    r """
    Actual Texture - refers to the real texture of an object
    
    In cases like architecture and sculpture, the differences in texture can be felt because of the different materials used
    
    When It comes to two-dimensional art, texture is when artists incorporate other objects, this is called ‘collage’ and is introduced by Picasso and Braque
    
    Vincent Van Gogh also used strokes using pigment that gives body to the artwork called impasto. 
    """

    play sound "audio/voice/r voice/Implied Texture.mp3"
    r """
    Implied or Simulated Texture is the imitation of real texture or real objects
    
    Obtained through visual effects with the aid of other elements
    
    Medium can be manipulated by the artists to give an impression of texture and visual effects
    
    Visual texture is an illusion of texture created by the artist
    
    Simulated texture in visual art is considered as one of the greatest challenges by contemporary artists
    """

    stop sound
    show rizzsa smile at center with dissolve
    r "I hope your learn something new today"
    show rizzsa
    r "You can comeback anytime if you still don't get it, or have any questions"
    hide rizsa with dissolve

    jump lessons_2

label principles_of_art:
    stop music
    scene bg principles with fade:
        zoom 0.8
    show christopher smile at center with dissolve:
        yalign 0.3
    c "Hey, there!"
    show christopher eclosed
    c "I guess I'm going to teach today about..."
    show christopher serious
    c "Principles of Arts and Design"
    c "Let's get started"
    show mov_principles with dissolve
    play sound "audio/voice/fiel lessons/principle of arts & design.mp3"
    hide christopher serious
    c """
    {b}Principles of Art and Design{/b}

    The principles of design are used to organize the elements of art to create an effective and visually appealing composition
    
    These principles guide artists in arranging different elements to achieve harmony and impact in their artwork.
    """

    play sound "audio/voice/fiel lessons/9 types of a &d.mp3"
    c "There are 9 Principles of Art & Design"
    play sound "audio/voice/fiel lessons/emphasis.mp3"
    c "{b}Emphasis{/b} The focal point or center of interest in an artwork"
    play sound "audio/voice/fiel lessons/balance.mp3"
    c """
    {b}Balance{/b} Distribution of visual weight for stability

    There are 3 types of balance

    {b}Symmetrical Balance{/b} Both sides mirror each other

    {b}Assymetrical Balance{/b} Different elements are arranged to create balance without mirroring

    {b}Radial Balance{/b} Elements radiate from a central point"""

    play sound "audio/voice/fiel lessons/harmony.mp3"
    c "{b}Harmony{/b} Creates interconnectedness and unity in the artwork"

    play sound "audio/voice/fiel lessons/variety.mp3"
    c "{b}Variety{/b} Introduces visual interest and appeal"

    play sound "audio/voice/fiel lessons/movement.mp3"
    c "{b}Movement{/b} Creates a sense of action and excitement. It Directs the viewer’s eye throughout the composition"

    play sound "audio/voice/fiel lessons/rhythm.mp3"
    c "{b}Rhythm{/b} Repetition of elements to create a sense of movement"

    play sound "audio/voice/fiel lessons/proportion.mp3"
    c "{b}Proportion/Scale{/b} Relationship of different elements concerning size"

    play sound "audio/voice/fiel lessons/unity.mp3"
    c "{b}Unity{/b} Ensures all elements work together to create a cohesive artwork"

    play sound "audio/voice/fiel lessons/contrast.mp3"
    c "{b}Contrast{/b} Creates excitement by using opposing elements (e.g., light vs. dark, complementary colors)"

    stop sound
    show christopher smile at center with dissolve:
        yalign 0.3
    c "Well, I hope you actually learn something from me today"
    show christopher wink
    c "See ya!"
    hide christopher
    jump lessons_2

label art_criticism:
    stop music
    scene bg art critic with fade
    show christopher smile at center with dissolve:
        yalign 0.3
    c "Hey, there!"
    show christopher eclosed
    c "I guess I'm going to teach today about..."
    show christopher serious
    c "Art Criticism"
    c "Let's get started"
    show mov_artcritic with dissolve
    play sound "audio/voice/fiel lessons/art critcism.mp3"
    hide christopher
    c """
    {b}Art Criticism{/b} is the evaluation and formal analysis of an artwork
    
    It helps in understanding and appreciating art
    
    It Encourages confidence in discussing art, and develops aesthetic judgment.
    """
    play sound "audio/voice/fiel lessons/4 steps art criticism.mp3"
    c "There are four steps in art criticism"

    play sound "audio/voice/fiel lessons/description.mp3"
    c """
    {b}Step 1 Description{/b}

    Identify details about the artwork and artist.

    Answer key questions: What is the title, medium, and year of creation?
    """
    
    play sound "audio/voice/fiel lessons/analysis.mp3"
    c """
    {b}Step 2 Analysis{/b}

    Examine how elements of art (color, texture, shape, line) are used.

    Identify the principles of design applied.

    Key questions: How are colors, lines, and shapes arranged?

    """

    play sound "audio/voice/fiel lessons/interpretation.mp3"
    c """
    {b}Step 3 Interpretation{/b}

    Determine the meaning behind the artwork.

    Answer reflective questions: What is the artist’s message?
    """ 

    play sound "audio/voice/fiel lessons/judgement.mp3"
    c """
    {b}Step 4 Interpretation{/b}

    Form a personal evaluation based on analysis and interpretation.
    
    Consider: The artwork’s aesthetic value.
    """

    stop sound
    show christopher smile at center with dissolve:
        yalign 0.3
    c "Well, I hope you actually learn something from me today"
    show christopher wink
    c "See ya!"
    hide christopher
    jump lessons_2

label death_ending:
    scene black with fade
    play sound "audio/bgm/never meant to belong.mp3"
    show screen credits
    pause 100 # or however long it takes to scroll through in a reasonable speed
    pause
    hide screen creditscreen
    return

transform credits_scroll(speed):
    xcenter 0.5 yanchor 0.0 ypos 1.0
    ypos 1100
    linear speed ypos -6000

screen credits():

    ## Ensure that the game_menu screens can't be stopped
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"

    timer 30 action Return()
    #30 seconds
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.

    frame at credits_scroll(65.0): #bigger is slower
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            null height 10
            text "After not joining the art club"
            null height 10
            text "you went on to fail your finals exam, miserably"
            null height 100
            text "Your scores were so bad that you lost your scholarship"
            null height 10
            text "and were expelled from your university"
            null height 100
            text "Your grades becomes the lowest in the history of the humanity"
            null height 10
            text "not only you losing your scholarship but also your dignity"
            null height 100 
            text "Your friends and family abandoned and disowned you"
            null height 10 
            text "as no one would want to be associated with you"
            null height 100
            text "You were never be able to get a job and became homeless"
            null height 10
            text "you still think about your answer in that exam"
            null height 100
            text "You eventually {color=#f00}died{/color} after getting stabbed 37 times"
            null height 10
            text "in an alleyway at Tondo after getting your first 4ps Payout"
            null height 1100
            label "You should have joined the Art club" xalign 0.5

style credits_hbox:
    spacing 40
    ysize 30
                    
style credits_vbox:
    xalign 0.5
    text_align 0.5

style credits_label_text:
    xalign 0.5
    justify True
    size 125
    text_align 0.5
    color "#ff0000"

style credits_text:
    xalign 0.5
    size 60
    justify True
    text_align 0.5
    color "#ffffff"

label ending:
    scene black with fade
    play sound "audio/bgm/a million dreams.wav" fadein 1.0
    show screen credits2
    pause 100 # or however long it takes to scroll through in a reasonable speed
    pause
    hide screen creditscreen
    "{b}Good luck on your Midterms, and Finals Exam{/b}"
    return

transform credits_scroll(speed):
    xcenter 0.5 yanchor 0.0 ypos 1.0
    ypos 1100
    linear speed ypos -6000

screen credits2():

    ## Ensure that the game_menu screens can't be stopped
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"

    timer 30 action Return()
    #30 seconds
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.

    frame at credits_scroll(65.0): #bigger is slower
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            label "Special Thanks to" xalign 0.5
            null height 100
            text "Katrisha Diega"
            null height 400
            label "Cast" xalign 0.5
            null height 100
            text "Jisa Caryl Esplanada as Jisa"
            null height 100
            text "Telia Jean Marino as Telia"
            null height 100
            text "Rizzsa Lou Castillo as Rizzsa"
            null height 100
            text "Christopher Fiel Jr. as Christopher"
            null height 1200
            label "Thank you for Playing <3" xalign 0.5
            null height 200
            label "Made with Ren'Py" xalign 0.5