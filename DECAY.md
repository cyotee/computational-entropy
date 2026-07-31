# Decay vectors for logic gates (worked examples)

Yes — treating logic gates as functions is not only appropriate, it is exactly how this repo uses them (the M11 AND-gate ledger is a finite map $f \colon \{0,1\}^n \to \{0,1\}^m$). A gate is just a total function on bits; IDEM’s decay vector is about **recoverability of inputs from the output of that map**.

This note has three layers:

1. **Explain it like I’m 5** — a teaching walkthrough of what the decay vector *means* and how to compute it by hand (finite gates).
2. **Worked tables** — formal hard/soft decay for AND, OR, NAND, NOR, XOR, NOT, and projection.
3. **Beyond truth tables** — continuous / infinite-domain functions with different arities, using the classical repo pair $\sqrt{x}$ and $\max(x,y)$.

---

# Explain it like I’m 5

## The one-sentence idea

A **decay vector** answers this question for each input wire:

> **If I only see the answer (the output), can I still figure out what that input was?**

- **0** means “yes — that input is still knowable from the output.” Nothing important was lost for that wire. Think: **kept**.
- **1** means “no — that input could be several different things.” Information about that wire **decayed** (got mixed away / thrown away). Think: **lost**.

So for a 2-input gate, the decay vector looks like:

$$
\mathbf{d} = [d_x,\ d_y]
$$

Examples of what those numbers mean:

| Vector | In plain English |
| --- | --- |
| $[0, 0]$ | Both inputs are still knowable from the output |
| $[1, 1]$ | Both inputs are lost; output alone doesn’t pin them down |
| $[0, 1]$ | First input is knowable; second is lost |
| $[1, 0]$ | First is lost; second is knowable |
| $[0]$ | One-input gate; that single input is knowable |

You do **not** need transistors, physics, or “how the chip works.” You only need the **truth table** (the map from inputs → output).

---

## A better picture: two private votes, one public announcement

Two people, **Alice** and **Bob**, each cast a private yes/no vote:

- Alice’s vote $= x$ (0 or 1)
- Bob’s vote $= y$ (0 or 1)

A known rule turns those two votes into **one public announcement** $Y$.  
You see only the announcement. You do not see the ballots.

That is exactly a 2-input gate.

**Decay** means: *from the announcement alone, is a given person’s vote still knowable?*

| For person $i$ | Meaning |
| --- | --- |
| $d_i = 0$ | **Kept** — given this announcement, their vote is forced |
| $d_i = 1$ | **Lost** — several vote pairs fit the same announcement, so that person could have voted either way |

The decay vector is just Alice’s score and Bob’s score side by side: $\mathbf{d} = [d_{\text{Alice}},\ d_{\text{Bob}}]$.

Why this metaphor works:

1. **Inputs** = private votes (the things you wish you still knew).  
2. **Output** = one public sentence (the only thing you get).  
3. **Decay of a person** = “can I still read their ballot from that sentence?”  
4. No gadgets, no shouting machines — only secrecy vs. publication.

How the main gates sound in this language:

| Gate (rule for the announcement) | What the public hears | Recoverability intuition |
| --- | --- | --- |
| **AND** — “Did *both* vote yes?” | “Yes, unanimous yes” or “No, not both yes” | If unanimous yes → both votes known. If not → someone said no, but you don’t know who → both votes lost. |
| **OR** — “Did *anyone* vote yes?” | “Nobody did” or “At least one did” | If nobody → both voted no (known). If at least one → don’t know who → both lost. |
| **XOR** — “Did they *disagree*?” | “Same” or “Different” | You learn the relation, never either person’s actual vote. |
| **Proj$_x$** — “Just publish Alice’s vote” | Alice’s bit only | Alice kept; Bob’s ballot was never published → Bob lost. |
| **NOT** — one person, flip their vote | The flipped bit | Fully reversible: invert the announcement to recover the only vote. |

That is the whole idea of the decay vector: **per person / per wire, kept or lost, after a summary replaces the full record.**

---

## What you are allowed to know when you calculate

**Standard rule used in this note:**

You know:

1. the **gate** (you know the function $f$), and  
2. the **output** $Y$.

You do **not** see the original inputs.

(If the function itself were secret, that is a different number called $d_f$. Ignore $d_f$ until the end; the usual decay vector is only about inputs.)

---

## The teachable recipe (do this every time)

Print this on a sticky note:

### Step 0 — Write the truth table

List every possible input and its output. For 2-bit gates there are only **4** rows.

### Step 1 — Group by output (make “buckets”)

For each possible output value, list every input that produces it.  
Those lists are called **preimages** (“what came before this output?”).

```text
Output bucket Y = 0:   all input pairs that make Y=0
Output bucket Y = 1:   all input pairs that make Y=1
```

### Step 2 — For one bucket, score each input wire

Look at **one** output bucket at a time.

For input wire $x$:

- Look at the $x$ column **only inside that bucket**.
- If every row has the **same** $x$ (all 0s, or all 1s) → $d_x = 0$ (**kept**).
- If the $x$ column has **both** 0 and 1 in that bucket → $d_x = 1$ (**lost**).

Do the same for wire $y$. That gives a **branch** decay vector for that output:

$$
\mathbf{d}(Y = y) = [d_x,\ d_y]
$$

