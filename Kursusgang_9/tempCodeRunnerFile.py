# Plot 2 - residualer vs forudsagt
plt.subplot(2,2,2)
plt.scatter(sys_predict, residuals)
plt.axhline(y=0, color="red", linestyle="--", alpha=0.6)



# plot 3 - Histogram af residualer
plt.subplot(2,2,3)
plt.hist(residuals)
plt.axvline(x=0, linestyle="--", color="red", alpha=0.6)
