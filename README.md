# AICTE Oasis Infobyte Python Programming Internship

This repository contains the projects completed during my Python Programming Internship at Oasis Infobyte. All tasks are fully implemented as stable command-line applications with robust input validations.

---

##  Project Structure

* **`Hitesh_Task1/`**: Voice & Text Assistant.
* **`Hitesh_Task2/`**: BMI Calculator.
* **`Hitesh_Task3/`**: Random Password Generator.
* **`.gitignore`**: Specifying untracked files to ignore.

---

##  Completed Tasks Detail

### Task 1: Voice & Text Assistant
A smart virtual assistant capable of executing system tasks based on voice commands, featuring an automated fallback mechanism.
* ** Features**: Welcomes the user, provides current real-time system time and date metrics, and opens up automated Google searches in the default web browser. Includes a critical fallback mechanism that automatically switches to text-input mode if microphone access permissions or hardware utilities are unavailable to prevent application crashes.

### Task 2: BMI Calculator
A command-line tool built to calculate an individual's Body Mass Index (BMI) based on weight (kg) and height (m).
* ** Features**: Gracefully flags invalid alphabetical inputs and includes a smart unit conversion utility that automatically checks if a user inputted height in centimeters (e.g., 177) and scales it down to meters to protect calculation metrics.

### Task 3: Random Password Generator
A robust utility that generates custom, completely random, structurally secure passwords based on user preferences.
* ** Features**: Collects custom length configurations and combines character arrays (Letters, Numbers, Symbols). Features mandatory character seeding logic to guarantee at least one character from every single user-selected set is explicitly injected into the resulting output string to optimize security.
