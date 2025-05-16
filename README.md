# 🔐 Project 14 – Garuda Zero-Knowledge Proof (Basic)

**Garuda Sentinel Mission – Project 14**

This project demonstrates a simple yet powerful cryptographic concept: **Zero-Knowledge Proofs (ZKPs)**. It simulates an interactive protocol between a **Prover (Alice)** and a **Verifier (Bob)** where Alice convinces Bob that she knows a secret **without ever revealing it**.

---

## 🧠 Concept

Zero-Knowledge Proofs allow a prover to demonstrate knowledge of a secret value (e.g., a password, private key, or identity) without disclosing any information about the secret itself. This is done through clever math and randomness.

In this simulation:

- A large public number `n` is shared by both Alice and Bob.
- Alice has a secret `x`, and she sends Bob a commitment `v = r² mod n`, where `r` is a random number.
- Bob sends back a challenge bit (0 or 1).
- Alice responds based on the challenge, and Bob verifies using modular arithmetic.

This process does not reveal `x`, but still convinces Bob that Alice knows it.

---

## 📁 Files

- `alice_prover.py` – Script for the Prover (Alice)
- `bob_verifier.py` – Script for the Verifier (Bob)

---

## ⚙️ How It Works

1. **Setup**
   - Public modulus `n` is shared.
   - Alice selects secret `x` and calculates `x² mod n` to share with Bob.

2. **Commitment Phase (Alice)**
   - Alice generates a random number `r`.
   - Computes `v = r² mod n` and sends it to Bob.

3. **Challenge Phase (Bob)**
   - Bob sends a random challenge `c ∈ {0, 1}`.

4. **Response Phase (Alice)**
   - If `c = 0`: Sends `r`.
   - If `c = 1`: Sends `r * x mod n`.

5. **Verification Phase (Bob)**
   - If `c = 0`: Verifies `r² mod n == v`
   - If `c = 1`: Verifies `(r*x)² mod n == v * x² mod n`

---

## ✅ Example Output

```shell
# alice_prover.py
🔐 Public value (x^2 mod n): 139
📤 Commitment sent to Bob (v): 523
🤖 Enter challenge from Bob (0 or 1): 1
📨 Response to challenge 1: r * x mod n = 1978

# bob_verifier.py
🔐 Enter x^2 mod n (public from Alice): 139
📥 Enter commitment (v) from Alice: 523
🤖 Challenge sent to Alice: 1
📨 Enter response from Alice (r * x mod n): 1978
🧪 Verifying: (rx)^2 mod n == v * x^2 mod n → 1431 == 1431
✅ Verified!
🚀 Why It Matters
This simple interactive ZKP forms the foundation of advanced cryptographic protocols used in:

Secure authentication

Digital identity

Blockchain privacy (e.g., zk-SNARKs, zk-STARKs)

Anonymous voting and credentials

📌 Project Scope
✅ Core ZKP simulation
✅ Separate Alice and Bob logic
✅ Challenge-response protocol
🚧 Future extensions:

Non-interactive proofs (Fiat-Shamir heuristic)

Real-world digital ID applications

Secure credential validation

🔒 Mission Alignment
This project aligns with the Garuda Sentinel Mission by strengthening the understanding of privacy-preserving cryptographic protocols — a key part of future secure authentication systems and digital identity management.

🛡️ Built With
Python 3.x

Random module

Modular arithmetic

📚 Reference
Serious Cryptography by Jean-Philippe Aumasson – Chapter on Zero-Knowledge Proofs

ZKP literature and mathematical principles
