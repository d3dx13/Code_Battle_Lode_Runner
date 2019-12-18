from math import sqrt

from loderunnerclient.internals.element import Element, _ELEMENTS
from loderunnerclient.internals.point import Point


class Board:
    """ Class describes the Board field for Bomberman game."""
    def __init__(self, board_string):
        self._string = board_string.replace('\n', '')
        self._len = len(self._string)  # the length of the string
        self._size = int(sqrt(self._len))  # size of the board 
        #print("Board size is sqrt", self._len, self._size)

    def _find_all(self, element):
        """ Returns the set of points for the given element type."""
        _points = []
        _a_char = element
        for i, c in enumerate(self._string):
            if c == _a_char:
                 _points.append(self._strpos2pt(i))
        return _points

    def char_at(self, x, y):
        """ Return an char at coordinates x,y."""
        return self._string[self._xy2strpos(x, y)]

    def get_at(self, x, y):
        """ Return an _ELEMENTS object at coordinates x,y."""
        return Element(self.char_at(x, y))

    def has_element_at(self, x, y, element_object):
        """ Return True if _ELEMENTS is at x,y coordinates."""
        return element_object == self.get_at(x, y)

    def is_barrier_at(self, x, y):
        """ Return true if barrier is at x,y."""
        char = self.char_at(x, y)
        if (char == _ELEMENTS['BRICK']):
            return True
        if (char == _ELEMENTS['UNDESTROYABLE_WALL']):
            return True
        return False

    def get_my_position(self):
        """ Return the point where your hero is."""
        points = set()
        points.update(self._find_all(_ELEMENTS['HERO_DIE']))
        points.update(self._find_all(_ELEMENTS['HERO_DRILL_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_DRILL_RIGHT']))
        points.update(self._find_all(_ELEMENTS['HERO_FALL_RIGHT']))
        points.update(self._find_all(_ELEMENTS['HERO_FALL_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_LADDER']))
        points.update(self._find_all(_ELEMENTS['HERO_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_RIGHT']))
        points.update(self._find_all(_ELEMENTS['HERO_PIPE_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_PIPE_RIGHT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_DRILL_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_DRILL_RIGHT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_LADDER']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_RIGHT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_FALL_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_FALL_RIGHT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_PIPE_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_PIPE_RIGHT']))
        assert len(points) <= 1, "There should be only one hero"
        return list(points)[0]

    def is_game_over(self):
        """ Returns False if your hero still alive."""
        return _ELEMENTS['HERO_DIE'] in self._string

    def get_enemy_positions(self):
        """ Return the set of points for other heroes."""
        points = set()
        points.update(self._find_all(_ELEMENTS['ENEMY_LADDER']))
        points.update(self._find_all(_ELEMENTS['ENEMY_LEFT']))
        points.update(self._find_all(_ELEMENTS['ENEMY_PIPE_LEFT']))
        points.update(self._find_all(_ELEMENTS['ENEMY_PIPE_RIGHT']))
        points.update(self._find_all(_ELEMENTS['ENEMY_RIGHT']))
        points.update(self._find_all(_ELEMENTS['ENEMY_PIT']))
        return list(points)

    def get_other_hero_positions(self):
        """ Return the set of points for other heroes."""
        points = set()
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_LADDER']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_LEFT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_RIGHT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_PIPE_LEFT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_PIPE_RIGHT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_SHADOW_LEFT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_SHADOW_RIGHT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_SHADOW_LADDER']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_SHADOW_PIPE_LEFT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_SHADOW_PIPE_RIGHT']))
        return list(points)

    def get_shadow_pills(self):
        points = set()
        points.update(self._find_all(_ELEMENTS['THE_SHADOW_PILL']))
        return list(points)

    def get_portals(self):
        points = set()
        points.update(self._find_all(_ELEMENTS['PORTAL']))
        return list(points)

    def __get_shadows(self):
        points = set()
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_DRILL_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_DRILL_RIGHT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_LADDER']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_RIGHT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_FALL_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_FALL_RIGHT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_PIPE_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_SHADOW_PIPE_RIGHT']))

        points.update(self._find_all(_ELEMENTS['OTHER_HERO_SHADOW_LEFT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_SHADOW_RIGHT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_SHADOW_LADDER']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_SHADOW_PIPE_LEFT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_SHADOW_PIPE_RIGHT']))
        return list(points)

    def get_wall_positions(self):
        """ Returns the set of walls _ELEMENTS Points."""
        points = set()
        points.update(self._find_all(_ELEMENTS['BRICK']))
        points.update(self._find_all(_ELEMENTS['UNDESTROYABLE_WALL']))
        return list(points)

    def get_ladder_positions(self):
        """Returns the set of ladder Points"""
        points = set()
        points.update(self._find_all(_ELEMENTS['LADDER']))
        points.update(self._find_all(_ELEMENTS['HERO_LADDER']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_LADDER']))
        points.update(self._find_all(_ELEMENTS['ENEMY_LADDER']))
        return list(points)

    def get_gold_positions(self):
        points = set()
        points.update(self._find_all(_ELEMENTS['YELLOW_GOLD']))
        points.update(self._find_all(_ELEMENTS['GREEN_GOLD']))
        points.update(self._find_all(_ELEMENTS['RED_GOLD']))
        return list(points)

    def get_pipe_positions(self):
        """Returns the set of pipe Points"""
        points = set()
        points.update(self._find_all(_ELEMENTS['PIPE']))
        points.update(self._find_all(_ELEMENTS['HERO_PIPE_LEFT']))
        points.update(self._find_all(_ELEMENTS['HERO_PIPE_RIGHT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_PIPE_LEFT']))
        points.update(self._find_all(_ELEMENTS['OTHER_HERO_PIPE_RIGHT']))
        points.update(self._find_all(_ELEMENTS['ENEMY_PIPE_LEFT']))
        points.update(self._find_all(_ELEMENTS['ENEMY_PIPE_RIGHT']))
        return list(points)

    def get_barriers(self):
        """ Return the set of barriers Points."""
        points = set()
        points.update(self.get_wall_positions())
        return list(points)
        
    def is_near_to_element(self, x, y, elem):
        _is_near = False
        if not Point(x, y).is_bad(self._size):
            _is_near = (self.has_element_at(x + 1, y, elem) or
                        self.has_element_at(x - 1, y, elem) or
                        self.has_element_at(x, 1 + y, elem) or
                        self.has_element_at(x, 1 - y, elem))
        return _is_near

    def has_enemy_at(self, x, y):
        char = self.char_at(x, y)
        if (char == _ELEMENTS['ENEMY_LADDER']):
            return True
        if (char == _ELEMENTS['ENEMY_LEFT']):
            return True
        if (char == _ELEMENTS['ENEMY_PIPE_LEFT']):
            return True
        if (char == _ELEMENTS['ENEMY_PIPE_RIGHT']):
            return True
        if (char == _ELEMENTS['ENEMY_RIGHT']):
            return True
        if (char == _ELEMENTS['ENEMY_PIT']):
            return True
        return False

    def has_other_hero_at(self, x, y):
        char = self.char_at(x, y)
        if (char == _ELEMENTS['OTHER_HERO_LADDER']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_LEFT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_RIGHT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_PIPE_LEFT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_PIPE_RIGHT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_SHADOW_LEFT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_SHADOW_RIGHT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_SHADOW_LADDER']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_SHADOW_PIPE_LEFT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_SHADOW_PIPE_RIGHT']):
            return True
        return False

    def has_wall_at(self, x, y):
        char = self.char_at(x, y)
        if (char == _ELEMENTS['BRICK']):
            return True
        if (char == _ELEMENTS['UNDESTROYABLE_WALL']):
            return True
        return False

    def has_ladder_at(self, x, y):
        char = self.char_at(x, y)
        if (char == _ELEMENTS['LADDER']):
            return True
        if (char == _ELEMENTS['HERO_LADDER']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_LADDER']):
            return True
        if (char == _ELEMENTS['ENEMY_LADDER']):
            return True
        return False

    def has_gold_at(self, x, y):
        char = self.char_at(x, y)
        if (char == _ELEMENTS['YELLOW_GOLD']):
            return True
        if (char == _ELEMENTS['GREEN_GOLD']):
            return True
        if (char == _ELEMENTS['RED_GOLD']):
            return True
        return False

    def has_pipe_at(self, x, y):
        char = self.char_at(x, y)
        if (char == _ELEMENTS['PIPE']):
            return True
        if (char == _ELEMENTS['HERO_PIPE_LEFT']):
            return True
        if (char == _ELEMENTS['HERO_PIPE_RIGHT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_PIPE_LEFT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_PIPE_RIGHT']):
            return True
        if (char == _ELEMENTS['ENEMY_PIPE_LEFT']):
            return True
        if (char == _ELEMENTS['ENEMY_PIPE_RIGHT']):
            return True
        return False
        return Point(x, y) in self.get_pipe_positions()

    def has_shadow_at(self, x, y):
        char = self.char_at(x, y)
        if (char == _ELEMENTS['HERO_SHADOW_DRILL_LEFT']):
            return True
        if (char == _ELEMENTS['HERO_SHADOW_DRILL_RIGHT']):
            return True
        if (char == _ELEMENTS['HERO_SHADOW_LADDER']):
            return True
        if (char == _ELEMENTS['HERO_SHADOW_LEFT']):
            return True
        if (char == _ELEMENTS['HERO_SHADOW_RIGHT']):
            return True
        if (char == _ELEMENTS['HERO_SHADOW_FALL_LEFT']):
            return True
        if (char == _ELEMENTS['HERO_SHADOW_FALL_RIGHT']):
            return True
        if (char == _ELEMENTS['HERO_SHADOW_PIPE_LEFT']):
            return True
        if (char == _ELEMENTS['HERO_SHADOW_PIPE_RIGHT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_SHADOW_LEFT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_SHADOW_RIGHT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_SHADOW_LADDER']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_SHADOW_PIPE_LEFT']):
            return True
        if (char == _ELEMENTS['OTHER_HERO_SHADOW_PIPE_RIGHT']):
            return True
        return False

    def get_count_elements_near_to_point(self, x, y, elem):
        """ Counts the number of occurencies of elem nearby """
        _near_count = 0
        if not Point(x, y).is_bad(self._size):
            for _x, _y in ((x + 1, y), (x - 1, y), (x, 1 + y), (x, 1 - y)):
                if self.has_element_at(_x, _y, elem):
                    _near_count += 1
        return _near_count

    def to_string(self):
        return ("Board:\n{brd}\Me at: {mbm}\nOther Heroes "
                "at: {obm}\nEnemies at: {mcp}\nGold at:".format(
                                          brd=self._line_by_line(),
                                          mbm=self.get_my_position(),
                                          obm=self.get_other_hero_positions(),
                                          mcp=self.get_enemy_positions(),
                                          dwl=self.get_gold_positions())
        )

    def print_board(self):
        print('\n'*20)
        print(self._line_by_line())

    def get_size(self):
        return (self._size, self._len//self._size)

    def _line_by_line(self):
        return '\n'.join([self._string[i:i + self._size]
                              for i in range(0, self._len, self._size)])

    def _strpos2pt(self, strpos):
        return Point(*self._strpos2xy(strpos))

    def _strpos2xy(self, strpos):
        return (strpos % self._size, strpos // self._size)

    def _xy2strpos(self, x, y):
        return self._size * y + x


if __name__ == '__main__':
    raise RuntimeError("This module is not designed to be ran from CLI")
