import random

# simulating coin flips
trials = 10000
heads = 0
tails = 0

for i in range(trials):
    # choose between heads and tails
    if random.choice(['H','T']) ==  'H':
        heads += 1
    else:
        tails+=1

print(f"head picks: {heads}")
print(f"tail picks: {tails}")
print()

probability1= heads/trials
probability2= tails/trials

# Shows how probability1 + probability2 = 1.0 exactly proving a fair coin
print(f"Heads probability: {probability1:.3f} (should be ~0.5)")
print(f"Tails probability: {probability2:.3f} (should be ~0.5)")
print()

#simulating dice rolls
dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} 
for i in range(trials):
    face = random.randint(1,6)
    dice[face] += 1

print(f"the number of picks for eeach face {dice}")
print()

for face in range(1, 7):
    # Computing the probability of each face
    prob = dice[face] / trials
    print(f"Face {face} probability: {prob:.3f} (should be ~0.167)") # Addition of all probabilities = 6.0
