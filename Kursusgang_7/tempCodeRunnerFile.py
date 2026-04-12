numerator = np.sum((RR-np.mean(RR)) * (R_amp- np.mean(R_amp)))
denominator = np.sum((RR-np.mean(RR))**2)
a = numerator/denominator

b_intersect = np.mean(R_amp) - a*np.mean(RR)

regressions_linje = a * RR  + b_intersect