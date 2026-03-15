# Module I — Introduction to Artificial Intelligence
## ITC604 | AI and DS – 1 | 4 Hours | CO1

---

## 1. What is Artificial Intelligence (AI)?

**Simple Definition:**
Artificial Intelligence is the science of making machines (computers) do things that would require intelligence if done by humans — like thinking, learning, problem-solving, understanding language, and recognizing images.

**Formal Definition:**
> "AI is the study of how to make computers do things at which, at the moment, people are better." — Elaine Rich

> "AI is the branch of computer science concerned with the automation of intelligent behavior." — Luger & Stubblefield

**In simple words:**
- Humans are intelligent — we can see, speak, learn, solve puzzles, drive cars.
- AI tries to give these abilities to computers/machines.
- Example: Siri understands your voice (speech recognition), Google Maps finds the shortest route (problem solving), Netflix recommends movies (learning from data).

---

## 2. Goals of AI

| Goal | Meaning |
|------|---------|
| **Think like humans** | Build systems that mimic human thought processes (Cognitive Modeling) |
| **Act like humans** | Build systems that behave like humans (Turing Test approach) |
| **Think rationally** | Build systems that use logic to reason correctly (Laws of Thought) |
| **Act rationally** | Build systems that do the right thing to achieve goals (Rational Agent approach) |

### The Turing Test (1950)
- Proposed by **Alan Turing**.
- A human interrogator asks questions (via text) to both a human and a machine.
- If the interrogator **cannot tell** which is the machine, the machine is said to be intelligent.
- To pass the Turing Test, a machine needs:
  - **Natural Language Processing (NLP)** — to understand and reply in English
  - **Knowledge Representation** — to store what it knows
  - **Automated Reasoning** — to answer questions and draw conclusions
  - **Machine Learning** — to adapt and detect patterns

---

## 3. AI Techniques

AI techniques are methods/approaches used to solve problems intelligently. A good AI technique must:

1. **Generalize** — work for many similar problems, not just one
2. **Handle uncertainty** — work even when information is incomplete
3. **Be efficient** — solve problems in reasonable time
4. **Be understandable** — humans should be able to follow the reasoning

### Major AI Techniques:
| Technique | What it does | Example |
|-----------|-------------|---------|
| **Search** | Explores possible solutions step by step | Finding shortest path in a map |
| **Knowledge Representation** | Stores facts and rules about the world | "All dogs are animals" |
| **Logic & Reasoning** | Draws conclusions from known facts | If A→B and A is true, then B is true |
| **Machine Learning** | Learns patterns from data | Spam email detection |
| **Natural Language Processing** | Understands human language | Chatbots, translators |
| **Computer Vision** | Understands images/videos | Face recognition |
| **Robotics** | Physical agents that interact with the world | Self-driving cars |

---

## 4. Problem Formulation

Before solving any AI problem, we must **define it clearly**. This is called Problem Formulation.

### Components of Problem Formulation:
| Component | Meaning | Example (8-Puzzle) |
|-----------|---------|-------------------|
| **Initial State** | Where we start | Tiles in scrambled position |
| **Actions / Operators** | What moves we can make | Slide a tile up, down, left, right |
| **Transition Model** | What happens after an action | New arrangement of tiles |
| **Goal Test** | How to check if we've reached the solution | All tiles in order 1-8 |
| **Path Cost** | Cost of reaching the goal | Number of moves made |

### Example — Route Finding (Google Maps):
- **Initial State:** Your current location (City A)
- **Actions:** Drive on available roads
- **Transition Model:** Moving from one city to another via a road
- **Goal Test:** Have you reached City B?
- **Path Cost:** Total distance or time traveled

### State Space:
- The **state space** is the set of ALL possible states reachable from the initial state.
- Think of it as a huge tree/graph where each node is a state and each edge is an action.
- AI searches this space to find a path from the initial state to the goal.

---

## 5. Intelligent Agents

### What is an Agent?
An **agent** is anything that:
1. **Perceives** its environment through **sensors**
2. **Acts** upon the environment through **actuators**

```
        ┌─────────────────────┐
        │       AGENT         │
        │                     │
Sensors │  Percepts → Think   │ Actuators
------->│        ↓            │-------->
        │     Actions         │
        │                     │
        └─────────────────────┘
              Environment
```

### Examples:
| Agent | Sensors | Actuators | Environment |
|-------|---------|-----------|-------------|
| **Human** | Eyes, Ears, Nose, Skin | Hands, Legs, Voice | Physical world |
| **Robot** | Camera, Infrared sensor | Motors, Grippers | Factory floor |
| **Software agent** | Keyboard input, File input | Screen output, File output | Computer / Internet |
| **Self-driving car** | Camera, LIDAR, GPS | Steering, Brakes, Accelerator | Roads, Traffic |

### Important Terms:
- **Percept:** A single input received by the agent at a given time
- **Percept Sequence:** The complete history of all percepts ever received
- **Agent Function:** Maps any percept sequence to an action (mathematical/abstract)
- **Agent Program:** The actual code/implementation that runs on a machine

