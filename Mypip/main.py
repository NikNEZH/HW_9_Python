import matplotlib.pyplot as plt
import numpy as np


my_list = [1,3,5,7,29]
plt.plot(my_list)

plt.show()
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# plt.rcdefaults()
# fig, ax = plt.subplots()
#
# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))
#
# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')
#
# plt.show()
















# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
#
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
#
# print(emoji.demojize('Python is 👍'))
#
# print(emoji.emojize("Python is fun :red_heart:"))
#
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
#
# print(emoji.is_emoji("👍"))
# True

# from progress.bar import Bar
# import time
# with Bar('Processing', max=20) as bar:
#     for i in range(20):
#         time.sleep(1)
#         bar.next()

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()

# from isOdd import isOdd
#
# print(isOdd(1))
# print(isOdd(4))