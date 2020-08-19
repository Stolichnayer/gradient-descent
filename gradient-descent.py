# Αριθμός Επαναλήψεων βρόγχου
max_iteration = 20

# Μέγεθος βήματος
a = 0.001

#---------------------- Είσοδος --------------------------
# Αρχικοποίηση του x0
x0 = -0.5

# Δημιουργία έκφρασης παραγώγου της L
def dL(x):
    return 2*x + 0.5 # f1'(x)

# -------- Εφαρμογή αλγορίθμου gradient descent ----------
def gradientDescent():
    xt = x0
    xt_previous = x0

    for i in range(max_iteration):
        xt = xt_previous - a * dL(xt_previous)
        xt_previous = xt
    
    return xt

#---------------------- Έξοδος ---------------------------
x = gradientDescent()
print(x)



