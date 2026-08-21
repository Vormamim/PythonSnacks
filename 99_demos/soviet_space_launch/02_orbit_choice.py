"""Soviet space adventure.

A simple branching story in a 1970s space program style.
This version has a few choices and a more dramatic ending.
"""

print("==============================================")
print("COSMOS: ORBITAL DECISION")
print("==============================================")
print()
print("The rocket is in orbit. The crew is floating in a bright metal cabin.")
print("The radio crackles with a message from mission control.")
print("'We have detected a problem with the thermal shield.'")
print("The temperature in the cabin begins to rise.")
print()

choice1 = input("Do you inspect the shield or launch the emergency cooling system? (shield/cooling): ")

if choice1 == "shield":
    print()
    print("You open the panel near the window.")
    print("A thin crack in the shield is glowing red with heat.")
    print("You see a loose cable flickering near the edge.")
    print()
    choice2 = input("Do you fix the cable or seal the panel? (fix/seal): ")

    if choice2 == "fix":
        print()
        print("You work quickly in zero gravity.")
        print("The cable sparks then steadies.")
        print("The temperature drops.")
        print("The ship survives. The crew continues their orbit.")
        print("A quiet voice from mission control says: 'Excellent work.'")
        print("Mission success.")
    else:
        print()
        print("You seal the panel in a hurry.")
        print("The seal holds for a moment, but the thermal problem worsens.")
        print("Heat floods through the cabin.")
        print("The crew is forced to abandon the mission and return home.")
        print("Mission ends in emergency.")

else:
    print()
    print("You launch the emergency cooling system.")
    print("Cold mist sprays through the cabin. The air shivers.")
    print("The temperature falls quickly, but the power system flickers.")
    print()
    choice3 = input("Do you keep the cooling on or switch it off? (keep/off): ")

    if choice3 == "keep":
        print()
        print("The cooling system holds steady.")
        print("The crew remains safe, but the ship loses power for a while.")
        print("Mission control sends a command to re-route power.")
        print("The orbit is maintained. The mission continues.")
        print("Mission success.")
    else:
        print()
        print("You switch the system off too soon.")
        print("The cabin heat returns with a violent rush.")
        print("The crew loses control of the ship for a few seconds.")
        print("The capsule spins wildly, then steadies.")
        print("The mission is saved, but the crew is shaken and the spaceship is damaged.")
        print("Mission complete, but barely.")

print()
print("End transmission.")
