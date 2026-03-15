# Module II — Search Techniques
## ITC604 | AI and DS – 1 | 9 Hours | CO2

---

# PART A: UNINFORMED SEARCH (Blind Search)

Uninformed search means the agent has **NO extra information** about which state is closer to the goal. It just explores states **systematically** without any guidance.

---

## 1. Key Concepts Before We Start

### Search Tree
- The search process creates a **tree** starting from the initial state.
- Each **node** = a state
- Each **edge** = an action
- **Root** = initial state
- **Leaf nodes** = states not yet expanded
- We "expand" a node by generating all its children (successor states).

### Important Terms:
| Term | Meaning |
|------|---------|
| **Frontier (Open List)** | Nodes that have been generated but not yet expanded |
| **Explored Set (Closed List)** | Nodes that have already been expanded |
| **Branching Factor (b)** | Maximum number of children of any node |
| **Depth (d)** | Depth of the shallowest goal node |
| **Maximum Depth (m)** | Maximum depth of the search tree |
| **Path Cost** | Total cost from root to a node |

### How to Compare Search Algorithms:
| Criterion | What it measures |
|-----------|-----------------|
| **Completeness** | Will it always find a solution if one exists? |
| **Optimality** | Does it find the best (least cost) solution? |
| **Time Complexity** | How many nodes are generated/expanded? |
| **Space Complexity** | How many nodes are stored in memory? |

---

## 2. Breadth-First Search (BFS) — Recap

- Expands the **shallowest** node first.
- Uses a **FIFO Queue** (First In, First Out).
- Explores level by level.

```
Level 0:    A
Level 1:   B   C
Level 2:  D E  F G
```
Order: A → B → C → D → E → F → G

| Property | Value |
|----------|-------|
| Complete? | ✅ Yes (if b is finite) |
| Optimal? | ✅ Yes (if all step costs are equal) |
| Time | O(b^d) |
| Space | O(b^d) — stores all nodes at current level |

---

## 3. Depth-First Search (DFS) — Recap

- Expands the **deepest** node first.
- Uses a **LIFO Stack** (Last In, First Out).
- Goes deep down one branch, then backtracks.

```
        A
       / \
      B   C
     / \
    D   E
```
Order: A → B → D → E → C (goes deep first)

| Property | Value |
|----------|-------|
| Complete? | ❌ No (can get stuck in infinite paths) |
| Optimal? | ❌ No |
| Time | O(b^m) — m = max depth |
| Space | O(b × m) — only stores nodes on current path |

**Advantage:** Uses **much less memory** than BFS.
**Disadvantage:** Can go very deep and never come back if path is infinite.

---

## 4. Uniform Cost Search (UCS)

### The Problem BFS Can't Solve:
BFS finds the shallowest goal, but what if edges have **different costs**? BFS might find a path with MORE cost because it only cares about depth, not cost.

### How UCS Works:
- Expands the node with the **lowest total path cost** (g(n)) first.
- Uses a **Priority Queue** (ordered by path cost).
- Like BFS, but instead of expanding level by level, it expands **cheapest first**.

### Algorithm:
```
1. Start with initial state in priority queue (cost = 0)
2. Loop:
   a. Remove node with LOWEST cost from queue
   b. If it's the goal → DONE! Return solution
   c. Add it to explored set
   d. For each child:
      - Calculate total path cost
      - If not explored and not in frontier → add to frontier
      - If in frontier with higher cost → replace with lower cost
3. If queue empty → No solution
```

### Example:
```
        A
      /   \
   (1)     (5)
    /       \
   B         C
    \       /
    (3)   (1)
      \   /
        D (Goal)
```

| Step | Frontier (node: cost) | Expanded |
|------|----------------------|----------|
| 1 | A: 0 | — |
| 2 | B: 1, C: 5 | A |
| 3 | C: 5, D: 4 | A, B |
| 4 | D: 4 | A, B |
| 5 | D: 4 → **GOAL FOUND!** | Cost = 4 (A→B→D) |

Path found: A → B → D (cost = 4), NOT A → C → D (cost = 6)

| Property | Value |
|----------|-------|
| Complete? | ✅ Yes (if all step costs > 0) |
| Optimal? | ✅ Yes — always finds the cheapest path |
| Time | O(b^(1 + ⌊C*/ε⌋)) where C* = optimal cost, ε = minimum step cost |
| Space | O(b^(1 + ⌊C*/ε⌋)) |

**Key Point:** UCS = BFS when all step costs are equal.

---

## 5. Depth-Limited Search (DLS)

### The Problem with DFS:
DFS can go infinitely deep and never find a solution.

### Solution — Put a Limit!
Depth-Limited Search is **DFS with a depth limit L**. It won't go deeper than L levels.

