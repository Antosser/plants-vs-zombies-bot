#include <Windows.h>
#include <iostream>

#define click(x, y) SetCursorPos(x, y);\
				mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);\
				Sleep(1);\
				mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);

int main(int argc, const char *argv[]) {
	int op = atoi(argv[1]);
	if (op == 0) {
		int x = atoi(argv[2]);
		int y = atoi(argv[3]);
		int w = atoi(argv[4]);
		int h = atoi(argv[5]);

		while (true)
			for (int i = 0; i < w; i += 60)
				for (int j = 0; j < h; j += 60) {
					click(x + i, y + j);
					Sleep(1);
					if (GetKeyState(VK_INSERT) & 0x8000)
						return 1;
				}
	}
	else if (op == 1 || op == 2) {
		int kx = atoi(argv[2]);
		int ky = atoi(argv[3]);
		int gap = atoi(argv[4]);
		int topleftx = atoi(argv[5]);
		int toplefty = atoi(argv[6]);
		int xgap = atoi(argv[7]);
		int ygap = atoi(argv[8]);
		if (op == 1) {
			for (int x = 0; x < 7; x++)
				for (int y = 0; y < 2; y++) {
					click(kx + gap * 1, ky);
					click(topleftx + x * xgap, toplefty + (y + 2) * ygap);
					//std::cout << topleftx + x * xgap << ", " << toplefty + (y + 2) * ygap << std::endl;
				}
			for (int x = 0; x < 2; x++)
				for (int y = 0; y < 6; y++) {
					click(kx + gap * 0, ky);
					click(topleftx + x * xgap, toplefty + y * ygap);
				}
			for (int y = 0; y < 6; y++) {
				click(kx + gap * 2, ky);
				click(topleftx + 2 * xgap, toplefty + y * ygap);
			}
			for (int x = 0; x < 4; x++)
				for (int y = 0; y < 6; y++) {
					click(kx + gap * 3, ky);
					click(topleftx + (x + 3) * xgap, toplefty + y * ygap);
				}
		}
		else {
			click(topleftx + 7 * xgap, toplefty + 0 * ygap);
			click(topleftx + 0 * xgap, toplefty + 2 * ygap);
			click(topleftx + 6 * xgap, toplefty + 2 * ygap);
			click(topleftx + 6 * xgap, toplefty + 4 * ygap);
			click(topleftx + 7 * xgap, toplefty + 1 * ygap);
			click(topleftx + 6 * xgap, toplefty + 1 * ygap);
			click(topleftx + 5 * xgap, toplefty + 1 * ygap);
			click(topleftx + 4 * xgap, toplefty + 1 * ygap);
			click(topleftx + 3 * xgap, toplefty + 1 * ygap);
			click(topleftx + 2 * xgap, toplefty + 1 * ygap);
		}
	}
}