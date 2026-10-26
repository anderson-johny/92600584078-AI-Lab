"""
11. Develop an Expert system for medical diagnosis. 
NAME: ANDERSON JOHNY GEORGE
ENROLLNO. : 92600584078
"""

print("============== EXPERT SYSTEM ==============")
print("Answer the follwing questionwith yes / no.")
print("\n")

fever = input("Do you have fever? : ")
cough = input("Do you have cough? : ")
headach = input("Do you have headache? : ")

if fever == "no" and cough == "no" and headach == "no":
    print("You seem to be healthy.")

elif fever == "yes" and cough == "no" and headach == "no":
    print("You may have a mild infection.")

elif fever == "no" and cough == "yes" and headach == "no":
    print("You may have a Throat infection or mild cold.")

elif fever == "no" and cough == "no" and headach == "yes":
    print("You may have Stress, Migraine, or Fatigue.")

elif fever == "yes" and cough == "yes" and headach == "no":
    print("You may have Flu.")

elif fever == "yes" and cough == "no" and headach == "yes":
    print("You may have Viral Fever.")

elif fever == "no" and cough == "yes" and headach == "yes":
    print("You may have Commnon Cold.")

elif fever == "yes" and cough == "yes" and headach == "yes":
    print("You may have Flu or a Viral Infection.")

else:
    print("Invalid INPUT")
