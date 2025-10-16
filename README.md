# Password Strength Analyzer & Custom Wordlist Generator

**Author:** Likhith Bharadwaj Reddy  
## Objective
Build a Python tool to analyze password strength and generate custom wordlists for auditing and educational purposes.

---

<details>
  <summary><b>Steps & Commands</b></summary>

1. **Install Requirements:**
    ```
    python -m pip install --user zxcvbn nltk
    ```
2. **Prepare Script:** Edit and save `password_tool.py` (provided in this repository).
3. **Run Analyzer:**
    ```
    python password_tool.py
    ```
4. **Follow Prompts:** Enter a password to analyze, and fill in details (name, year, pet name) for wordlist generation.
5. **Review Output:**  
    - Password analysis appears in the terminal/shell.
    - Custom word variations are generated and displayed.

</details>

---

## Observations & Learnings

- zxcvbn gives a password strength score (0=weak, 4=strong) plus feedback and crack-time estimates.
- The generated wordlist includes user-provided info, leetspeak variations, and common number patterns.
- Running the script helped understand password vulnerabilities and common attack patterns.

---

## Project Structure

- `password_tool.py` — Main script  
- `README.md` — Documentation
- `wordlist.txt` — words given by user

---

## Conclusion

This project gave practical experience in using password analysis libraries, creating tools for password auditing, and understanding real-world password weaknesses and attacker strategies.


