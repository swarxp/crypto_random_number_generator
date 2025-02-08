import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Generate secure random numbers using AES-CTR
def generate_random_numbers(seed, num_bytes=16):
    # Ensure the seed is long enough
    if len(seed) < 48:
        raise ValueError("Seed must be at least 48 bytes long to extract a 32-byte key and a 16-byte nonce.")
   
    # Split the seed into key and nonce
    key = seed[:32]  # 32 bytes key for AES-256
    nonce = seed[32:48]  # 16 bytes nonce for AES-CTR
   
    # Initialize AES cipher in CTR mode
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    encryptor = cipher.encryptor()

    # Generate the requested number of random bytes
    random_bytes = encryptor.update(bytes([0] * num_bytes))  # Generate dummy bytes and encrypt them
    return random_bytes

# Simulate key exchange and QRNG as before
def generate_shared_secret():
    # Alice's private key (in reality, this should be securely generated)
    alice_private_key = ec.generate_private_key(ec.SECP384R1())
   
    # Bob's private key (in reality, this should be securely generated)
    bob_private_key = ec.generate_private_key(ec.SECP384R1())
   
    # Each party generates their public key and computes the shared secret
    alice_public_key = alice_private_key.public_key()
    bob_public_key = bob_private_key.public_key()
   
    # Alice computes the shared secret using Bob's public key
    alice_shared_secret = alice_private_key.exchange(ec.ECDH(), bob_public_key)
   
    # Bob computes the shared secret using Alice's public key
    bob_shared_secret = bob_private_key.exchange(ec.ECDH(), alice_public_key)
   
    # Verify that both parties have the same shared secret
    assert alice_shared_secret == bob_shared_secret
    return alice_shared_secret

def get_quantum_random_number():
    # We'll use os.urandom to simulate randomness; in practice, replace with QRNG service
    return os.urandom(32)  # Generate 32 bytes of randomness

def create_seed(shared_secret, qrng_output):
    # Combine shared secret and QRNG output
    combined_input = shared_secret + qrng_output

    # Use SHA-384 instead of SHA-256 (produces 48 bytes)
    digest = hashes.Hash(hashes.SHA384())
    digest.update(combined_input)
    seed = digest.finalize()

    return seed  # Now it's 48 bytes long

def main():
    # Step 1: Simulate key exchange (QKD) and get a shared secret
    shared_secret = generate_shared_secret()
   
    # Step 2: Simulate QRNG to get quantum-like randomness
    qrng_output = get_quantum_random_number()
    print("Quantum-like Random Number: ", qrng_output.hex())
   
    # Step 3: Combine the shared secret and QRNG output to create a seed
    seed = create_seed(shared_secret, qrng_output)
    print("Generated Seed: ", seed.hex())

    # Step 4: Use AES-CTR CSPRNG to generate secure random numbers
    random_numbers = generate_random_numbers(seed, num_bytes=16)
    print("Generated Random Numbers: ", random_numbers.hex())

if _name_ == "_main_":
    main()
