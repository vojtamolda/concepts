#include <stdio.h>
#include <stdlib.h>

#include "line.h"
#include "point.h"


void show_line(line_t line) {
    printf("Line in C is (%d, %d)->(%d, %d)\n",
        line.start.x, line.start.y,
        line.end.x, line.end.y);
}

void move_line(line_t *line) {
    show_line(*line);
    move_point(&line->start);
    move_point(&line->end);
    show_line(*line);
}

line_t get_line(void) {
    line_t line = { get_point(), get_point() };
    return line;
}