### Algorithm:
```
function DEPTH_LIMITED_SEARCH(problem, limit):
    return RECURSIVE_DLS(make_node(initial_state), problem, limit)

function RECURSIVE_DLS(node, problem, limit):
    if problem.GOAL_TEST(node.state):
        return SOLUTION(node)
    else if limit == 0:
        return CUTOFF    ← "I hit the limit, might be more below"
    else:
        cutoff_occurred = false
        for each action in problem.ACTIONS(node.state):
            child = CHILD_NODE(problem, node, action)
            result = RECURSIVE_DLS(child, problem, limit - 1)
            if result == CUTOFF:
                cutoff_occurred = true
            else if result != FAILURE:
                return result
        if cutoff_occurred:
            return CUTOFF
        else:
            return FAILURE
```

### Example with limit = 2:
```
        A (depth 0)
       / \
      B   C (depth 1)
     / \   \
    D   E   F (depth 2) ← STOP HERE, don't go deeper
   /
  G (depth 3) ← NOT explored (beyond limit)
```

| Property | Value |
|----------|-------|
| Complete? | ✅ Yes, if goal is within depth limit L |
| Optimal? | ❌ No |
| Time | O(b^L) |
| Space | O(b × L) |

**Problem:** How to choose the right limit L? If L is too small, we miss the goal. If L is too large, we waste time.

---

## 6. Iterative Deepening Depth-First Search (IDDFS)

### Best of Both Worlds!
Combines the **space efficiency of DFS** with the **completeness of BFS**.

### How It Works:
Run Depth-Limited Search repeatedly with **increasing depth limits**: 0, 1, 2, 3, ...

```
Run DLS with limit = 0  →  Only check root
Run DLS with limit = 1  →  Check root + level 1
Run DLS with limit = 2  →  Check root + level 1 + level 2
Run DLS with limit = 3  →  Check root + level 1 + level 2 + level 3
... keep going until goal is found
```

### Algorithm:
```
function ITERATIVE_DEEPENING_SEARCH(problem):
    for depth = 0 to ∞:
        result = DEPTH_LIMITED_SEARCH(problem, depth)
        if result ≠ CUTOFF:
            return result
```

### Isn't Repeating Work Wasteful?
It seems wasteful, but the **overhead is small**! Most nodes are at the deepest level.

**Example:** If b = 10 and d = 5:
- BFS generates: 10 + 100 + 1000 + 10000 + 100000 = **111,110 nodes**
- IDDFS generates: 6 + 50 + 400 + 3000 + 20000 + 100000 = **123,456 nodes**
- Only about **11% more** work than BFS, but with **much less memory!**

| Property | Value |
|----------|-------|
| Complete? | ✅ Yes |
| Optimal? | ✅ Yes (if step costs are equal) |
| Time | O(b^d) — same as BFS |
| Space | O(b × d) — same as DFS! |

> **IDDFS is the preferred uninformed search method** when search space is large and depth of solution is unknown.

---

## 7. Bidirectional Search

### The Idea:
Instead of searching from start to goal, search **from BOTH ends simultaneously**:
- **Forward search** from the initial state
- **Backward search** from the goal state
- When they **meet in the middle** → we've found a path!

```
Start ──→ ● ● ● ──┐
                    ├── MEET! → Path found
Goal  ──→ ● ● ● ──┘
```

### Why is it Faster?
- Normal BFS: explores O(b^d) nodes
- Bidirectional: each side explores O(b^(d/2)) nodes
- Total: O(2 × b^(d/2)) = **O(b^(d/2))** — MUCH faster!

**Example:** b = 10, d = 6
- BFS: 10^6 = 1,000,000 nodes
- Bidirectional: 2 × 10^3 = 2,000 nodes — **500x faster!**

### Requirements:
1. Must be able to generate **predecessors** (search backward from goal)
2. Need an efficient way to check if the two searches have met
3. Must know the goal state explicitly (not just a goal test)

| Property | Value |
|----------|-------|
| Complete? | ✅ Yes (if BFS is used on both sides) |
| Optimal? | ✅ Yes (if BFS used and uniform step costs) |
| Time | O(b^(d/2)) |
| Space | O(b^(d/2)) |

---

## Summary: Comparing Uninformed Search Algorithms

| Algorithm | Complete? | Optimal? | Time | Space |
|-----------|----------|----------|------|-------|
| **BFS** | ✅ Yes | ✅ Yes* | O(b^d) | O(b^d) |
| **DFS** | ❌ No | ❌ No | O(b^m) | O(bm) |
| **UCS** | ✅ Yes | ✅ Yes | O(b^(1+⌊C*/ε⌋)) | O(b^(1+⌊C*/ε⌋)) |
| **DLS** | If d ≤ L | ❌ No | O(b^L) | O(bL) |
| **IDDFS** | ✅ Yes | ✅ Yes* | O(b^d) | O(bd) |
| **Bidirectional** | ✅ Yes | ✅ Yes* | O(b^(d/2)) | O(b^(d/2)) |