**Kid test for one wire:**  
“In this bucket, is that wire always the same answer, or does it wiggle?”  
Always the same → 0. Wiggles → 1.

### Step 3 — Global decay (the usual summary for the whole gate)

For each wire, if it is lost in **any** output bucket, mark it lost globally:

$$
d_i^{\text{global}} =
\begin{cases}
1 & \text{if some output bucket has } d_i = 1 \\
0 & \text{if every output bucket has } d_i = 0
\end{cases}
$$

One-line adult version:

> If two different inputs give the **same** output but disagree on wire $i$, then global $d_i = 1$.

### Step 4 (optional) — Soft / “how much” decay

Hard 0/1 only says *whether* a wire can be lost.  
**Export** asks *how much* input uncertainty remains after seeing $Y$:

$$
H(X \mid Y) = \sum_y p(y) \log_2 \lvert f^{-1}(y) \rvert.
$$

Bigger preimage buckets ⇒ more leftover uncertainty ⇒ more export. You can teach hard decay without this; soft export is the “how many bits of the private ballots are still unknown?” upgrade.

---

## Walkthrough A — AND (full hand calculation)

Gate: $Y = x \land y$ (both inputs must be 1 to get output 1).

### Step 0 — Truth table

| $x$ | $y$ | $Y = x \land y$ |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### Step 1 — Buckets (preimages)

**Bucket $Y = 0$** (three pairs):

| $x$ | $y$ |
| --- | --- |
| 0 | 0 |
| 0 | 1 |
| 1 | 0 |

**Bucket $Y = 1$** (one pair):

| $x$ | $y$ |
| --- | --- |
| 1 | 1 |

### Step 2 — Score each bucket

**Bucket $Y = 0$:**

- Wire $x$: values are 0, 0, 1 → **wiggles** → $d_x = 1$
- Wire $y$: values are 0, 1, 0 → **wiggles** → $d_y = 1$
- Branch vector: $\mathbf{d}(Y=0) = [1, 1]$

Plain English: if the announcement is only “not both yes,” three vote pairs still fit. You cannot recover Alice’s or Bob’s vote.

**Bucket $Y = 1$:**

- Wire $x$: only 1 → **fixed** → $d_x = 0$
- Wire $y$: only 1 → **fixed** → $d_y = 0$
- Branch vector: $\mathbf{d}(Y=1) = [0, 0]$

Plain English: if the announcement is “both yes,” both votes **must** have been 1. Nothing decayed on this branch.

### Step 3 — Global vector

$x$ was lost on $Y=0$, so global $d_x = 1$.  
$y$ was lost on $Y=0$, so global $d_y = 1$.

$$
\mathbf{d}(\mathrm{AND}) = [1, 1]
$$

**Teaching takeaway:** global $[1,1]$ does **not** mean “you never recover anything.” It means “there exists a situation where you lose the wire.” On the lucky branch $Y=1$, AND actually keeps both wires.

---

## Walkthrough B — OR (same skill, mirrored buckets)

Gate: $Y = x \lor y$.

| $x$ | $y$ | $Y$ |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Bucket $Y = 0$:** only $(0,0)$ → both wires fixed → $\mathbf{d}(Y=0) = [0,0]$  
**Bucket $Y = 1$:** $(0,1),\ (1,0),\ (1,1)$ → both wires wiggle → $\mathbf{d}(Y=1) = [1,1]$

Global: $\mathbf{d}(\mathrm{OR}) = [1,1]$

**Compare to AND:**

| | Lucky (fully recoverable) branch | Unlucky (both lost) branch |
| --- | --- | --- |
| AND | $Y = 1$ → only $(1,1)$ | $Y = 0$ → three pairs |
| OR | $Y = 0$ → only $(0,0)$ | $Y = 1$ → three pairs |

Same **global** decay vector $[1,1]$. Different **which announcement** is the lucky one.

---

## Walkthrough C — XOR (no lucky branch)

Gate: $Y = x \oplus y$ (true when the two bits **differ**).

| $x$ | $y$ | $Y$ |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Bucket $Y = 0$:** $(0,0)$ and $(1,1)$

- $x$ is 0 and 1 → wiggles → $d_x = 1$
- $y$ is 0 and 1 → wiggles → $d_y = 1$
- $\mathbf{d}(Y=0) = [1,1]$

**Bucket $Y = 1$:** $(0,1)$ and $(1,0)$

- same story → $\mathbf{d}(Y=1) = [1,1]$

Global: $\mathbf{d}(\mathrm{XOR}) = [1,1]$

**Kid difference from AND:**  
With XOR you learn a **rule** (“same” vs “different”), but you never learn the actual pair. There is **no** output that pins both bits down. AND sometimes does ($Y=1$); XOR never does.

---

## Walkthrough D — Projection (one wire kept, one lost)

Gate: $Y = x$ (ignore $y$). Call it $\mathrm{Proj}_x$.

| $x$ | $y$ | $Y$ |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Bucket $Y = 0$:** $(0,0),\ (0,1)$

- $x$ always 0 → $d_x = 0$ (**kept**)
- $y$ is 0 and 1 → $d_y = 1$ (**lost**)
- $\mathbf{d}(Y=0) = [0,1]$

**Bucket $Y = 1$:** $(1,0),\ (1,1)$ → same pattern → $[0,1]$

