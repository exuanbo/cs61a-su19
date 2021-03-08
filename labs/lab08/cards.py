# All cards available in a standard deck.
from classes import *

#TAs
aaron = TACard('Baron Aaron', 2100, 1300)
albert = TACard('Al-bear', 1600, 1700)
aman = TACard('Aman', 1000, 2100)
cesar = TACard('Cesar, Sponsor of Good Vibes™', 1600, 1700)
chae = TACard('Chae', 1500, 1900)
danelle = TACard('Danelle Nachos', 2200, 1100)
derrick = TACard('EZ4ENCE', 1100, 2000)
isabelle = TACard('Isabelle', 1500, 1800)
jemmy = TACard('Jemmy', 1600, 1800)
lauren = TACard("Explorin' Lauren", 1200, 2200)
michelle = TACard('MICHELLE, De SOUs chef of ZA kingdom', 1500, 1800)
olivia  = TACard('shocked pikachu', 1900, 1500)
pavan = TACard('Pavan', 1400, 2000)
richard = TACard('Richard', 1500, 1900)
ryan = TACard('Ryan', 1500, 1800)
sean = TACard('Sean, Maker of Boba', 1700, 1500)
shide = TACard('ShidzZz of YeetzZz', 1700, 1500)

#Tutors
ada = TutorCard('Hu is Ada???', 2100, 1300)
aini = TutorCard('MacarAini and Cheese', 1800, 1500)
christine = TutorCard('Christine', 1500, 1700)
grant = TutorCard('Grant', 1100, 2100)
jennifer  = TutorCard('Jen, Head of Squirrels On Campus', 1600, 1700)
kaavya = TutorCard('Kaavya', 2200, 1200)
kaitlyn = TutorCard('Kaitlyn', 1300, 2000)
kevin = TutorCard('Kevin', 1500, 1900)
kunal = TutorCard('Kunal', 1500, 1500)
nancy = TutorCard('Banancy', 1500, 1700)
raghav = TutorCard('Raghav', 1400, 2000)
rahul_a = TutorCard('Rahul (disambiguation needed)', 2400, 1000)
rahul_d = TutorCard('Rahul', 1700, 1600)
rina = TutorCard('Rina', 1500, 1800)


# Insturctors
alex = InstructorCard('President Lieutenant Stennet for Senate', 2000, 4000)
tiffany = InstructorCard('Tall Tiff', 4000, 2000)
chris = InstructorCard('Chris, Caller of Men', 3000, 3000)

# A standard deck contains all standard cards.
standard_cards = [alex, tiffany, chris, aaron, albert, aman, cesar, chae, danelle, derrick, isabelle, jemmy, lauren, michelle, olivia , pavan, richard, ryan, sean, shide, ada, aini, christine, grant, jennifer , kaavya, kaitlyn, kevin, kunal, nancy, raghav, rahul_a, rahul_d, rina]
standard_deck = Deck(standard_cards)

# The player and opponent's decks are the standard deck by default.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()