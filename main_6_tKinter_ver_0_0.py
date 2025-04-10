import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Программа проверки знаний нормативов общестроительных работ")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Данные пользователя
        self.user_data = {
            "last_name": "",
            "first_name": "",
            "middle_name": ""
        }

        self.questions = [
            {
                "question": "При проведении ПВТ очищенная поверхность должна превышать контролируемую не менее:",
                "options": [
                    "на 50 мм с каждой стороны.",
                    "на 100 мм с каждой стороны.",
                    "5 толщин контролируемого изделия."
                ],
                "answer": "на 100 мм с каждой стороны."
            },
            {
                "question": "Проведение ПВТ контролируемого участка резервуара проводится при температуре окружающего воздуха и контролируемого участка:",
                "options": [
                    "не допускающей замерзание или испарение используемых жидкостей",
                    "от 10 °С до 40 °С.",
                    "от 0 °С до 50 °С."
                ],
                "answer": "не допускающей замерзание или испарение используемых жидкостей"
            },
            {
                "question": "Для проведения ПВТ (вакуумирование) должны применяться вакуумные камеры, обеспечивающие создание вакуума не менее:",
                "options": [
                    "0,08 Па.",
                    "0,08 кПа.",
                    "0,08 МПа."
                ],
                "answer": "0,08 МПа."
            },
            {
                "question": "Минимальная освещенность контролируемых поверхностей резервуара при проведении ПВТ, Лк:",
                "options": [
                    "500 Лк.",
                    "350 Лк.",
                    "1000 Лк."
                ],
                "answer": "350 Лк."
            },
            {
                "question": "Наличие несплошности при вакуумировании определяется:",
                "options": [
                    "просачивание пенного индикатора с противоположной стороны шва.",
                    "снижением давления в камере.",
                    "появление пузырей пенного индикатора."
                ],
                "answer": "появление пузырей пенного индикатора."
            },
            {
                "question": "С какой стороны контролируемой поверхности после нанесения и высыхания проявителя (суспензии) при пробе \"мел-керосин\", наносится индикаторная жидкость (керосин):",
                "options": [
                    "с противоположной стороны контролируемого участка с проявителем.",
                    "на туже сторону где нанесен проявитель.",
                    "на обе стороны контролируемого участка."
                ],
                "answer": "с противоположной стороны контролируемого участка с проявителем."
            },
            {
                "question": "Нанесение индикаторной жидкости (осветительный керосин) производится:",
                "options": [
                    "после высыхания меловой суспензии.",
                    "до нанесения меловой суспензии.",
                    "одновременно с нанесением меловой суспензии."
                ],
                "answer": "после высыхания меловой суспензии."
            },
            {
                "question": "При проведении ПВТ (проба мел-керосин) противоположная сторона шва обильно смачивается керосином:",
                "options": [
                    "не менее 2 раз.",
                    "от 2 до 3 раз.",
                    "от 3 до 4 раз."
                ],
                "answer": "от 3 до 4 раз."
            },
            {
                "question": "При проведении ПВТ наблюдение за сварным соединением нужно вести:",
                "options": [
                    "с момента начала нанесения на него керосина.",
                    "по окончании нормативной выдержки керосина.",
                    "после 1 часа с момента нанесения на него керосина."
                ],
                "answer": "с момента начала нанесения на него керосина."
            },
            {
                "question": "Время выдержки сварных соединений (продолжительность испытания), после смачивания их керосином составляет:",
                "options": [
                    "не менее 12 часов при положительной температуре и не менее 24 часов при отрицательной.",
                    "не менее 12 часов.",
                    "не менее 24 часов."
                ],
                "answer": "не менее 12 часов при положительной температуре и не менее 24 часов при отрицательной."
            },
            {
                "question": "В местах перехода через траншеи, ямы, канавы должны быть установлены переходные мостки шириной не менее:",
                "options": ["0,8 метра", "1 метр", "1,2 метра", "1,5 метра"],
                "answer": "1 метр"
            },
            {
                "question": "Требуемая крутизна откосов в глинистых грунтах при глубине выемки не более 5,0 м составляет:",
                "options": ["1:0,67", "1:0,25", "1:0,5"],
                "answer": "1:0,67"
            },
            {
                "question": "Виды землеройной техники, обязательные к оснащению системой видеофиксации рабочей зоны при выполнении земляных работ в охранных зонах МТ:",
                "options": ["экскаваторы, бульдозеры, погрузчики на всех видах шасси",
                            "экскаваторы и бульдозеры на гусеничном ходу",
                            "экскаваторы на гусеничном ходу и автомобильном \n шасси, бульдозеры на гусеничном ходу"],
                "answer": "экскаваторы на гусеничном ходу и автомобильном \n шасси, бульдозеры на гусеничном ходу"
            },
            {
                "question": "Минимальное количество видеокамер, устанавливаемых на землеройную технику, при выполнении земляных работ в охранных зонах МТ.",
                "options": ["1", "2", "3", "4"],
                "answer": "1"
            },
            {
                "question": "При необходимости передвижения людей в пазухе расстояние между поверхностью откоса и боковой поверхностью возводимого в выемке сооружения (кроме искусственных оснований трубопроводов, коллекторов и т.п.) должно быть в свету не менее: ",
                "options": ["0,6 м.", "0,8 м.", "1,0 м."],
                "answer": "0,6 м."
            },
            {
                "question": "Отклонение отметок дна траншеи от значений, установленных в ПД при разработке грунта землеройными машинами не более ",
                "options": ["-100 мм.", "+100 мм.", "-150 мм."],
                "answer": "-100 мм."
            },
            {
                "question": "При сооружении трубопроводов DN 1000 и более должна производиться нивелировка дна траншеи по всей длине трассы на вертикальных кривых упругого изгибах через:  ",
                "options": ["10 м.", "20 м.", "30 м."],
                "answer": "10 м."
            },
            {
                "question": "При сооружении трубопроводов DN 1000 и более должна производиться нивелировка дна траншеи по всей длине трассы на вертикальных кривых, выполняемых с помощью гнутых отводов через:   ",
                "options": ["2 м.", "5 м.", "10 м."],
                "answer": "2 м."
            }
        ]


        self.current_question = 0
        self.score = 0
        self.selected_answer = tk.StringVar(value="")
        self.max_options = max(len(q["options"]) for q in self.questions)
        self.answer_checked = False

        self.create_user_info_form()

    def format_name(self, name):
        name = ' '.join(name.strip().split())
        """Форматирует имя: первая буква заглавная, остальные строчные"""
        return name.strip().capitalize() if name else ""

    def create_user_info_form(self):
        """Создает форму для ввода данных пользователя"""
        self.clear_window()

        tk.Label(
            self.root,
            text="Введите ваши данные",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        ).pack(pady=20)

        # Фамилия
        tk.Label(self.root, text="Фамилия:", bg="#f0f0f0").pack()
        self.last_name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.last_name_entry.pack(pady=5)

        # Имя
        tk.Label(self.root, text="Имя:", bg="#f0f0f0").pack()
        self.first_name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.first_name_entry.pack(pady=5)

        # Отчество
        tk.Label(self.root, text="Отчество:", bg="#f0f0f0").pack()
        self.middle_name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.middle_name_entry.pack(pady=5)

        # Кнопка начала викторины
        tk.Button(
            self.root,
            text="Начать проверку",
            command=self.start_quiz,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=15,
            pady=8
        ).pack(pady=20)

    def clear_window(self):
        """Очищает все виджеты в окне"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_quiz(self):
        """Проверяет данные пользователя и начинает проверку"""
        # Применяем capitalize() к введенным данным
        last_name = self.format_name(self.last_name_entry.get())
        first_name = self.format_name(self.first_name_entry.get())
        middle_name = self.format_name(self.middle_name_entry.get())

        if not last_name or not first_name or not middle_name:
            messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля!")
            return

        self.user_data = {
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": middle_name
        }

        self.clear_window()
        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        """Создает виджеты для проверки"""
        # Приветствие с отформатированным именем пользователя
        user_greeting = f"{self.user_data['last_name']} {self.user_data['first_name']} {self.user_data['middle_name']}"
        tk.Label(
            self.root,
            text=f"Добро пожаловать, {user_greeting}!",
            font=("Arial", 12),
            bg="#f0f0f0"
        ).pack(pady=10)

        self.question_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14, "bold"),
            wraplength=450,
            bg="#f0f0f0"
        )
        self.question_label.pack(pady=20)

        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            bg="#f0f0f0"
        )
        self.feedback_label.pack(pady=5)

        self.radio_buttons = []
        for i in range(self.max_options):
            rb = tk.Radiobutton(
                self.root,
                text="",
                variable=self.selected_answer,
                value="",
                font=("Arial", 12),
                bg="#f0f0f0",
                command=self.on_answer_selected
            )
            rb.pack(anchor="w", padx=50, pady=5)
            self.radio_buttons.append(rb)
            rb.pack_forget()

        self.check_button = tk.Button(
            self.root,
            text="Проверить",
            command=self.check_answer,
            state=tk.DISABLED,
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            padx=15,
            pady=5
        )
        self.check_button.pack(pady=10)

        self.next_button = tk.Button(
            self.root,
            text="Далее →",
            command=self.next_question,
            state=tk.DISABLED,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=15,
            pady=5
        )
        self.next_button.pack(pady=5)

    def show_question(self):
        self.answer_checked = False
        self.feedback_label.config(text="")
        self.selected_answer.set("")
        self.check_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)

        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            for rb in self.radio_buttons:
                rb.pack_forget()

            for i in range(len(question_data["options"])):
                self.radio_buttons[i].config(
                    text=question_data["options"][i],
                    value=question_data["options"][i]
                )
                self.radio_buttons[i].pack(anchor="w", padx=50, pady=5)
        else:
            # Показываем результаты и сохраняем в файл
            self.save_results()
            user_name = f"{self.user_data['last_name']} {self.user_data['first_name'][0]}.{self.user_data['middle_name'][0]}."
            messagebox.showinfo(
                "Результат",
                f"Ув. {user_name}! Проверка завершена!\n\nВаш результат: правильных ответов {self.score} из {len(self.questions)} \n\nРезультаты проверки размещены \nв файле results.txt"
            )
            self.root.destroy()

    def save_results(self):
        """Сохраняет результаты проверки в файл results.txt"""
        try:
            with open("results.txt", "a", encoding="utf-8") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                result_line = (
                    f"{timestamp} | "
                    f"{self.user_data['last_name']} {self.user_data['first_name']} {self.user_data['middle_name']} | "
                    f"Результат: {self.score}/{len(self.questions)}\n"
                )
                file.write(result_line)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить результаты: {str(e)}")

    def on_answer_selected(self):
        self.check_button.config(state=tk.NORMAL)

    def check_answer(self):
        if not self.selected_answer.get():
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите ответ!")
            return

        current_answer = self.questions[self.current_question]["answer"]
        user_answer = self.selected_answer.get()

        if user_answer == current_answer:
            self.score += 1
            self.feedback_label.config(text="✓ Ответ верный!", fg="green")
        else:
            self.feedback_label.config(text=f"✗ Неправильно! \nПравильный ответ: {current_answer}", fg="red")

        self.answer_checked = True
        self.check_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

        for rb in self.radio_buttons:
            rb.config(state=tk.DISABLED)

    def next_question(self):
        if not self.answer_checked:
            messagebox.showwarning("Предупреждение", "Сначала проверьте ответ!")
            return

        for rb in self.radio_buttons:
            rb.config(state=tk.NORMAL)

        self.current_question += 1
        self.show_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
