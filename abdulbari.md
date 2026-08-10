Here are the structured, easy-to-understand study notes covering all the topics and code examples from your PDF slides.

---

## 1. Introduction & Algorithm Basics

### Algorithm vs. Program

* **Algorithm:** A step-by-step design or strategy to solve a problem. It is written in plain language/pseudocode, independent of programming languages, hardware, or operating systems. Analyzed using **Priori Analysis**.


* **Program:** An actual implementation of an algorithm using a specific programming language. It depends on language and hardware. Tested using **Posteriori Testing**.



---

### Priori Analysis vs. Posteriori Testing

| Feature | Priori Analysis | Posteriori Testing |
| --- | --- | --- |
| **Stage** | Pre-implementation (Algorithm level)

 | Post-implementation (Program level)

 |
| **Language** | Independent of programming language

 | Dependent on programming language

 |
| **Hardware** | Independent of hardware

 | Dependent on hardware

 |
| **Output** | Time/Space expressed as a mathematical function $f(n)$<br> | Watch time (seconds/milliseconds) and memory usage (bytes)

 |

---

### 5 Essential Characteristics of an Algorithm

1. **Input:** 0 or more well-defined inputs.


2. **Output:** At least 1 output.


3. **Definiteness:** Every statement must be clear and unambiguous.


4. **Finiteness:** Must terminate after a finite number of steps.


5. **Effectiveness:** Every instruction must be basic enough to be carried out.



---

### Resources Analyzed in Algorithms

1. **Time** (Primary)


2. **Space / Memory** (Primary)


3. Network bandwidth


4. Power consumption


5. CPU Register usage



---

## 2. Space and Time Analysis Examples

### Example 1: Swap Function

```text
Algorithm Swap(a, b) {
    temp = a;
    a = b;
    b = temp;
}

```

* **Space Complexity:** Variables `a`, `b`, and `temp` each take 1 unit of space. $S(n) = 3 \text{ words} = \mathcal{O}(1)$ (Constant).


* **Time Complexity:** 3 constant execution statements. $f(n) = 3 \implies \mathcal{O}(1)$.



---

### Example 2: Array Sum

```text
Algorithm Sum(A, n) {
    s = 0;                     // 1 execution
    for (i = 0; i < n; i++) {  // i=0 (1), i<n (n+1), i++ (n)
        s = s + A[i];          // n executions
    }
    return s;                  // 1 execution
}

```

* **Time Complexity Analysis:**
* Total step counts: $1 + (n + 1) + n + n + 1 = 3n + 3$ (or $2n + 3$ counting loop interior operations).


* Time: $f(n) = 2n + 3 \implies \mathcal{O}(n)$.




* **Space Complexity Analysis:**
* Space needed: Array $A$ of size $n$, plus variables $n, s, i$ (1 unit each).


* $S(n) = n + 3 \implies \mathcal{O}(n)$.





---

### Example 3: Matrix Addition

```text
Algorithm Add(A, B, n) {
    for (i = 0; i < n; i++) {            // Runs (n + 1) times
        for (j = 0; j < n; j++) {        // Runs n * (n + 1) times
            C[i, j] = A[i, j] + B[i, j]; // Runs n * n times
        }
    }
}

```

* **Time Complexity:** $f(n) = 2n^2 + 2n + 1 \implies \mathcal{O}(n^2)$.


* **Space Complexity:** Matrices $A, B, C$ each take $n^2$ space, plus scalar counters $i, j, n$.


* $S(n) = 3n^2 + 3 \implies \mathcal{O}(n^2)$.





---

### Example 4: Matrix Multiplication

```text
Algorithm Multiply(A, B, n) {
    for (i = 0; i < n; i++) {                // n + 1
        for (j = 0; j < n; j++) {            // n * (n + 1)
            C[i, j] = 0;                     // n * n
            for (k = 0; k < n; k++) {        // n * n * (n + 1)
                C[i, j] += A[i, k] * B[k, j];// n * n * n
            }
        }
    }
}

```

