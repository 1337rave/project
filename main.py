import flet as ft
from flet import (
    Column,
    Container,
    ElevatedButton,
    Row,
    Text,
    Page,
    UserControl,
    border_radius,
    colors,
)
class CalculatorApp(UserControl):
    def build(self):
        self.reset()
        self.result = Text(value="0", color=colors.WHITE, size=55)
        return Container(
            margin=70,
            height=500,
            width=320,
            bgcolor=ft.colors.GREEN_300,
            border_radius=border_radius.all(10),
            padding=10,
            content=Column(
                controls=[
                    Row(controls=[self.result], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.StadiumBorder(), padding=32),
                                text="   AC   ",
                                bgcolor=colors.GREY,
                                color=colors.WHITE,
                                on_click=self.button_clicked,
                                data="AC",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.StadiumBorder(), padding=32),
                                text="    %    ",
                                bgcolor=colors.GREY,
                                color=colors.WHITE,
                                on_click=self.button_clicked,
                                data="%",
                            ),
                            ElevatedButton(
                                text="÷",
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                bgcolor=ft.colors.CYAN_900,
                                color=colors.WHITE,
                                on_click=self.button_clicked,
                                data="÷",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="7",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                on_click=self.button_clicked,
                                data="7",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="8",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                on_click=self.button_clicked,
                                data="8",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="9",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                on_click=self.button_clicked,
                                data="9",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="x",
                                bgcolor=ft.colors.CYAN_900,
                                color=colors.WHITE,
                                on_click=self.button_clicked,
                                data="x",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="4",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                on_click=self.button_clicked,
                                data="4",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="5",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                on_click=self.button_clicked,
                                data="5",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="6",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                on_click=self.button_clicked,
                                data="6",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="-",
                                bgcolor=ft.colors.CYAN_900,
                                color=colors.WHITE,
                                on_click=self.button_clicked,
                                data="-",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="1",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                on_click=self.button_clicked,
                                data="1",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="2",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                on_click=self.button_clicked,
                                data="2",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="3",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                on_click=self.button_clicked,
                                data="3",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="+",
                                bgcolor=ft.colors.CYAN_900,
                                color=colors.WHITE,
                                on_click=self.button_clicked,
                                data="+",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.StadiumBorder(),padding=32),
                                text="     0     ",
                                bgcolor=colors.GREY,
                                color=colors.WHITE,
                                on_click=self.button_clicked,
                                data="0",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.StadiumBorder(),padding=32),
                                text="    .    ",
                                bgcolor=colors.GREY,
                                color=colors.WHITE,
                                on_click=self.button_clicked,
                                data=".",
                            ),
                            ElevatedButton(
                                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
                                text="=",
                                bgcolor=ft.colors.CYAN_900,
                                color=colors.WHITE,
                                on_click=self.button_clicked,
                                data="=",
                            ),
                        ]
                    ),
                ],
            ),
        )
    def button_clicked(self, e):
        data = e.control.data
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("+", "-", "x", "÷"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif data in ("%"):
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)

            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )

        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):

        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "x":
            return self.format_number(operand1 * operand2)

        elif operator == "÷":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = "Calc App"
    calc = CalculatorApp()
    row = ft.Row(controls=[calc], alignment=ft.MainAxisAlignment.CENTER)
    page.add(row)
ft.app(target=main)