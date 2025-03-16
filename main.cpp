// g++ main.cpp -o snake -lraylib -lGL -lm -lpthread -ldl -lrt -lX11
#include "raylib.h"
#include <iostream>
#include <map>
#include <unistd.h>
using namespace std;

int screen_h = 450;
int screen_w = 450;
int p_x = screen_w / 2;
int p_y = screen_h / 2;
int length = 5;
char dir = 'w';
map<int, tuple<int, int>> pos;

void drawShit();
bool update();

int main(void) {
  pos[0] = {p_x, p_y};
  for (int i = 1; i < length; i++) {
	pos[i] = tuple(get<0>(pos[0]), get<1>(pos[0]) + (25 * i));
  }
  SetTargetFPS(5);
  InitWindow(screen_w, screen_h, "snake");

  while (true) {

	if (update()) {
  	return 0;
	}
	BeginDrawing();
	drawShit();
	EndDrawing();
  }

  return 0;
}

bool update() {
  if (IsKeyPressed('W')) {
	if (dir != 's') {
  	dir = 'w';
	}

  } else if (IsKeyPressed('A')) {
	if (dir != 'd') {
  	dir = 'a';
	}

  } else if (IsKeyPressed('S')) {
	if (dir != 'w') {
  	dir = 's';
	}

  } else if (IsKeyPressed('D')) {
	if (dir != 'a') {
  	dir = 'd';
	}
  }

  if (dir == 'w') {
	pos[0] = tuple(get<0>(pos[0]), get<1>(pos[0]) - 25);
  } else if (dir == 'a') {
	pos[0] = tuple(get<0>(pos[0]) - 25, get<1>(pos[0]));
  } else if (dir == 's') {
	pos[0] = tuple(get<0>(pos[0]), get<1>(pos[0]) + 25);
  } else {
	pos[0] = tuple(get<0>(pos[0]) + 25, get<1>(pos[0]));
  }

  for (int i = length - 1; i > 0; i--) {
	pos[i] = pos[i - 1];
  }

  if (get<0>(pos[0]) == 450 or get<1>(pos[0]) == 450 or get<0>(pos[0]) == 0 or
  	get<1>(pos[0]) == 0) {
	return true;
  } else {
	// for (int i = 1; i < length; i++) {
	//   if (get<0>(pos[0]) == get<0>(pos[i]) and
	//   	get<1>(pos[0]) == get<1>(pos[i])) {
	// 	return true;
	//   }
	// }
	return false;
  }
}

void drawShit() {
  ClearBackground({0, 0, 0, 255});

  for (int i = 0; i < length; i++) {
	DrawRectangle(get<0>(pos[i]), get<1>(pos[i]), 25, 25, GREEN);
  }
}