* **Time Complexity:** Dominant term is $n \times n \times n = n^3 \implies \mathcal{O}(n^3)$.


* **Space Complexity:** $S(n) = 3n^2 + 4 \implies \mathcal{O}(n^2)$.



---

## 3. Loop Analysis Patterns

### Pattern 1: Basic Step Increment

```text
for (i = 1; i < n; i = i + 2) {
    Stmt;
}

```

* **Analysis:** Increments by 2 each iteration. Executes $\frac{n}{2}$ times.


* **Time Complexity:** $\mathcal{O}(n)$.



---

### Pattern 2: Nested Dependent Loop

```text
for (i = 0; i < n; i++) {
    for (j = 0; j < i; j++) {
        Stmt;
    }
}

```

* **Analysis:** Outer loop index $i$ goes $0 \to n-1$. Inner loop runs $i$ times:



$$\text{Total executions} = 0 + 1 + 2 + \dots + (n-1) = \frac{n(n-1)}{2} = \frac{n^2 - n}{2}$$


* **Time Complexity:** $\mathcal{O}(n^2)$.



---

### Pattern 3: Quadratic Increment Loop

```text
p = 0;
for (i = 1; p <= n; i++) {
    p = p + i;
}

```

* **Analysis:** Values of $p$ over iterations $k$: $p = 1 + 2 + 3 + \dots + k = \frac{k(k+1)}{2}$.


* Loop stops when $p > n \implies \frac{k^2}{2} \approx n \implies k \approx \sqrt{n}$.


* **Time Complexity:** $\mathcal{O}(\sqrt{n})$.



---

### Pattern 4: Multiplicative Loop

```text
for (i = 1; i < n; i = i * 2) {
    Stmt;
}

```

* **Analysis:** Sequence of $i$: $1, 2, 4, 8, \dots, 2^k$.


* Loop terminates when $2^k \ge n \implies k = \log_2 n$.


* **Time Complexity:** $\mathcal{O}(\log_2 n)$.



---

### Pattern 5: Square Condition Loop

```text
for (i = 0; i * i < n; i++) {
    Stmt;
}

```

* **Analysis:** Loop continues while $i^2 < n \implies i < \sqrt{n}$.


* **Time Complexity:** $\mathcal{O}(\sqrt{n})$.



---

### Pattern 6: Nested Logarithmic Loop

```text
p = 0;
for (i = 1; i < n; i = i * 2) {
    p++;
}
for (j = 1; j < p; j = j * 2) {
    Stmt;
}

```

* **Analysis:**
* First loop calculates $p = \log_2 n$.


* Second loop executes $\log_2 p$ times.


* Total iterations $= \log_2(\log_2 n)$.




* **Time Complexity:** $\mathcal{O}(\log \log n)$.



---

### Pattern 7: Linear-Logarithmic Combination

```text
for (i = 0; i < n; i++) {           // Runs n times
    for (j = 1; j < n; j = j * 2) { // Runs log(n) times per outer iteration
        Stmt;
    }
}

```

* **Time Complexity:** $n \times \log_2 n \implies \mathcal{O}(n \log n)$.



---

### Pattern 8: Square Sum While Loop

```text
t = 1; k = 1;
while (k < n) {
    k = k + i;
    i++;
}

```

* **Analysis:** $k = 1 + 2 + 3 + \dots + m = \frac{m(m+1)}{2}$. Loop stops when $m^2 \ge n \implies m = \sqrt{n}$.


* **Time Complexity:** $\mathcal{O}(\sqrt{n})$.



---

## 4. Hierarchy & Comparison of Functions

### Growth Rates Hierarchy (Fastest to Slowest Growth)

$$1 < \log n < \sqrt{n} < n < n \log n < n^2 < n^3 < \dots < 2^n < 3^n < \dots < n^n$$

* **Constant:** $\mathcal{O}(1)$

* **Logarithmic:** $\mathcal{O}(\log n)$