Global: $\mathbf{d} = [0,1]$

**Teaching takeaway:** decay is **per wire**, not “the whole gate is bad.” The announcement publishes Alice perfectly and never reveals Bob.

---

## Walkthrough E — NOT (nothing decays)

Gate: $Y = \lnot x$ (one input only).

| $x$ | $Y$ |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

Each output bucket has **exactly one** preimage. The single wire never wiggles.

$$
\mathbf{d}(\mathrm{NOT}) = [0]
$$

If you hear $Y$, you can always invert: $x = \lnot Y$. **No decay.**

---

## Practice checklist (teach someone else)

Have the learner pick any gate and fill this sheet:

```text
Gate name: _______________

1) Truth table (all inputs → Y)

2) Bucket Y=0: list inputs
   - Does x wiggle?  yes→1 / no→0
   - Does y wiggle?  yes→1 / no→0
   - Branch d(Y=0) = [ ?, ? ]

3) Bucket Y=1: list inputs
   - Does x wiggle?  yes→1 / no→0
   - Does y wiggle?  yes→1 / no→0
   - Branch d(Y=1) = [ ?, ? ]

4) Global d:
   - d_x = 1 if either branch said 1, else 0
   - d_y = 1 if either branch said 1, else 0
   - Global d = [ d_x, d_y ]

5) (Optional) Say in one sentence:
   "When Y is ___, I can recover ___; when Y is ___, I lose ___."
```

**Answers they should get for the standard set:**

| Gate | Branch highlights | Global $\mathbf{d}$ |
| --- | --- | --- |
| AND | $[1,1]$ on $Y=0$; $[0,0]$ on $Y=1$ | $[1,1]$ |
| OR | $[0,0]$ on $Y=0$; $[1,1]$ on $Y=1$ | $[1,1]$ |
| NAND / NOR | same *sizes* as AND/OR; lucky branch flipped in label | $[1,1]$ |
| XOR / XNOR | $[1,1]$ on **both** branches | $[1,1]$ |
| $\mathrm{Proj}_x$ | $[0,1]$ on both branches | $[0,1]$ |
| NOT | always $[0]$ | $[0]$ |

---

## Common beginner mistakes

1. **Thinking global $[1,1]$ means “never recoverable.”**  
   Wrong for AND: $Y=1$ recovers both inputs. Global only says a wire is *sometimes* lost.

2. **Scoring wires across the whole table instead of inside one bucket.**  
   Always group by **output first**, then look for wiggling.

3. **Confusing “I know the rule of the gate” with “I know the inputs.”**  
   Knowing $f$ is allowed. Decay asks whether the **inputs** are fixed by $Y$.

4. **Mixing hard decay with export entropy.**  
   Hard $\mathbf{d}$ is 0/1 recoverability flags.  
   $H(X \mid Y)$ is “how many bits of uncertainty remain.”  
   XOR and $\mathrm{Proj}_x$ both export 1 bit, but their hard vectors differ ($[1,1]$ vs $[0,1]$).

5. **Forgetting arity.**  
   NOT has one number $[0]$. Two-input gates have two numbers $[d_x, d_y]$.

---

## Mini glossary for teachers

| Term | Friendly meaning |
| --- | --- |
| Function / gate $f$ | Rule that turns inputs into an output |
| Output $Y$ | The only thing the observer sees |
| Preimage / bucket | All input pairs that produce a given $Y$ |
| Wire / coordinate | One input slot ($x$ or $y$) |
| $d_i = 0$ | That wire is fixed in the bucket → recoverable |
| $d_i = 1$ | That wire wiggles in the bucket → lost (“decayed”) |
| Branch decay $\mathbf{d}(Y)$ | Score **for one output value** |
| Global decay $\mathbf{d}$ | Score for the **whole gate** (lost if ever lost) |
| Export $H(X \mid Y)$ | Soft measure of leftover uncertainty after seeing $Y$ |

---

# Formal worked examples

Below: hard decay (global + per-output branch), then soft/export comparison.  
Same rules as the teaching section; denser tables for reference.

---

## Setup (same for every 2-input gate)

- Domain: $\{0,1\}^2$, inputs $(x,y)$, 4 possible inputs, fair prior $p = 1/4$ each unless noted.
- Map: $Y = f(x,y)$.
- Observer sees **only** $Y$ (and knows $f$).

**Hard branch decay** (most informative):

$$
d_i(y) =
\begin{cases}
0 & \text{if } x_i \text{ is the same on every preimage of } y \\
1 & \text{if that coordinate varies in the preimage}
\end{cases}
$$

**Hard global decay:** $d_i = 1$ if *any* branch loses coordinate $i$ (equivalently: $x_i$ is not a function of $Y$ alone).

**Soft/export** (for intuition):

$$
H(X \mid Y) = \sum_y p(y) \log_2 \lvert f^{-1}(y) \rvert.
$$

---

## 1. AND — $Y = x \land y$

Truth table:

| $x$ | $y$ | $Y$ |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Preimages**

| $Y$ | Preimages | $\mathbf{d}(Y) = [d_x, d_y]$ | Why |
| --- | --- | --- | --- |
| 0 | $(0,0),\ (0,1),\ (1,0)$ | $[1,1]$ | both coords take 0 and 1 |
| 1 | $(1,1)$ only | $[0,0]$ | both coords fixed |

