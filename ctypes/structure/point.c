#include <stdio.h>
#include <stdlib.h>

#include "point.h"


point_t get_point(void) {
    static int counter = 0;
    point_t point = {counter, counter + 1};
    counter += 2;
    printf("Creating Point in C (%d, %d)\n", point.x, point.y);
    return point;
}

void move_point(point_t *point) {
    show_point(*point);
    point->x++;
    point->y++;
    show_point(*point);
}

void show_point(point_t point) {
    printf("Point in C (%d, %d)\n", point.x, point.y);
}
