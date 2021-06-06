print('''
 ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----|
 \_/_________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (   )   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------|
 \_/__________________________________________________________________/
''')
print("Welcome to the land of Merandle.")
print('''You are a orphan living in the medieval city of Merandle. You have lived on the streets as a beggar for as long as you remember, but now that you have become a teenager money has been harder and harder to come by. Out of desperation you have taken to graverobbing. Its hard dangerous work but you and your friend Reeve take turns digging and being a look out.

One night you and Reeve dig up a body that is still holding something tightly to his chest. It takes a considerable amount of prying to get the skeleton hand to give up the precious object, but once free you see that it is a treasure map and 10 gold coins. The X on the map is located in the valley of the night located north of Merandle past the mountains. A place that is feared by the people of Merandle and its even rumored that necromancers live there.

You split the coins with Reeve. Now you can choose to pay 3coins for a ride on a ship  up the west coast. This is a one way trip that will take 1 week and then another 3 days to reach the valley by foot. Or you can buy your own horse and supplies and take a 3week ride through the plains and forest to the east. Reeve said he is going to take the ship. What do you choose? ship or horse? type your answer''') 

c1 = input().lower()
if c1 == ('ship'):
 print('''


                       _____|/\ 
                  _.--| SSt |:
                 <____|.----||
                        .---''---,
                         ;..__..'    _...
                       ,'/  ;|/..--''    /\ 
                     ,'_/.-/':            :
                _..-''/  /  |  \    \   _|/|
               \      /-./_ \;   \    \,;'  /\ 
               ,\    / \:  `:\    \   //    `:`.
             ,'  \  /-._;   | :    : ::    ,.   .
           ,'     ::   /`-._| |    | || ' :  `.`.)
        _,'       |;._:: |  | |    | `|   :    `'
      ,'   `.     /   |`-:_ ; |    |  |  :/\ 
      `--.   )   /|-._:    :          |   \/\ 
         /  /   :_|   ;`-._;   __..--';    : :
        /  (    ;|;-./_  _/.-:'o |   /     ' |
       /  , \._/_/_./--''/_|:|___|_,'        |
      :  /   `'-'--'----'---------'          |
      | :     O ._O   O_. O ._O   O_.      ; ;
      : `.      //    //    //    //     ,' /
    ~~~`.______//____//____//____//_______,'~
              //    //~   //    //
       ~~   _//   _//   _// ~ _//     ~
     ~     / /   / /   / /   / /  ~      ~~
          ~~~   ~~~   ~~~   ~~~
 
 You take the boat with your freind Reeves. However one night Reeves pushes you overboard in order to steal your two coins. I guess he was evil this whole time.''')
 
elif c1 == ('horse'):
  print ('''
                _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\ 
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    |
   ||       |      \_,-'
   ||       |___,,--")_|
   ||         |_|   ccc/
   ||        ccc/       
   ||                hjm
   
   You split the map with Reeve, he takes the left half and you take the right. You buy the horse and go on your journey. 3 weeks later you arrive in the valley. However you run into a necromancer what do you do?
  a. throw rocks
  b. pretend you know magic to scare the necromancer
  c. run away
  type a,b or c''')
else:
    print('please select an answer')

c2 = input().lower()
if c2 == ('b'):
    print('the necromancer calls your bluf and kills you')
elif c2 == ('c'):
        print('he hits you in the back with a magic beam, killing you')
elif c2 == ('a'):
        print('''
        
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

Turns out that the necromancers weakness is rocks. You hit him right on the nose and he passes out. You find his treasure in his secret layer!''')
else:
    print('error: does not compute2')
