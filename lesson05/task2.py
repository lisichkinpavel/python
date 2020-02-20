# Мороз и солнце; день чудесный!
# Еще ты дремлешь, друг прелестный —
# Пора, красавица, проснись:
# Открой сомкнуты негой взоры
# Навстречу северной Авроры,
# Звездою севера явись!

with open('task2_text.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(f'Всего {len(content)} строк')
    for idx, line in enumerate(content, 1):
        words = [i for i in line.split(' ')]
        print(f'В {idx} строке {len(words)} слов(а)')
