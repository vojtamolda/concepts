#ifndef __LINE_H__
#define __LINE_H__

#include "point.h"

typedef struct {
    point_t start;
    point_t end;
} line_t;

line_t get_line(void);
void show_line(line_t line);
void move_line(line_t *line);

#endif
