"""Soviet space launch simulator.

A simple text adventure inspired by the 1970s space race.
This is intentionally written in a very basic style.
No functions, no dictionaries, and no advanced Python features.
"""

print("===========================================")
print("COSMOS CONTROL SYSTEM")
print("SOVIET MANNED LAUNCH SIMULATOR")
print("===========================================")
print()
print("Mission: Launch the crew into orbit and survive the countdown.")
print("Your team: Cosmonaut Ivan, Luna, and Sergei.")
print("Launch site: Baikonur Cosmodrome")
print()

print("The night is cold. The engines hum like a giant metal beast.")
print("A red light flashes on the control console.")
print("The launch officer speaks: 'We have a problem with the guidance system!'")
print()

answer = input("Do you check the guidance panel or trust the computer? (panel/computer): ")

if answer == "panel":
    print()
    print("You climb into the cramped control bay.")
    print("A dial is flickering between 7 and 9.")
    print("You hear a crackle over the radio: 'The guidance is unstable!'")
    print()
    print("Do you reset the dial or ignore it and continue?")
    choice = input("(reset/continue): ")

    if choice == "reset":
        print()
        print("You twist the dial. The flashing stops.")
        print("The room fills with a satisfying hum.")
        print("The launch countdown resumes.")
        print("The rocket rises. The windows shake. The stars blur.")
        print("Mission success. Orbit achieved.")
    else:
        print()
        print("You decide to trust the computer.")
        print("The guidance system fails.")
        print("The rocket tilts, sparks burst from the side, and the mission ends in smoke.")
        print("Mission failed.")

else:
    print()
    print("You trust the computer.")
    print("The machine speaks in a calm voice: 'Autopilot engaged.'")
    print("The countdown continues. The rocket trembles and lifts.")
    print("Suddenly a warning siren cuts through the cabin.")
    print()
    print("Do you abort the launch or keep going? (abort/go): ")
    decision = input()

    if decision == "abort":
        print()
        print("The crew survives the emergency shutdown.")
        print("The engines cool. The mission is delayed but not lost.")
        print("The cosmonauts cheer as the rocket settles back on the pad.")
        print("Mission paused. You live to try again.")
    else:
        print()
        print("You keep going.")
        print("The rocket punches through the clouds.")
        print("A bright trail of flame follows the vehicle into the black sky.")
        print("The crew reaches orbit and sends a message home:")
        print("'We are in space! The Motherland watches us.'")
        print("Mission success.")

print()
print("End of simulation.")
