<p align="center">
  <img src=".github/assets/banner.svg" width="100%" alt="Fitness Tracker" />
</p>

# Fitness Tracker

Сводка тренировки из данных датчиков: дистанция, скорость и расход калорий.

**Учебный проект** · Python · ООП · dataclasses · pytest  
[Русский](#about) · [English](#english) · [Профиль](https://github.com/artemleonich)

<a id="about"></a>

## О проекте

Модуль `homework.py` преобразует пакет данных о тренировке в объект, рассчитывает показатели и выводит текстовую сводку. Учебное упражнение по наследованию, переопределению методов, аннотациям типов и dataclasses.

Поддерживаются три вида активности: бег (`RUN`), спортивная ходьба (`WLK`) и плавание (`SWM`).

## Запуск

Для модуля нужен Python 3.7 или новее: в коде используется стандартный модуль `dataclasses`.

```bash
git clone https://github.com/artemleonich/hw_python_oop.git
cd hw_python_oop
python3 homework.py
```

Скрипт выведет сводки для трёх демонстрационных тренировок, заданных в конце файла. Для тестов:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest
```

В Windows PowerShell: `.venv\Scripts\Activate.ps1`. Версии инструментов тестирования закреплены в [requirements.txt](requirements.txt).

## Как устроен модуль

| Компонент | Задача |
| --- | --- |
| `Training` | Общие параметры и расчёт дистанции и скорости |
| `Running` | Расчёт для бега |
| `SportsWalking` | Расчёт для ходьбы с учётом роста |
| `Swimming` | Расчёт для плавания с учётом длины бассейна |
| `InfoMessage` | Форматирование сводки с точностью до трёх знаков |
| `read_package()` | Выбор класса по коду активности |
| `main()` | Вывод сообщения о тренировке |

Пример использования:

```python
from homework import main, read_package

training = read_package("RUN", [15000, 1, 75])
main(training)
```

## Формат входных данных

| Код | Параметры по порядку |
| --- | --- |
| `RUN` | число шагов, длительность в часах, вес в кг |
| `WLK` | число шагов, длительность в часах, вес в кг, рост в см |
| `SWM` | число гребков, длительность в часах, вес в кг, длина бассейна в м, число бассейнов |

Неизвестный код активности вызывает `ValueError`.

<details>
<summary>Формулы и интерфейс учебного задания</summary>

Общие параметры `Training`: `action`, `duration`, `weight`. Длина шага — 0.65 м; длина гребка у `Swimming` — 1.38 м.

- `get_distance()`: `action * LEN_STEP / 1000`, результат в км.
- `get_mean_speed()`: `distance / duration`, результат в км/ч.
- `get_spent_calories()`: реализация в классе активности.
- `show_training_info()`: возвращает `InfoMessage`.
- `InfoMessage.get_message()`: формирует строку о типе, длительности, дистанции, скорости и калориях.

Формулы сохранены в том виде, в котором они реализованы в учебном коде:

```python
# Running
(18 * speed - 20) * weight / 1000 * (duration * 60)

# SportsWalking
(0.035 * weight + (speed ** 2 // height) * 0.029 * weight) * (duration * 60)

# Swimming: speed
length_pool * count_pool / 1000 / duration

# Swimming: calories
(speed + 1.1) * 2 * weight
```

`InfoMessage` хранит `training_type`, `duration`, `distance`, `speed` и `calories`. Функция `read_package(workout_type, data)` создаёт объект активности; `main(training)` получает сводку и печатает её.

</details>

## Навигация

[homework.py](homework.py) — реализация и примеры · [tests/](tests/) — учебные проверки · [pytest.ini](pytest.ini) — конфигурация тестов.

<a id="english"></a>

<details>
<summary>English overview</summary>

A Python OOP exercise that converts sensor data into a workout summary. It supports running (`RUN`), sports walking (`WLK`) and swimming (`SWM`) through a shared `Training` base class. `InfoMessage` is a dataclass that formats duration, distance, speed and calories.

Run `python3 homework.py` for the three built-in examples. Install `requirements.txt` in a virtual environment and run `python -m pytest` for tests. The module requires Python 3.7 or newer for dataclasses; test dependencies retain their original pinned versions.

</details>

---

Автор: [Артём Леонов](https://github.com/artemleonich).