> **Agent Function** is the concept (theory), **Agent Program** is the implementation (code).

---

## 6. Structure of Intelligent Agents

An agent = **Architecture + Program**

- **Architecture:** The physical or virtual machine (hardware/software platform)
- **Program:** The logic/algorithm that decides what action to take based on percepts

```
Agent = Architecture + Program
```

### The Agent Program takes the current percept as input and returns an action:

```
function AGENT_PROGRAM(percept):
    // use percept to decide
    return action
```

---

## 7. Types of Agents

There are **5 types** of agents, going from simplest to most complex:

### 7.1 Simple Reflex Agent
- Acts **only** on the **current percept** (ignores history).
- Uses **condition-action rules** (IF-THEN rules).
- **No memory** of past.

```
IF car_in_front_is_braking THEN apply_brakes
IF traffic_light_is_red THEN stop
```

**Advantages:** Simple, fast
**Disadvantages:** Cannot handle situations where current percept alone isn't enough. Fails in **partially observable** environments.

```
┌──────────────────────────────┐
│     Simple Reflex Agent      │
│                              │
│  Percept → Condition-Action  │
│              Rules           │
│                → Action      │
└──────────────────────────────┘
```

---

### 7.2 Model-Based Reflex Agent
- Maintains an **internal model** (state) of the world.
- Keeps track of parts of the world it **can't see right now**.
- Two key things it tracks:
  1. **How the world evolves** (independent of the agent)
  2. **How the agent's actions affect the world**

```
IF I_was_going_straight AND I_turned_left THEN I_am_now_facing_west
```

**Advantage:** Can work in partially observable environments.
**Disadvantage:** The internal model may be inaccurate.

```
┌──────────────────────────────────┐
│   Model-Based Reflex Agent       │
│                                  │
│  Percept → Update Internal State │
│               ↓                  │
│  Internal State → Condition-     │
│               Action Rules       │
│                    → Action      │
└──────────────────────────────────┘
```

---

### 7.3 Goal-Based Agent
- Has **goals** (what it wants to achieve).
- Considers **future actions** and their outcomes.
- Uses **search and planning** to find a sequence of actions that reaches the goal.

```
Goal: Reach Airport
Current State: At Home
→ Search for route → Take actions step by step
```

**Advantage:** More flexible — can change behavior when goals change.
**Disadvantage:** Slower — needs to search/plan before acting.

---

### 7.4 Utility-Based Agent
- Not just "Did I reach the goal?" but "**How well** did I reach it?"
- Uses a **utility function** that assigns a number (happiness score) to each state.
- Chooses the action that **maximizes expected utility**.

```
Two routes to airport:
  Route A: 30 min, smooth road     → Utility = 0.9
  Route B: 25 min, heavy traffic   → Utility = 0.6
→ Choose Route A (higher utility)
```

**Advantage:** Can make trade-offs, handles uncertainty well.
**Disadvantage:** Computing utility for every option can be expensive.

---

### 7.5 Learning Agent
- Can **learn** and **improve** from experience.
- Has 4 components:
  1. **Learning Element** — learns from experience, improves performance
  2. **Performance Element** — selects actions (this is the actual agent from before)
  3. **Critic** — gives feedback on how well the agent is doing
  4. **Problem Generator** — suggests new exploratory actions to learn more

```
┌──────────────────────────────────────┐
│         Learning Agent               │
│                                      │
│  ┌──────────┐    ┌───────────────┐   │
│  │  Critic   │←──│ Performance   │   │
│  └────┬─────┘    │   Element     │   │
│       │          └───────┬───────┘   │
│       ↓                  ↑           │
│  ┌──────────┐    ┌───────────────┐   │
│  │ Learning  │──→│   Problem     │   │
│  │ Element   │   │  Generator    │   │
│  └──────────┘    └───────────────┘   │
└──────────────────────────────────────┘
```

**Example:** A chess-playing AI that learns from past games.

---

## 8. Agent Environments

The **environment** is the world in which the agent operates. Environments have different properties:

### 8.1 Properties of Environments (IMPORTANT!)

| Property | Option A | Option B | Meaning |
|----------|----------|----------|---------|
| **Observable** | Fully Observable | Partially Observable | Can the agent see the COMPLETE state of the environment? |
| **Deterministic** | Deterministic | Stochastic | Is the next state completely determined by current state + action? |
| **Episodic** | Episodic | Sequential | Are decisions independent (episodes) or do past decisions affect future? |
| **Static** | Static | Dynamic | Does the environment change while the agent is thinking? |
| **Discrete** | Discrete | Continuous | Are there finite or infinite states/actions? |
| **Agents** | Single Agent | Multi-Agent | Is the agent alone or are there other agents? |
| **Known** | Known | Unknown | Does the agent know the rules of the environment? |

### Examples:

