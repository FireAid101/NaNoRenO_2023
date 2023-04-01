# Main script for the NanoReno Jam 2023

# Characters in the game
define nurse = Character("Nurse", who_color="#73A6CE")
define drunk = Character("Homeless Drunk",who_color="#BD2E17")
define business_man = Character("Business Man", who_color="#0E1F9A")
define kicked_guy = Character("Kicked-Out Woman", who_color="#C2B329")
define dj = Character("DJ", who_color="#14B51F")

# Start of game
label start:

    # Fades out all music from menu and other sources
    stop music

    # Start of the game
    scene bg with None

    play music "audio/Bus Lofi.ogg" fadeout 1.0 fadein 1.0 
    pause 1.0    
    play sound "audio/bus_door_opening.ogg"
    pause 2.0
    scene nurse with fade
    pause 2.0
    play sound "audio/bus_door_closing.ogg"
    pause 2.0
    play sound "audio/bus_leaving.ogg"
    pause 2.0

    nurse "Hi, could you take me to the General Hospital?"
    nurse "Thank you."
    nurse "..."
    nurse "So..."
    nurse "How has your night been?"
    nurse "Oh..."
    nurse "Have you just started your shift?"
    nurse "This late at night huh?"
    nurse "I guess you're just like me."
    nurse "This is..."
    nurse "Fairly new to me."
    nurse "I'm not really used to working at this time."
    nurse "Ah.."
    nurse "I started babbling and I forgot to mention."
    nurse "I'm a Nurse."
    nurse "I too work the night shift."
    nurse "I started about a week and a half ago"
    nurse "So I'm quite new."
    nurse "I like the job though."
    nurse "You help people so they can get better."
    nurse "It's nice."
    nurse "But man..." 
    nurse "sometimes..."
    nurse "..."
    nurse "I don't know."
    nurse "Maybe I'm just not used to it."
    nurse "There is blood."
    nurse "There are angry people."
    nurse "Don't even get me started on pregnancies."
    nurse "The Coffee..."
    nurse "Too much coffee."
    nurse "During the evenings, people get even more upset and angry."

    # Option
    menu:
        "You respond: Sounds tough":
            nurse "Yeah, I guess so."
            nurse "Then again, I like the job."
            nurse "So I just... need to get used to it."
            nurse "For the people that need me."
            nurse "..."
            nurse "This is my stop."
            nurse "Thanks for the talk."
            nurse "See you another night."

        "You respond: Doesn't sound that hard":
            nurse "Hey, I know that this is not my stop."
            nurse "But I think I'll stop here and..."
            nurse "Think a bit."
            nurse "Bye."

    play sound "audio/bus_door_opening.ogg"

    scene bg    
    with fade

    pause 2.0

    "The nurse then leaves the bus to start his shift."
    "As the nurse leaves, a scruffy looking guy almost falls into the bus."
    
    scene homeless
    with fade

    pause 2.0

    play sound "audio/bus_door_closing.ogg" 
    
    pause 2.0

    drunk "G'day *gulp*"
    
    play sound "audio/bus_leaving.ogg"
    
    drunk "To *** street"
    drunk "{i}*hic*{/i}"
    drunk "...."
    drunk "Y'looking funny?"
    drunk "Eh.."
    drunk "{i}*hic*{/i}"
    drunk "Funny looking."
    drunk "Fight me if you looking at me funny."
    drunk "..."
    drunk "{i}*hic*{/i}"
    drunk "Dude"
    drunk "{size=+8}Fight me!{/size}"
    
    menu:
        "You respond: Want some water instead?":
            drunk "... "
            drunk "{i}*hic*{/i}"
            drunk "Yeah."
            drunk "Gonna go and get some."
            drunk "Thanks."
            drunk "See ya.."
            drunk "{i}*gulp*{/i}"

        "You respond: Wow calm down.":
            drunk "{size=+10}Fight me!{/size}"
            drunk "{i}*gulp*{/i}"
            drunk "Coward!"
            drunk "Gonna take down your bus"
            drunk "Be right back."

    play sound "audio/bus_door_opening.ogg"

    pause 1.0

    "The drunk man then stumbles off the bus to go and pursue other ventures."
    "Just as you were going to close the doors a stern looking man on the phone stops you"

    scene phone with fade

    play sound "audio/bus_door_closing.ogg"
    pause 2.0

    business_man "Yes."
    business_man "..."
    business_man "Good evening."
    business_man "To *** street"
    business_man "Thank you."   
    
    play sound "audio/bus_leaving.ogg"
    
    business_man "..."
    business_man "{i}Excuse me?{/i}"
    business_man "..." 
    business_man "{i}I was talking to the bus driver.{/i}"
    business_man "..."
    business_man "{i}As I was saying.{/i}"
    business_man "{i}The price of the enterprise's stock is very high at the moment.{/i}"
    business_man "{i}Which is not a terrible thing for us.{/i}"
    business_man "{i}If we can take the advantage of the situation{/i}"
    business_man "{i}We could get our stock price to rise up as well.{/i}"
    business_man "..."
    business_man "{i}No.{/i}"
    business_man "{i}I think you misundertood me.{/i}"
    business_man "{i}I'm not talking about shady business here.{/i}"
    business_man "{i}Just plain old business tactics.{/i}"
    business_man "{i}We are not doing bad in the market.{/i}"
    business_man "{i}But{/i}"
    business_man "{i}We could do better.{/i}"
    business_man "..."
    business_man "{i}Yes.{/i}" 
    business_man "{i}Now you're finally understanding me.{/i}"
    business_man "{i}What about the plans?{/i}"
    business_man "{i}Yesterday afternoon I had emailed you the document.{/i}"
    business_man "{i}Have you had a chance to read it?{/i}"
    business_man "..."

    menu:
        "Say nothing":
            business_man "{i}Great{/i}"
            "..."
            business_man "{i}So about that part of the document.{/i}"
            business_man "{i}Wait a minute.{/i}"
            business_man "{i}I'll be right with you.{/i}"
            business_man "Hey, Bus Driver."
            business_man "This is my stop."
            business_man "Thanks for the ride."

        "Interrupt him":
            "You interupt him by coughing"
            "Ejem!"
            business_man "{size=+10}Excuse me!{/size}" 
            business_man "I'm talking here!"
            business_man "{i}Sorry, I was talking to the bus driver.{/i}"
            business_man "{i}I'll leave the bus so I can talk with you.{/i}"
            business_man "{i}Okay, give me a second.{/i}"
 
    play sound "audio/bus_door_opening.ogg"

    pause 1.0   

    "The man on the phone gets off the bus to finish talking to his colleague."
    "Just as the man left, a somber looking woman gets on."

    scene kicked with fade

    play sound "audio/bus_door_closing.ogg"
    pause 2.0

    kicked_guy "Hi."
    kicked_guy "Could you take me to *** street?"
    kicked_guy "Thanks."
    
    play sound "audio/bus_leaving.ogg"
    
    kicked_guy "{i}*sigh*{/i}"
    kicked_guy "Sorry, I'm just..."
    kicked_guy "Can I ask for advice?"
    kicked_guy "No, you're just a bus driver."
    kicked_guy "I can't..."
    kicked_guy "{i}*sigh*{/i}"
    kicked_guy "I..."
    kicked_guy "I got in a fight."
    kicked_guy "With my partner."
    kicked_guy "I don't want to talk about the details."
    kicked_guy "But..."
    kicked_guy "It got..."
    kicked_guy "Bad."
    kicked_guy "Personal."
    kicked_guy "But the worst thing is"
    kicked_guy "I'm heading to my parents' house."
    kicked_guy "It got that bad."
    kicked_guy "Probably the worst night of my life."

    menu:
        "Apologize":
            kicked_guy "Thanks, I guess."
            kicked_guy "This will get better tomorrow."
            kicked_guy "I'm sure."
            kicked_guy "This is the first time we fought, so I have never really dealt with it before."
            kicked_guy "Things are going to get better."
            kicked_guy "Yeah."
            kicked_guy "Ah..."
            kicked_guy "My stop."
            kicked_guy "Thanks for chatting with me."
            kicked_guy "Really..."
            kicked_guy "It means a lot."

        "You respond: You deserved it.":
            kicked_guy "{size=+8}What do you know!{/size}"
            kicked_guy "{size=+8}I tried my best there!{/size}"
            kicked_guy "You know what?"
            kicked_guy "I'm getting off."
            kicked_guy "{size=+8}I'll just walk!{/size}"
            kicked_guy "{size=+10}Thanks for nothing!{/size}"

    play sound "audio/bus_door_opening.ogg"
    scene bg with fade

    pause 1.0   

    "The woman gets off the bus"
    
    "Look at the time! Your shift is nearly over."

    "You pick up your last passenger"
    "A man with headphones and glasses."
    "He looks a bit gloomy though."
 
    scene dj with fade

    play sound "audio/bus_door_closing.ogg"
    pause 2.0

    dj "{size=+10}Yo{/size} {size=+8}yo{/size} {size=+6}yo!{/size}"
    
    play sound "audio/bus_leaving.ogg"
    
    dj "{size=+10}It's time to party!{/size}"
    dj "{size=+10}Turn the music up bus DJ!{/size}"
    dj "{size=+10}Party Time!{/size}"
    
    menu:
        "You raise the volume":
            dj "{size=+8}Party!{/size}"
            dj "{size=+4}Yeah!{/size}"
            dj "..."
            dj "..."
            dj "Party..."
            dj "Yeah..."
            dj "..."
            dj "..."
            dj "They just fired me."
            dj "They said that I'm not {b}'lively enough'{/b}."
            dj "I try to do my best."
            dj "Every night."
            dj "What's my reward?"
            dj "I lost my job."
            dj "..."
            dj "You turning up the music."
            dj "It really made my night."
            dj "Tonight wasn't great."
            dj "As you could tell."
            dj "But that."
            dj "That was the move of a true DJ!"
            dj "..."
            dj "This is my stop."
            dj "Thanks."
            dj "I mean it."

        "You lower the volume":
            dj "Hey!"
            dj "What a downer!"
            dj "Drop me off at the next stop."
            dj "So that I can board a better party bus."
            dj "..."
            dj "..."
            dj "..."
            dj "Okay."
            dj "See ya never, downer!"

    play sound "audio/bus_door_opening.ogg"

    pause 1.0   

    scene bg with fade

    "The DJ then hops off the bus and into the night."
    "After that you drive the bus back to the Bus Terminal."
    "You're shift has now ended"

    play sound "audio/bus_door_closing.ogg"
    scene bg
    pause 1.0
    play sound "audio/bus_leaving.ogg"
    pause 2.0

    scene blackscreen with fade

    centered "{b}{size=+75}{cps=8}The 3 a.m Bus\n\nA Game for the {color=6a0dad}NaNoReno 2023 Game Jam{/color}{/cps}{/size}{p=5.0}{nw}{/b}"
    pause 2.0
    centered "{b}{size=+75}{cps=8}Directed By: RedRuby{/cps}{/size}{p=5.0}{nw}{/b}"
    pause 2.0
    centered "{b}{size=+75}{cps=8}Writer: RedRuby{/cps}{/size}{p=5.0}{nw}{/b}"
    pause 2.0
    centered "{b}{size=+75}{cps=8}Character Art: RetroKnight{/cps}{/size}{p=5.0}{nw}{/b}"
    pause 2.0
    centered "{b}{size=+75}{cps=8}Background Art: RetroKnight{/cps}{/size}{p=5.0}{nw}{/b}"
    pause 2.0
    centered "{b}{size=+75}{cps=8}Music Composer: LesReves{/cps}{/size}{p=5.0}{nw}{/b}"
    pause 2.0
    centered "{b}{size=+75}{cps=8}Sound Director: LesReves{/cps}{/size}{p=5.0}{nw}{/b}"
    pause 2.0
    centered "{b}{size=+75}{cps=8}Programmer: FireAid{/cps}{/size}{p=5.0}{nw}{/b}"
    pause 2.0
    centered "{b}{size=+75}{cps=8}UI Designer: FireAid{/cps}{/size}{p=5.0}{nw}{/b}"
    pause 2.0
    centered "{b}{size=+40}{cps=8}Special thanks for sounds used:{/size} {size=+20}
    
        {a=https://freesound.org/people/13FPanska_Sychra_Petr/sounds/379372/}13FPanska_Sychra_Petr's bus_door_opening{/a}\n\n
        {a=https://freesound.org/people/cribbler/sounds/369194/}cribbler's Bus leaving busstop{/a}\n\n
        {a=https://freesound.org/people/chimerical/sounds/104275/}chimerical's Bus door1{/a}
        
    {/size}{/cps}{p=5.0}{nw}{/b}"

    pause 2.0
    centered "{b}{size=+100}{cps=8}We thank you for playing our game{/cps}{/size}{p=5.0}{nw}{/b}"
    pause 1.0
    stop music fadeout 1.0
    pause 2.0
    # This ends the game.
    return
