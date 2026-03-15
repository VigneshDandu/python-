# Question Bank with Answers — Modules 1 & 2
## ITC604 | AI and DS – 1

---

# MODULE I — Introduction to AI

---

## Q1. Define Artificial Intelligence. State its goals.

**Answer:**

**Definition:** Artificial Intelligence (AI) is the branch of computer science that deals with creating machines or software that can perform tasks that normally require human intelligence — such as reasoning, learning, problem-solving, perception, and language understanding.

> "AI is the study of how to make computers do things at which, at the moment, people are better." — Elaine Rich

**Goals of AI (4 approaches to AI):**

| Approach | Goal |
|----------|------|
| **Thinking Humanly** | Build systems that think like humans (Cognitive Modeling) |
| **Acting Humanly** | Build systems that act like humans (Turing Test) |
| **Thinking Rationally** | Build systems that think using logic (Laws of Thought) |
| **Acting Rationally** | Build systems that act to achieve the best outcome (Rational Agent) |

The current mainstream goal is **acting rationally** — building rational agents that make the best decisions to achieve their goals.

---

## Q2. Explain the Turing Test. What capabilities must a machine have to pass it?

**Answer:**

The **Turing Test** was proposed by **Alan Turing in 1950** to determine whether a machine can exhibit intelligent behavior.

**How it works:**
- A human **interrogator** communicates (via text) with both a **human** and a **machine** without knowing which is which.
- The interrogator asks questions to both.
- If the interrogator **cannot reliably distinguish** the machine from the human, the machine is said to have passed the Turing Test.

**Capabilities needed to pass:**
1. **Natural Language Processing (NLP):** To communicate in English (or any language)
2. **Knowledge Representation:** To store information and facts
3. **Automated Reasoning:** To answer questions and draw new conclusions from stored knowledge
4. **Machine Learning:** To adapt to new situations and detect patterns

For the **Total Turing Test** (includes physical interaction):
5. **Computer Vision:** To perceive objects
6. **Robotics:** To manipulate objects and move

---

## Q3. What is an intelligent agent? Explain its structure.

**Answer:**

An **intelligent agent** is an entity that:
- **Perceives** its environment through **sensors**
- **Acts** upon the environment through **actuators**

**Structure:** Agent = Architecture + Program

- **Architecture:** The computing device with sensors and actuators (physical or virtual)
- **Agent Program:** The function that maps percept sequences to actions

```
Environment → Sensors → [Agent Program] → Actuators → Environment
                              ↕
                        Agent Architecture
```

**Key terms:**
- **Percept:** Single input at one time
- **Percept Sequence:** Complete history of inputs
- **Agent Function:** Abstract mathematical mapping (percept sequence → action)
- **Agent Program:** Concrete implementation of the agent function

---

## Q4. Explain the types of agents with examples.

**Answer:**

There are **5 types** of agents:

### 1. Simple Reflex Agent
- Acts based on **current percept only** (no memory)
- Uses **IF-THEN (condition-action) rules**
- Example: Thermostat — IF temperature > 25°C THEN turn on AC
- **Limitation:** Fails in partially observable environments

