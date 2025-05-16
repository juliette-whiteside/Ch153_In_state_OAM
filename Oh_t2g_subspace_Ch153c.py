
####
import sympy as sp

print("=" * 80)
print("DIAGONALIZING THE ANGULAR MOMENTUM OPERATOR Lz IN THE t2g BASIS")
print("=" * 80)

# Step 1: Define constants and symbolic variables
i = sp.I
sqrt2 = sp.sqrt(2)
ħ = sp.Symbol('ħ', real=True)

print("STEP 1: Define constants and symbolic variables")
print(f"i = {i}")
print(f"sqrt2 = {sqrt2}")
print(f"ħ = {ħ}")
print("=" * 80)

# Step 2: Define the Y_2^m basis as 5D column vectors
# Basis ordering: [Y2^2, Y2^1, Y2^0, Y2^{-1}, Y2^{-2}]
Y2_basis = {
    2: sp.Matrix([[1], [0], [0], [0], [0]]),
    1: sp.Matrix([[0], [1], [0], [0], [0]]),
    0: sp.Matrix([[0], [0], [1], [0], [0]]),
   -1: sp.Matrix([[0], [0], [0], [1], [0]]),
   -2: sp.Matrix([[0], [0], [0], [0], [1]])
}

print("STEP 2: Define the Y_2^m basis as 5D column vectors")
for m, vec in Y2_basis.items():
    print(f"Y2^{m} = {vec}")
print("=" * 80)

# Step 3: Define the real t2g orbital combinations in terms of Y2^m
d_xy = -(i / sqrt2) * (Y2_basis[2] - Y2_basis[-2])  # d_xy ∝ i(Y_{-2} - Y_2)
d_xz = -(1 / sqrt2) * (Y2_basis[1] - Y2_basis[-1])  # d_xz ∝ (Y_{-1} - Y_1)
d_yz = (i / sqrt2) * (Y2_basis[-1] + Y2_basis[1])  # d_yz ∝ i(Y_{-1} + Y_1)

print("STEP 3: Define the real t2g orbital combinations in terms of Y2^m")
print(f"d_xy = {d_xy}")
print(f"d_xz = {d_xz}")
print(f"d_yz = {d_yz}")
print("=" * 80)

# Step 4: Stack these into a projection matrix (5x3)
P_t2g = sp.Matrix.hstack(d_xz, d_yz, d_xy)

print("STEP 4: Stack these into a projection matrix (5x3)")
print("P_t2g = [ d_xz | d_yz | d_xy]")
print(f"P_t2g = \n{P_t2g}")
print("=" * 80)

# Step 5: Define the Lz operator in the original Y_2^m basis
Lz_Y2 = sp.Matrix.diag([ħ * m for m in [-2, -1, 0, 1, 2]])

print("STEP 5: Define the Lz operator in the original Y_2^m basis")
print("Lz_Y2 = diag(2ħ, ħ, 0, -ħ, -2ħ)")
print(f"Lz_Y2 = \n{Lz_Y2}")
print("=" * 80)

# Step 6: Project Lz into the real t2g basis
Lz_t2g = (P_t2g.H * Lz_Y2 * P_t2g).applyfunc(sp.simplify)

print("STEP 6: Project Lz into the real t2g basis")
print("Lz_t2g = P_t2g^T * Lz_Y2 * P_t2g")
print(f"Lz_t2g = \n{Lz_t2g}")
print("=" * 80)

# Step 7: Substitute ħ = 1 and diagonalize
Lz_t2g_numeric = Lz_t2g.subs(ħ, 1).evalf()
eigvecs, eigvals = Lz_t2g_numeric.diagonalize()

print("STEP 7: Substitute ħ = 1 and diagonalize")
print(f"Lz_t2g (ħ = 1) = \n{Lz_t2g_numeric}")
print("\nEigenvalues of Lz in the t2g basis:")
print(eigvals)
print("\nEigenvectors (columns) corresponding to eigenfunctions:")
print(eigvecs)
print("=" * 80)

print("\n" + "="*80)
print("PART 2: ANALYZING THE EIGENFUNCTIONS IN THE Y2^m BASIS")
print("="*80)
print("Eigenvectors in t2g basis:")
print(eigvecs)

print("\nStep 2: Projecting eigenvectors into the Y2^m basis")
# Project each eigenvector into the Y2^m basis
eigenfunctions_Y2_basis = P_t2g * eigvecs
eigenfunctions_Y2_basis = eigenfunctions_Y2_basis.applyfunc(sp.simplify)

print("\nEigenfunctions in Y2^m basis:")
print(eigenfunctions_Y2_basis)

print("\nStep 3: Analyzing each eigenfunction separately")
for j in range(3):
    print(f"\nEigenfunction {j+1} (corresponding to eigenvalue {eigvals[j, j]}):")
    eigenfunction_j = eigenfunctions_Y2_basis[:, j]
    eigenfunction_j = eigenfunction_j / sp.sqrt(eigenfunction_j.norm()**2)
    print(eigenfunction_j)
    
    print(f"Components in Y2^m basis:")
    for m, idx in zip([2, 1, 0, -1, -2], range(5)):
        component = eigenfunction_j[idx, 0]
        if component != 0:
            print(f"  Y2^{m}: {component}")
        else:
            print(f"  Y2^{m}: 0")

print("\n" + "="*80)
print("SUMMARY OF RESULTS")
print("="*80)

print("The t2g Basis:")
print("-" * 40)
print("The t2g basis consists of three d-orbitals:")
print("1. d_xy = (i/√2) * (Y2^(-2) - Y2^(2))")
print("2. d_xz = (1/√2) * (Y2^(-1) - Y2^(1))")
print("3. d_yz = (i/√2) * (Y2^(-1) + Y2^(1))")
print("\nThese form a 3-dimensional subspace of the 5-dimensional l=2 space.")
print("-" * 40)

print("\nDiagonalization Results:")
print("-" * 40)
print("1. The Lz operator in the t2g basis is:")
print(Lz_t2g_numeric)
print("\n2. The eigenvalues of Lz in the t2g basis are:")
print(eigvals)
print("\n3. The eigenvectors in the t2g basis are:")
print(eigvecs)
print("\n4. The eigenvectors in the spherical harmonic (Y2^m) basis are:")

for j in range(3):
    print(f"\nEigenfunction {j+1} (Lz eigenvalue = {eigvals[j, j]}):")
    eigenfunction_j = eigenfunctions_Y2_basis[:, j]
    
    terms = []
    for m, idx in zip([2, 1, 0, -1, -2], range(5)):
        c = eigenfunction_j[idx, 0]
        if c != 0:
            terms.append(f"{sp.pretty(c)} * Y_2^{m}")
    expression = " + ".join(terms) if terms else "0"
    print(f"ψ_{j+1} = {expression}")

print("-" * 40)

