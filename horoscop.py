import random


times = ['утром', 'днём', 'вечером', 'ночью', 'после обеда', 'перед сном']
advices = ['ожидайте', 'предостерегайтесь', 'будьте открыты для']
promises = ['гостей из забытого прошлого', 'встреч со старыми знакомыми', 'неожиданного праздника', 'приятных перемен']

generated_prophecies = []


def prediction_generator():
    time = random.choice(times).capitalize() + ' '
    advice = random.choice(advices) + ' '
    promise = random.choice(promises) + '.'
    return time + advice + promise

for i in range(0,5):
    generated_prophecies.append(prediction_generator())
    print(generated_prophecies[i])
