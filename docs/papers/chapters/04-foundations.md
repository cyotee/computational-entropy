# 4. Foundations --- Computational entropy, equivalence, and conservation

## 1.1 Definition of computational entropy

The program's primary classical and quantum objects are standard information-theoretic entropies of **outputs**, not of internal algorithm complexity alone. The canonical source is Section 1.

**Premise.** Any map that transforms random inputs induces a marginal distribution on outputs. The predictability of that output law is an entropy. Computational entropy quantifies the statistical pattern of possible results of a computation, independent of the internal mechanics that produced it.

**General case.** For any map $f$ --- deterministic, stochastic, or quantum channel --- taking input $X\sim p_X$ and producing output $Y$, computational entropy is the entropy of the induced marginal $p_Y$:

- **Classical discrete** (Tag **A** when unambiguous; Tag **E** on finite M11 maps): Shannon entropy of the output mass function  
  


$$
H_c(f; p_X) := H(Y) = -\sum_y p_Y(y)\,\log_2 p_Y(y).
$$


- **Classical continuous:** differential Shannon entropy of the output density  
  


$$
H_c(f; p_X) := h(Y) = -\int f_Y(y)\,\log_2 f_Y(y)\,dy.
$$


- **Quantum / gravity channel** (Tag **B**): von Neumann entropy of the channel output  
  


$$
S_c(\Phi;\rho_X) := S\bigl(\Phi(\rho_X)\bigr) = -\operatorname{Tr}\bigl(\Phi(\rho_X)\log_2\Phi(\rho_X)\bigr).
$$


In the gravity thread, the gravitational channel $\Phi_g$ acts on a local density operator $\rho$, and $S_c = S(\Phi_g(\rho))$ is the corresponding output entropy (canonical master-equation side: Eq.\ (\ref{eq:load}) family below). Classical $H_c$ and quantum $S_c$ share the **role** "entropy of what the channel emits," not a free symbolic identity of every repository object named $H_c$.

**Rigor:** definitions are **constructive** in the sense of standard Shannon/von Neumann theory on finite alphabets and density operators; the program's use of $S_c$ on $\Phi_g$ is framework-canonical, not a new information-theory theorem.

## 1.2 Informational equivalence of maps

**Key property.** Two or more different maps --- whether deterministic, probabilistic, or quantum --- are **informationally equivalent** if they induce output distributions with the same computational entropy. The internal mechanics (algorithm, intermediate randomness, or quantum circuit layout) do not enter the definition; only the final statistical pattern of possible outputs does.

This property is what makes computational entropy a unifying measure across classical gates, lambda reduction, games-as-maps, and CPTP channels: any probability-based prediction that depends only on $p_Y$ is shared by all maps with that $p_Y$.

## 1.3 Worked continuous example: $\sqrt{U}$ versus $\max(U_1,U_2)$

Consider two genuinely different functions on independent uniforms $U,U_1,U_2\sim\mathrm{Uniform}[0,1]$:

- Function 1: $Y_1=\sqrt{U}$ (square root of one uniform).  
- Function 2: $Y_2=\max(U_1,U_2)$ (maximum of two independent uniforms).

Both induce the **same** output PDF on $[0,1]$,


$$
f(y)=2y,
$$


and therefore the same differential computational entropy


$$
H_c(Y)=-\int_0^1 2y\log_2(2y)\,dy = -1+\frac{1}{2\ln 2}\approx -0.27865\ \mathrm{bits}.
$$


(The reflected map $Y_3=\min(U_1,U_2)$ is informationally equivalent under the substitution $z=1-y$.) Despite completely different internal operations, any prediction that depends only on the law of $Y$ --- e.g. $\mathbb{P}(Y>0.7)$, mean, variance --- is identical. This is the exact content of informational equivalence for continuous classical maps (Section 1.1).

## 1.4 Global conservation and local transfer: the AND-gate ledger

