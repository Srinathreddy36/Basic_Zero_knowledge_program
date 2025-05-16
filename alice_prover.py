import random

# Public modulus (must be a large safe prime in real applications)
n = 2357
# Alice's secret (should not be shared)
x = 123  # Alice knows this, but Bob doesn't

# Precompute x^2 mod n (shared with Bob)
x_squared = (x ** 2) % n
print(f"🔐 Public value (x^2 mod n): {x_squared}")

# Alice chooses a random r
r = random.randint(1, n-1)
v = (r ** 2) % n
print(f"📤 Commitment sent to Bob (v): {v}")

# Simulate receiving challenge from Bob
challenge = int(input("🤖 Enter challenge from Bob (0 or 1): ").strip())

# Respond to Bob's challenge
if challenge == 0:
    print(f"📨 Response to challenge 0: r = {r}")
else:
    response = (r * x) % n
    print(f"📨 Response to challenge 1: r * x mod n = {response}")