**Global hard decay:** $\mathbf{d}(\mathrm{AND}) = [1,1]$

Seeing $Y=1$ recovers both bits; seeing $Y=0$ recovers neither. Globally, neither input is always recoverable from $Y$ alone.

**Export:**

$$
H(X \mid Y) = \tfrac{3}{4}\log_2 3 + \tfrac{1}{4}\cdot 0 \approx 1.189
$$

bits (classic M11 AND figure).

---

## 2. OR — $Y = x \lor y$

| $x$ | $y$ | $Y$ |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

| $Y$ | Preimages | $\mathbf{d}(Y)$ |
| --- | --- | --- |
| 0 | $(0,0)$ | $[0,0]$ |
| 1 | $(0,1),\ (1,0),\ (1,1)$ | $[1,1]$ |

**Global hard decay:** $\mathbf{d}(\mathrm{OR}) = [1,1]$

Same pattern as AND, **mirrored**: the unique preimage is the all-zero input (for OR) vs all-one (for AND).

**Export:** same as AND, $\approx 1.189$ bits (same preimage sizes $3$ and $1$).

---

## 3. NAND and NOR (same decay pattern family)

**NAND** $Y = \lnot(x \land y)$:

| $Y$ | Preimages | $\mathbf{d}(Y)$ |
| --- | --- | --- |
| 0 | $(1,1)$ | $[0,0]$ |
| 1 | three others | $[1,1]$ |

**NOR** $Y = \lnot(x \lor y)$:

| $Y$ | Preimages | $\mathbf{d}(Y)$ |
| --- | --- | --- |
| 1 | $(0,0)$ | $[0,0]$ |
| 0 | three others | $[1,1]$ |

**Global hard decay for both:** $[1,1]$

**Export:** same $\approx 1.189$ bits.

So **AND / OR / NAND / NOR** all share:

- one fully recoverable branch (singleton preimage),
- one fully lost branch (triple preimage),
- global $\mathbf{d} = [1,1]$.

They differ only in **which output value** is the “safe” branch.

---

## 4. XOR — $Y = x \oplus y$ (more irreversible in a different way)

| $x$ | $y$ | $Y$ |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

| $Y$ | Preimages | $\mathbf{d}(Y)$ |
| --- | --- | --- |
| 0 | $(0,0),\ (1,1)$ | $[1,1]$ |
| 1 | $(0,1),\ (1,0)$ | $[1,1]$ |

**Global hard decay:** $\mathbf{d}(\mathrm{XOR}) = [1,1]$

Unlike AND/OR, **no output fully recovers the inputs**. Every branch has size 2, and both coordinates vary.

**Export:** $H(X \mid Y) = 1$ bit always  
(knowing $Y$ still leaves one free bit of uncertainty about $(x,y)$).

**XNOR** is the same for decay: every preimage size 2, $\mathbf{d}(y) = [1,1]$ always, global $[1,1]$, export $1$ bit.

---

## 5. NOT and wire (unary / “trivial” gates)

**NOT** $Y = \lnot x$ (arity 1):

| $Y$ | Preimage | $\mathbf{d}(Y)$ |
| --- | --- | --- |
| 0 | $x = 1$ | $[0]$ |
| 1 | $x = 0$ | $[0]$ |

**Global:** $\mathbf{d}(\mathrm{NOT}) = [0]$ — fully recoverable ($x = \lnot Y$).

**Export:** $H(X \mid Y) = 0$.

**BUF / identity** $Y = x$: same, $\mathbf{d} = [0]$, export $0$.

These are the **irreversible vs reversible** contrast: NOT is bijective; AND is not.

---

## 6. Projection (useful comparison — not “lost equally”)

**$\mathrm{Proj}_x$** $Y = x$ (ignore $y$):

| $Y$ | Preimages | $\mathbf{d}(Y)$ |
| --- | --- | --- |
| 0 | $(0,0),\ (0,1)$ | $[0,1]$ |
| 1 | $(1,0),\ (1,1)$ | $[0,1]$ |

**Global:** $\mathbf{d} = [0,1]$

$x$ always recoverable ($x = Y$); $y$ always lost.

**Export:** $H(X \mid Y) = 1$ bit (exactly the free $y$).

This shows decay is **per coordinate**, not a single “gate is irreversible” flag.

---

## Comparative summary

| Gate | Global hard $\mathbf{d}$ | Branch pattern | $H(X \mid Y)$ (fair bits) | Intuition |
| --- | --- | --- | --- | --- |
| NOT / BUF | $[0]$ | always recoverable | $0$ | reversible |
| $\mathrm{Proj}_x$ | $[0,1]$ | always keep $x$, lose $y$ | $1$ | pure erasure of one wire |
| AND | $[1,1]$ | $[0,0]$ on $Y=1$; $[1,1]$ on $Y=0$ | $\approx 1.189$ | mostly irreversible |
| OR | $[1,1]$ | $[0,0]$ on $Y=0$; $[1,1]$ on $Y=1$ | $\approx 1.189$ | dual of AND |
| NAND / NOR | $[1,1]$ | same sizes as AND/OR | $\approx 1.189$ | same export, flipped labels |
| XOR / XNOR | $[1,1]$ | $[1,1]$ on **both** branches | $1$ | no “lucky” output recovers inputs |