*When all step costs are equal

---

---

# PART B: INFORMED SEARCH (Heuristic Search)

Informed search uses **extra knowledge (heuristics)** to guide the search toward the goal more efficiently.

---

## 8. Heuristic Functions

### What is a Heuristic?
A **heuristic** h(n) is an **estimate** of how close a node n is to the goal.

- h(n) = estimated cost from node n to the **nearest goal**
- h(goal) = 0 (you're already there!)
- A heuristic is like a "hint" or "rule of thumb"

### Examples:

**8-Puzzle:**
```
Current State:        Goal State:
┌───┬───┬───┐       ┌───┬───┬───┐
│ 7 │ 2 │ 4 │       │ 1 │ 2 │ 3 │
├───┼───┼───┤       ├───┼───┼───┤
│ 5 │   │ 6 │       │ 4 │ 5 │ 6 │
├───┼───┼───┤       ├───┼───┼───┤
│ 8 │ 3 │ 1 │       │ 7 │ 8 │   │
└───┴───┴───┘       └───┴───┴───┘
```

Two common heuristics for 8-puzzle:

1. **h₁ = Number of Misplaced Tiles**
   - Count tiles NOT in their goal position
   - h₁ = 5 (tiles 7, 5, 8, 3, 1 are misplaced)

2. **h₂ = Manhattan Distance (City Block Distance)**
   - Sum of horizontal + vertical distances of each tile from its goal position
   - Tile 7: needs to move 2 down → distance = 2
   - Tile 5: needs to move 1 left → distance = 1
   - ... and so on for each tile
   - h₂ = sum of all individual distances

**Route Finding:**
- h(n) = **Straight-line distance** from city n to the goal city
- This is always ≤ actual road distance (roads aren't perfectly straight)

### Properties of Good Heuristics:

**Admissible Heuristic:**
- **Never overestimates** the true cost to reach the goal
- h(n) ≤ actual cost from n to goal
- Example: Straight-line distance never overestimates road distance (roads can't be shorter than a straight line)

**Consistent (Monotonic) Heuristic:**
- For every node n and successor n' with action cost c:
- h(n) ≤ c(n, n') + h(n')
- (Triangle inequality — like "shortcut can't be longer than detour")
- Every consistent heuristic is also admissible (but not vice versa)

### Dominance:
- h₂ **dominates** h₁ if: h₂(n) ≥ h₁(n) for all n
- A dominant heuristic is **better** because it's more informative
- For 8-puzzle: Manhattan Distance dominates Misplaced Tiles (h₂ ≥ h₁ always)

---

## 9. Best-First Search (Greedy Best-First Search)

### How It Works:
- Expands the node that **appears closest to goal** based on the heuristic.
- Uses evaluation function **f(n) = h(n)** (only heuristic, ignores path cost).
- Uses a **Priority Queue** ordered by h(n).

### Algorithm:
```
1. Start with initial state in priority queue
2. Loop:
   a. Remove node with LOWEST h(n)
   b. If it's the goal → DONE!
   c. Expand it, add children to queue
3. If queue empty → No solution
```

### Example — Route Finding:
```
Cities with straight-line distances to Goal (Bucharest):
Arad = 366, Sibiu = 253, Fagaras = 176, 
Timisoara = 329, Rimnicu = 193, Bucharest = 0

Map:
Arad ---(140)--- Sibiu ---(99)--- Fagaras ---(211)--- Bucharest
  \                \
  (118)            (80)
    \                \
  Timisoara       Rimnicu Vilcea ---(146)--- Pitesti ---(101)--- Bucharest
```

Greedy Best-First expands (picks the one with smallest h(n)):
1. Arad (h=366)
2. Sibiu (h=253) ← smallest h among Arad's children
3. Fagaras (h=176) ← smallest h among Sibiu's children
4. Bucharest (h=0) ← GOAL!

Path: Arad → Sibiu → Fagaras → Bucharest (cost = 450)

But optimal path is: Arad → Sibiu → Rimnicu → Pitesti → Bucharest (cost = 418)

**Greedy Best-First is NOT optimal!** It's greedy — it goes toward the goal but might miss a shorter path.

| Property | Value |
|----------|-------|
| Complete? | ❌ No (can get stuck in loops in tree version) |
| Optimal? | ❌ No |
| Time | O(b^m) worst case, but good heuristic → much better |
| Space | O(b^m) |

---

## 10. A* Search (A-Star)

### The Most Important Search Algorithm in AI!

### The Key Idea:
Combine:
- **g(n)** = actual cost from start to node n (what UCS uses)
- **h(n)** = estimated cost from node n to goal (what Greedy uses)
- **f(n) = g(n) + h(n)** = estimated total cost through node n

### How It Works:
- Expands the node with the **lowest f(n) = g(n) + h(n)**
- Uses a **Priority Queue** ordered by f(n)
- Takes into account BOTH the cost already spent AND the estimated remaining cost

### Algorithm:
```
1. Start with initial state in priority queue (f = 0 + h(start))
2. Loop:
   a. Remove node with LOWEST f(n) = g(n) + h(n)
   b. If it's the goal → DONE! Return solution
   c. Add to explored set
   d. For each child:
      - g(child) = g(node) + step_cost
      - f(child) = g(child) + h(child)
      - If not explored and not in frontier → add
      - If in frontier with higher f → replace
3. If queue empty → No solution
```

### Detailed Example:

```
Graph:
        A (start)
      /     \
   (1)       (4)
   /           \
  B             C
  |             |
 (5)           (2)
  |             |
  D             D
   \           /
    (3)     (1)
      \     /
       Goal G

Heuristic values h(n):
A = 7, B = 6, C = 2, D_from_B = 2, D_from_C = 2, G = 0
```

Let's trace A*:

| Step | Node | g(n) | h(n) | f(n)=g+h | Action |
|------|------|------|------|----------|--------|
| 1 | A | 0 | 7 | 7 | Expand A |
| 2 | B | 1 | 6 | 7 | In frontier |
| 2 | C | 4 | 2 | 6 | In frontier |
| 3 | **Pick C** (f=6) | 4 | 2 | 6 | Expand C |
| 4 | D (via C) | 6 | 2 | 8 | In frontier |
| 5 | **Pick B** (f=7) | 1 | 6 | 7 | Expand B |
| 6 | D (via B) | 6 | 2 | 8 | Already in frontier, same cost |
| 7 | **Pick D** (f=8) | 6 | 2 | 8 | Expand D |
| 8 | G | 7 | 0 | 7 | **GOAL!** |

Path: A → C → D → G (cost = 4 + 2 + 1 = 7) ✅ Optimal!

### ⭐ A* is Optimal and Complete if:
1. **h(n) is admissible** (never overestimates) — for tree search
2. **h(n) is consistent** (monotonic) — for graph search
3. **Optimal efficiency** — no other optimal algorithm expands fewer nodes

| Property | Value |
|----------|-------|
| Complete? | ✅ Yes (if step costs > 0 and b is finite) |
| Optimal? | ✅ Yes (if h is admissible) |
| Time | O(b^d) worst case — exponential |
| Space | O(b^d) — keeps all nodes in memory |

### Why A* is Special:
```
UCS:    f(n) = g(n)          → ignores future (too conservative)
Greedy: f(n) = h(n)          → ignores past (too greedy)
A*:     f(n) = g(n) + h(n)   → considers BOTH (just right!) ✅
```

### A* Theorem (Proof of Optimality):
If h(n) is admissible, A* always expands the node on the optimal path first.
- Suppose an optimal goal G* is on the frontier
- And a suboptimal goal G₂ is also on the frontier
- f(G*) = g(G*) + 0 = g(G*) = actual optimal cost
- f(G₂) = g(G₂) > g(G*) since G₂ is suboptimal
- So A* will always pick G* before G₂

---

## 11. Hill Climbing

### The Idea:
- Start somewhere and keep moving **uphill** (to better states).
- Like climbing a mountain in fog — can only see immediately around you.
- At each step, move to the **neighbor with the highest value** (or lowest cost).
- **No backtracking!** Once you move, you don't go back.

### Algorithm:
```
function HILL_CLIMBING(problem):
    current = problem.initial_state
    loop:
        neighbor = best valued successor of current
        if neighbor is not better than current:
            return current    ← We're stuck! This is our answer.
        current = neighbor
```

### Types of Hill Climbing:

#### Simple Hill Climbing:
- Evaluate neighbors **one by one**
- Move to the **first** neighbor that is better than current
- Doesn't look at all neighbors

#### Steepest-Ascent Hill Climbing:
- Evaluate **ALL** neighbors
- Move to the **best** neighbor
- More thorough, but slower per step

#### Stochastic Hill Climbing:
- Choose randomly among uphill neighbors
- Slower convergence but can avoid some local maxima

### Problems with Hill Climbing:

```
                    * ← Global Maximum (we want this!)
                   / \
                  /   \
        * ←Local/     \
       / \ Maximum     \
      /   \             \
     /     \             \
    /       \_____* ← Shoulder/Plateau (flat area)
   /        Ridge ↑
──/─────────────────────────────
```

1. **Local Maximum:** A peak that is NOT the highest point. Hill climbing gets stuck here because all neighbors are worse.

2. **Plateau (Flat Region):** A flat area where all neighbors have the same value. The algorithm doesn't know which way to go.

3. **Ridge:** A narrow elevated region. Hard to navigate because the search moves in only one direction at a time.

### Solutions to Hill Climbing Problems:

| Solution | How it works |
|----------|-------------|
| **Random Restart** | Start from different random positions, run hill climbing each time, keep the best result |
| **Sideways Moves** | Allow moves to neighbors with equal value (limited number to avoid infinite loops on plateaus) |
| **Simulated Annealing** | Allow some downhill moves (explained next) |

---

## 12. Simulated Annealing

### The Idea (from Metallurgy):
In metallurgy, **annealing** means heating metal and slowly cooling it to remove defects. Similarly:
- **Early on (high temperature):** Allow lots of "bad" moves (going downhill) to explore widely
- **Later (low temperature):** Only allow good moves (going uphill) to converge to a solution
- Over time, the algorithm settles into a good solution

### How It Works:
```
function SIMULATED_ANNEALING(problem, schedule):
    current = problem.initial_state
    for t = 1 to ∞:
        T = schedule(t)           ← Temperature at time t
        if T == 0:
            return current        ← Frozen! Return answer
        next = random neighbor of current
        ΔE = value(next) - value(current)
        if ΔE > 0:               ← Next is BETTER
            current = next        ← Always move to better state
        else:                     ← Next is WORSE
            move to next with probability e^(ΔE/T)
            ← Higher T → more likely to accept bad moves
            ← Lower T → less likely to accept bad moves
            ← More negative ΔE → less likely to accept
```

### Key Points:
- **T (Temperature)** starts high and gradually decreases
- When T is high → algorithm explores widely (accepts bad moves)
- When T is low → algorithm exploits locally (rejects bad moves)
- When T = 0 → behaves exactly like hill climbing
- **e^(ΔE/T)** = probability of accepting a worse move
  - If ΔE = -1, T = 100 → e^(-1/100) = 0.99 → 99% chance (almost always accept)
  - If ΔE = -1, T = 1 → e^(-1/1) = 0.37 → 37% chance
  - If ΔE = -1, T = 0.01 → e^(-1/0.01) ≈ 0 → almost never accept

### Cooling Schedule:
- How T decreases over time
- Common: T(t) = T₀ × α^t where α is slightly less than 1 (e.g., 0.95)
- If cooled slowly enough, guaranteed to find optimal solution (in theory)

| Property | Value |
|----------|-------|
| Complete? | Theoretically yes if cooled slowly enough |
| Optimal? | Probabilistically — finds near-optimal solutions |
| Use case | Optimization problems, VLSI design, scheduling |

---

---

# PART C: CONSTRAINT SATISFACTION PROBLEMS (CSP)

---

## 13. What is a CSP?

A **Constraint Satisfaction Problem** consists of:
1. **Variables:** X₁, X₂, ..., Xₙ
2. **Domains:** Each variable has a set of possible values
3. **Constraints:** Rules that restrict which combinations of values are allowed

**Goal:** Find an assignment of values to ALL variables that satisfies ALL constraints.

### Types of Constraints:
| Type | Meaning | Example |
|------|---------|---------|
| **Unary** | Restricts a single variable | X₁ ≠ 3 |
| **Binary** | Restricts two variables | X₁ ≠ X₂ |
| **Higher-order** | Restricts 3+ variables | AllDifferent(X₁, X₂, X₃) |
| **Soft constraints** | Preferences, not strict rules | "Prefer morning classes" |

---

## 14. Crypto-Arithmetic Problem

### What is it?
A puzzle where digits (0-9) replace letters in an arithmetic equation. Each letter = a unique digit.

### Classic Example: SEND + MORE = MONEY

```
    S E N D
  + M O R E
  ---------
  M O N E Y
```

**Variables:** S, E, N, D, M, O, R, Y (and carry variables C₁, C₂, C₃, C₄)

**Domains:** {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

**Constraints:**
- All variables have different values: AllDifferent(S, E, N, D, M, O, R, Y)
- S ≠ 0 and M ≠ 0 (leading digits can't be zero)
- Column-by-column arithmetic constraints:
  - Column 1 (rightmost): D + E = Y + 10 × C₁
  - Column 2: N + R + C₁ = E + 10 × C₂
  - Column 3: E + O + C₂ = N + 10 × C₃
  - Column 4: S + M + C₃ = O + 10 × C₄
  - C₄ = M

**Solution:** S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2

```
    9 5 6 7
  + 1 0 8 5
  ---------
  1 0 6 5 2    →    9567 + 1085 = 10652 ✅
```

### Another Example: TWO + TWO = FOUR
```
    T W O
  + T W O
  -------
  F O U R
```

Variables: T, W, O, F, U, R
Constraints: AllDifferent, T ≠ 0, F ≠ 0

Solution: T=7, W=3, O=4, F=1, U=6, R=8
```
    734
  + 734
  -----
  1468   →   734 + 734 = 1468 ✅
```

---

## 15. Water Jug Problem

### Problem Statement:
You have two jugs:
- **Jug A:** capacity 4 liters
- **Jug B:** capacity 3 liters
- **Goal:** Get exactly 2 liters in Jug A

You can:
1. Fill a jug completely from the tap
2. Empty a jug completely
3. Pour from one jug to another (until source is empty or target is full)

### State Representation:
State = (a, b) where a = liters in Jug A, b = liters in Jug B

### Possible Actions (Production Rules):

| Rule | Action | Condition | New State |
|------|--------|-----------|-----------|
| 1 | Fill Jug A | a < 4 | (4, b) |
| 2 | Fill Jug B | b < 3 | (a, 3) |
| 3 | Empty Jug A | a > 0 | (0, b) |
| 4 | Empty Jug B | b > 0 | (a, 0) |
| 5 | Pour A → B | a > 0, b < 3 | (a - d, b + d) where d = min(a, 3-b) |
| 6 | Pour B → A | b > 0, a < 4 | (a + d, b - d) where d = min(b, 4-a) |

### Solution:

| Step | Action | Jug A (4L) | Jug B (3L) |
|------|--------|-----------|-----------|
| 0 | Start | 0 | 0 |
| 1 | Fill Jug A | **4** | 0 |
| 2 | Pour A → B | 1 | **3** |
| 3 | Empty Jug B | 1 | **0** |
| 4 | Pour A → B | 0 | **1** |
| 5 | Fill Jug A | **4** | 1 |
| 6 | Pour A → B | **2** | 3 |

**GOAL: Jug A has 2 liters! ✅**

---

## 16. Graph Coloring Problem

### Problem Statement:
Given a graph (map), assign colors to each node (region) such that **no two adjacent nodes have the same color**.

### Example — Map Coloring Australia:
```
        ┌─────────────────────┐
        │         NT          │
        │    ┌───────────┐    │
        │    │    SA      │ Q │
        │    │  ┌─────┐   │   │
        │WA  │  │     │   │   │
        │    │  │     │NSW│   │
        │    │  │     │   │   │
        │    │  │ V   │   │   │
        │    │  │     │   │   │
        │    └──┴─────┘   │   │
        └─────────T───────┘   │
                              │
```

**Variables:** WA, NT, SA, Q, NSW, V, T (7 regions)

**Domains:** {Red, Green, Blue}

**Constraints:** Adjacent regions must have different colors:
- WA ≠ NT, WA ≠ SA
- NT ≠ SA, NT ≠ Q
- SA ≠ Q, SA ≠ NSW, SA ≠ V
- Q ≠ NSW
- NSW ≠ V

**One valid solution:**
| Region | Color |
|--------|-------|
| WA | Red |
| NT | Green |
| SA | Blue |
| Q | Red |
| NSW | Green |
| V | Red |
| T | Red (no constraint — it's an island) |

### CSP Solving Techniques:
1. **Backtracking Search:** Try assigning values; if constraint violated, backtrack
2. **Constraint Propagation:** Reduce domains by eliminating impossible values
3. **Arc Consistency (AC-3):** For every constraint, ensure every value in one variable's domain is consistent with some value in the other

---

---

# PART D: ADVERSARIAL SEARCH (Game Playing)

---

## 17. Game Playing

### Why Study Games in AI?
- Games have **clear rules** and **well-defined goals**
- They are **competitive** (adversarial) — there's an opponent trying to beat you
- They require **strategy** — looking ahead and making smart decisions
- Many games are **hard** problems that push AI capabilities

### Formal Definition of a Game:
| Component | Meaning |
|-----------|---------|
| **S₀** | Initial state (starting position) |
| **Player(s)** | Which player's turn it is in state s |
| **Actions(s)** | Legal moves in state s |
| **Result(s, a)** | Resulting state after action a in state s |
| **Terminal-Test(s)** | Is the game over? (win/loss/draw) |
| **Utility(s, p)** | Numeric value for player p in terminal state s |

### Example — Tic-Tac-Toe:
- **S₀:** Empty 3×3 board
- **Player(s):** X or O (alternate turns)
- **Actions(s):** Place mark in any empty cell
- **Terminal-Test:** 3 in a row, or board is full
- **Utility:** +1 (X wins), -1 (O wins), 0 (draw)

---

## 18. Min-Max Search (Minimax)

### The Core Idea:
In a two-player game:
- **MAX** player wants to **maximize** the score (this is us/AI)
- **MIN** player wants to **minimize** the score (this is the opponent)
- Both players play **optimally** (make the best possible move)

### How Minimax Works:
1. Build the **complete game tree** from current state to all terminal states
2. Assign **utility values** to terminal states
3. **Propagate values up** the tree:
   - At **MAX nodes:** choose the **maximum** child value
   - At **MIN nodes:** choose the **minimum** child value

### Example:

```
                    MAX
                   / | \
                 /   |   \
               3     5     2       ← MAX chooses 5 (maximum)
             / | \
            /  |  \
           3   12   8             ← MIN at this node chooses 3 (minimum of 3,12,8)
```

Full example with a game tree:
```
                        A (MAX)
                      / | \
                    /   |   \
                  B     C     D     (MIN level)
                / \   / \   / \
               E   F G   H I   J    (Terminal nodes)
               3   5 6   9 1   2

Step 1: Terminal values → E=3, F=5, G=6, H=9, I=1, J=2

Step 2: MIN nodes pick minimum of children:
  B = min(3, 5) = 3
  C = min(6, 9) = 6
  D = min(1, 2) = 1

Step 3: MAX node picks maximum of children:
  A = max(3, 6, 1) = 6

Result: MAX chooses move to C (value 6)
```

### Minimax Algorithm:
```
function MINIMAX(node, depth, maximizingPlayer):
    if depth == 0 OR node is terminal:
        return utility value of node
    
    if maximizingPlayer:        ← MAX's turn
        maxEval = -∞
        for each child of node:
            eval = MINIMAX(child, depth-1, FALSE)
            maxEval = max(maxEval, eval)
        return maxEval
    
    else:                       ← MIN's turn
        minEval = +∞
        for each child of node:
            eval = MINIMAX(child, depth-1, TRUE)
            minEval = min(minEval, eval)
        return minEval
```

| Property | Value |
|----------|-------|
| Complete? | ✅ Yes (if tree is finite) |
| Optimal? | ✅ Yes (against an optimal opponent) |
| Time | O(b^m) — b = branching factor, m = max depth |
| Space | O(b × m) — DFS-like |

**Problem:** For chess, b ≈ 35, m ≈ 100 → 35^100 nodes! **Impossible** to compute.

---

## 19. Alpha-Beta Pruning

### The Brilliant Optimization:
Alpha-Beta Pruning **skips branches** that **can't possibly affect the final decision**. It gives the **exact same result as Minimax** but much faster!

### Key Variables:
- **α (Alpha)** = Best value that MAX can guarantee so far (initially -∞)
- **β (Beta)** = Best value that MIN can guarantee so far (initially +∞)
- **Prune** (cut off a branch) when **α ≥ β**

### Rules:
- At **MAX node:** Update α = max(α, child_value). If α ≥ β → **prune** remaining children (β cutoff)
- At **MIN node:** Update β = min(β, child_value). If α ≥ β → **prune** remaining children (α cutoff)

### Detailed Example:

```
                         A (MAX)  α=-∞, β=+∞
                       /         \
                     /             \
              B (MIN)              C (MIN)
             /    \              /    \
           D       E          F       G
          /  \    / \        / \     / \
         3    5  6   9      1   2   0   ✂ (pruned)
```

**Step by step:**

```
1. Start at A (MAX), α=-∞, β=+∞

2. Go to B (MIN), α=-∞, β=+∞
   2a. Go to D → value = 3
       At B (MIN): β = min(+∞, 3) = 3
   2b. Go to E → value = 5
       At B (MIN): β = min(3, 5) = 3
   B returns 3

3. At A (MAX): α = max(-∞, 3) = 3, β = +∞

4. Go to C (MIN), α=3, β=+∞
   4a. Go to F → value = 1
       At C (MIN): β = min(+∞, 1) = 1
       CHECK: α(3) ≥ β(1)? YES! → PRUNE! ✂
       Don't need to look at G!
   C returns 1

5. At A (MAX): α = max(3, 1) = 3
   A returns 3
```

**Why could we prune G?**
- A (MAX) already has option B with value 3
- C (MIN) found child F with value 1, so C will return AT MOST 1
- MAX will never choose C (value ≤ 1) over B (value 3)
- So looking at G is pointless — the result won't change!

### Larger Example with Full Trace:

```
                              A (MAX)
                           /          \
                     B (MIN)          C (MIN)
                    /      \         /      \
              D (MAX)   E (MAX)  F (MAX)  G (MAX)
              / \       / \      / \      / \
             3   5     6   9    1   2    0   ✂
```

| Step | Node | Type | α | β | Value | Action |
|------|------|------|---|---|-------|--------|
| 1 | A | MAX | -∞ | +∞ | ? | Go to B |
| 2 | B | MIN | -∞ | +∞ | ? | Go to D |
| 3 | D | MAX | -∞ | +∞ | ? | Eval child: 3 |
| 4 | D | MAX | 3 | +∞ | ? | Eval child: 5, return max=5 |
| 5 | B | MIN | -∞ | 5 | ? | β=min(+∞,5)=5, Go to E |
| 6 | E | MAX | -∞ | 5 | ? | Eval child: 6 |
| 7 | E | MAX | 6 | 5 | ? | α=6 ≥ β=5 → **PRUNE!** Skip 9 |
| 8 | E | - | - | - | 6 | Return 6 |
| 9 | B | MIN | -∞ | 5 | 5 | β=min(5,6)=5, return 5 |
| 10 | A | MAX | 5 | +∞ | ? | α=max(-∞,5)=5, Go to C |
| 11 | C | MIN | 5 | +∞ | ? | Go to F |
| 12 | F | MAX | 5 | +∞ | ? | Eval child: 1 |
| 13 | F | MAX | 5 | +∞ | ? | Eval child: 2, return max=2 |
| 14 | C | MIN | 5 | 2 | ? | β=min(+∞,2)=2, α=5 ≥ β=2 → **PRUNE!** Skip G |
| 15 | C | - | - | - | 2 | Return 2 |
| 16 | A | MAX | 5 | +∞ | 5 | max(5,2)=5, **RESULT = 5** |

### Effectiveness:
- **Best case** (moves ordered best first): Time = O(b^(m/2))
  - Effectively doubles the searchable depth!
  - Chess: instead of 35^100, we can search 35^50
- **Worst case** (worst ordering): Time = O(b^m) — no improvement
- **Average case** with decent ordering: O(b^(3m/4))

### Move Ordering:
To maximize pruning, try the **best moves first**:
- Use iterative deepening — search shallow first, use results to order deeper search
- Use heuristic evaluation functions to estimate move quality

---

## 20. Comparing All Search Techniques

| Algorithm | Category | Complete | Optimal | Time | Space | Key Feature |
|-----------|----------|----------|---------|------|-------|-------------|
| BFS | Uninformed | ✅ | ✅* | O(b^d) | O(b^d) | Level-by-level |
| DFS | Uninformed | ❌ | ❌ | O(b^m) | O(bm) | Goes deep first |
| UCS | Uninformed | ✅ | ✅ | O(b^⌊C*/ε⌋) | O(b^⌊C*/ε⌋) | Cheapest first |
| DLS | Uninformed | If d≤L | ❌ | O(b^L) | O(bL) | DFS with limit |
| IDDFS | Uninformed | ✅ | ✅* | O(b^d) | O(bd) | Best uninformed |
| Bidirectional | Uninformed | ✅ | ✅* | O(b^(d/2)) | O(b^(d/2)) | Search from both ends |
| Greedy Best-First | Informed | ❌ | ❌ | O(b^m) | O(b^m) | h(n) only |
| **A*** | **Informed** | **✅** | **✅** | O(b^d) | O(b^d) | **g(n)+h(n) — Best!** |
| Hill Climbing | Local | ❌ | ❌ | O(varies) | O(1) | No backtracking |
| Simulated Annealing | Local | ~✅ | ~✅ | O(varies) | O(1) | Accept bad moves early |
| Minimax | Adversarial | ✅ | ✅ | O(b^m) | O(bm) | Two-player optimal |
| Alpha-Beta | Adversarial | ✅ | ✅ | O(b^(m/2))† | O(bm) | Pruned minimax |

*With uniform step costs
†Best case with perfect move ordering

---

## Self-Learning Topics

### IDA* (Iterative Deepening A*)
- Combines A* with iterative deepening
- Uses f-cost limit instead of depth limit
- Each iteration: search all nodes with f(n) ≤ limit
- If no solution found, increase limit to the smallest f value that exceeded the current limit
- **Advantage:** Uses linear space O(bd) like IDDFS, but uses heuristic like A*

### SMA* (Simplified Memory-Bounded A*)
- A* that uses all available memory
- When memory is full, drops the worst (highest f-value) leaf node
- Remembers the f-value of dropped nodes in their parent
- Can re-expand dropped nodes if needed later
- **Advantage:** Uses whatever memory is available optimally

---
