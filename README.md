# Ranshell: Automated Ransomware Detection and Lockdown

Originally engineered in 2021, I developed a localized ransomware detection system utilizing honeypots and continuous file integrity checking. Designed to serve as a functional, active defense mechanism rather than a theoretical concept, this project bridges the gap between high-level security theory and low-level system execution.

In December 2023, while dual-enrolled, I presented this framework on a larger stage where it gained massive public traction and objective validation.

### Project Impact & Highlights

* **Adversarial Simulation:** Developed a full-spectrum framework utilizing AES-256 encryption contexts and multi-threaded file traversal.
* **Active Defense Mechanism:** Engineered a Real-Time File Integrity Monitor (FIM) as a defensive counterpart, utilizing cryptographic anomaly detection to trigger automated system lockdowns.
* **Performance Optimization:** Successfully optimized the FIM's multi-threaded hashing loop to maintain a minimal memory footprint, resolving severe RAM consumption bottlenecks during continuous, system-wide monitoring.
* **Public Impact & Engagement:** Presented technical architecture to 450+ secondary students and 50+ industry experts; project booth engaged 4,000+ university attendees.
* **Objective Recognition:** Awarded **3rd Place at a University Tech Expo** (field of 1,300+ entries) for excellence in system architecture and security innovation, demonstrating the ability to deliver high-quality research under competitive pressure.

### Architecture & Technical Velocity

Building Ranshell required rapid mastery of complex systems and a focus on technical velocity. The core philosophy of the project relies on analytical, proactive deception. Ransomware typically operates by encrypting files indiscriminately across a directory tree. Ranshell combats this by strategically placing invisible, highly monitored "honeypot" files throughout the system to act as an immediate tripwire. 

### How It Works

To ensure modularity and rapid incident response, the system logic is decoupled into specific, multi-threaded scripts:

* **Initialization & Placement:** `walker_beta.py` and `first_start_all_combine.py` map the directory structure and seed the initial honeypot files without disrupting the user environment.
* **Continuous Monitoring (FIM):** The `hash_cheker.py` script acts as the primary watchdog. It continuously calculates the cryptographic hashes of the honeypots and compares them against a clean, isolated baseline. 
* **Automated Lockdown:** Normal users never interact with honeypot files. Therefore, any modification, deletion, or encryption attempt is immediately flagged as a malicious process. If a hash mismatch occurs, `lockdown.py` executes an automated sequence to isolate the environment and halt execution before the encryption can reach critical user data.
* **Maintenance:** `clean_up.py` allows for the safe removal of the honeypots and resetting of the environment state.

### The Tech Stack
* **Language:** Python 3.10
* **Core Concepts:** File Integrity Monitoring (FIM), Multi-threading, Cryptographic Hashing, AES-256 Contexts, Memory Optimization, Honeypots, Automated Incident Response

### Deployment Instructions

1. Clone the repository to an isolated testing environment or virtual machine (highly recommended when testing automated lockdown scripts).
2. Install the necessary dependencies via `requirements.txt`.
3. Configure your target directories and monitoring thresholds in `config.ini`.
4. Run the initialization scripts to plant the tripwires.
5. Execute `hash_cheker.py` to initiate the active, multi-threaded monitoring loop.