---

## How to calculate (repeatable recipe)

For any gate $f$:

1. List the truth table.
2. For each output value $y$, collect preimages $f^{-1}(y)$.
3. For each input wire $i$:
   - if that bit is constant on the preimage → $d_i(y) = 0$;
   - if it takes both 0 and 1 → $d_i(y) = 1$.
4. Global hard vector: $d_i = \max_y d_i(y)$ (or $1$ if any branch loses $i$).
5. Optional soft: use preimage sizes → $H(X \mid Y)$, or average $\mathbb{E}_y[\mathbf{d}(y)]$.

One-line test for global $d_i$:

> If two different inputs with the **same** $Y$ ever disagree on wire $i$, then $d_i = 1$.

---

## Is treating gates as functions appropriate?

**Yes.** In this framework:

| View | Role |
| --- | --- |
| Gate as function $f$ | Domain/codomain map; output distribution defines $H_c$ |
| IDEM | $\mathrm{IDEM}_f(x,y) = (f(x,y),\ \mathrm{info}_f)$ with decay in $\mathrm{info}_f$ |
| Decay | Information loss **of that map**, not transistor physics |
| “Irreducible” gates | Good examples of **non-injective** maps (AND/OR/XOR family) vs bijections (NOT) |

Caveats (honesty, matching the repo):

1. **Know $f$** when computing $d_i$; unknown gate identity is the separate scalar $d_f$.
2. **Global vs branch** matter: AND’s global $[1,1]$ hides that $Y=1$ fully recovers both bits.
3. **Soft ≠ hard:** XOR and Proj both export 1 bit, but Proj has $\mathbf{d} = [0,1]$ while XOR has $[1,1]$ on every branch — hard decay and export measure related but different things.
4. Multi-gate circuits: compose maps (or track intermediate wires if those wires are “public outputs”); decay of a circuit is not always just component-wise AND of gate decays.

---

## Tiny intuition picture

```text
AND, Y=1:  only (1,1)  →  both wires fixed   →  d = [0,0]  "no decay on this branch"
AND, Y=0:  three preimages → both wires free →  d = [1,1]  "full decay"

XOR, any Y: two preimages, both wires flip together → always d = [1,1]
            (you learn the relation, not the values)

Proj_x:     Y tells you x exactly; y is free      → always d = [0,1]
```

---

**Bottom line (gates):** For logic gates, calculate decay by **preimage analysis on the truth table**. AND/OR/NAND/NOR share the same hard global vector $[1,1]$ and the same export entropy, with recoverability on opposite output branches; XOR is also $[1,1]$ but **never** recovers on either branch; NOT has $[0]$; projection shows asymmetric $[0,1]$. Treating them as functions is the right and intended model for IDEM.

---

# Beyond truth tables: continuous functions ($\sqrt{x}$ and $\max$)

Logic gates are a perfect training ground because the domain is tiny: four input pairs, write a table, done.  
Real IDEM examples in this research thread often look more like:

| Function | Arity $n(f)$ | Domain (typical) | Codomain | Repo hard $\mathbf{d}$ |
| --- | --- | --- | --- | --- |
| $\sqrt{\,\cdot\,}$ | **1** | $[0,\infty)$ or $[0,1]$ | $[0,\infty)$ or $[0,1]$ | $[0]$ |
| $\max$ | **2** | $\mathbb{R}^2$ or $[0,1]^2$ | $\mathbb{R}$ or $[0,1]$ | $[1,1]$ |

Same **recoverability question** as for gates. Different **tools**, because:

1. Inputs can take an **infinite** (even continuous) range — you cannot list a truth table.
2. The two maps have **different arity**, so their decay vectors have **different lengths**.
3. Under a standard random-input story, they can even induce the **same output distribution** (same $H_c$), while having **different decay** — which is exactly why the pair is famous in this repo.

---

## Explain it like I’m 5 (continuous edition)

### Same question as the gates

Still only this:

> I see the public number $Y$.  
> For each private input, is that input **forced** by $Y$, or could it still be many things?

- Forced → $d_i = 0$ (kept)  
- Still free to wiggle inside the set of inputs that produce this $Y$ → $d_i = 1$ (lost)

### What replaces the truth table?

A **preimage geometry** (the “bucket,” but continuous):

$$
f^{-1}(y) \;=\; \{\text{all inputs that produce output } y\}.
$$

For gates, a bucket was a short list of bit-pairs.  
For continuous maps, a bucket is usually a **point**, a **curve**, a **surface**, an **L-shaped set**, etc.

**Kid test (unchanged in spirit):**  
Look at one bucket. Does private coordinate $i$ stay fixed, or does it slide along the bucket?

| In the bucket $f^{-1}(y)$… | Score |
| --- | --- |
| coordinate $i$ is the same for every input in the bucket | $d_i(y) = 0$ |
| coordinate $i$ takes more than one value in the bucket | $d_i(y) = 1$ |

Global hard decay: if that coordinate is free for some (or, under soft variants, typical) outputs, mark it lost for the function.

### Vote metaphor, continuous version

- **$\sqrt{x}$:** one private number $x \ge 0$. Announcement: “the square root is $Y$.”  
  From $Y$ you can recover $x = Y^2$ uniquely (on this domain). Alice’s only secret is kept. $\mathbf{d}=[0]$.