### 2. Model-Based Reflex Agent
- Maintains an **internal model** of the world (keeps track of what it can't see)
- Updates internal state based on:
  - How the world evolves independently
  - How the agent's actions affect the world
- Example: A car's lane-keeping system that remembers where other cars were

### 3. Goal-Based Agent
- Has explicit **goals** and plans actions to achieve them
- Uses **search and planning** to decide what to do
- More flexible — behavior changes when goals change
- Example: GPS navigation — goal is to reach destination, plans the route

### 4. Utility-Based Agent
- Uses a **utility function** that measures "how happy" a state makes the agent
- Chooses actions that **maximize expected utility**
- Can make trade-offs between conflicting goals
- Example: Self-driving car choosing between a fast but rough road vs slow but smooth road

### 5. Learning Agent
- Can **improve** its performance through experience
- Components: Learning Element, Performance Element, Critic, Problem Generator
- Example: Chess AI that learns from past games to improve strategy

---

## Q5. Explain the properties of agent environments with examples.

**Answer:**

| Property | Description | Example |
|----------|-------------|---------|
| **Fully Observable** vs **Partially Observable** | Can the agent see the entire environment? | Chess (fully) vs Poker (partially — can't see opponent's cards) |
| **Deterministic** vs **Stochastic** | Is the outcome of an action certain? | Chess (deterministic) vs Dice games (stochastic — random outcomes) |
| **Episodic** vs **Sequential** | Are decisions independent? | Image classification (episodic — each image independent) vs Chess (sequential — each move affects future) |
| **Static** vs **Dynamic** | Does environment change while agent thinks? | Crossword (static) vs Self-driving car (dynamic — traffic keeps moving) |
| **Discrete** vs **Continuous** | Finite or infinite states/actions? | Chess (discrete — finite positions) vs Driving (continuous — infinite steering angles) |
| **Single Agent** vs **Multi-Agent** | One agent or many? | Puzzle solving (single) vs Chess (multi-agent — opponent exists) |
| **Known** vs **Unknown** | Does agent know the rules? | Chess (known rules) vs Exploring a new planet (unknown) |

**Semi-dynamic:** Environment doesn't change but performance score does (e.g., chess with a clock).

---

## Q6. Explain PEAS representation with examples for any TWO agents.

**Answer:**

**PEAS** stands for **Performance measure, Environment, Actuators, Sensors** — a framework to completely describe an agent.

### Agent 1: Automated Taxi Driver

| PEAS | Description |
|------|-------------|
| **Performance** | Safe, legal, comfortable, fast ride; maximize profits; minimize fuel |
| **Environment** | Roads, other vehicles, pedestrians, traffic signals, weather |
| **Actuators** | Steering wheel, accelerator, brake, horn, signal lights, display |
| **Sensors** | Cameras, LIDAR, GPS, speedometer, microphone, engine sensors |

### Agent 2: Medical Diagnosis System

| PEAS | Description |
|------|-------------|
| **Performance** | Correct diagnosis, minimize unnecessary tests, minimize patient cost |
| **Environment** | Patient, hospital, medical staff, medical history database |
| **Actuators** | Display screen (shows diagnosis, prescriptions, recommended tests) |
| **Sensors** | Keyboard/forms (patient symptoms input), database access (medical records) |

---

## Q7. What is problem formulation? Explain its components with an example.

**Answer:**

**Problem formulation** is the process of defining a problem precisely so that an AI agent can search for a solution.

**Components:**

| Component | Meaning | Example (Route Finding) |
|-----------|---------|------------------------|
| **Initial State** | Starting configuration | Current city (e.g., Arad) |
| **Actions** | Possible moves from any state | Drive to adjacent city |
| **Transition Model** | Result of performing an action | Result(Arad, GoTo_Sibiu) = Sibiu |
| **Goal Test** | Check if goal is reached | Am I in Bucharest? |
| **Path Cost** | Cost of the solution path | Sum of road distances |

**State Space** = Set of all possible states reachable by any sequence of actions from the initial state. It can be represented as a graph where nodes are states and edges are actions.

---

## Q8. Differentiate between Agent Function and Agent Program.

**Answer:**

| Aspect | Agent Function | Agent Program |
|--------|---------------|---------------|
| **Nature** | Abstract / Mathematical | Concrete / Implementation |
| **Definition** | Maps every possible percept sequence to an action | Code that runs on the architecture |
| **Representation** | Table with infinite entries | Actual algorithm/code |
| **Size** | Can be infinite (all possible percept histories) | Finite (implemented in code) |
| **Example** | f: {all percept sequences} → {actions} | Python/Java code that processes input and returns action |

The agent program is a **practical implementation** of the (potentially infinite) agent function.

---

## Q9. List and explain AI techniques.

**Answer:**

AI techniques are methods used to build intelligent systems. A good AI technique should:
1. **Generalize** to many problems
2. **Handle uncertainty** and incomplete information
3. Be **computationally efficient**
4. Allow **human understanding** of the reasoning

**Major AI Techniques:**

1. **Search:** Systematically exploring possible solutions (BFS, DFS, A*)
2. **Knowledge Representation:** Storing facts and relationships (logic, semantic networks, frames)
3. **Reasoning:** Drawing conclusions from known facts (forward/backward chaining)
4. **Machine Learning:** Learning patterns from data (classification, regression, clustering)
5. **Natural Language Processing:** Understanding and generating human language
6. **Computer Vision:** Understanding images and videos
7. **Planning:** Creating sequences of actions to achieve goals
8. **Probabilistic Reasoning:** Handling uncertainty (Bayesian networks)

---

## Q10. Give PEAS representation for: Vacuum Cleaner, Chess Agent, Online Shopping Agent.

**Answer:**

### Vacuum Cleaner Agent
| PEAS | Description |
|------|-------------|
| **P** | Cleanliness of floor, battery life, time taken, area covered |
| **E** | Room, floor, dirt, obstacles, furniture |
| **A** | Wheels (move forward/turn), suction motor, brushes |
| **S** | Dirt sensor, bump sensor, infrared sensor, cliff sensor |

### Chess Playing Agent
| PEAS | Description |
|------|-------------|
| **P** | Win/Loss/Draw, rating points, time per move |
| **E** | Chess board (8×8), pieces, opponent, clock |
| **A** | Move piece to a position on the board |
| **S** | Board state (position of all pieces), clock reading |

### Online Shopping Agent
| PEAS | Description |
|------|-------------|
| **P** | Lowest price found, quality, delivery time, reliability |
| **E** | E-commerce websites, product databases, user reviews, payment systems |
| **A** | Web search, display products, place order, submit payment |
| **S** | Web page content (HTML/APIs), user preferences input, price data |

---

---

# MODULE II — Search Techniques

---

## Q11. Explain Uniform Cost Search with an example.

**Answer:**

**Uniform Cost Search (UCS)** expands the node with the **lowest total path cost g(n)** first. It uses a **Priority Queue**.

**Algorithm:**
1. Initialize frontier with start node (cost 0)
2. Repeat:
   - Remove node with lowest g(n) from priority queue
   - If goal → return solution
   - Add to explored set
   - For each successor: compute path cost, add to frontier if not explored

**Example:**
```
        S (Start)
      /    \
   (1)      (5)
   /          \
  A            B
   \          /
   (3)     (2)
     \     /
       G (Goal)
```

| Step | Frontier (node: g(n)) | Action |
|------|----------------------|--------|
| 1 | {S: 0} | Expand S |
| 2 | {A: 1, B: 5} | Expand A (lowest cost) |
| 3 | {G: 4, B: 5} | Expand G (lowest cost) |
| 4 | **G is the goal!** | Path: S→A→G, Cost = 4 |

UCS finds S→A→G (cost 4) instead of S→B→G (cost 7). ✅ Optimal!

**Properties:**
- **Complete:** Yes (if costs > 0)
- **Optimal:** Yes — always finds cheapest path
- **Time/Space:** O(b^(1 + ⌊C*/ε⌋)) where C* = optimal cost, ε = min step cost

---

## Q12. Explain Depth-Limited Search and Iterative Deepening DFS.

**Answer:**

### Depth-Limited Search (DLS)
DFS with a **depth limit L** — it won't explore beyond depth L.

- Solves the problem of DFS going infinitely deep
- If goal is within depth L → finds it
- If goal is deeper than L → fails (returns "cutoff")
- **Complete:** Only if d ≤ L
- **Optimal:** No
- **Time:** O(b^L), **Space:** O(bL)

**Problem:** Choosing the right L. If unknown, the solution depth might be missed.

### Iterative Deepening DFS (IDDFS)
Solves the depth limit problem by running DLS with **increasing limits: 0, 1, 2, 3, ...**

```
Iteration 1: DLS(limit=0)  → search only root
Iteration 2: DLS(limit=1)  → search depth 0-1
Iteration 3: DLS(limit=2)  → search depth 0-2
... continue until goal found
```

**Key insight:** Repeating work is NOT wasteful because most nodes are at the deepest level. Only ~11% more nodes are generated compared to BFS.

**Properties:**
- **Complete:** ✅ Yes
- **Optimal:** ✅ Yes (uniform step costs)
- **Time:** O(b^d) — same as BFS
- **Space:** O(bd) — same as DFS!

> **IDDFS is the preferred uninformed search** when the solution depth is unknown.

---

## Q13. Explain Bidirectional Search. What are its advantages and requirements?

**Answer:**

**Bidirectional Search** runs **two simultaneous searches:**
- **Forward search** from start state
- **Backward search** from goal state
- They **meet in the middle** → solution found

```
Start →→→ ● ● ● ●
                   ↕  MEET
Goal  →→→ ● ● ● ●
```

**Advantages:**
- Dramatically reduces the search space
- Time complexity: **O(b^(d/2))** instead of O(b^d)
- Example: b=10, d=6 → BFS: 10^6 = 1,000,000 nodes. Bidirectional: 2×10^3 = 2,000 nodes

**Requirements:**
1. Goal state must be **explicitly known** (not just a goal test)
2. Must be able to generate **predecessors** (search backward)
3. Need efficient check for intersection between the two frontiers
4. Must decide which search strategy to use for each direction

**Properties:**
- **Complete:** Yes (when BFS is used for both)
- **Optimal:** Yes (uniform costs, BFS both sides)
- **Space:** O(b^(d/2)) — must store both frontiers

---

## Q14. What is a heuristic function? Explain admissibility and consistency.

**Answer:**

### Heuristic Function h(n)
A heuristic is a function that **estimates the cost** from node n to the nearest goal. It provides "extra knowledge" to guide search.

- h(n) ≥ 0 for all n
- h(goal) = 0

**Examples:**
- 8-puzzle: h₁ = misplaced tiles, h₂ = Manhattan distance
- Route finding: h = straight-line distance to goal

### Admissible Heuristic
A heuristic is **admissible** if it **never overestimates** the true cost:

$$h(n) \leq h^*(n)$$

where h*(n) is the actual minimum cost from n to goal.

**Example:** Straight-line distance ≤ actual road distance (roads can't be shorter than a straight line). So straight-line distance is admissible.

**Importance:** If h is admissible, A* is guaranteed to find the optimal solution (in tree search).

### Consistent (Monotonic) Heuristic
A heuristic is **consistent** if for every node n and successor n':

$$h(n) \leq c(n, n') + h(n')$$

(Triangle inequality — direct estimate ≤ step cost + estimate from successor)

**Properties:**
- Every consistent heuristic is admissible (but not vice versa)
- Consistency guarantees A* optimality in graph search
- f(n) values along any path are non-decreasing

### Dominance
h₂ **dominates** h₁ if h₂(n) ≥ h₁(n) for all n. A dominant heuristic is better (more informative, explores fewer nodes).

---

## Q15. Explain A* Search algorithm. Prove that A* is optimal.

**Answer:**

### A* Search
A* uses evaluation function: **f(n) = g(n) + h(n)**
- g(n) = actual cost from start to n
- h(n) = estimated cost from n to goal
- f(n) = estimated total cost of the path through n

Expands the node with the **lowest f(n)** using a priority queue.

### Example:
```
Start S, Goal G
         S
       / | \
    (1) (4) (5)
    /    |    \
   A     B     C
   |     |     
  (7)   (2)    
   |     |     
   G     G     

h(S)=6, h(A)=5, h(B)=2, h(C)=0

Node S: f = 0+6 = 6
Node A: f = 1+5 = 6
Node B: f = 4+2 = 6
Node C: f = 5+0 = 5  ← expand first

Then A: f=6, B: f=6
B's child G: f = 4+2+0 = 6
A's child G: f = 1+7+0 = 8

A* picks G via B (cost 6) → Optimal! ✅
```

### Proof of Optimality:
**Theorem:** If h(n) is admissible, A* returns an optimal solution.

**Proof (by contradiction):**
- Suppose A* returns a suboptimal goal G₂ with g(G₂) > C* (where C* = optimal cost)
- Let n be a node on the optimal path that is still in the frontier
- For node n on optimal path: f(n) = g(n) + h(n) ≤ g(n) + h*(n) = C* (since h is admissible, h(n) ≤ h*(n))
- So f(n) ≤ C*
- For suboptimal goal G₂: f(G₂) = g(G₂) + h(G₂) = g(G₂) + 0 = g(G₂) > C*
- So f(n) ≤ C* < f(G₂)
- This means A* would have expanded n before G₂, contradicting our assumption
- Therefore, A* never returns a suboptimal solution ∎

---

## Q16. Explain Best-First (Greedy) Search. Compare it with A*.

**Answer:**

### Greedy Best-First Search
- Uses **f(n) = h(n)** (heuristic only, ignores actual path cost)
- Expands the node that **appears** closest to goal
- "Greedy" because it tries to get to the goal as quickly as possible

| Property | Greedy Best-First | A* Search |
|----------|------------------|-----------|
| **Evaluation** | f(n) = h(n) | f(n) = g(n) + h(n) |
| **Considers past cost?** | ❌ No | ✅ Yes |
| **Considers future estimate?** | ✅ Yes | ✅ Yes |
| **Complete?** | ❌ No (can loop) | ✅ Yes |
| **Optimal?** | ❌ No | ✅ Yes (if h admissible) |
| **Time** | O(b^m) worst | O(b^d) worst |
| **Space** | O(b^m) | O(b^d) |
| **Speed in practice** | Fast with good h | Slower but finds optimal path |

**Example showing Greedy is not optimal:**

If greedy finds path with cost 450 but optimal path costs 418, greedy goes wrong because it ignores the actual cost already spent (g(n)).

A* avoids this by considering BOTH g(n) and h(n).

---

## Q17. Explain Hill Climbing algorithm. What are its drawbacks?

**Answer:**

**Hill Climbing** is a local search algorithm that continuously moves to the **best neighboring state**.

### Algorithm:
```
current = initial state
loop:
    neighbor = best successor of current
    if neighbor is not better than current:
        return current   ← stuck!
    current = neighbor
```

### Types:
1. **Simple:** Pick first better neighbor
2. **Steepest-Ascent:** Evaluate all neighbors, pick the best
3. **Stochastic:** Randomly pick among better neighbors

### Drawbacks (Problems):

**1. Local Maximum:**
- A peak that is NOT the global maximum
- All neighbors are worse, so algorithm stops
- But the true best solution is elsewhere

**2. Plateau (Flat Region):**
- A flat area where all neighbors have the same evaluation value
- Algorithm doesn't know which direction to move

**3. Ridge:**
- A narrow elevated area that doesn't align with the search directions
- Algorithm oscillates without making progress

### Solutions:
| Problem | Solution |
|---------|----------|
| Local Max | **Random Restart** — restart from random positions, keep best result |
| Plateau | **Sideways Moves** — allow limited moves to equal-value neighbors |
| All | **Simulated Annealing** — allow controlled bad moves |
| All | **Stochastic Hill Climbing** — add randomness |

---

## Q18. Explain Simulated Annealing. How does it overcome the limitations of Hill Climbing?

**Answer:**

**Simulated Annealing** is inspired by the **metallurgy process** where metals are heated and slowly cooled to remove defects.

### Algorithm:
```
current = initial state
for t = 1 to ∞:
    T = temperature_schedule(t)    // T decreases over time
    if T == 0: return current      // frozen — done!
    next = random neighbor
    ΔE = value(next) - value(current)
    if ΔE > 0:                     // next is BETTER
        current = next             // always accept
    else:                          // next is WORSE
        accept with probability e^(ΔE/T)
```

### How it overcomes Hill Climbing's problems:

1. **Escapes Local Maxima:** Unlike hill climbing, SA **accepts worse moves** with some probability. Early on (high T), it frequently accepts bad moves, allowing it to jump out of local maxima.

2. **Handles Plateaus:** Random moves help navigate flat regions where hill climbing gets stuck.

3. **Controlled Exploration vs Exploitation:**
   - **High T (early):** Explores widely, accepts most moves (like random walk)
   - **Low T (late):** Exploits locally, mostly accepts improvements (like hill climbing)
   - This transition from exploration to exploitation is the key advantage

4. **Probability of accepting bad moves:**
   - e^(ΔE/T) depends on both how bad the move is (ΔE) and the temperature (T)
   - Very bad moves are less likely to be accepted
   - As T decreases, fewer bad moves are accepted
   - When T ≈ 0, it becomes pure hill climbing

5. **Theoretical guarantee:** If cooled slowly enough, simulated annealing **will find the global optimum** with probability approaching 1.

---

## Q19. Explain the Water Jug Problem. Solve it using state space search.

**Answer:**

### Problem:
- Jug A: 4-liter capacity
- Jug B: 3-liter capacity
- Goal: Get exactly 2 liters in Jug A
- Unlimited water supply (tap)

### State: (a, b) where a = liters in A, b = liters in B

### Operators:
| # | Operation | Precondition | Result |
|---|-----------|-------------|--------|
| 1 | Fill A | a < 4 | (4, b) |
| 2 | Fill B | b < 3 | (a, 3) |
| 3 | Empty A | a > 0 | (0, b) |
| 4 | Empty B | b > 0 | (a, 0) |
| 5 | Pour A→B | a>0, b<3 | (a-d, b+d), d=min(a,3-b) |
| 6 | Pour B→A | b>0, a<4 | (a+d, b-d), d=min(b,4-a) |

### Solution:

| Step | State (A, B) | Operation |
|------|-------------|-----------|
| 0 | (0, 0) | Start |
| 1 | (4, 0) | Fill A |
| 2 | (1, 3) | Pour A→B (pour 3 liters) |
| 3 | (1, 0) | Empty B |
| 4 | (0, 1) | Pour A→B (pour 1 liter) |
| 5 | (4, 1) | Fill A |
| 6 | **(2, 3)** | Pour A→B (pour 2 liters) ✅ **GOAL!** |

**Alternative Solution:**

| Step | State (A, B) | Operation |
|------|-------------|-----------|
| 0 | (0, 0) | Start |
| 1 | (0, 3) | Fill B |
| 2 | (3, 0) | Pour B→A |
| 3 | (3, 3) | Fill B |
| 4 | (4, 2) | Pour B→A (pour 1 liter, A is full) |
| 5 | (0, 2) | Empty A |
| 6 | **(2, 0)** | Pour B→A ✅ **GOAL!** |

---

## Q20. Explain the Crypto-Arithmetic Problem. Solve SEND + MORE = MONEY.

**Answer:**

### Crypto-Arithmetic Problem:
A puzzle where each **letter represents a unique digit (0-9)**, and the arithmetic equation must hold true.

### Problem: SEND + MORE = MONEY

```
    S E N D
  + M O R E
  ---------
  M O N E Y
```

### Constraints:
1. Each letter = unique digit (0-9)
2. S ≠ 0, M ≠ 0 (leading digits can't be 0)
3. Column arithmetic must be satisfied

### Column Analysis (right to left, with carries C₁, C₂, C₃, C₄):

- **Column 1:** D + E = Y + 10×C₁
- **Column 2:** N + R + C₁ = E + 10×C₂
- **Column 3:** E + O + C₂ = N + 10×C₃
- **Column 4:** S + M + C₃ = O + 10×C₄
- **Column 5:** C₄ = M

### Solution:
From Column 5: C₄ = M, and since carry is 0 or 1 → **M = 1**
From Column 4: S + 1 + C₃ = O + 10 → S + C₃ = O + 9
Since S is max 9: S = 9, C₃ = 0, O = 0 OR S = 9, C₃ = 1, O = 0
→ **S = 9, O = 0**

Working through remaining constraints:
- **E = 5, N = 6, D = 7, R = 8, Y = 2**

### Verification:
```
    9 5 6 7
  + 1 0 8 5
  ---------
  1 0 6 5 2

  9567 + 1085 = 10652 ✅
```

---

## Q21. Explain the Graph Coloring Problem as a CSP.

**Answer:**

### Problem:
Assign colors to nodes of a graph such that **no two adjacent nodes share the same color**, using at most k colors.

### CSP Formulation:
- **Variables:** One variable per node → {X₁, X₂, ..., Xₙ}
- **Domains:** Set of available colors → {Red, Green, Blue, ...}
- **Constraints:** For each edge (Xᵢ, Xⱼ): Xᵢ ≠ Xⱼ

### Example: Map Coloring (Australia with 3 colors)

**Variables:** WA, NT, SA, Q, NSW, V, T

**Domains:** {Red, Green, Blue} for each variable

**Constraints (adjacency):**
WA ≠ NT, WA ≠ SA, NT ≠ SA, NT ≠ Q, SA ≠ Q, SA ≠ NSW, SA ≠ V, Q ≠ NSW, NSW ≠ V

**Solution:**
| Region | Color |
|--------|-------|
| WA | Red |
| NT | Green |
| SA | Blue |
| Q | Red |
| NSW | Green |
| V | Red |
| T | Red |

### Solving Methods:
1. **Backtracking:** Assign values one by one; if conflict → undo and try another
2. **Constraint Propagation (AC-3):** Remove values from domains that violate constraints
3. **MRV (Minimum Remaining Values):** Choose variable with fewest legal values next
4. **Forward Checking:** After assigning a value, remove inconsistent values from neighbors' domains

---

## Q22. Explain Minimax algorithm with an example.

**Answer:**

### Minimax Algorithm:
Used in **two-player zero-sum games** where:
- **MAX** player wants to **maximize** the score
- **MIN** player wants to **minimize** the score

### Algorithm:
1. Generate the complete game tree
2. Apply utility values to terminal states
3. Propagate values upward:
   - MAX nodes → take the **maximum** child value
   - MIN nodes → take the **minimum** child value

### Example:
```
                    A (MAX)
                   / \
                  B   C       (MIN)
                / \   / \
               D   E F   G   (MAX)
              /\ /\ /\ /\
             3 5 6 9 1 2 0 7  (Terminal values)
```

**Step-by-step evaluation:**

| Node | Type | Children Values | Chosen Value |
|------|------|----------------|-------------|
| D | MAX | 3, 5 | max(3,5) = **5** |
| E | MAX | 6, 9 | max(6,9) = **9** |
| F | MAX | 1, 2 | max(1,2) = **2** |
| G | MAX | 0, 7 | max(0,7) = **7** |
| B | MIN | 5, 9 | min(5,9) = **5** |
| C | MIN | 2, 7 | min(2,7) = **2** |
| **A** | **MAX** | **5, 2** | **max(5,2) = 5** |

**Result:** MAX chooses move to B (value 5).

**Properties:**
- Complete: Yes (finite tree)
- Optimal: Yes (against optimal opponent)
- Time: O(b^m)
- Space: O(bm)

---

## Q23. Explain Alpha-Beta Pruning with a detailed example.

**Answer:**

### Alpha-Beta Pruning:
An optimization of Minimax that **prunes (skips) branches** that cannot affect the final decision. Returns the **same result as Minimax** but faster.

### Key Variables:
- **α (Alpha):** Best value MAX can guarantee (initially -∞)
- **β (Beta):** Best value MIN can guarantee (initially +∞)
- **Prune when:** α ≥ β

### Rules:
- **MAX node:** α = max(α, child_value). If α ≥ β → prune remaining children
- **MIN node:** β = min(β, child_value). If α ≥ β → prune remaining children

### Example:
```
                    A (MAX)
                   / \
                  B   C       (MIN)
                / \   / \
               D   E F   G   (Terminal)
               3   5 1   ?   
```

**Trace:**

| Step | Node | α | β | Action |
|------|------|---|---|--------|
| 1 | A (MAX) | -∞ | +∞ | Visit B |
| 2 | B (MIN) | -∞ | +∞ | Visit D=3 |
| 3 | B (MIN) | -∞ | 3 | β=min(∞,3)=3. Visit E=5 |
| 4 | B (MIN) | -∞ | 3 | β=min(3,5)=3. Return 3 |
| 5 | A (MAX) | 3 | +∞ | α=max(-∞,3)=3. Visit C |
| 6 | C (MIN) | 3 | +∞ | Visit F=1 |
| 7 | C (MIN) | 3 | 1 | β=min(∞,1)=1. **α(3) ≥ β(1) → PRUNE G!** ✂ |
| 8 | C | - | - | Return 1 |
| 9 | **A** | 3 | +∞ | max(3,1) = **3** |

**Why G was pruned:** MAX already has value 3 from B. C's value will be ≤ 1 (since MIN found 1). MAX will never choose C over B, so G doesn't matter.

### Effectiveness:
- **Best case** (perfect ordering): O(b^(m/2)) — effectively **doubles the search depth**
- **Worst case** (worst ordering): O(b^m) — no improvement
- **Move ordering** is critical — try best moves first for maximum pruning

---

## Q24. Compare Uninformed and Informed search strategies.

**Answer:**

| Aspect | Uninformed Search | Informed Search |
|--------|------------------|-----------------|
| **Other name** | Blind Search | Heuristic Search |
| **Uses extra knowledge?** | ❌ No | ✅ Yes (heuristic function) |
| **Efficiency** | Less efficient | More efficient |
| **Search direction** | Systematic/Exhaustive | Guided toward goal |
| **Examples** | BFS, DFS, UCS, IDDFS | Greedy Best-First, A* |
| **Speed** | Slow for large spaces | Faster with good heuristic |
| **Evaluation function** | None or g(n) only | h(n) or g(n)+h(n) |
| **When to use** | No domain knowledge available | Domain knowledge available |

---

## Q25. Compare BFS, DFS, UCS, IDDFS, A*. (Table format)

**Answer:**

| Property | BFS | DFS | UCS | IDDFS | A* |
|----------|-----|-----|-----|-------|-----|
| **Data Structure** | FIFO Queue | LIFO Stack | Priority Queue (by g) | Stack (repeated) | Priority Queue (by g+h) |
| **Expands** | Shallowest | Deepest | Cheapest | Shallowest (with depth limit) | Lowest f(n) |
| **Complete** | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Optimal** | ✅* | ❌ | ✅ | ✅* | ✅** |
| **Time** | O(b^d) | O(b^m) | O(b^⌊C*/ε⌋) | O(b^d) | O(b^d) |
| **Space** | O(b^d) | O(bm) | O(b^⌊C*/ε⌋) | O(bd) | O(b^d) |
| **Uses heuristic** | ❌ | ❌ | ❌ | ❌ | ✅ |

*With uniform step costs
**With admissible heuristic

---

## Q26. Short Notes: IDA* and SMA* (Self-Learning)

### IDA* (Iterative Deepening A*):
- Combines iterative deepening with A*
- Instead of depth limit, uses **f-cost limit**
- Each iteration searches all nodes where f(n) ≤ current limit
- If no solution found, set new limit = smallest f-value that exceeded current limit
- **Advantage:** Linear space O(bd) like IDDFS, but guided by heuristic like A*
- **Disadvantage:** Repeats work (like IDDFS), may be slow with many distinct f-values

### SMA* (Simplified Memory-Bounded A*):
- A* but limited to **available memory**
- When memory is full: drop the **worst** leaf node (highest f-value)
- Store the f-value of dropped node in its parent (for potential re-expansion)
- Re-expand dropped nodes if nothing better is available
- **Advantage:** Uses all available memory optimally
- **Disadvantage:** May repeatedly expand and forget nodes (thrashing) if memory is too small

---

## Q27. Solve: Apply A* to find the shortest path from S to G.

```
Graph:
S ---(3)--- A ---(4)--- G
|           |           |
(1)        (2)         (5)
|           |           |
B ---(6)--- C ---(3)--- D
           
h values: h(S)=7, h(A)=4, h(B)=6, h(C)=2, h(D)=3, h(G)=0
```

**Answer:**

| Step | Node Expanded | g(n) | h(n) | f(n)=g+h | Frontier After |
|------|--------------|------|------|----------|----------------|
| 1 | S | 0 | 7 | 7 | A(3+4=7), B(1+6=7) |
| 2 | A (or B, tie) | 3 | 4 | 7 | B(1+6=7), G(7+0=7), C(5+2=7) |
| 3 | B | 1 | 6 | 7 | G(7+0=7), C(5+2=7), C_via_B(7+2=9) |
| 4 | G | 7 | 0 | 7 | — |

**Path found: S → A → G, Cost = 3 + 4 = 7 ✅**

A* explores fewer nodes than UCS or BFS because the heuristic guides it.

---

## Q28. Explain Constraint Satisfaction Problem (CSP). What are its components?

**Answer:**

A **Constraint Satisfaction Problem** is a mathematical problem defined by:

1. **Variables:** X = {X₁, X₂, ..., Xₙ} — the unknowns to be solved
2. **Domains:** D = {D₁, D₂, ..., Dₙ} — possible values for each variable
3. **Constraints:** C = {C₁, C₂, ..., Cₘ} — rules restricting allowed value combinations

**Goal:** Find an assignment of values to all variables such that all constraints are satisfied (or prove none exists).

### Types of Constraints:
| Type | Involves | Example |
|------|----------|---------|
| **Unary** | 1 variable | X₁ ≠ 5 |
| **Binary** | 2 variables | X₁ ≠ X₂ |
| **Global** | All variables | AllDifferent(X₁, X₂, ..., Xₙ) |
| **Soft** | Preference | "Prefer X₁ < X₂" |

### CSP Solving Methods:
1. **Backtracking Search:** Assign one variable at a time, backtrack on failure
2. **Constraint Propagation:** Reduce domains early (Arc Consistency, Forward Checking)
3. **Variable/Value Ordering:** MRV (pick most constrained variable), LCV (pick least constraining value)
4. **Local Search:** Min-conflicts heuristic

### Examples of CSPs:
- Map coloring, Sudoku, N-Queens, Cryptarithmetic, Scheduling, Timetabling

---

## Q29. Compare Hill Climbing and Simulated Annealing.

**Answer:**

| Aspect | Hill Climbing | Simulated Annealing |
|--------|--------------|---------------------|
| **Type** | Greedy local search | Probabilistic local search |
| **Accepts worse moves?** | ❌ Never | ✅ Yes, with probability e^(ΔE/T) |
| **Escapes local maxima?** | ❌ No — gets stuck | ✅ Yes — bad moves help escape |
| **Memory** | O(1) | O(1) |
| **Deterministic?** | Yes (steepest ascent) | No — has randomness |
| **Speed** | Fast to converge | Slower (needs cooling schedule) |
| **Quality of solution** | Local optimum | Near-global optimum |
| **Completeness** | Not complete | Theoretically complete (slow cooling) |
| **Parameter tuning** | None | Needs cooling schedule (T₀, α) |
| **Based on** | Pure greedy | Metallurgy (annealing process) |
| **When T is high** | N/A | Accepts most moves (random walk) |
| **When T = 0** | Same behavior as HC | Same behavior as HC |

---

## Q30. What are the application areas of AI? Explain any five.

**Answer:**

### 1. Healthcare
- **Disease Diagnosis:** AI analyzes symptoms, medical images (X-rays, MRIs) to detect diseases like cancer
- **Drug Discovery:** AI predicts molecular structures to speed up drug development
- **Example:** IBM Watson for oncology, Google DeepMind for eye disease detection

### 2. Autonomous Vehicles (Self-Driving Cars)
- AI uses computer vision, sensors (LIDAR), and planning algorithms
- Perceives the environment, detects obstacles, plans routes
- **Example:** Tesla Autopilot, Waymo

### 3. Natural Language Processing
- Machine translation (Google Translate), chatbots, voice assistants
- Sentiment analysis for social media monitoring
- **Example:** ChatGPT, Siri, Alexa

### 4. Gaming
- AI plays complex games like Chess, Go, and video games
- Uses minimax, alpha-beta pruning, reinforcement learning
- **Example:** Deep Blue (Chess), AlphaGo (Go), OpenAI Five (Dota 2)

### 5. Finance
- Fraud detection by analyzing transaction patterns
- Algorithmic trading — AI makes stock market decisions
- Credit scoring — predicting loan default risk
- **Example:** PayPal fraud detection, robo-advisors

---
