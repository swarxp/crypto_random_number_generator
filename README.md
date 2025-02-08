# crypto_random_number_generator
Cryptographically Secure Random Number Generator (CSPRNG) with Quantum-Inspired Entropy .

Overview
This project implements a Cryptographically Secure Random Number Generator (CSPRNG) using AES-CTR mode. It integrates Elliptic Curve Diffie-Hellman (ECDH) key exchange and Quantum-inspired entropy to generate highly secure random numbers.


Elliptic Curve Diffie-Hellman (ECDH) Key Exchange: Establishes a shared secret between two parties using elliptic curve cryptography, which is more efficient and secure compared to traditional key exchange mechanisms.

Quantum Random Number Generator (QRNG) Simulation: Introduces additional entropy using system-generated randomness (os.urandom(32)) to ensure unpredictability.

Secure Seed Generation: Uses SHA-384 to create a cryptographically strong seed that combines the shared secret and quantum entropy.

AES-CTR Based CSPRNG: Uses AES in Counter (CTR) mode to generate high-quality random numbers for cryptographic purposes.

Understanding Key Concepts
Elliptic Curve Diffie-Hellman (ECDH) Key Exchange
ECDH is a method of securely exchanging cryptographic keys using elliptic curve mathematics. It allows two parties (Alice and Bob) to independently generate a shared secret without ever transmitting it directly.
Private Key: A randomly generated secret number.
Public Key: Derived from the private key using an elliptic curve function.
Shared Secret: Computed using one's own private key and the other party's public key.
Security: ECDH is highly secure because an attacker cannot feasibly compute the private key from the public key (Elliptic Curve Discrete Logarithm Problem).
Quantum-Inspired Entropy (QRNG Simulation)
In real quantum random number generation (QRNG), randomness comes from quantum mechanical phenomena.
Since true QRNG devices are not always available, we simulate randomness using os.urandom(32), which provides cryptographically secure random numbers from the operating system.
Secure Seed Generation: Uses SHA-384
SHA-384 is a cryptographic hash function that takes an input and produces a 48-byte (384-bit) output.
Why SHA-384? It provides a longer hash output than SHA-256, which strengthens security.
Purpose in this project: Combines the shared secret and quantum randomness to create a highly secure seed for the CSPRNG.
AES-CTR Mode: A Cryptographic Secure PRNG
AES (Advanced Encryption Standard) is a widely used encryption algorithm. CTR (Counter) mode turns AES into a stream cipher, making it useful for generating secure random numbers.
How it works: Encrypts a counter value that is incremented for each block, producing unique and unpredictable outputs.
Why AES-CTR?
Does not require padding like other AES modes.
Efficient and fast.
Ensures forward and backward security (previous and future outputs cannot be inferred).

How It Works
Key Exchange using ECDH: Two parties (Alice & Bob) generate a shared secret using elliptic curve cryptography.
Quantum Randomness (Simulated): Uses os.urandom(32) as a stand-in for a real QRNG.
Seed Creation: Combines the shared secret and QRNG output, then hashes them with SHA-384.
CSPRNG Using AES-CTR: Uses AES-256 in CTR mode to generate cryptographically secure random numbers.