- **$\max(x,y)$:** two private numbers. Announcement: “the larger one is $Y$.”  
  You know the **winner’s value**, but not which person won, and the loser can be anything $\le Y$. Both secrets are lost in general. $\mathbf{d}=[1,1]$.

No truth table required — only “what set of private numbers is still possible after the announcement?”

---

## Recipe when the domain is infinite

### Step 0 — Fix the domain and the exact map

This is more important than for bits. Example traps:

| Choice | Effect on $\sqrt{\,\cdot\,}$ |
| --- | --- |
| Domain $[0,\infty)$, principal (nonnegative) square root | $x = Y^2$ unique → $d=[0]$ |
| Real square root as a multi-valued $\pm$ relation | not a single-valued function; recoverability story changes |
| Domain $\mathbb{R}$ with $x \mapsto \sqrt{\lvert x\rvert}$ | preimage of $Y$ is usually **two** points $\{\pm Y^2\}$ if signed — then $d=[1]$ |

**House convention in this note (and the IDEM formalization):**

$$
\sqrt{\,\cdot\,} \colon [0,\infty) \to [0,\infty),
\qquad
\max \colon \mathbb{R}^2 \to \mathbb{R}
\quad\text{(or both restricted to unit cubes/intervals when comparing output laws).}
$$

### Step 1 — Pick a generic output $y$ and describe $f^{-1}(y)$

Do **not** enumerate. Write a set definition.

### Step 2 — For each input coordinate, ask: does it vary on that set?

- If the preimage is a singleton and fixes coordinate $i$ → $d_i(y)=0$.  
- If the preimage is a continuum (interval, ray, L-shape, …) along which coordinate $i$ moves → $d_i(y)=1$.

### Step 3 — Assemble the vector (length = arity)

$$
\mathbf{d}(f) = [d_1,\ldots,d_{n(f)}].
$$

Arity $1$ → length $1$. Arity $2$ → length $2$. **Do not pad or force equal length.**

### Step 4 — (Optional) Soft / continuous export

Hard 0/1 still answers kept/lost.  
“How much is lost?” needs a measure on inputs (e.g. $H(X\mid Y)$ or differential analogues). Hard decay does **not** require that.

### Step 5 — (Optional) $d_f$ when the function is unknown

If the observer sees only $Y$ and does **not** know whether the map was $\sqrt{\,\cdot\,}$ or $\max$, that is **function unidentifiability** $d_f$, not input decay. See the comparison table at the end of this section.

---

## Worked example 1 — $\sqrt{x}$ (arity 1, infinite domain)

### Setup

$$
f(x) = \sqrt{x}, \qquad x \in [0,\infty), \qquad Y = f(x) \in [0,\infty).
$$

Arity $n(f) = 1$, so the decay vector has **one** entry: $\mathbf{d} = [d_x]$.

### Step 1 — Preimage of a fixed output $y \ge 0$

Solve $\sqrt{x} = y$ with $x \ge 0$:

$$
f^{-1}(y) = \{ y^2 \}.
$$

One point. Not a list of $2^n$ rows — a **singleton set**.

### Step 2 — Does $x$ wiggle in the bucket?

No. The only possible private input is $x = y^2$.

Recovery map:

$$
g(Y) = Y^2, \qquad g(f(x)) = x \quad\text{for all } x \ge 0.
$$

So $d_x(y) = 0$ for every $y$, hence:

$$
\mathbf{d}(\sqrt{\,\cdot\,}) = [0].
$$

### Teaching read

This is the continuous cousin of **NOT** / identity: the map is **invertible on its domain**, so the single private number is kept.  
Infinite domain did **not** create decay. **Non-injectivity** creates decay; infinity alone does not.

### IDEM packaging (repo style)

$$
\mathrm{IDEM}_{\sqrt{\,}}(x) = \bigl(\sqrt{x},\ \mathrm{info}\bigr),
\qquad
\mathrm{info} = \bigl(n=1,\ D_r=1,\ \mathbf{d}=[0]\bigr).
$$

Example: $x=4$ → $(2,\ (1,1,[0]))$.

---

## Worked example 2 — $\max(x,y)$ (arity 2, infinite domain)

### Setup

$$
f(x,y) = \max(x,y), \qquad (x,y) \in \mathbb{R}^2, \qquad Y = f(x,y) \in \mathbb{R}.
$$

Arity $n(f) = 2$, so $\mathbf{d} = [d_x, d_y]$.

### Step 1 — Preimage of a fixed output $z$

$$
f^{-1}(z)
=
\{ (x,y) : \max(x,y) = z \}
=
\underbrace{\{ (z,y) : y \le z \}}_{\text{$x$ wins or ties}}
\;\cup\;
\underbrace{\{ (x,z) : x \le z \}}_{\text{$y$ wins or ties}}.
$$

Picture an **L-shaped** set (two rays meeting at $(z,z)$):

```text
y
^
|          *
|          *
|          *  (x=z, y≤z)
|          *
|  ********+**** →  (y=z, x≤z)
|          (z,z)
+--------------------→ x
```

(On $[0,1]^2$ with $z \in [0,1]$, the same idea: an L cut off by the unit square.)

### Step 2 — Score each coordinate on that set

