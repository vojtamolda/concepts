#ifndef __POINT_H__
#define __POINT_H__

typedef struct {
    int x;
    int y;
} point_t;

point_t get_point(void);
void show_point(point_t point);
void move_point(point_t *point);

#endif
