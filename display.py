import pygame as pg
from abc import *
from pygame.locals import *
import uno.Constants as C
import numpy as np
import torch

class Display(metaclass=ABCMeta): # Abstract Class
    # Static Variable
    mode = [C.START, C.START]
    display_idx = 0
    key_idx = -1
    colorblind_idx = -1
    COLORBLIND_MATRIX = [torch.tensor(C.PROTANOPIA_MATRIX), torch.tensor(C.DEUTERANOPIA_MATRIX), torch.tensor(C.TRITANOPIA_MATRIX)]

    def __init__(self):
        self.Button_list = []
        self.Text_list = []
        self.screen = pg.display.set_mode(C.DISPLAY_SIZE[Display.display_idx])

    def color(self):
        array = pg.surfarray.array3d(self.screen)
        rgb_tensor = torch.from_numpy(np.transpose(array[:, :, :3], (2, 0, 1))).float()
        filtered_rgb_tensor = torch.matmul(Display.COLORBLIND_MATRIX[Display.colorblind_idx], rgb_tensor.view(3, -1)).view(rgb_tensor.shape)
        filtered_array = np.transpose(filtered_rgb_tensor.numpy(), (1,2,0))
        filtered_img = pg.surfarray.make_surface(filtered_array.astype('uint8'))        
        self.screen.blit(filtered_img, (0, 0))

    def update_screen(self, mouse_pos): # 현재 화면 업데이트
        for item in self.Button_list:
            item.change_size(Display.display_idx)
            item.update(mouse_pos)
            item.draw(self.screen)
        for item in self.Text_list:
            item.change_size(Display.display_idx)
            item.draw(self.screen)
        if Display.colorblind_idx != -1:
            self.color()
        pg.display.update()


    @abstractmethod
    def next_screen(self): # 버튼 클릭시 다음 화면으로 전환
        pass

    @abstractmethod
    def main_loop(self):
        pass
        