A common apparent paradox is that a computation can **reduce** local entropy (high-entropy random inputs → lower-entropy structured outputs), seemingly violating the second law. The framework resolves this by **global conservation with local transfer**: entropy is not destroyed; it is exported from the declared system output into environment / preimage registers that an observer of $Y$ alone does not hold.

### Classical irreversible AND (constructive)

Let $X=(X_1,X_2)$ be i.i.d. fair bits, so $H(X)=2$ bits. Let $Y=X_1\land X_2$. Then


$$
P(Y=1)=\tfrac14,\qquad P(Y=0)=\tfrac34,
$$


and the **declared system** computational entropy is the binary entropy of $Y$:


$$
H_c = H(Y) = h_2\bigl(\tfrac14\bigr)\approx 0.811278\ \mathrm{bits}.
$$


The "missing" mass relative to the input is **export**, not destruction:


$$
H(X\mid Y)\approx 1.188722\ \mathrm{bits},
$$


and the chain rule for a deterministic map is an identity,


$$
H(X)=H(Y)+H(X\mid Y),
$$


verified to machine precision ($<10^{-12}$) in the Phase 1 ledger (Appendix A.1). Rounding for exposition: **output $\approx 0.811$ bits**, **export $\approx 1.189$ bits**, total $2$.

Branch-wise, the export is concentrated on the ambiguous output:

| $Y$ | $P(Y)$ | Preimage size | $H(X\mid Y=y)$ |
|-------|----------|---------------|------------------|
| $1$ | $1/4$  | $1$         | $0$            |
| $0$ | $3/4$  | $3$         | $\log_2 3\approx 1.585$ |


$$
H(X\mid Y)=\tfrac34\log_2 3\approx 1.188722.
$$


**Program reading.** Local observers of $Y$ see an apparent reduction; globally, system + environment entropy is accounted by the chain rule. In the gravity narrative, $\Phi_g$ plays the analogous role of overwriting prior micro-details while exporting distinguishability; continuum load $L$ quantifies demand of that process (preview in later parts; definition in Eq.\ (\ref{eq:load}) family below). That narrative does **not** by itself prove Einstein equations or continuum GfE.

**Rigor:** finite classical chain-rule accounting is **constructive**; holographic / gravitational language for the environment register remains **semantic** until an explicit continuum map is built (explicitly not claimed here).

## 1.5 Three-stage mental model

The program is organized so that stages are not collapsed into symbolic identity of actions and master equations (see the staged workflow in Section 1.5):

```text
STAGE 1 --- Computational induction (this program report's discrete core)
  ρ, Φ_g, S_c / H_c, L, 

$$
d\tau=dt/(1+\alpha L)
$$


  IDEM / decay / games = discrete microstructure (M11 design + Phase 1--2 ledgers)
        |
        v
STAGE 2 --- Geometric imprint (bridge)
  Structure-induced metric G  (or computational cousin)
  TYPE SAFETY: L is a dimensionless scalar; G is a metric --- L ≠ G
        |
        v
STAGE 3 --- Continuum GfE (macro target)
  Relative entropy of metrics → modified Einstein, Λ_G, G-field
```

**Discipline.** Stage-1 constructive bookkeeping (AND ledgers, composition laws, Landauer contact) **motivates** Stage-2/3 language structurally; it does **not** construct continuum $L$ or $G$. Euclidean dual results (ACD-EW, residual T1′) live on a warm-up lattice and are **not** continuum gravitational equivalence. Continuum GfE contact is treated later as shared weak-field Poisson (**WEAK PASS**) without framework identity (**FAIL**).

## 1.6 Notation and type-safety table

