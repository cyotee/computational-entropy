# Appendix A. Constructive witnesses (self-contained summaries)

This appendix replaces repository file pointers. Numerical values below are fixed by finite classical probability (or fixed dual-toy protocols) and can be regenerated from the associated open-source research repository if desired; the **paper does not depend on hyperlinks**.

## A.1 Irreversible AND ledger

Fair bits $X=(X_1,X_2)$, $Y=X_1\land X_2$:
$H(X)=2$, $H(Y)=h_2(1/4)\approx 0.811278$, $H(X\mid Y)\approx 1.188722$,
$L_E=1$, $L_S=H(X\mid Y)$, soft $L_B=0.5$, $L^{\mathrm{disc}}\approx 2.689$.
Chain rule residual $<10^{-12}$.

## A.2 Composition / path dependence

Same final AND law $H(Z)\approx 0.811278$ and same residual export $H(X\mid Z)\approx 1.188722$, but cumulative stage cost differs:
- Direct AND: $\sum L_S \approx 1.188722$, $\sum L_E=1$
- Circuit (publish wire then AND): $\sum L_S \approx 2.188722$, $\sum L_E=2$
Markov cascade $Y=\mathrm{AND}$, $Z=\mathrm{NOT}(Y)$: $H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)$ exactly.

## A.3 Landauer contact (Protocol R)

After AND, keep $Y$, reset residual input conditional on $Y$. Landauer (external) gives
$Q \ge k_B T\ln 2 \cdot H(X\mid Y)$. In units of $k_B T\ln 2$, $Q_{\min}/(k_B T\ln 2)=H(X\mid Y)=L_S$ for this single-shot assignment. Reversible dilation parks the same entropy as garbage until erased.

## A.4 Discrete PM energy descent (Layer W)

On the 1D noisy-step dual protocol, explicit-Euler Perona--Malik with matched edge energy $E_h$ is non-increasing along the trajectory; with matched coupling, $E_h=-(K^2/2)S_{\mathrm{matched}}$. This is Layer W (warm-up energy), not residual dual (Layer D).

## A.5 Smooth warm-up action (conditional)

Under $C^3$ periodic $\phi$, fixed $\alpha>0$, mesh $h\to 0$,
$S_h=h\sum_i -\ln(1+\alpha(D_h\phi)_i^2)$ approximates $\int -\ln(1+\alpha|\phi'|^2)\,dx$ at rate $O(h)$ (Taylor + Lipschitz + Riemann sum). Not $\Gamma$-convergence; not BV/jumps.

## A.6 Entropy-object non-identity (dual toys)

On dual times in $U_\star$, MC-mean residual dual score $H_c^{\mathrm{toy}}\sim 1.1$--$1.3$ while ensemble Shannon $H(Z)$ of coarsened edge location is $\approx 0$. Objects are not identical.

## A.7 Next-order promotion no-go (summary)

GfE next-order extras ($D_{\mu\nu}$, $\Lambda_G$) live in metric EOM; load $\gamma_L,\delta_L$ live in the clock 

$$
d\tau=dt/(1+\alpha L)
$$

. Identifying them requires an extra promotion rule not supplied by the present master equation (structural no-go, not a PPN calculation).

## A.8 Euclidean dual toys (pattern witnesses)

1D/2D joint toys and a game-motivated belief dual report 6/6 SUPPORT scorecards for a Euclidean dual **pattern** (PM vs heat, load co-motion, etc.). These are **not** continuum gravity detections. Residual dual of PM vs heat is time-windowed on $U_\star=[1.36,2.40]$ under soft ensemble hypotheses (PCRH$_b$, $\rho_b=0.42$).

---
