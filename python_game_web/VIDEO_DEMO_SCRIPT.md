# Python Quest 视频演示路线（8 分钟以内）

这份路线适合录制最终项目演示视频。  
操作说明用中文写；你在视频里说的话用英文写，可以直接照读或稍微自然化表达。

## 录制前准备

1. 打开终端，进入项目文件夹。
2. 准备两个窗口：
   - 浏览器：运行 Flask Web UI。
   - IDE：打开关键代码文件。
3. 启动 Web 版本：

```bash
python3 app.py
```

4. 浏览器打开：

```text
http://127.0.0.1:5000
```

5. 如果需要展示 CLI，可以另开一个终端运行：

```bash
python3 main.py
```

## 必须打开给老师看的代码文件

建议按这个顺序打开：

1. `main.py`：展示 CLI 入口仍然存在。
2. `app.py`：展示 Flask Web 入口和 routes。
3. `models.py`：展示 `Player`、`Question`、`Level`、`BossLevel`，尤其是 inheritance。
4. `python_questions.py`：展示 Python 知识题库。
5. `user_auth.py`：展示注册、登录、密码 hash 和 validation。
6. `data_manager.py`：展示 JSON file IO 和 exception handling。
7. `game_logic.py`：展示原 CLI game flow。
8. `templates/question.html` 和 `static/style.css`：展示 Web UI enhancement。

## 必须展示的网页页面

1. Welcome / Landing page
2. Register page
3. Login page
4. Dashboard page
5. Level selection page
6. Question page
7. Feedback / result page
8. Progress page
9. Leaderboard page
10. Logout

---

## 0:00 - 1:00 Project Concept

### 操作

1. 浏览器打开首页 `/`。
2. 展示标题、深色 dungeon 风格、bug monster/coding theme。
3. 简单点击或指向 Start Quest、Continue、Leaderboard。

### 英文台词

> Hello, this is my INT101 Python for AI Assessment 1 project.  
> The project is called Python Quest: The Coding Dungeon.  
> It is a Python learning game where the player defeats bug monsters by answering Python knowledge questions.  
> The original version is a modular command-line game, and I added a Flask web interface as an enhancement without removing the CLI version.  
> The main idea is that learning Python is not separate from the game. The Python quiz is the core gameplay.

---

## 1:00 - 2:00 Modular Code Structure

### 操作

切到 IDE，依次快速展示文件结构：

- `main.py`
- `app.py`
- `models.py`
- `user_auth.py`
- `data_manager.py`
- `game_logic.py`
- `python_questions.py`
- `templates/`
- `static/style.css`
- `users.json`
- `progress.json`

### 英文台词

> My project uses a modular structure instead of putting everything in one file.  
> The file main.py starts the CLI version, while app.py starts the Flask web version.  
> The models.py file contains the object-oriented classes.  
> The user_auth.py file handles registration and login.  
> The data_manager.py file handles JSON file input and output.  
> The game_logic.py file controls the original command-line gameplay.  
> The python_questions.py file stores the question bank and level data.  
> The templates folder contains the HTML pages, and the static folder contains the CSS for the web interface.

---

## 2:00 - 3:00 OOP and Inheritance

### 操作

打开 `models.py`，展示：

- `Player`
- `Question`
- `Level`
- `BossLevel(Level)`

重点停在 `class BossLevel(Level):` 和 `super().play(player)`。

### 英文台词

> This project clearly uses object-oriented programming.  
> The Player class stores the username, score, current level, unlocked levels, and badges.  
> The Question class represents one multiple-choice Python question.  
> The Level class stores a group of questions and controls how a level is completed.  
> The BossLevel class demonstrates inheritance because it extends the Level class.  
> It reuses the parent class play method by calling super, but it adds a special boss battle message for the final level.  
> This makes the design easier to understand and avoids repeating code.

---

## 3:00 - 4:00 Python Knowledge Integration

### 操作

打开 `python_questions.py`，展示不同 topic：

- basic syntax
- control structures
- functions
- data structures
- OOP
- file IO
- exception handling

然后切回浏览器，进入 Levels 页面。

### 英文台词

> Python knowledge is integrated directly into the game.  
> The player cannot progress just by clicking buttons. They must answer Python questions correctly.  
> The question bank covers basic syntax, control structures, functions, data structures, object-oriented programming, file IO, and exception handling.  
> Each level has a theme, and each question has options, a correct answer, an explanation, and a topic.  
> This supports learning because the player receives feedback and explanations after answering.