**Wire $x$:** on the horizontal arm, $x$ runs through $(-\infty, z]$ (or $[0,z]$ on the unit square). So $x$ **varies**. → $d_x(z) = 1$.

**Wire $y$:** on the vertical arm, $y$ runs through $(-\infty, z]$. So $y$ **varies**. → $d_y(z) = 1$.

For every $z$:

$$
\mathbf{d}(z) = [1,1].
$$

Global:

$$
\mathbf{d}(\max) = [1,1].
$$

### Why you cannot “just invert”

There is **no** function $g_x$ with $g_x(\max(x,y)) = x$ for all $(x,y)$.  
Counterexample: $\max(3,1) = \max(3,2) = 3$, but the first coordinates are both 3 while seconds differ; worse, $\max(1,3)=3$ has first coordinate $1 \neq 3$. Same output, different $x$.

Same argument for $y$.

### Teaching read

$\max$ is the continuous cousin of **OR** (or of “announce the larger vote value without saying who”):

- You learn a **summary statistic** of the two secrets.
- You do **not** learn a unique pair $(x,y)$.
- Both coordinates remain free along a continuum → both decay.

### Branch nuance (optional, advanced)

Hard global $\mathbf{d}=[1,1]$ is unambiguous.  
If you condition on extra side information (e.g. you already know $x$, and hear $z=\max(x,y)$), then $y$ may become recoverable on some regions ($y=z$ when $z>x$, etc.). That is a **different observer model** — same caveat as “decay given other inputs” for gates.

### IDEM packaging (repo style)

$$
\mathrm{IDEM}_{\max}(x,y) = \bigl(\max(x,y),\ \mathrm{info}\bigr),
\qquad
\mathrm{info} = \bigl(n=2,\ D_r=1,\ \mathbf{d}=[1,1]\bigr).
$$

Example: $(3,4)$ → $(4,\ (2,1,[1,1]))$.

---

## Side-by-side teaching comparison

| | $\sqrt{x}$ | $\max(x,y)$ |
| --- | --- | --- |
| Arity $n(f)$ | 1 | 2 |
| Decay vector **length** | 1 | 2 |
| Typical preimage of one $Y$ | singleton $\{Y^2\}$ | L-shaped continuum |
| Hard $\mathbf{d}$ | $[0]$ | $[1,1]$ |
| Invert from $Y$ alone? | yes ($x=Y^2$) | no |
| Finite truth table? | no | no |
| Closest gate cousin | NOT / identity | OR-like many-to-one summary |

**Key lesson:** arity changes the **shape** of $\mathbf{d}$. You must not force $\sqrt{\,\cdot\,}$ and $\max$ into the same vector length. Comparing them means comparing **different-length** recoverability records, plus (if you want) shared output statistics.

---

## Same output law, different decay (why the pair is sharp)

This is the repo’s classic “informational equivalence of outputs ≠ same decay” demo.

### Random inputs (unit interval)

- $\sqrt{\,\cdot\,}$ case: let $U \sim \mathrm{Unif}[0,1]$, set $Y_1 = \sqrt{U}$.  
- $\max$ case: let $U_1,U_2 \stackrel{\mathrm{iid}}{\sim} \mathrm{Unif}[0,1]$, set $Y_2 = \max(U_1,U_2)$.

Both $Y_1$ and $Y_2$ have the **same** law on $[0,1]$: density

$$
f_Y(y) = 2y, \qquad y \in [0,1].
$$

Therefore the **computational entropies match** (same output distribution):

$$
H_c(\sqrt{\,\cdot\,}; p_U) = H_c(\max; p_{U_1,U_2})
$$

(in the differential-entropy sense used illustratively in Paper A; the point is equality of output laws).

But the **decay vectors do not match**:

| Map | Output law | Hard decay |
| --- | --- | --- |
| $\sqrt{U}$ | density $2y$ on $[0,1]$ | $[0]$ |
| $\max(U_1,U_2)$ | **same** density $2y$ | $[1,1]$ |

### What this teaches

1. **$H_c$ only sees the public output histogram.** Same histogram ⇒ same $H_c$.  
2. **$\mathbf{d}$ sees per-input recoverability.** Different private structure ⇒ different $\mathbf{d}$.  
3. So $\sqrt{\,\cdot\,}$ and $\max$ can look identical if you only watch $Y$, yet one is reversible in its single input and the other is not.  
4. That is why IDEM carries **both** the result and metadata $(\,n(f),\ D_r,\ \mathbf{d}\,)$ — output value alone under-describes the map.

### ELI5 for this twist

Two different classroom rules can produce the **same grade distribution** on the blackboard:

- Rule A: one student, announce $\sqrt{\text{score}}$.  
- Rule B: two students, announce the higher score.

Histograms of announcements can match.  
But “can I reconstruct the private score(s)?” is **not** the same under the two rules. Decay tracks that second question.

---

## Practice: calculate continuous decay without a table

### Drill sheet

```text
Function: ____________________
Domain:   ____________________
Arity n:  ____   (⇒ decay vector has ____ slots)

For a generic output y:
  1) Write the set f^{-1}(y) = ...
  2) For each input coordinate i = 1..n:
       Does that coordinate take more than one value on the set?
         no  → d_i(y) = 0
         yes → d_i(y) = 1
  3) Global d = [ d_1, ..., d_n ]
     (usually: 1 if free on a positive-measure set of y)

Optional:
  - Give an explicit recovery map g_i if d_i = 0.
  - Give two different inputs with same output if d_i = 1.
```

