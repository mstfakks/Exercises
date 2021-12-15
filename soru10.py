import matplotlib.pyplot as plt
from matplotlib import style
plt.figure(figsize=(10,8))
boy = [150,154,157,163,174,182,185,189,191,194]
kilo = [65,73,70,89,80,95,99,110,78,89]
plt.title('BOY-KİLO GRAFİĞİ')
plt.xlabel('Boy(cm)')
plt.ylabel('Kilo(kg)')
style.use('ggplot')
plt.grid(True,color='black')
plt.scatter(boy,kilo,color='green')
plt.plot(boy,kilo,linewidth=2)
plt.show()
