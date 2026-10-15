# R-P3-UTILITY-B — independent adversarial review

I read A's completed `research/utility-invariance.md` following the new user
steering. This was same-model internal inference/counterexample review, not
independent literature verification. **Verdict: the stated results pass.**

- U2: extrema transport under positive affinity, so min-max normalization
  identifies the cardinal group exactly. Constants cannot be confused with
  nonconstant normalized tables because profile maps are onto. Distinct-level
  ranks similarly identify the ordinal group. Range-signature criteria and
  the stated necessary/sufficient orbit equality conditions follow because an
  order bijection must take kth source level to kth target level.
- U3: a focal-fixed ordinal map induces an increasing permutation of one
  finite payoff range, hence fixes every value. Thus every ordinal player-kernel
  element is exact, yielding the claimed common kernel. The note correctly
  avoids identifying whole stabilizer groups: their nonfocal behavior differs.
- U4: full ranges exclude hidden strategy-relabeling escapes in both examples.
  The exact/cardinal and cardinal/ordinal transitivity separations are valid.
- U5: the stated matrices satisfy `u_1(swap s)=u_0(s)^2`. Indifference equations
  are `3-3q=1+q` and `9-9p=1+3p`, giving `(p,q)=(2/3,1/2)`;
  its swapped profile fails indifference. The two displayed pure equilibria
  are valid and exchanged, confirming the pure/mixed distinction.
- U6: positive weighted exactness follows by multiplying normalized unilateral
  differences by each player's positive range width; constant players cause
  no exception. Rank differences have exactly the signs of original utility
  differences, including zero, so the ordinal-potential conclusion is valid.
  Face mixed differences 2 versus 4 exclude an exact potential in U4.1;
  0 versus 2 exclude every positive weighted exact potential in U4.2.

The general U6 claims remain conditional on the separately reviewed exact
binary theorem and its precise n=1/n=2 qualifications. No independent-mixed
lottery domain is silently treated as the full correlated lottery simplex.
No numerical interpersonal welfare conclusion follows from normalization.
I found no correction needed and communicated these checks to A/coordinator.

## Targeted review of the added independent-product necessity proof

After the preceding review, A supplied the complete hybrid-segment proof that
all-pairs independent-mixed-profile preference equivalence already implies a
positive affine relation. I checked it adversarially; it passes.

Use free marginal coordinates in the relative affine hull, omitting singleton
blocks. Each hybrid polynomial `U(h_S(x,y))-t` is nonzero: on the diagonal it
restricts to the nonconstant polynomial `U(z)-t`. Their finite product is
nonzero, so its zero set cannot fill the nonempty open region
`U(x)<t<U(y)` within relative-interior pairs. A generic pair therefore avoids
all equal-to-t hybrid vertices. Replacing one marginal block at a time gives
an edge crossing t. Both expected utilities are affine on that feasible edge,
so the shared weak ordering forces the scalar function f to be affine on an
interval around t, with positive slope. Local affine patches on the connected
open utility interval force a single affine function. Full-support profiles
place positive mass on every pure profile, so for nonconstant u their U-values
lie strictly between the extrema; approaching extremal pure profiles extends
the identity continuously to both endpoints. Constant utilities and
zero-dimensional singleton blocks are handled separately as stated.

This proves the assertion without treating the product-law image as convex.
It uses the complete weak order on all pairs of whole product profiles,
including ties. It does not apply to mere unilateral best-response invariance.
The literature label remains foundational reconstruction, not novelty.
