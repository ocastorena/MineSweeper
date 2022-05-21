from tkinter import Button, Label
import random

import settings


def get_cell_by_axis(x, y):
    for cell in Cell.all:
        if cell.x == x and cell.y == y:
            return cell


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-2>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells left:{Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        print("I am a mine")

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # replace the text of cell count label with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells left:{Cell.cell_count}"
                )
        # mark the cell as open
        self.is_opened = True

    @property
    def surrounded_cells(self):
        cells = [
            get_cell_by_axis(self.x - 1, self.y - 1),
            get_cell_by_axis(self.x - 1, self.y),
            get_cell_by_axis(self.x - 1, self.y + 1),
            get_cell_by_axis(self.x, self.y - 1),
            get_cell_by_axis(self.x + 1, self.y - 1),
            get_cell_by_axis(self.x + 1, self.y),
            get_cell_by_axis(self.x + 1, self.y + 1),
            get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg="orange"
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg="SystemButtonFace"
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
