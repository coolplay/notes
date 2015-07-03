Application of Jack polynomials in FQHE
=======================================

The purpose of the note is to introduce Jack polynomials and develop applicable
technique to implement its usage in fractional quantum Hall effect, which
entirely removes the need to perform exact diagnolization.

**Outline**:

* Configuration representation

  For N = 3, root configuration for 1/2 FQHE can be equivalently represented as:

  * partition (monomial (Slater) basis for bosons (fermions))
    
    (4, 2), which is abbreviation of (4, 2, 0)
  * occupation (generalization of Fock space for particles with fractional
    statstics)
    
    [1, 0, 1, 0, 1]
* Squeezing rule

  .. image:: /images/Jacks_worksheet.png
     :align: center
     :width: 80%

* Recursion formula

  * boson

    We expand the Jacks into the monomial basis:

    .. math::

        J_{\lambda}^{\alpha} = \sum_{\kappa \le \lambda} c_{\lambda
        \kappa}(\alpha) \mathcal{M}_\kappa,

    where `\kappa` runs over all monomial partitions squeezed from the root
    partition `\lambda`.

    There is a known recurrence relation for the expansion coefficients
    `c_{\lambda \kappa}(\alpha)`:

    .. math::

        c_{\lambda \kappa}(\alpha) =
        \frac{2/\alpha}{\rho_{\lambda}(\alpha)-\rho_{\kappa}(\alpha)}
        \sum_{\kappa<\mu\le \lambda}\hspace{-5pt} \left( (l_i+t)-(l_j-t) \right)
        c_{\mu \kappa}(\alpha), \label{recbos}

    where `\rho_{\lambda}(\alpha)=\sum_i \lambda_i \left(\lambda_i -1 -
    \frac{2}{\alpha}(i-1)\right)`.

  * fermion

    We expand the polynomials into the Slaters:

    .. math::

        S_{\lambda}^{\alpha}(z_1,\dots,z_N)=J_{\lambda_{\text{B}}}^\alpha
        \prod_{i<j}^N (z_i-z_j)=\sum_{\mu \le \lambda} b_{\lambda \mu}
        \text{sl}_\mu. \label{salpha}

    There is a known recurrence relation for the expansion coefficients:

    .. math::

        b_{\lambda \mu} = \frac{2(\frac{1}{\alpha}-1)}{\rho^{\text{F}}_\lambda
        (\alpha) - \rho^{\text{F}}_\mu (\lambda)} \sum_{\theta; \; \mu < \theta
        \le \lambda} (\mu_i-\mu_j) b_{\lambda \theta} (-1)^{N_{\text{SW}}},

    where `\rho^{\text{F}}_\lambda (\alpha) = \sum_i \lambda_i (\lambda_i +2i
    (1-1/\alpha))`.

* Product rule

  It relates a subset entity of expansion coefficients of a given FQH
  `N=N_A+N_B`-particle state to the product of certain coefficients of the
  `N_A`- and `N_B`-particle state.
