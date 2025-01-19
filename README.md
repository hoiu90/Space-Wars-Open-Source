
---

## Development Steps for the Space War Game

### **STEP 1: Initial Development**
I spent most of my time here as this was my first experience with programming. The hardest part was designing the general structure and framework for the Space War game. I want to mention that the resources and materials for this game were sourced from the internet.

---

### **STEP 2: Refactoring and Enhancements**
I tried to convert global variables into functions (`def`) because I wanted to create multiple levels, such as the first level, second level, and so on. However, I struggled to find the best approach and faced many issues in `game_window_v2`.  
For example:
- I encountered challenges using `for` loops during runtime, and even though they solved some problems, I wasn’t entirely sure why they worked.

---

### **STEP 3: Compiling to .EXE**
I attempted to compile the program into a `.exe` file to share it with other players. During this process, I faced several issues:
1. Images, videos, and music needed to be imported properly using `os` and `base` modules to avoid errors after using `pyinstaller`.
2. After compiling, the program couldn’t locate these assets, and I had to adjust paths to solve the problem.

---

### **STEP 4: Bug Fixes and Optimization**
I fixed several bugs, including:
1. Resolving why the BGM (background music) didn’t play.
2. Fixing the issue where the upper-right corner of the screen didn’t display properly.
3. Compressing the game into a ZIP file for easy sharing.

---

