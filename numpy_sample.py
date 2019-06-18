import numpy as np
import seaborn as sns

# Generate some normally distributed data
dat = np.random.normal(0.0, 0.2, 1000)

# Create a histogram using seaborn
sns.distplot(dat)