* **Linear:** $\mathcal{O}(n)$

* **Quadratic:** $\mathcal{O}(n^2)$

* **Cubic:** $\mathcal{O}(n^3)$

* **Exponential:** $\mathcal{O}(2^n), \mathcal{O}(3^n)$

* **Factorial / Power:** $\mathcal{O}(n!)$ or $\mathcal{O}(n^n)$


---

### Useful Mathematical Log Rules for Function Comparison

1. $\log(a \cdot b) = \log a + \log b$

2. $\log(a / b) = \log a - \log b$

3. $\log(a^b) = b \cdot \log a$

4. $a^{\log_c b} = b^{\log_c a}$


---

## 5. Asymptotic Notations

### 1. Big-O Notation ($\mathcal{O}$) — Upper Bound

* **Definition:** $f(n) = \mathcal{O}(g(n))$ if there exist positive constants $c$ and $n_0$ such that:

$$f(n) \le c \cdot g(n) \quad \forall n \ge n_0$$



* Represents the maximum/worst-case runtime ceiling.



### 2. Big-Omega Notation ($\Omega$) — Lower Bound

* **Definition:** $f(n) = \Omega(g(n))$ if there exist positive constants $c$ and $n_0$ such that:

$$f(n) \ge c \cdot g(n) \quad \forall n \ge n_0$$



* Represents the minimum/best-case runtime floor.



### 3. Theta Notation ($\Theta$) — Tight / Average Bound

* **Definition:** $f(n) = \Theta(g(n))$ if there exist positive constants $c_1, c_2$ and $n_0$ such that:

$$c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \quad \forall n \ge n_0$$



* $f(n) = \Theta(g(n))$ holds if and only if $f(n) = \mathcal{O}(g(n))$ and $f(n) = \Omega(g(n))$.



---

## 6. Properties of Asymptotic Notations

1. **General Multiplication:** If $f(n) = \mathcal{O}(g(n))$, then $a \cdot f(n) = \mathcal{O}(g(n))$ for any constant $a$.


2. **Reflexive:** $f(n) = \mathcal{O}(f(n))$.


3. **Transitive:** If $f(n) = \mathcal{O}(g(n))$ and $g(n) = \mathcal{O}(h(n))$, then $f(n) = \mathcal{O}(h(n))$.


4. **Symmetric:** If $f(n) = \Theta(g(n))$, then $g(n) = \Theta(f(n))$.


5. **Transpose Symmetric:** If $f(n) = \mathcal{O}(g(n))$, then $g(n) = \Omega(f(n))$.


6. **Sum Rule:** If $f(n) = \mathcal{O}(g(n))$ and $d(n) = \mathcal{O}(e(n))$, then:

$$f(n) + d(n) = \mathcal{O}(\max(g(n), e(n)))$$



7. **Product Rule:** If $f(n) = \mathcal{O}(g(n))$ and $d(n) = \mathcal{O}(e(n))$, then:

$$f(n) \cdot d(n) = \mathcal{O}(g(n) \cdot e(n))$$




---

## 7. Best, Worst, and Average Cases

### Linear Search Analysis

* **Best Case:** Target element is at index 0.


* $B(n) = 1 \implies \mathcal{O}(1)$



* **Worst Case:** Target element is at index $n-1$ or not present.


* $W(n) = n \implies \mathcal{O}(n)$



* **Average Case:**

$$A(n) = \frac{1 + 2 + 3 + \dots + n}{n} = \frac{\frac{n(n+1)}{2}}{n} = \frac{n+1}{2} \implies \mathcal{O}(n)$$




### Binary Search Tree (BST) Search

* **Best Case:** Target element is at the root node $\implies \mathcal{O}(1)$.


* **Worst Case (Balanced Tree):** Target element is a leaf node in a balanced tree $\implies \mathcal{O}(\log_2 n)$.


* **Worst Case (Skewed Tree):** Target element is a leaf node in a completely unbalanced/skewed tree $\implies \mathcal{O}(n)$.