| Environment | Observable | Deterministic | Episodic | Static | Discrete | Agents |
|-------------|-----------|---------------|----------|--------|----------|--------|
| **Chess** | Fully | Deterministic | Sequential | Semi-dynamic | Discrete | Multi |
| **Poker** | Partially | Stochastic | Sequential | Static | Discrete | Multi |
| **Self-driving car** | Partially | Stochastic | Sequential | Dynamic | Continuous | Multi |
| **Crossword puzzle** | Fully | Deterministic | Sequential | Static | Discrete | Single |
| **Image classification** | Fully | Deterministic | Episodic | Static | Discrete | Single |

### Detailed Explanations:

**Fully vs Partially Observable:**
- **Fully:** Agent can see everything. Chess → you see all pieces on the board.
- **Partially:** Agent can't see everything. Poker → you don't know other players' cards.

**Deterministic vs Stochastic:**
- **Deterministic:** Same action from same state → always same result. Chess → moving a piece always works.
- **Stochastic:** Randomness involved. Poker → next card is random.

**Episodic vs Sequential:**
- **Episodic:** Each decision is independent. Quality check on a factory line → each item is checked independently.
- **Sequential:** Past decisions affect future. Chess → each move changes the entire game.

**Static vs Dynamic:**
- **Static:** Environment doesn't change while you think. Chess (without a clock).
- **Dynamic:** Environment changes while you think. Self-driving car → other cars keep moving.
- **Semi-dynamic:** Environment doesn't change but your score/time does. Chess with a clock.

**Discrete vs Continuous:**
- **Discrete:** Finite number of states/actions. Chess → finite positions.
- **Continuous:** Infinite states/actions. Self-driving car → steering angle can be any value.

---

## 9. PEAS Representation

**PEAS** = **P**erformance measure, **E**nvironment, **A**ctuators, **S**ensors

PEAS is a framework to **describe an agent completely**. Before designing any agent, we must define its PEAS.

### Examples:

#### 1. Automated Taxi Driver
| Component | Description |
|-----------|-------------|
| **Performance** | Safe, fast, legal, comfortable ride, maximize profit |
| **Environment** | Roads, traffic, pedestrians, weather, other vehicles |
| **Actuators** | Steering, accelerator, brake, signal, horn, display |
| **Sensors** | Camera, LIDAR, GPS, speedometer, odometer, engine sensors |

#### 2. Medical Diagnosis System
| Component | Description |
|-----------|-------------|
| **Performance** | Correct diagnosis, minimize costs, minimize patient suffering |
| **Environment** | Patient, hospital, staff |
| **Actuators** | Screen display (diagnosis, prescriptions, tests to recommend) |
| **Sensors** | Keyboard input (symptoms), patient history database |

#### 3. Vacuum Cleaner Agent
| Component | Description |
|-----------|-------------|
| **Performance** | Cleanliness, efficiency (time, battery) |
| **Environment** | Room with dirt, obstacles, floors |
| **Actuators** | Wheels (move), vacuum motor (suck), brushes |
| **Sensors** | Dirt sensor, bump sensor, infrared sensor |

#### 4. Online Shopping Agent
| Component | Description |
|-----------|-------------|
| **Performance** | Best price, quality, reliability of seller |
| **Environment** | E-commerce websites, product listings, user reviews |
| **Actuators** | Display results, place order, make payment |
| **Sensors** | Web pages (HTML content), user input (preferences) |

#### 5. Chess Playing Agent
| Component | Description |
|-----------|-------------|
| **Performance** | Winning, maximizing score |
| **Environment** | Chess board, opponent, clock |
| **Actuators** | Move pieces on the board (digital or physical) |
| **Sensors** | Camera / Board state input |

---

## 10. Application Areas of AI (Self-Learning)

| Domain | Applications |
|--------|-------------|
| **Healthcare** | Disease diagnosis, drug discovery, robotic surgery |
| **Finance** | Fraud detection, stock trading, credit scoring |
| **Transportation** | Self-driving cars, route optimization, traffic management |
| **Education** | Adaptive learning, automated grading, chatbot tutors |
| **Gaming** | Game playing (chess, Go), NPC behavior, game testing |
| **Manufacturing** | Quality control, predictive maintenance, robotic assembly |
| **Security** | Face recognition, cyber threat detection, surveillance |
| **Agriculture** | Crop monitoring, yield prediction, pest detection |
| **Retail** | Recommendation systems, demand forecasting, chatbots |
| **Natural Language** | Translation, summarization, sentiment analysis, voice assistants |

---

## Summary Table

| Topic | Key Points |
|-------|-----------|
| AI Definition | Making machines think/act intelligently |
| Turing Test | If machine fools human → it's intelligent |
| Problem Formulation | Initial state, Actions, Goal test, Path cost |
| Agent | Perceives (sensors) + Acts (actuators) |
| 5 Agent Types | Simple Reflex → Model-Based → Goal-Based → Utility-Based → Learning |
| Environment Properties | Observable, Deterministic, Episodic, Static, Discrete, Agents |
| PEAS | Performance, Environment, Actuators, Sensors |

---
