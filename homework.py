from dataclasses import dataclass, asdict
from typing import Type, List, Dict


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    MESSAGE = ('Тип тренировки: {training_type}; '
               'Длительность: {duration:.3f} ч.; '
               'Дистанция: {distance:.3f} км; '
               'Ср. скорость: {speed:.3f} км/ч; '
               'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        """Возврат сообщения о тренировке."""
        return self.MESSAGE.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65
    M_IN_KM = 1000
    MIN_IN_HOUR = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            training_type=self.__class__.__name__,
            duration=self.duration,
            distance=self.get_distance(),
            speed=self.get_mean_speed(),
            calories=self.get_spent_calories()
        )


class Running(Training):
    """Тренировка: бег."""

    MET_COEFF_RUN_1 = 18
    MET_COEFF_RUN_2 = 20

    def get_spent_calories(self) -> float:
        pace = (self.MET_COEFF_RUN_1 * self.get_mean_speed()
                - self.MET_COEFF_RUN_2) * self.weight
        pace_in_km = pace / self.M_IN_KM
        pace_in_min = self.duration * self.MIN_IN_HOUR
        calories = pace_in_km * pace_in_min
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    MET_COEFF_WLK_1 = 0.035
    MET_COEFF_WLK_2 = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: int,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        pace = (self.MET_COEFF_WLK_1 * self.weight
                + (self.get_mean_speed() ** 2 // self.height)
                * self.MET_COEFF_WLK_2 * self.weight)
        pace_in_min = self.duration * self.MIN_IN_HOUR
        calories = pace * pace_in_min
        return calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38
    MET_COEFF_SWM_1 = 1.1
    MET_COEFF_SWM_2 = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость плавания."""
        distance_meters = self.length_pool * self.count_pool
        distance_km = distance_meters / self.M_IN_KM
        speed = distance_km / self.duration
        return speed

    def get_spent_calories(self) -> float:
        calories = ((self.get_mean_speed() + self.MET_COEFF_SWM_1)
                    * self.MET_COEFF_SWM_2 * self.weight)
        return calories


def read_package(workout_type: str, data: List[int]) -> Training:
    """Прочитать данные полученные от датчиков."""
    TraningTypes = Dict[str, Type[Training]]
    activities: TraningTypes = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type not in activities:
        raise ValueError(
            f'{workout_type} is not a supported workout type '
            f'(try one of these: {", ".join(activities.keys())})'
        )
    name: Training = activities[workout_type](*data)
    return name


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