| Symbol | Meaning | Type / hygiene |
|--------|---------|----------------|
| $H_c(f;p_X)$ | Classical computational entropy of map output | Scalar (bits); Tag **A** (foundations); Tag **E** on M11 finite maps |
| $S_c(\Phi;\rho)$ | Quantum/gravity computational entropy | Von Neumann of channel output; Tag **B** |
| $H_c^{\mathrm{toy}}$ | Dual-toy residual + edge score | Tag **C** --- **not** map $H(Y)$ |
| $H_c^{\mathrm{game}}$ | Predictive game Shannon given filtration | Tag **D** --- **not** belief-field dual residual |
| $H_c^{\mathrm{disc}}$ | Finite map / IDEM ledger $H(Y)$ | Tag **E** (M11) |
| $\Phi_g$ | Gravitational CPTP channel | Map on density operators |
| $L$ / $L(\rho,g)$ | Continuum **computational load** (demand) | **Dimensionless scalar**; clocks $d\tau$ |
| $L^{\mathrm{disc}}$ | Discrete three-slot load ledger | Scalar bookkeeping; $L^{\mathrm{disc}}\neq L(\rho,g)$ |
| $G$ | Structure-/matter-induced **metric** (GfE / ACD-EW) | Metric (or edgewise cousin); **$L\neq G$** |
| $G_{\mathrm{Newton}}$ | Newton's constant | Distinct from metric $G$; appear only in Path M calibration language |
| IDEM | Expanded identity + metadata | Result + arity, decay vector, $d_f$, AST metrics |
| $\mathbf{d}$ | Decay / recoverability flags | $\{0,1\}^n$ or soft $[0,1]^n$ |
| $d_f$ | Function unidentifiability | $[0,1]$ |
| GfE | Gravity from Entropy (Bianconi) | Continuum macro target; peer literature, not GR-peer foundation |
| ACD-EW | Action--Channel Duality (Euclidean warm-up) | Constructive dual on warm-up layer only |

**Locked type-safety rules.**

1. **$L$ is a dimensionless scalar.** **$G$ is a metric.** Never write $L\equiv G$.  
2. **$H_c$ / $S_c$ are entropies of declared outputs**, not internal AST size alone (AST size may enter **energy-like** load proxies).  
3. **$L^{\mathrm{disc}}\neq L(\rho,g)$** and discrete bookkeeping weights $\beta',\gamma',\delta'$ are not Newton-calibrated $\alpha\beta=4\pi G/c^4$.  
4. Dual-toy lattice field $\phi$ is a **test signal**, not spacetime geometry and not the M11 microstate of continuum $\rho$.

## 1.7 Entropy object tags (M10, brief)

Earlier drafts historically overloaded the token "$H_c$." M10 freezes five tags so that load rates $|\Delta H_c|$ cannot be mixed across layers (Section 1.7):

| Tag | Symbol | Object |
|-----|--------|--------|
| **A** | $H_c(f;p_X)$ | Classical **map** output Shannon / differential entropy (foundations) |
| **B** | $S_c(\Phi;\rho)$ | Von Neumann entropy of **channel** output $\Phi(\rho)$ |
| **C** | $H_c^{\mathrm{toy}}$ | Dual-toy residual + edge entropy (ACD-EW scorecards); supervised residual quality, not unsupervised $H(Y)$ alone |
| **D** | $H_c^{\mathrm{game}}$ | Predictive game Shannon $H(Y_k\mid\mathcal{F}_{k-1})$ |
| **E** | $H_c^{\mathrm{disc}}$ | Finite map / IDEM / M11 ledger $H(Y)$ |

**Non-identities (do not assert):** $H_c^{\mathrm{toy}}\not\equiv S_c$; $H_c^{\mathrm{disc}}\not\equiv S_c$; $H_c^{\mathrm{game}}\not\equiv H_c^{\mathrm{toy}}$; $H_c\not\equiv S_{\mathrm{GfE}}$. House style: bare $H_c$ only for Tag **A** when unambiguous; theory claims mixing layers must tag.

**Semantic preview of demand (C14).** Prefer reading continuum load $L$ as demand from the **scale and rate of channel outcomes** --- energy-like work, entropy flux / export, and boundary or distinguishability budget --- so that active scrambling and high export raise $L$. That reading is a **semantic** program convention until continuum matching exists; it is the same polarity that discrete ledgers enforce by construction in §2.

---
