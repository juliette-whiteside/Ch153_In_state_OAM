import sympy as sp

print("=" * 80)
print("DIAGONALIZING THE ANGULAR MOMENTUM OPERATOR Lz IN THE (dxz, dyz) SUBSPACE")
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

# Step 3: Define only d_xz and d_yz in terms of Y2^m
d_xz = -(1 / sqrt2) * (Y2_basis[1] - Y2_basis[-1])  # d_xz ∝ (Y_{-1} - Y_1)
d_yz = (i / sqrt2) * (Y2_basis[-1] + Y2_basis[1])   # d_yz ∝ i(Y_{-1} + Y_1)

print("STEP 3: Define the real orbitals d_xz and d_yz")
print(f"d_xz = {d_xz}")
print(f"d_yz = {d_yz}")
print("=" * 80)

# Step 4: Stack these into a projection matrix (5x2)
P_sub = sp.Matrix.hstack(d_xz, d_yz)

print("STEP 4: Stack into projection matrix (5x2)")
print("P_sub = [ d_xz | d_yz ]")
print(f"P_sub = \n{P_sub}")
print("=" * 80)

# Step 5: Define Lz in the Y2^m basis
Lz_Y2 = sp.Matrix.diag([ħ * m for m in [-2, -1, 0, 1, 2]])

print("STEP 5: Define the Lz operator in the original Y_2^m basis")
print(f"Lz_Y2 = \n{Lz_Y2}")
print("=" * 80)

# Step 6: Project Lz into the (dxz, dyz) subspace
Lz_sub = (P_sub.H * Lz_Y2 * P_sub).applyfunc(sp.simplify)

print("STEP 6: Project Lz into the (dxz, dyz) subspace")
print(f"Lz_sub = \n{Lz_sub}")
print("=" * 80)

# Step 7: Substitute ħ = 1 and diagonalize
Lz_sub_numeric = Lz_sub.subs(ħ, 1).evalf()
eigvecs, eigvals = Lz_sub_numeric.diagonalize()

print("STEP 7: Substitute ħ = 1 and diagonalize")
print(f"Lz_sub (ħ = 1) = \n{Lz_sub_numeric}")
print("\nEigenvalues of Lz in the (dxz, dyz) basis:")
print(eigvals)
print("\nEigenvectors (columns) corresponding to eigenfunctions:")
print(eigvecs)
print("=" * 80)

# Project eigenfunctions back into the Y2^m basis
print("\nProjecting eigenvectors into the Y2^m basis")
eigenfunctions_Y2_basis = P_sub * eigvecs
eigenfunctions_Y2_basis = eigenfunctions_Y2_basis.applyfunc(sp.simplify)

for j in range(2):
    print(f"\nEigenfunction {j+1} (Lz eigenvalue = {eigvals[j, j]}):")
    eigenfunction_j = eigenfunctions_Y2_basis[:, j]
    eigenfunction_j = eigenfunction_j / sp.sqrt(eigenfunction_j.norm()**2)
    for m, idx in zip([2, 1, 0, -1, -2], range(5)):
        component = eigenfunction_j[idx, 0]
        print(f"  Y2^{m}: {component}")