---

## 4:00 - 5:00 Registration, Login, and Validation

### 操作

1. 浏览器点击 Register。
2. 先留空 username 或 password，提交一次，展示错误提示。
3. 输入一个新用户名和密码，注册。
4. 跳到 Login，先故意输错密码一次，展示 login failed。
5. 输入正确密码登录，进入 Dashboard。

### 英文台词

> The web version includes user registration and login.  
> Here I am testing input validation. If the username or password is empty, the system shows a clear error message.  
> If the username already exists, the user also gets an error message.  
> During login, incorrect credentials are rejected.  
> The same user authentication logic is reused from user_auth.py, so the web version and the CLI version share the same backend design.

---

## 5:00 - 6:00 Gameplay and Reward Mechanism

### 操作

1. 登录后展示 Dashboard。
2. 点击 Levels。
3. 展示 unlocked / locked level cards。
4. 点击 Level 1 的 Battle。
5. 展示 Question 页面：
   - “Bug Monster appears!”
   - monster 形象
   - topic
   - question
   - answer choices
6. 选择一个答案并提交。
7. 展示 Feedback 页面。

### 英文台词

> This is the main gameplay loop.  
> The dashboard shows the player name, score, current completed level, unlocked levels, and badges.  
> On the level selection page, unlocked levels can be played, while locked levels are greyed out.  
> When I enter a level, the page becomes a bug monster battle.  
> The player answers a Python question to attack the bug monster.  
> If the answer is correct, the player earns points.  
> After each answer, the feedback page shows whether the answer is correct or incorrect, the explanation, the points earned, and the current score.  
> When a player passes a level, the game awards a badge and unlocks the next level.

---

## 6:00 - 7:00 Progress Saving, Loading, and File IO

### 操作

1. 答完一关或至少答一题后，进入 Progress 页面。
2. 展示 progress bar、score、unlocked levels、badges。
3. 点击 Logout。
4. 重新 Login。
5. 再次进入 Progress，展示数据仍然存在。
6. 切到 IDE，打开 `progress.json` 和 `users.json`。
7. 打开 `data_manager.py`，展示 `load_json()`、`save_json()`、`try/except`。

### 英文台词

> The project saves each user's progress separately.  
> The saved progress includes the current level, score, unlocked levels, and badges.  
> After logging out and logging back in, the progress is loaded again from progress.json.  
> The users.json file stores user account information, while progress.json stores gameplay progress.  
> In data_manager.py, the project uses JSON file input and output to load and save data.  
> It also includes exception handling for missing files, corrupted JSON, and operating system errors.  
> This means the program will not crash immediately if the data file has a problem.

---

## 7:00 - 7:40 CLI Version Still Works

### 操作

切到终端，运行：

```bash
python3 main.py
```

展示 CLI 菜单：

- Register
- Login
- Exit

可以输入 `3` 退出。

### 英文台词

> The original command-line version still works.  
> I did not replace the CLI project with a completely different web project.  
> The Flask version is an enhancement on top of the existing modular Python game.  
> This is important because the original assessment requirements are still satisfied.

---

## 7:40 - 8:00 Innovation and Enhancements

### 操作

1. 浏览器打开 Leaderboard。
2. 展示排名表格。
3. 可快速展示 `templates/leaderboard.html` 或 `app.py` 里的 leaderboard route。

### 英文台词

> As an enhancement, I added a Flask web interface with a polished coding dungeon theme.  
> I also added a leaderboard that reads all users' progress from progress.json and sorts players by score.  
> The web interface includes a dashboard, level cards, animated bug monster battle page, feedback page, progress page, and leaderboard.  
> Overall, the project meets the mandatory requirements and adds extra innovation while keeping the code simple enough for a first-year Python student to explain.

---

## 如果时间不够，优先展示这些内容

1. 首页：project concept。
2. `models.py`：OOP 和 inheritance。
3. `python_questions.py`：Python knowledge integration。
4. Register/Login：用户系统和 validation。
5. Question/Feedback：gameplay 和 explanations。
6. Progress + `progress.json`：保存和加载。
7. `data_manager.py`：file IO 和 exception handling。
8. Leaderboard：innovation。

## 最后一句总结

### 英文台词

> In conclusion, Python Quest is a modular, object-oriented Python learning game with both CLI and Flask web versions. It uses Python questions as the core gameplay, saves user progress with JSON file IO, includes validation and exception handling, and adds web UI and leaderboard features as enhancements.
