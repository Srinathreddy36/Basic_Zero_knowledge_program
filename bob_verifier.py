30# Public modulus
n = 2357

# Get public value x^2 from Alice
x_squared = int(input("🔐 Enter x^2 mod n (public from Alice): "))
# Get commitment v from Alice
v = int(input("📥 Enter commitment (v) from Alice: "))

# Send random challenge
import random
challenge = random.randint(0, 1)
print(f"🤖 Challenge sent to Alice: {challenge}")

# Get Alice's response
if challenge == 0:
    r = int(input("📨 Enter response from Alice (r): "))
    lhs = (r ** 2) % n
    print(f"🧪 Verifying: r^2 mod n == v → {lhs} == {v}")
    print("✅ Verified!" if lhs == v else "❌ Verification failed.")
else:
    rx = int(input("📨 Enter response from Alice (r * x mod n): "))
    lhs = (rx ** 2) % n
    rhs = (v * x_squared) % n
    print(f"🧪 Verifying: (rx)^2 mod n == v * x^2 mod n → {lhs} == {rhs}")
    print("✅ Verified!" if lhs == rhs else "❌ Verification failed.")