### Self-check answers

| Function (stated domain) | $f^{-1}(y)$ sketch | $\mathbf{d}$ |
| --- | --- | --- |
| $\sqrt{x}$ on $[0,\infty)$ | $\{y^2\}$ | $[0]$ |
| $x \mapsto x^2$ on $\mathbb{R}$ | $\{-\sqrt{y},+\sqrt{y}\}$ for $y>0$ | $[1]$ |
| $x \mapsto x^2$ on $[0,\infty)$ | $\{\sqrt{y}\}$ | $[0]$ |
| $\max(x,y)$ on $\mathbb{R}^2$ | L-shape at level $y$ | $[1,1]$ |
| $\min(x,y)$ on $\mathbb{R}^2$ | inverted L (rays $x\ge y$ / $y\ge x$ style) | $[1,1]$ |
| $(x,y)\mapsto x$ on $\mathbb{R}^2$ | vertical line $x=y_{\mathrm{out}}$ ( $y$ free) | $[0,1]$ |
| $(x,y)\mapsto (x,y)$ | singleton | $[0,0]$ |

### One-line global tests (continuous)

- $d_i = 0$ iff there exists $g_i$ with $x_i = g_i(f(\mathbf{x}))$ for **all** inputs in the domain.  
- $d_i = 1$ iff there exist $\mathbf{x} \neq \mathbf{x}'$ with $f(\mathbf{x})=f(\mathbf{x}')$ but $x_i \neq x_i'$.

Same logical tests as for gates — only the search for those witnesses is geometric, not tabular.

---

## Different arity, “equal size” outputs — what people mix up

Three different “sizes” that are easy to confuse:

| Notion | $\sqrt{\,\cdot\,}$ | $\max$ | Equal? |
| --- | --- | --- | --- |
| Input dimension / arity | 1 | 2 | **No** |
| Output dimension $D_r$ | 1 scalar | 1 scalar | **Yes** |
| Output **law** under the Unif story above | density $2y$ | density $2y$ | **Yes** |
| Hard decay vector | $[0]$ | $[1,1]$ | **No** |

So it is fair to say:

- both produce a **single** real result ($D_r = 1$);  
- both can be arranged to produce a result **distribution of the same size/law**;  
- they still do **not** share arity or decay.

IDEM metadata is built exactly to keep those distinctions explicit: $(n(f),\ D_r(f),\ \mathbf{d}(f))$.

---

## Soft note: continuous “export” vs hard decay

For finite gates we used

$$
H(X \mid Y) = \sum_y p(y)\log_2 \lvert f^{-1}(y)\rvert.
$$

Continuously, $\lvert f^{-1}(y)\rvert$ is often infinite, so the right soft object is a **conditional entropy / residual freedom** along the preimage (with a chosen input measure). Qualitatively:

| Map | Hard $\mathbf{d}$ | Soft intuition |
| --- | --- | --- |
| $\sqrt{\,\cdot\,}$ on $[0,\infty)$ | $[0]$ | residual uncertainty about $x$ given $Y$ is zero |
| $\max$ on $[0,1]^2$ | $[1,1]$ | given $Y=z$, one degree of freedom remains on the L-shape |

Hard decay is still the right first teaching tool: it only needs geometry of preimages, not a full measure-theoretic entropy calculation.

---

## When $\sqrt{\,\cdot\,}$ vs $\max$ is unknown ($d_f$)

Suppose an observer sees only a number $Y \in (0,1]$ and knows the generator was **either** $\sqrt{U}$ or $\max(U_1,U_2)$ under the uniform stories above. Then:

- **Input decay** is not even well-posed until $f$ is fixed (arity differs!).  
- **Function unidentifiability** $d_f$ stays positive until enough structure (or side information) rules one hypothesis out.

That is a separate IDEM metadata slot from $\mathbf{d}$. Teaching order:

1. Fix $f$ and domain → compute $\mathbf{d}$ (this section).  
2. Only then, if $f$ is secret in a class $\{\sqrt{\,\cdot\,},\max,\ldots\}$, track $d_f$ with Bayesian updates on I/O evidence.

---

## Continuous checklist (sticky note)

```text
1. Write f and its domain (arity = number of private inputs).
2. For generic y, describe the set f^{-1}(y)  [point / curve / L / …].
3. Per coordinate: fixed on that set → 0, free on that set → 1.
4. Vector length must equal arity.
5. Optional: same output law as another f' does NOT imply same d.
6. Optional: d_f is "which f?" — not the same as d_i "which x_i?".
```

---

**Bottom line (continuous):**  
To compute decay for $\sqrt{x}$ and $\max(x,y)$, abandon truth tables and inspect **preimage sets**. On $[0,\infty)$, $\sqrt{\,\cdot\,}$ has singleton preimages and $\mathbf{d}=[0]$. On $\mathbb{R}^2$, $\max$ has L-shaped preimages and $\mathbf{d}=[1,1]$. Different arities ⇒ different vector lengths. They may share an output distribution while disagreeing on decay — so $H_c$ and $\mathbf{d}$ answer different questions, and IDEM keeps both.
