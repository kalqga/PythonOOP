import unittest

from testing.exercises.hero.project.hero import Hero


class HeroTests(unittest.TestCase):
    username = "mial"
    level = 60
    health = 100
    damage = 50

    def tests_username(self):
        hero_test = Hero(self.username, self.level, self.health, self.damage)
        result = hero_test.username
        expected = "mial"
        self.assertEqual(expected, result)

    def tests_level(self):
        hero_test = Hero(self.username, self.level, self.health, self.damage)
        result = hero_test.level
        expected = 60
        self.assertEqual(expected, result)

    def tests_health(self):
        hero_test = Hero(self.username, self.level, self.health, self.damage)
        result = hero_test.health
        expected = 100
        self.assertEqual(expected, result)

    def tests_damage(self):
        hero_test = Hero(self.username, self.level, self.health, self.damage)
        result = hero_test.damage
        expected = 50
        self.assertEqual(expected, result)

    def tests_hero_username_same_as_enemy_username__should_raise_exception(self):
        hero_test = Hero(self.username, self.level, self.health, self.damage)
        enemy_test = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as result:
            hero_test.battle(enemy_test)
        self.assertEqual(result.exception.args[0], "You cannot fight yourself")

    def tests_hero_health__when_equal_to_zero__should_raise_value_error(self):
        hero_test = Hero("hero", 10, 0, 5)
        enemy_test = Hero("enemy", 10, 150, 10)
        with self.assertRaises(ValueError) as result:
            hero_test.battle(enemy_test)
        self.assertEqual(result.exception.args[0], "Your health is lower than or equal to 0. You need to rest")

    def tests_hero_health__when_less_than_zero__should_raise_value_error(self):
        hero_test = Hero("hero", 10, -5, 5)
        enemy_test = Hero("enemy", 10, 150, 10)
        with self.assertRaises(ValueError) as result:
            hero_test.battle(enemy_test)
        self.assertEqual(result.exception.args[0], "Your health is lower than or equal to 0. You need to rest")

    def tests_enemy_health__when_equal_to_zero__should_raise_value_error(self):
        hero_test = Hero("hero", 10, 10, 5)
        enemy_test = Hero("enemy", 10, 0, 10)
        with self.assertRaises(ValueError) as result:
            hero_test.battle(enemy_test)
        self.assertEqual(result.exception.args[0], "You cannot fight enemy. He needs to rest")

    def tests_enemy_health__when_less_than_zero__should_raise_value_error(self):
        hero_test = Hero("hero", 10, 10, 5)
        enemy_test = Hero("enemy", 10, -5, 10)
        with self.assertRaises(ValueError) as result:
            hero_test.battle(enemy_test)
        self.assertEqual(result.exception.args[0], "You cannot fight enemy. He needs to rest")

    def tests_hero_damage_if_works_correctly(self):
        hero_test = Hero("hero", 10, 100, 5)
        enemy_test = Hero("enemy", 5, 100, 11)
        hero_test.battle(enemy_test)
        result = enemy_test.health
        expected = 50
        self.assertEqual(expected + 5, result)

    def tests_enemy_damage_if_works_correctly(self):
        hero_test = Hero("hero", 10, 100, 5)
        enemy_test = Hero("enemy", 5, 100, 11)
        hero_test.battle(enemy_test)
        result = hero_test.health
        expected = 45
        self.assertEqual(expected, result)

    def tests_hero_and_enemy_health__when_zero__should_return_draw(self):
        hero_test = Hero("hero", 10, 100, 10)
        enemy_test = Hero("enemy", 10, 100, 10)
        result = hero_test.battle(enemy_test)
        expected = "Draw"
        self.assertEqual(expected, result)

    def tests_hero_and_enemy_health__when_lower_than_zero__should_return_draw(self):
        hero_test = Hero("hero", 11, 100, 10)
        enemy_test = Hero("enemy", 10, 100, 11)
        result = hero_test.battle(enemy_test)
        expected = "Draw"
        self.assertEqual(expected, result)

    def tests_enemy_health__when_hero_health_positive_and_enemy_health_equals_zero__should_increase_stats_and_return(
            self):
        hero_test = Hero("hero", 10, 1000, 10)
        enemy_test = Hero("enemy", 5, 100, 11)
        result = hero_test.battle(enemy_test)
        expected = "You win"
        self.assertEqual(expected, result)
        self.assertEqual(11, hero_test.level)
        self.assertEqual(950, hero_test.health)
        self.assertEqual(15, hero_test.damage)

    def tests_enemy_health__when_hero_health_positive_and_enemy_health_lower_than_zero__should_increase_stats_and_return(
            self):
        hero_test = Hero("hero", 10, 1000, 11)
        enemy_test = Hero("enemy", 5, 100, 11)
        result = hero_test.battle(enemy_test)
        expected = "You win"
        self.assertEqual(expected, result)
        self.assertEqual(11, hero_test.level)
        self.assertEqual(950, hero_test.health)
        self.assertEqual(16, hero_test.damage)

    def tests_hero_health__when_enemy_health_positive_and_hero_health_equals_zero__should_increase_stats_and_return(
            self):
        hero_test = Hero("hero", 5, 100, 11)
        enemy_test = Hero("enemy", 10, 1000, 10)
        result = hero_test.battle(enemy_test)
        expected = "You lose"
        self.assertEqual(expected, result)
        self.assertEqual(11, enemy_test.level)
        self.assertEqual(950, enemy_test.health)
        self.assertEqual(15, enemy_test.damage)

    def tests_hero_health__when_enemy_health_positive_and_hero_health_lower_than_zero__should_increase_stats_and_return(
            self):
        hero_test = Hero("hero", 5, 100, 11)
        enemy_test = Hero("enemy", 10, 1000, 11)
        result = hero_test.battle(enemy_test)
        expected = "You lose"
        self.assertEqual(expected, result)
        self.assertEqual(11, enemy_test.level)
        self.assertEqual(950, enemy_test.health)
        self.assertEqual(16, enemy_test.damage)

    def tests_str_method__should_return_correctly(self):
        hero_test = Hero("hero", 5, 100, 11)
        result = hero_test.__str__()
        expected = "Hero hero: 5 lvl\n" \
                   "Health: 100\n" \
                   "Damage: 11\n"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
