"""Soviet lunar landing scenario.

This is a short adventure where the player must choose what to do
as a mission commander during a dangerous descent.
"""

print("==============================================")
print("LUNAR DESCENT: SOVIET MOON MISSION")
print("==============================================")
print()
print("The landing module carries three cosmonauts toward the Moon.")
print("The surface is covered in grey dust and jagged rocks.")
print("The engine alarm begins to flash.")
print("Mission control says: 'We are losing altitude control!'")
print()

answer = input("Do you descend quickly or slow the craft and scan the terrain? (quick/scan): ")

if answer == "quick":
    print()
    print("You push the craft lower toward the surface.")
    print("The lunar dust rises in a great cloud.")
    print("The module shakes and slips sideways.")
    print()
    emergency = input("Do you fire the thrusters or hold steady? (thrusters/steady): ")

    if emergency == "thrusters":
        print()
        print("The thrusters roar. The craft drifts back into balance.")
        print("You touch down in a wide crater with a soft metal jolt.")
        print("The crew steps out onto the Moon and raises the red flag.")
        print("Mission success.")
    else:
        print()
        print("You hold steady too long.")
        print("The craft tips hard. One landing leg collapses.")
        print("The module lurches and the crew is forced to abort the landing.")
        print("Mission ends in a damaged return.")

else:
    print()
    print("You slow the craft and scan the terrain.")
    print("You spot a flat plain between two rocks.")
    print("The ground looks safe and stable.")
    print()
    landing = input("Do you land there or continue searching? (land/search): ")

    if landing == "land":
        print()
        print("The module settles gently on the plain.")
        print("The window fogs as the crew steps onto the Moon.")
        print("The silence is heavy and wonderful.")
        print("A message is sent home: 'The Moon is ours.'")
        print("Mission success.")
    else:
        print()
        print("You continue searching too long.")
        print("Fuel drops to a dangerous level.")
        print("The module hovers above the surface and then drifts toward a crater wall.")
        print("The crew aborts the mission and returns to orbit.")
        print("Mission incomplete.")

print()
print("Transmission complete.")
